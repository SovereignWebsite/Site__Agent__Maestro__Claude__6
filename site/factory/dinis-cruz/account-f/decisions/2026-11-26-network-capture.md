# Network: no web reads from the maestro; capture every agent's network requests (26 Nov 2026)

Dinis, in cl-6.maestro's session, about 16:50 UTC on 26 Nov 2026, word for word, after declining the "PrompTugal places (London)" environment cl-6.maestro proposed (it named this maestro repository):

> "because
>
> a) why do you need that since the environment you have has full access to the internet
> b) that kind of access and calls should never be done from a Maestro repo (at most that should be from a london data agent)
>
> can you ask the security and account and abp to figure out a way to also capture all network requests made by the agents here (which I've seen done before) so that we can track them and detect ABPs (since we should have super strick ABP for Network access for all agents here)"

## What follows

1. **The maestro never does, and never asks for, network access for data work.** Web reads for a place belong to that place's own agent (for London, a London data agent), never to a maestro repository or environment.
2. **Every agent on account 6 gets a strict network ABP** (an allow-list of hosts per agent), and every network request is captured so it can be tracked and breaches detected.
3. **Asked at 16:52 UTC** to design it together: cl-6.security@dinis, cl-6.accountant@dinis (cost and the ledger), cl-6.abp@PrompTugal.dinis (the policies), with cl-6.telemetry@PrompTugal.dinis (it already counts hosts and refusals) in copy. Their design comes back to Dinis.

## Then (about 16:45 UTC)

Dinis: "that is actually a good one for the places environment right? since only the London , or even better the data.london agent should be the one making those requests". Done: environment "PrompTugal data (London)" (env_014fJkugLPBiSUBfBqSeK1G7), six hosts, no repository named; cl-6.data.london@PrompTugal.dinis started in it (session_016CrbJMrN6VztFm2YVXmp3b), logging every request; cl-6.place.london keeps no network and reads its data. cl-6.abp asked for its grant as the first network ABP.

Dinis, same time: "FYI account B is currently at 73% capacity" (passed to cl-6.conductor-sw).
