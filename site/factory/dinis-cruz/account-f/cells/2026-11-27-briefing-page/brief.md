# Cell brief: make Dinis's briefing page readable

Opened 2026-11-27T10:45Z by cl-6.maestro@dinis. Objective, in Dinis's words: "good start but can you work with the
designer, ux and dev agents to fix this".

## The page

https://observability.agents.sovereignweb.site/factory/dinis-cruz/account-f/briefing/ (built and owned by
cl-6.observability@dinis). It reads, in the browser at view time:
- briefing.json (Site__Agent__Maestro__Claude__6, dev, site/factory/dinis-cruz/account-f/briefing.json)
- questions.json (Site__Agent__Decisions, dev, site/factory/dinis-cruz/account-f/questions.json)
- sessions.json, cost-events.json (maestro), agents view (observability), social drafts

## What is wrong (from Dinis's screenshot, loaded 2026-11-27T10:39:35Z)

1. "Dinis's questions" cards show only an urgency badge, the id (for example "iac-34-37", "s17") and "status: open".
   The id means nothing to Dinis. Every useful field is missing: `question`, `line_to_paste`, `urgency` (the full
   text, for example "now: strike window ends 11:59 UTC"), `asked_by`, `since`, `context_url`.
2. The most urgent things (strikes window) do not stand out above the rest; the cards are large and mostly empty.
3. "Sources" takes the top of the page; it matters least to Dinis.

## What good looks like (acceptance)

- Top of page: what needs Dinis now, ordered by urgency, each with the question in plain words, the exact line to
  paste (with a copy button), and a link to the session it goes in (claude.ai/code/<session id>).
- Questions and briefing.json's waiting_on_dinis[] shown as one list, no duplicates (same id or same line).
- Items with a deadline show it.
- Compact rows, readable on a phone (16px gutter, no sideways scroll), light and dark.
- Sources moved to the bottom, collapsed.
- No new hosts: still only raw.githubusercontent.com, read in the browser.

## Roles

- Designer and UX: cl-6.design@dinis (layout, hierarchy, the "what do I do next" flow).
- Developer: cl-6.observability@dinis (owns the page; writes the change).
- Reviewer: cl-6.maestro@dinis (checks against this brief and the live data).

## Deliverable

One diff against the page's current commit, written to this folder as change.diff by whoever drafts it, or
applied directly by cl-6.observability in its own repository and signed there with the cell named in the commit
message. Then state: applied, with the commit and a reload of the live page.
