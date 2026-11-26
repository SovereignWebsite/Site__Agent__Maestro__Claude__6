# Plan: Vicky's team to the new format (draft, 26 Nov 2026, 14:20 UTC)

Asked by Dinis in cl-6.maestro's session, 26 Nov 2026: "yes, draft the upgrade plan for her team". A draft for Dinis and Vicky to agree; nothing in it has started. Facts are from PrompTugal__News__Website dev at about 14:05 UTC (board/keys.json, desks/*-vicky, commits) and the PrompTugal__Agent__* homes; see [vicky.md](../vicky.md).

## Where her team is now

- **One big repository.** Her agents work in PrompTugal__News__Website, in desks/<role>-vicky/ and board/team/, on her own account, with one main conductor (Vicky, 26 Nov 14:02: "Yes, still one main conductor").
- **Active this week:** checker, reviewer, journalist-ai, curator (26 Nov); designer, analyst (23 Nov). **Quiet:** journalist-europe (21 Nov), journalist-portugal (20 Nov), dev (15 Nov), conductor@web-summit.vicky and reporter (14 Nov). Status files are stale: desks/conductor-vicky/status.json was last updated 12 Nov.
- **Keys:** 15 active entries in board/keys.json for her agents, all sgit-style with **no ssh field**. The gate's signature check (newsroom/build/lib/signed-root.mjs) only trusts ssh keys, so none of her agents can change a trust-root file, and her own signatures cannot be checked the new way.
- **Her history is already copied** into most role homes by the account 6 twins: history/desks/<role>-vicky/ in PrompTugal__Agent__{Checker, Reviewer, Analyst, Designer, Dev, Weather, Journalist}. Not yet in Curator, Programme (only conductor-vicky) or Conductor.

## The new format (what "upgraded" means)

Every agent: its role's home repository (PrompTugal__Agent__<Role>, shared by twins), its own area there (agent.json, now.md, role.md, restart.md), its own key with an ssh field published in that home and in the website's board/keys.json, its entire history in the home (history/, PROVENANCE.md, git-log.md), its old folder frozen with a pointer, a wake, and work in the project repositories by signed commits. Account 6 already runs this way (waves.json: 41 agents).

## Her agents, and where each goes

| Her agent | Home | Account 6 twin there | Her history there |
|---|---|---|---|
| conductor (one main; conductor@web-summit.vicky, conductor.B, conductor.fringe) | PrompTugal__Agent__Conductor | cl-6.conductor@PrompTugal.dinis | no: copy desks/conductor-vicky |
| checker | PrompTugal__Agent__Checker | cl-6.checker | yes |
| reviewer | PrompTugal__Agent__Reviewer | cl-6.reviewer | yes |
| curator | PrompTugal__Agent__Curator | cl-6.curator | no desk of hers found; board/team only |
| analyst | PrompTugal__Agent__Analyst | cl-6.analyst | yes |
| designer | PrompTugal__Agent__Designer | cl-6.designer | yes |
| dev | PrompTugal__Agent__Dev | cl-6.dev | yes |
| weather | PrompTugal__Agent__Weather | cl-6.weather | yes |
| journalist-ai, -europe, -portugal, -connections, reporter | PrompTugal__Agent__Journalist | cl-6.journalist | yes (journalist-vicky) |
| programme (keys superseded) | PrompTugal__Agent__Programme | cl-6.programme | conductor-vicky only |

## Steps

1. **Unblock first (today):** openssh-client in her environment's setup script and a full clone in every session (the red gate); cl-6.dev makes the gate name that cause (asked 14:12 UTC).
2. **Agree the names** (Dinis and Vicky): keep `<role>@PrompTugal.vicky`, and her area path in each home: `site/factory/<her owner id>/<her account>/` (she chooses; we do not invent it).
3. **Her conductor first:** a new session on her account on PrompTugal__Agent__Conductor (Vicky starts it; R4 binds account 6 only). It makes its key (P-256 with ssh field, RSA-4096), publishes it in the home and the website's board/keys.json, writes its area, copies desks/conductor-vicky into history/ with PROVENANCE.md and git-log.md.
4. **Then each active agent, one at a time** (checker, reviewer, curator, journalist-ai, analyst, designer): same steps in its role's home, by her conductor; her old key entry marked superseded; desks/<role>-vicky/ frozen with a README pointer to the home. Quiet agents (europe, portugal, connections, reporter, dev, programme) move only if she wants them back; otherwise their desks are frozen with a pointer and their keys superseded.
5. **Twins share the work, not the keys:** in each home her agent and the account 6 twin keep separate areas and keys; who does what goes in the home's README (for example her checker checks, cl-6.checker covers her quiet hours). cl-6.conductor@PrompTugal.dinis and her conductor agree the split.
6. **Wakes on her account**, set by her conductor; times staggered against account 6's (pending-wakes.md) so the two teams do not race the same release.
7. **Done when** each moved agent has: key with ssh in board/keys.json, area current, history in its home, desk frozen, one green signed release. vicky.md then also reads each home's agent.json.

## For Dinis to decide

- Whether her team keeps its own roles beside the account 6 twins, or the twins take over the quiet roles.
- Her owner id for the area paths (ask Vicky).
- Who briefs her conductor: Dinis directly, or cl-6.maestro writes the start prompt for Vicky to paste.
