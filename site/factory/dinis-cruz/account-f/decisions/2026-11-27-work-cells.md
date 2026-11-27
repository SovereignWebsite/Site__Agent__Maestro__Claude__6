# Work cells: a unit of work built around one diff

Date: 2026-11-27. Asked by Dinis (in cl-6.maestro's session). Status: proposal, first cell running by message.

## What Dinis asked

A "task force" or "ephemeral squad", named after agenticcells.ai: a small team focused on one specific task, working
off git diffs rather than commits, that can run in its own session, so that it becomes the unit of work we delegate,
with a Kanban board and a production line. Reason given: many projects lying around, weak quality control, because
single agents do not see the whole picture.

## What agenticcells.ai already says (read 2026-11-27, site v0.1.286)

- "An agentic cell is a small team of AI agents doing one focused job for you. Each agent has a role, a brief that
  says what it does, and a behaviour policy that says what it may and may not touch."
- "What every cell has" includes "An objective: the one job it exists for, said in your words" and "A deliverable".
- "The smallest cells run in one session; bigger ones span several sessions and people."
- Its four sizes are commercial (one agent, a few sessions, a team, a network). It names no short-lived or
  task-focused cell type and no unit-of-work term, so the name below is new.

## Proposal: the work cell

A **work cell** is a cell that exists for one brief and ends when its diff lands.

1. **Brief** (cells/<date>-<slug>/brief.md): the objective in Dinis's words, the evidence (screenshot, links), the
   files in scope, the roles, and the acceptance checks. The maestro writes it.
2. **Roles**, chosen per brief (for example designer, UX, developer, reviewer). A role can be an existing agent
   or a short-lived session started only for the cell.
3. **Deliverable: one diff** (cells/<slug>/change.diff, `git diff` output against a named base commit) plus a
   short note of what each role checked. The cell does not push to the target repository.
4. **The owner applies it.** The agent that owns the target repository reviews the diff, applies it, signs the
   commit with its own key and names the cell in the message. Keys, write scopes and ABPs stay as they are: the
   cell needs no new grant on the target repository.
5. **Board**: cells/board.json lists each cell (brief, roles, state: briefed, working, diff ready, applied,
   dropped). The briefing page can show it as a Kanban.
6. **End**: once applied (or dropped), the cell's sessions are archived when nothing is held.

## What needs a decision

- The name (work cell, or another) and the folder layout: Dinis.
- A session started only for a cell: R4 is met (the maestro starts it), but cl-6.abp must give the "cell" role a
  grant (home only, writes cells/<slug>/** in its home, no push elsewhere, no add_repo, session or schedule).
- Where cells live long term: here for now; a shared Site__Agent__Cells repository later if it works.

## First cell

cells/2026-11-27-briefing-page: fix the briefing page's questions section, run by message with the existing
agents (no new session).
