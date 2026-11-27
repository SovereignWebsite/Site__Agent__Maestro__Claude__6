# Calendar under version control (a calendar on sgit)

Architecture design for Dinis Cruz, by cl-6.maestro@dinis, 27 November 2026. Companion design: [Events MVP: one place for every event in a person's life](events-mvp.md), whose layer 4 is this vault.

**How to read this.** **Exists today** items cite sgit evidence as repository, path and commit: SGit-AI__CLI (HEAD ada1813, version v0.27.1), SGit-AI__Website (sgit.ai docs, HEAD 4e00434, describing roughly 0.18 to 0.21; where they disagree the CLI is newer) and the-cyber-boardroom/SGraph-AI__App__Send (HEAD 522192c). Everything else is **Proposed**. iCalendar (RFC 5545), ULIDs and IANA time zones are general knowledge and marked as such. No calendar, `.ics` or event schema exists in any of these repositories (grep for `calendar|.ics|icalendar|vevent`).

## 1. The idea

Dinis: "the power of change control for events, for calendar entries ... a killer feature ... your calendar is now version controlled. Not only you have full provenance and full understanding and prevention from mistakes, but also prevents conflicts from happening ... allows multiple entities to be updating the same calendar at the same time, which is basically a vault ... what would the calendar look like when it's based on top of sgit?"

The answer here: a calendar is a vault of small JSON files, one per event, laid out so that people and agents who change different events never touch the same file, with every change a signed, explained commit.

## 2. What sgit gives us (exists today)

| Need | sgit fact | Evidence |
|---|---|---|
| Private storage | Client-side AES-256-GCM; server never sees contents, filenames, folder structure, commit messages | SGit-AI__Website `security/index.md` (4e00434) |
| History per file | `sgit history log --file p --follow`, `--patch`, `--json`; `sgit history blame` | `docs/sgit-for-git-users.md` (4e00434) |
| Single-file commit | `sgit write <path> --file f --message m --push --json`; `--also` for atomic multi-file | `docs/agents.md` (4e00434) |
| Path commits | `commit <paths>` and `commit -p` | SGit-AI__CLI CHANGELOG 0.27.0 (ada1813) |
| No silent overwrite | Push is compare-and-swap; a stale push is rejected; `sgit push` pulls first, merges, uploads | `docs/agents-sharing-one-vault.md`, `docs/two-branch-model.md` (4e00434) |
| Merge | Three-way per file; untouched files merge automatically; conflicts as `<path>.conflict`; `sgit resolve --show`; `sgit merge-abort` | same docs |
| Line merge | Opt-in `--merge lines`, byte-identical to `git merge-file`, only for files both sides changed | CLI `safe_types/Enum__Merge_Style.py`, CHANGELOG (ada1813) |
| Signatures | `sgit commit -S`, `sgit check verify --require-user-signature`, signed tags `sgit vault tag create -s` | `docs/sgit-for-git-users.md`; CLI 0.27.0 |
| Undo | `sgit history revert` | `docs/sgit-for-git-users.md` |
| Read-only sharing | Read key reads every file and every commit in history; cannot commit | `docs/credentials.md` (4e00434) |
| Blind inbound | Append lanes: a stranger can send an encrypted message without the vault key | `docs/vault/sg-bridge.md`, `docs/vault-messaging.md` |
| Browser | `window.sg` (`vfs`, `history`, `sync`, `append`); vault library `addFiles` for one commit of many files | `docs/vault/sg-bridge.md`, `docs/vault/vault-from-javascript.md` |
| Scoped clones | `sgit clone --path <folder> --depth 1` | `docs/agents-sharing-one-vault.md` |

## 3. The vault tree (proposed)

```
calendar.json                         manifest: calendar.vault/1
events/
  k2/01JDX3F8Q2W9M4T7K2.json          event/1, one file per event
  r7/01JDX5B1N8C2V6P0R7.json
series/
  01JDW9A4H3J5K8M2Q1.json             series/1: the recurrence rule
  01JDW9A4H3J5K8M2Q1/
    occurrences/2026-12-08.json       override of one occurrence
    occurrences/2026-12-15.json       (status: cancelled)
decisions/
  cnd-01JDX7Q0M3.json                 accepted or rejected candidate
proposals/
  agent.family/                       append-only lane of one trusted writer
    2026-11-27T0914Z-cnd-01JDX7Q0M3.json
index/                                derived, rebuilt by the merger
  by-day/2026-12.json
  clashes.json
export/
  calendar.ics                        derived, iCalendar (RFC 5545, general knowledge)
signers.json                          writers' public key fingerprints
```

Decisions and their grounding:

- **One file per event, named by a stable id, not by date.** Moving an event changes `start` and `end` inside the file; the path never changes. Two people editing two events edit two files, and sgit's per-file three-way merge combines them with no conflict (exists today: "Non-conflicting changes merge automatically"). Dating the path would turn every move into a delete plus an add, which collides with any concurrent edit of the old file.
- **Sharded by id.** `events/<shard>/` keeps folders small for scoped clones and small tree objects per push (a push uploads the commit, each changed tree level and the changed file: `docs/agents-sharing-one-vault.md`). If ids are ULIDs (time-ordered by design, general knowledge), their first characters barely vary, so the shard is taken from the last two, random, characters (`...K2` goes to `k2/`). No file-count limit per vault or folder was found in sgit.
- **Recurring series.** `series/<id>.json` holds the rule (RRULE, RFC 5545, general knowledge). Each changed occurrence is its own file, named by the occurrence's original date, which never moves (the RECURRENCE-ID idea in iCalendar). Edits to different occurrences never touch the same file; a cancelled occurrence is a file with `status: "cancelled"`.
- **Derived files are never hand-edited.** `index/` and `export/` are rebuilt from `events/` and `series/` by the merger after each merge. Writers do not commit them; if one ever conflicts, it is thrown away and rebuilt.
- **Single writer per file.** sgit has no per-user or per-folder permission inside a vault: "A partial clone is not an access boundary ... give each its own vault" (`docs/limitations.md`). So the design makes every file have one writer by convention, and uses separate vaults or lanes where the convention cannot be trusted:
  - the **owner, or the owner's agent, is the one merger**: the only writer to `events/`, `series/`, `decisions/`, `index/`, `export/`;
  - a **trusted writer** (a partner's device, the owner's own agent) gets an append-only folder `proposals/<writer>/`, new files only, never edits;
  - a writer that **must not be able to edit events** (an outside assistant, a booking service, an organiser) gets its own proposals vault, which the merger reads, or writes into an append lane (blind, outside the commit tree).
- **Keys are not in the manifest.** `calendar.json` names linked vaults (the calendar twin, friends' calendars) by id; their read keys are sealed to the owner's browser key, as the CRM does with vault keys (Site__Tool__CRM `site/app/pki.js`, c106016). Anyone holding this vault's read key reads `calendar.json`.

`calendar.json` (proposed):

```json
{
  "schema": "calendar.vault/1",
  "name": "Home",
  "owner": "owner@example.org",
  "tz": "Europe/London",
  "merger": "owner",
  "writers": [
    { "name": "owner", "key": "sha256:9f2c...", "writes": ["events/", "series/", "decisions/", "index/", "export/"] },
    { "name": "agent.family", "key": "sha256:51ab...", "writes": ["proposals/agent.family/"] }
  ],
  "linked": [
    { "kind": "twin.calendar/1", "vault": "vlt-twin-g1", "role": "mirror of Google" },
    { "kind": "calendar.vault/1", "vault": "vlt-friend-a", "role": "friend, read-only" }
  ]
}
```

`writes` is a declaration the schema check enforces before commit; sgit itself does not enforce it.

## 4. event/1 (proposed)

Pretty-printed, keys in a fixed order, one field per line, so that line merge (when chosen) has the best chance of combining edits to different fields.

```json
{
  "schema": "event/1",
  "id": "01JDX3F8Q2W9M4T7K2",
  "title": "Design review",
  "start": "2026-12-02T14:00",
  "end": "2026-12-02T15:00",
  "tz": "Europe/London",
  "all_day": false,
  "location": "Room 3, example.org office",
  "organiser": { "crm": "crm-main", "org": "o-example-studio" },
  "attendees": [
    { "crm": "crm-main", "person": "p-ana-example", "rsvp": "accepted" },
    { "crm": "crm-main", "person": "p-ben-example", "rsvp": "needs-action" }
  ],
  "status": "confirmed",
  "sources": [
    { "kind": "candidate/1", "vault": "this", "path": "decisions/cnd-01JDX7Q0M3.json" },
    { "kind": "twin.message/1", "vault": "vlt-mail-twin", "path": "mail/clean/messages/2026/11/m-8812.json", "commit": "c3e19a0" },
    { "kind": "twin.event/1", "vault": "vlt-twin-g1", "source_id": "google:evt-abc123" }
  ],
  "ical_uid": "abc123@example.org",
  "series": null,
  "created_at": "2026-11-27T09:20:00Z",
  "updated_at": "2026-11-27T09:20:00Z"
}
```

Times are local wall time plus an IANA zone (general knowledge), so a recurring 09:00 stays 09:00 across a clock change. `status` follows iCalendar's tentative, confirmed, cancelled (general knowledge). Attendees are CRM references (Site__Tool__CRM `crm.person/1`, `crm.org/1`, c106016), never copies.

## 5. Provenance

Exists today: per-file log and blame, signed commits, JSON output. Proposed: a commit message convention.

```
event(move): Design review [01JDX3F8Q2W9M4T7K2]
Who: owner (signed)
Why: clash with school run
Source: candidate cnd-01JDX7Q0M3; twin.event google:evt-abc123 @ sync 2026-11-27T08:00Z
```

Illustrative only (made-up ids and output shape, not captured from a real run):

```
$ sgit history log --oneline --file events/k2/01JDX3F8Q2W9M4T7K2.json --follow
e41b7d0  event(move): Design review 14:00 -> 15:00   owner     Why: clash with school run
9c03a22  event(rsvp): Ben needs-action -> accepted   merger    Source: lane agent.family
3f9e1c4  event(add): Design review                   owner     Source: candidate cnd-01JDX7Q0M3
```

`sgit history blame` on the same file answers "who set this location, and in which commit". `sgit check verify --require-user-signature` rejects history that contains unsigned commits.

## 6. Mistake prevention

| Mechanism | Status |
|---|---|
| Schema check before commit (valid `event/1`, writer allowed for the path, `end` after `start`, zone known) | Proposed, run by the app or agent before `sgit write` |
| Diff preview of the event before sign-off (`sgit history diff`) | Diff exists; preview UI proposed |
| Clash check after every merge, into `index/clashes.json` | Proposed |
| Revert one event: `sgit history revert` of the commit that touched it | Exists; per-event undo UI proposed |
| Signed tags for published states, for example `published-2026-12-agenda` | Exists (`sgit vault tag create -s`); naming proposed |
| Stale copy push rejected, merged, then pushed | Exists (compare-and-swap) |
| Conflicts never silent: `<path>.conflict`, `sgit resolve --show`, `sgit merge-abort` | Exists |
| Pull refuses to overwrite uncommitted edits to incoming files | Exists since 0.18.0 |
| Read back after a browser write | Proposed, because the vault library v0.2.3 can silently drop a file written into a folder not yet loaded (reproduced 12 October 2026, `docs/vault/vault-from-javascript.md`) |

One limit to state plainly: two different events at the same hour are two files, so sgit merges them without complaint. A double booking is a meaning problem, not a file conflict. The clash index catches it.

## 7. Two concurrent edits

Both parents' devices are at commit `c41`. Each device has its own clone branch (exists today: `docs/two-branch-model.md`).

1. Parent A moves the dentist from 10:00 to 11:00: changes `start` and `end` in `events/k2/01JD...K2.json`, commits `a1`, pushes. The server's head moves to `a1`.
2. Parent B, still at `c41`, adds the clinic's address to `location` in the same file, commits `b1`, pushes.
3. `sgit push` pulls first and finds `a1`. Both sides changed the same file, so the per-file merge applies:
   - default style `FILES`: B's version is kept and A's is written to `events/k2/01JD...K2.json.conflict`; B must resolve (`sgit resolve --show` shows base, ours, theirs);
   - style `lines`: the lines changed (`start`, `end` versus `location`) are separate, so the line merge combines them; if the changed lines were adjacent, `git merge-file` semantics would mark a conflict (general knowledge of git).
4. The schema check runs on the merged file (a line merge can produce valid text but invalid JSON), then B commits the merge `m1`, signed, and pushes. Compare-and-swap succeeds.
5. The merger rebuilds `index/` and `export/`.

If A and B had edited different events, step 3 is an automatic merge with nothing to resolve.

## 8. Multi-entity scenarios

**A family calendar: two parents and an agent.** Both parents hold the vault key and sign their commits; either may act as merger. The family agent holds no vault key for writing events; it writes candidates to its own proposals vault (or to `proposals/agent.family/` if the family trusts it with the vault key, accepting that sgit cannot stop it editing elsewhere). Two parents change the same event at once: section 7. A parent and the agent at once: the agent only adds new files, so nothing conflicts; the parent's later decision supersedes the proposal.

**An assistant booking for an executive.** The executive owns the vault; the executive's agent is the merger. The assistant gets a read key to see the diary and a proposals vault of their own to write bookings into. The executive's agent checks clashes, merges or asks. If the executive moves a meeting while the assistant books the same slot, both land as different files, the merge is clean, and the clash index raises the double booking for a human. If the assistant must write directly, they hold the vault key and sign every commit, and provenance, not permission, is the control.

**An event organiser pushing updates to attendees.** The organiser keeps an event vault (one event or a series) and is its only writer. Attendees get its read key and link it from their own `calendar.json`. Each attendee's copy cites the organiser's event id and commit; when the organiser changes the time, the attendee's app shows "source changed" and the attendee accepts or declines the update into their own vault. RSVPs go back by append lane to the organiser (lanes exist; addressing a lane from a public key "is not wired end to end": `docs/limitations.md`). Two organisers' staff editing at once is the same per-file merge as the family case. A signed tag marks each published version of the agenda.

## 9. Privacy

- Exists today: contents, filenames, folder structure and commit messages are encrypted client-side; the server never holds a key.
- The server still sees the vault id, encrypted object sizes, timing of reads and writes and object counts (`security/index.md`). From object counts per push one can infer roughly how many files changed (the facts file's inference, not a documented claim). For a calendar, timing alone can say "this person edits their diary at 07:00".
- A metadata "structure key" split is described by the project as an in-progress design change.
- Viewers get the read key: they read every file and every past commit. Revocation is not retroactive; rotate with `sgit vault rekey`. A calendar that is shared should hold only what is meant to be shared; private notes go in a separate vault.

## 10. Honest limits

- JSON-aware merge is designed but not shipped; only file-level and opt-in line merge exist (`docs/limitations.md`; CLI 0.27.1).
- Simple Token sharing is unavailable: disabled per the SEND skill, and no `share` command is registered in CLI 0.27.1.
- Browser writes cap at about 3 MB per file (`EFBIG`); events are tiny, but attached posters are not.
- No per-user permissions inside a vault; single writer per file is a convention backed by separate vaults and lanes.
- Batch writes are capped (50 operations in the CLI, under a server limit of 100), so a bulk import is several commits.
- An encrypted vault cannot be subscribed to by a normal calendar app; `export/calendar.ics` is downloaded and imported, or published in plaintext by deliberate choice.

## 11. Relation to Google Calendar

- The calendar twin (Design A, layer 2) mirrors Google, written only by the sync tool.
- This vault is the source of truth for the person: accepted events, with provenance.
- Twin events arrive as candidates; once accepted they carry the twin's source id, so later Google changes show as "source changed".
- Changes go back to Google only as signed-off drafts applied by the calendar tool, which records what it applied, following the existing mail sign-off pattern (Site__Tool__Google__Gmail `site/app/core/signoff.mjs`, 862f363). The next twin sync confirms the change.

---

Design by cl-6.maestro@dinis, 27 November 2026. Exists-today items cite their evidence; everything else is proposed.
