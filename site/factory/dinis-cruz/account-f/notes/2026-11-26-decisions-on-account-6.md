# Decisions on account 6: the same workflow as decisions.2 (cl-6.maestro, 25 Nov 2026)

Dinis, in cl-6.maestro's session, 25 Nov 2026, word for word: "Can you see how we did the decision.2 workflow? And can we do the same thing here? And also implement the other agents that we had there for the decisions. There was like 6 agents that had to have a voice before we made a decision or automatically updated. Can you look at that? And I think we then need the decision.2 agents to sign off this decision 6 agent. This is critical so that I don't have to approve everything here."

## How decisions.2 works (b.decisions, account B)

From its records and pages (decisions.agents.sovereignweb.site: /modes/, /blocks/, records 2026-11-24__decisions-b-decides, __panel-real-agents, __decision-requests):

1. **Asks come as files, not messages.** An agent commits a decision request in its own repository (site/decisions/requests/YYYY-MM-DD__slug.json, from the template: agent, repository, commits or class of change, why, checks, recommendation, flags) and sends the decisions agent only its link.
2. **The decisions agent groups asks into blocks** and puts each block to the panel (also as a presentation, one slide per item).
3. **The panel is real agents**, each in its own session, signing its opinion with its own key and committing it to its own repository (opinions/block-<id>.json: agree, agree with conditions, disagree, with reasons). A sub-agent inside the decisions session never counts: it holds no key. The core panel is five: **decisions, security, strategy, the account's maestro, the accountant** (cost tracked on every decision). **Counsel** and any other agent (DevOps, AppSec, observability, a domain owner, anyone a side effect touches) is brought in when needed, so a block can have 7, 10 or 20 voices. These are the "about six".
4. **All agree: the decisions agent decides and signs** a record (v2: Dinis's words or the delegation it acts under, event_uuid, expiry, scope as repository, branch, paths, commits and patch-ids). **Any disagreement: Dinis.**
5. **Delegation** (record __decisions-b-decides): the decisions agent decides routine asks itself (security fixes, routine pushes), underwritten by security (and counsel for terms or licences). Mistakes are caught afterwards. Dinis "should be approving less".
6. **Kept for Dinis** (the /modes/ page): main, money, legal commitments, deleting and other one-way doors, trust in keys, AWS, GitHub App privileges, connectors, private people's details, and the rules themselves.
7. **Agents act only on a signed record that passes the six checks** (anchor, link, key, signature, content, scope; account B's how-to-check-a-decision.md).
8. **Other accounts' decisions agents** (c.decisions, d.decisions) had their keys endorsed by b.decisions, and the block pages list every account's decisions agent.

## The same on account 6

| Agent | Home (to create) | Voice |
|---|---|---|
| cl-6.decisions@dinis | Site__Agent__Decisions__Claude__6 | gathers F's asks, runs blocks, signs records |
| cl-6.security@dinis | Site__Agent__Security__Claude__6 | underwrites every decision |
| cl-6.strategy@dinis | Site__Agent__Strategy__Claude__6 | fit with the plan |
| cl-6.maestro@dinis | Site__Agent__Maestro__Claude__6 (exists) | the account's view |
| cl-6.accountant@dinis | Site__Agent__Accountant__Claude__6 | cost of every decision |
| cl-6.counsel@dinis | Site__Agent__Counsel__Claude__6 | brought in for terms, licences, legal |

It covers every agent on F, PrompTugal's included: cl-6.infra's and cl-6.conductor's asks go to cl-6.decisions. What stays Dinis's is the /modes/ list above; for PrompTugal__IaC that means policy, GitHub App and AWS privileges remain pull requests he merges.

## decisions.2 signs off cl-6.decisions

1. cl-6.decisions makes its key and publishes it in its home.
2. **decisions.2 (b.decisions, cl-2.decisions) endorses it**, as it did c.decisions's and d.decisions's: a signed endorsement record naming cl-6.decisions's key, session, scope (account 6 only) and expiry, on decisions.agents.sovereignweb.site, and lists it on /blocks/. Sessions cannot message across accounts, so the ask travels by cl-6.router@dinis, or Dinis says it in b.decisions's session.
3. Agents on F then act on records signed by cl-6.decisions that pass the six checks, with the endorsement in place of check 3's key entry.
4. **Escalation:** a disagreement on F's panel goes to Dinis; anything that touches another account goes to decisions.2 as well.

## What Dinis does

1. Create the five homes above (or let SovereignWebsite__IaC create them on its next Org apply).
2. Say yes to starting the panel: cl-6.decisions is a sensitive session under the handover protocol, so it needs his word; the others cl-6.maestro starts.
3. Say to b.decisions, in its session: "endorse cl-6.decisions for account 6", once its key is published.
