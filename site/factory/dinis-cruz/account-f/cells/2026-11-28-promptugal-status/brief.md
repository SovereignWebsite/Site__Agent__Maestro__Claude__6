# Cell brief: PrompTugal's admin status page (every agent, what it is doing, the state of the data)

Opened 2026-11-28T01:1xZ by cl-6.maestro@dinis. Dinis's words (28 Nov, maestro's session): "where's in the prompt to Go page on the admin section, which we should have is the current status of everything happening and all the mapping of every single agent that we have, and that information of what is all the agents and what is everybody doing and what's the status of the data. So I asked this on the data, but it should also be on the website."

## What exists (checked 28 Nov 01:1x UTC)
- https://promptugal.news/newsroom/dashboard/ ("Dinis's view of the team": now, agents, where they fire), from content/newsroom/dashboard.md, last changed 64b007fa (26 Nov). It reads board/team/<role>/status.json in the website repo, so it shows almost none of account 6's agents (one cl-6 id found on the live page; Vicky's team appears).
- No /admin/, /status/ or /agents/ page (all 404).
- cl-6.observability already keeps agents.json and an agents page (status, grants, context, cost, wakes) for account 6; cl-6.data keeps the data vaults; Vicky's team's activity is in the website's git log (maestro's tools/vicky.py).

## What good looks like
- One page on promptugal.news (the existing dashboard, extended, or /newsroom/status/), linked from Newsroom: every agent on every account that works on PrompTugal (account 6, Vicky's, any other), grouped by desk, each with: role, last activity (time and what), next step, blocked on what, its home repo.
- A "Data" section: each dataset or vault, last refresh, source, rows, freshness verdict, owner (from cl-6.data).
- "Waits on Dinis" at the top, the same list as his briefing page.
- Fed by JSON that agents already keep (observability's agents.json, cl-6.data's status file, briefing.json, questions.json), read at build or in the browser; nothing new hand-edited.
- Phone-safe, no new hosts beyond those the site already uses.

## Roles
- Data feeds: cl-6.observability@dinis (agents, all accounts it can see), cl-6.data@PrompTugal.dinis (a data-status JSON).
- Design and UX: cl-6.designer@PrompTugal.dinis.
- Developer: cl-6.dev@PrompTugal.dinis (the change to the website, as a diff).
- Apply: whoever holds the website with push (blocked today: the journalist session with the website, waiting on Dinis's word).
- Review: cl-6.maestro@dinis and cl-6.conductor@PrompTugal.dinis.

## Deliverable
One diff against PrompTugal__News__Website dev (content/newsroom/ and the build feature it needs), plus the two JSON feeds in their owners' repos.
