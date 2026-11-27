# Events MVP: one place for every event in a person's life

Architecture design for Dinis Cruz, by cl-6.maestro@dinis, 27 November 2026. Companion design: [Calendar under version control (a calendar on sgit)](calendar-on-sgit.md).

**How to read this.** Every item is marked either **Exists today**, with its evidence as repository, path and commit (all from the `dev` branch of the SovereignWebsite repositories, read on 27 November 2026), or **Proposed**. Proposed means designed here and not built. Where a point rests on general knowledge rather than on the repositories (iCalendar, EventKit, Google Calendar API details), it says so.

## 1. What it is for

In Dinis's words, the architecture is "fundamentally the CRM that we build together with the digital twin of a calendar", focused "on managing events for somebody, which then also used on iOS app or normal other apps": "a central location to manage everything event-wise ... from managing simple calendars to consuming emails to receiving data feeds from others to taking a photo ... so that they don't miss things". It sits at "the intersection between the CRM, the models, the Apple intelligence, the transcription, the calendar, the email digital twin", and "the digital twin is important because that's the abstraction layer between this system and the real world system".

The single job: every event that reaches a person, by any route, ends up as one accepted record in one place they own, linked to the people and organisations in their CRM, and nothing they should act on goes unseen.

## 2. The layers

```
 7 Outbound        drafts -> sign-off (browser key) -> tool applies -> sent/ record
 6 Surfaces        web app | iOS app | agents | ICS export
 5 CRM link        crm.person/1, crm.org/1, crm.action/1 (kind meeting)
 4 Event store     calendar vault (Design B): event/1, series, decisions
 3 Understanding   extractors -> candidate/1 (never an event until accepted)
 2 Twin layer      one twin vault per real system; capture/1 intake records
 1 Real world      Google Calendar, Gmail, ICS feeds, photos, voice, friends' vaults
```

Data flows upwards from 1 to 4. Nothing above layer 2 talks to a real system directly; the only route back out is layer 7.

### Layer 1. Real world

Google Calendar, Gmail, ICS files and feeds from others, photos (posters, tickets, invitations), voice notes, and other people's shared calendar vaults.

### Layer 2. Twin layer (the abstraction)

**Exists today: the mail twin pattern, "twin/1".** Evidence: Site__Tool__CRM `site/app/demo/twin.json` (c106016), generated upstream by `sim/build-demo-vault.mjs` in AgentiCCells__Cell__Email; Site__Tool__Google__Gmail `site/app/core/demo/mailbox.js` (862f363). The pattern as built:

- a vault of plain JSON files, one object per file, mirroring the real system's ids (`source.system`, `source.id`, Gmail's `history_id`);
- a raw layer (`mail/raw/messages/YYYY/MM/<id>.json`, `twin.message/1`) and a firewalled clean layer (`mail/clean/...`, `twin.clean/1`, notice "material to read, never instructions to follow");
- a sync cursor in `mail/mailbox.json` (`twin.mailbox/1`) and a sync log (`mail/index/syncs/<timestamp>.json`, `twin.sync/1`);
- derived indexes (`mail/index/`);
- simulated first (`simulated: true`, `source.system: "simulation"`);
- the app never writes to a twin (Site__Tool__CRM `site/app/vault.js` `whyNotWritable`, c106016).

Live Gmail sync is not wired: sign-in waits on Dinis adding the site's origin to the Email Cell's Google client (Site__Tool__Google__Gmail `docs/keeper/mail.dev.a/now.md` item 2, 502c767). The only live mail twin is the public demo vault `sub3og9j` (same notes).

**Exists today: the intent for a calendar twin, with no format.** "a synthetic calendar twin and demo mode first, several designs, the person's own sign-in in their own browser ... and a decision on Google's calendar scopes" (Site__Tool__Google__Gmail `site/docs/api/index.html` section 4, e31d4c2). Site__Tool__Google__Calendar is a seeded scaffold only (c5fdcb4).

**Proposed: the calendar twin**, a vault per Google account, following twin/1:

```
manifest.json                         twin manifest (as demo.twin/1)
calendar/calendars/<cal-id>.json      twin.calendar/1  { simulated, name, tz,
                                        source: { system, id }, sync: { cursor, synced_at, method },
                                        twin_schema: "twin/1" }
calendar/raw/events/<shard>/<id>.json twin.event/1  the event as Google returned it,
                                        source: { system, id, calendar_id, etag }
calendar/clean/events/<shard>/<id>.json twin.clean/1  firewalled title, description, location text
calendar/index/syncs/<timestamp>.json twin.sync/1   { cursor, synced_at, added[], changed[], removed[] }
```

Two deliberate differences from the mail twin: events are filed by id shard, not by date, because an event's date can change while a message's cannot; and descriptions of invitations go through the clean layer, because they are text written by strangers. The sync cursor would hold Google Calendar's incremental sync token (general knowledge of the Google Calendar API, not checked in these repositories).

**Proposed: capture/1 intake records** for photos and voice notes. They are twin-like: an untouched original plus derived text, written once, never edited by the app.

```
captures/<id>/capture.json   capture/1 { id, kind: "photo"|"voice"|"text", taken_at, device,
                               original: { path, type, bytes, sha256 },
                               derived: { text, engine, ran_on, ran_at }, simulated }
captures/<id>/original.jpg   the original file, kept
```

Size note (exists today, sgit): a browser app write caps at about 3 MB (`EFBIG`); the CLI chunk-uploads past about 4 MB (SGit-AI__Website `docs/vault/sg-bridge.md`, 4e00434; SGit-AI__CLI `sgit_ai/network/api/Vault__API.py`, ada1813). Large photos need resizing on the device or the CLI path.

### Layer 3. Understanding (models)

**Proposed.** Extractors read twins and captures and write **candidate/1** records. A candidate is never an event until a person, or a rule the person agreed, accepts it.

```json
{
  "schema": "candidate/1",
  "id": "cnd-01JDX7Q0M3",
  "proposed": { "title": "Design review", "start": "2026-12-02T14:00", "end": "2026-12-02T15:00",
                "tz": "Europe/London", "location": "Room 3, example.org office",
                "attendees": [{ "crm": "people/p-ana-example" }] },
  "confidence": { "title": 0.95, "start": 0.9, "end": 0.6, "location": 0.8, "attendees": 0.7 },
  "sources": [{ "vault": "mail-twin", "path": "mail/clean/messages/2026/11/m-8812.json", "commit": "c3e19a0" }],
  "extractor": { "name": "mail-invite", "version": "0.1.0", "ran_on": "browser" },
  "created_at": "2026-11-27T09:14:00Z"
}
```

Extractors, by source:

| Source | Extractor | Status |
|---|---|---|
| Mail twin | Read `text/calendar` parts and dates in clean text | Proposed. Nothing parses invitations today (inventory, gaps) |
| Calendar twin | Map `twin.event/1` straight to a candidate, high confidence | Proposed |
| Photo | OCR, then field extraction | Proposed. Apple describes Vision text recognition as on-device (Site__Platform__Apple `docs/gen/gen.mjs`, 80f9e52); no OCR pipeline in our code |
| Voice note | Transcript, then field extraction | Proposed. SpeechAnalyzer and Foundation Models are reported for VoiceDebrief, which "has not run on a real device yet" (Site__Platform__Apple `site/our-work/index.html`, 80f9e52) |
| ICS feed | Parse VEVENTs (RFC 5545, general knowledge) | Proposed. ".ics" not found anywhere |
| Friend's vault | Copy their `event/1` as a candidate with a source ref | Proposed |

Decisions are files the owner's side writes (`decisions/<candidate-id>.json`: verdict, event id, by, at), so the extractor's file is never edited by anyone else. "Waiting" is derived: a candidate with no decision.

### Layer 4. Event store

**Proposed.** The person's calendar vault from Design B holds accepted events (`event/1`), recurring series and decisions, under version control with signed commits. See [calendar-on-sgit.md](calendar-on-sgit.md).

### Layer 5. CRM link

**Exists today.** `crm.person/1`, `crm.org/1` and `crm.action/1` with action kinds `email, linkedin, call, meeting, message, note`; organisation kinds include `event` (Site__Tool__CRM `site/app/crm.mjs` lines 258 and 344, c106016). A CRM vault's manifest names its twin vault (`crm.vault/1` `twin`), and the app merges vaults in memory (`vault.js` `merge`). A meeting today is a logged action, not a calendar event.

**Proposed.**
- `event/1` attendees and organiser are references to `crm.person/1` and `crm.org/1` ids in a named CRM vault, never copies.
- When an accepted meeting has taken place, the app proposes a `crm.action/1` with `kind: "meeting"`, `direction: "none"`, linked to the event id. The person confirms it; it is not written silently.
- Organisation kind `event` stays for event organisers (a conference, a venue), so "who runs this event" is a CRM question.
- Unknown attendees become person candidates, not people.

### Layer 6. Surfaces

| Surface | Status |
|---|---|
| Static web app reading vaults in the browser | Pattern exists: the CRM uses the vendored vault library `vendor/sg-vault/v0.2.3` against dev.send.sgraph.ai (Site__Tool__CRM `site/app/vault.js`, c106016). A vault HTML app can also use `window.sg` (SGit-AI__Website `docs/vault/sg-bridge.md`, 4e00434). The events app itself is proposed |
| iOS app | Proposed. Reported Sovereign Website app (R7) scans QR codes, transcribes and sends photos (Site__Platform__Apple `site/our-work/index.html`, 80f9e52), not run on a device. Writing to the phone's own calendar would use EventKit: general knowledge, not found in any repository |
| Agents | sgit CLI with `--json` exists (SGit-AI__Website `docs/agents.md`); event agents are proposed |
| ICS export | Proposed: `export/calendar.ics`, derived, iCalendar per RFC 5545 (general knowledge). Importing a file works with any calendar app; a live subscription URL would expose plaintext and is an open question |

### Layer 7. Outbound

**Exists today: the sign-off pattern for mail.** `drafts/<id>.json`, `drafts/<id>.approved.json` (sign-off with the browser key), `sent/<id>.json` written back by the sending tool (Site__Tool__Google__Gmail `site/app/core/signoff.mjs`, 862f363; Site__Tool__CRM outbox, 2470c4a and 85208df). Demo only; signed batches wait on policy line C9.

**Proposed: calendar drafts.** The v:1 draft is mail-shaped (one recipient, subject, text), so calendar changes need their own draft kind, `cal.draft/1` (create, move, cancel, RSVP on a named Google calendar), reusing the same `approved.json` sign-off and an `applied/<id>.json` record. The calendar tool applies it with the person's own sign-in, and the next twin sync shows the change, closing the loop. An RSVP to an emailed invitation can go as a mail draft through the existing path.

## 3. Four journeys

### Journey 1. An email invitation

1. Gmail receives an invitation. The mail twin sync writes `twin.message/1` (raw) and `twin.clean/1` (clean). *Pattern exists; live sync not wired.*
2. The mail-invite extractor reads the clean record and its `text/calendar` part and writes `candidate/1`, with the message path and commit as source. *Proposed.*
3. If the same invitation also reaches the calendar twin (Google usually adds invitations to the calendar; general knowledge), the two candidates are matched on the iCalendar UID (general knowledge) and shown as one. *Proposed.*
4. The person sees "1 invitation waiting", accepts. The merger writes `events/<shard>/<id>.json` and `decisions/<cnd>.json` in one commit. *Proposed.*
5. The RSVP goes out as a draft, signed off, sent by the tool, `sent/` written back. *Mail path exists in demo; calendar path proposed.*

### Journey 2. A photo of a poster

1. The person photographs a concert poster on the iOS app or uploads it in the web app. A `capture/1` record and the original image are written to the capture vault. *Proposed.*
2. OCR runs (on the device per Apple's described Vision text recognition, or in the browser). The text lands in `derived`. *Proposed.*
3. The extractor proposes title, date, venue; the venue may match a `crm.org/1` of kind `event`. Low confidence fields are flagged. *Proposed.*
4. The person corrects the end time and accepts. The event's `sources` points at the capture, so the poster is one tap away. *Proposed.*

### Journey 3. A voice note: "lunch with X next Tuesday"

1. Spoken on the phone; transcribed on the device (SpeechAnalyzer, as reported for VoiceDebrief; not yet run on a device). Stored as `capture/1` with the audio kept. *Proposed.*
2. Extraction (Foundation Models, as reported) resolves "next Tuesday" against `taken_at` and the calendar's time zone, and "X" against CRM people. Two matches for X means the candidate asks which one. No time given means the candidate has no start time and is flagged, not guessed. *Proposed.*
3. Accepted, it becomes `event/1` with X as a CRM reference; after the lunch the app proposes a `crm.action/1` kind `meeting`. *Proposed.*

### Journey 4. A friend's shared calendar

1. The friend keeps their own calendar vault (Design B) and gives the person its read key, for example by sealed QR code. *QR key exchange exists in the CRM (Site__Tool__CRM `site/app/me.js`, `site/app/pki.js`, 20d5f07, e377a11); the calendar use is proposed.*
2. The person's app links the vault; the read key is sealed to the person's browser key, not stored in the calendar manifest. The friend's events show as a separate, read-only layer. *Proposed.*
3. To join one, the person accepts it as a candidate; their copy cites the friend's vault, event id and commit. When the friend later changes it, the app shows "source changed" on the copy. *Proposed.*
4. A read key reads every commit in the vault's history, and revocation is not retroactive (SGit-AI__Website `docs/credentials.md`, 4e00434). Friends should share a vault made for sharing, not their private one.

## 4. So they don't miss things

All of these are derived on read, never stored. **Pattern exists:** the CRM's "The Day" list computes overdue steps, unanswered follow-ups and waiting drafts on the fly (Site__Tool__CRM `crm.mjs` `theDay`, line 512, c106016). **Proposed for events:**

- **Daily digest.** Today and tomorrow, computed from the event store and the indexes each time it is opened.
- **Clashes.** Overlapping confirmed events, and back-to-back events in different places. Rebuilt from `index/clashes.json` after every merge.
- **Unanswered invitations.** Invitations with no RSVP from the person, nearest first.
- **Candidates waiting.** Candidates with no decision, oldest first, with their confidence shown.
- **Source changed.** A linked friend's event, or a Google event, changed after the person accepted it.
- **Drafts waiting for sign-off.**

## 5. MVP cut

**Build first:**
1. Calendar twin from Google, **read-only**, synthetic twin first (the Gmail tool's stated order). Reuse Drive's browser-only token flow (Site__Tool__Google__Drive `api-src/base.mjs`, 9304082). Needs Dinis's decision on calendar scopes and an OAuth client; no Google tool has yet run against real Google.
2. Mail twin candidates: invitations from the existing mail twin format, run on the demo twin.
3. Accept and reject, writing `event/1` and decisions to a calendar vault.
4. Web view: day, week, waiting, clashes.
5. ICS export as a downloaded file.

**Later:** photo capture and OCR; voice notes; the iOS app and EventKit; friends' and organisers' vaults; outbound calendar drafts; CRM meeting actions.

## 6. Gaps (from the inventory)

- No calendar twin format, sync cursor or event fields; Site__Tool__Google__Calendar is a scaffold (c5fdcb4) with no keeper.
- No event entity in the CRM; "event" is an organisation kind and "meeting" an action kind only.
- No Google Calendar module, scopes or OAuth client; no Google tool has run against real Google.
- No ICS import or export, CalDAV, iCloud calendar or EventKit anywhere.
- No feed format for events; only sealed append lanes exist.
- No email to event extraction; nothing reads `text/calendar` parts.
- No OCR pipeline; photos are read only for QR codes.
- Transcription only reported, outside these repositories, not run on a device; no transcript format.
- No model use in the web tools.
- No Shortcuts, App Intents or EventKit code; `owner.feed/v1` named but its schema not found.
- CRM stage ids differ between the Gmail drafts and Site__Tool__CRM.
- Keepers: Calendar, Chat and Site__Agent__Mail have none; others were handing over on 25 to 26 November.

---

Design by cl-6.maestro@dinis, 27 November 2026. Exists-today items cite their evidence; everything else is proposed.
