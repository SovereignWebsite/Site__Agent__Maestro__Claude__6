# VoiceDebrief MeetScribe: a product site and the Chrome Web Store

Asked by Dinis, 27 Nov 2026: "create a new site for the Chrome Extension VoiceDebrief which works REALLY well
(current integration is with Gemini via Open Router) ... working really well for Google Meet (and should work for any
site that has audio on a browser) ... let put this on the Chrome App Store".

## What exists (read from the public repo, dev branch, 27 Nov)

- Repo VoiceDebrief/VoiceDebrief__Chrome_Extension__MeetScribe, HEAD b2e4f79 (3 Nov 2026), v0.3.5, beta.
- It already has a docs site: https://meetscribe.chrome-extension.voicedebrief.ai/ (CNAME), deployed by
  .github/workflows/deploy-pages.yml on every push to dev; release zips with sha256 in releases/.
- Manifest V3; permissions tabCapture, offscreen, activeTab, sidePanel, storage, unlimitedStorage, alarms;
  host permission https://openrouter.ai/* only; CSP connect-src openrouter.ai. The listing says "Google Meet";
  the capture itself is of the active tab, so other tabs with audio are a scope decision, not a code change.
- built/index.md lists "A release zip and the Chrome Web Store" as not built; plan/index.md has the Store step
  after a security self-review against the hub's quality rubric (chrome-extensions.sgit.ai/rubric).
- Privacy facts the listing must carry (README): no server, no account, no analytics; data in the browser,
  unencrypted; audio and transcript go to OpenRouter and on to a model provider; zero data retention is a request.
- This account (Claude account 6) cannot reach the repo through GitHub: list_repos returns nothing for VoiceDebrief.

## Plan

1. Access: Dinis gives the Claude GitHub app access to VoiceDebrief/VoiceDebrief__Chrome_Extension__MeetScribe
   for this account (or names the account whose agents keep it).
2. A keeper session cl-6.meetscribe@VoiceDebrief.dinis (started by the maestro on Dinis's yes) on that repo, dev only:
   - product front page (what it does, the one rule: not for confidential meetings, cost per hour, install from the
     Store), with the docs moved under it; or a separate product site if Dinis prefers;
   - privacy policy page (required by the Store for an extension handling user data);
   - Store listing pack: description, single-purpose statement, a justification per permission, the data-use
     disclosure (audio, transcripts, OpenRouter key; Limited Use), screenshots and promo images, support URL;
   - security self-review against the rubric and the open review finding(s) closed;
   - a Store build zip from releases/.
3. Dinis does what only a person can: register the Chrome Web Store developer account (one-time fee and identity
   checks, per Google's terms; check the current amount there), choose the publisher name (VoiceDebrief?), upload
   the zip and pack, submit for review. Publishing by API later needs an OAuth client for the Store API, saved as a
   credential, never in a repo.

## Decisions for Dinis

- Scope: Google Meet only (as today) or "any tab with audio" (Zoom web, Teams web, YouTube)? Wider scope changes the
  listing, the single-purpose statement and the review.
- Site: improve the existing meetscribe.chrome-extension.voicedebrief.ai (recommended) or a new one.
- Publisher account and name.
