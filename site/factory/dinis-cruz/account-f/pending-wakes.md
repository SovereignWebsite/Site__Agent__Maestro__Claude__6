# Wakes to create, under cl-6.abp's R4 (proposed by cl-6.conductor, 26 Nov 06:20 UTC)

cl-6.abp's R4: only cl-6.maestro starts sessions and wakes, until Dinis says P4 in cl-6.abp's session. Create each wake when its agent (or the conductor) says it can work; tick it here with the trigger id. Lisbon time (CRON_TZ=Europe/Lisbon). Prompt: the conductor's standard wake text (its message of 06:20 UTC), with the R14 identity line once checked against cl-6.abp's published policy.

| Agent | Session | Cron (Lisbon) | Create when | Done |
|---|---|---|---|---|
| sherpa | session_016CrbJMWWVdEEuaqxoSn7QC | 27 9,20 | ready | trig_015ypwpPefevdtENVZEDCnzy |
| library | session_016CrbJNfPpkijB4Czf4L2DD | 7 9,20 | the section key route lands (PrompTugal__IaC PR 25) | |
| events | session_016CrbJNMHQRQmkvWGwFt7BL | 37 8,19 | key route | |
| live | session_016CrbJMc7qc59eSmeqUAW6q | 47 8,19 | key route | |
| videos | session_016CrbJMuWrQhMqNFVLoX3dS | 17 9,20 | key route | |
| signals | session_016CrbJLzfdz51sDBekg8v8X | 37 9,20 | key route | |
| cyber | session_016CrbJLwU9iQ41Xv3q2VZwk | 43 9,20 | key route | |
| bulletins | session_016CrbJN84epGHrjZ5CT51bY | 53 9,20 | key route | |
| travel | session_016CrbJMxEaAKd9efCfrsom6 | 7 7,18 | its gate change lands | |
| outreach | session_016CrbJKSAFT2v7Mkhpc4uJd | 57 9,20 | the website is attached | |
| accountant (PrompTugal) | session_016CrbJLU6NN6yvcGyy3HEg3 | 17 10,21 | the website is attached | |
| observability | session_016CrbJK6qQvXVy64vKPgEe1 | 27 10,21 | Dinis's two answers (account A handover) | |
| abp | session_016CrbJK3xXBhUMA6rucuPPd | 37 10,21 | it said it can work (15:56 UTC 26 Nov); prompt starts with its line below | trig_01UBF8M2222JWokDoFs2skhV |

## Lines to put at the start of wake prompts

- **cl-6.abp** (its message, 15:56 UTC 26 Nov, at Dinis's word in its session): "First read standing instruction S1 and rule R15 in abp/policies.json (the hook prints them; if it did not, read abp/cl-6.abp.md). Dinis's own line applies: cl-6.abp applies what cl-6.decisions signs on his behalf, except the one-way doors, after verifying the chain. Nothing is applied from memory."

## Sessions to start

- **cl-6.place.london@PrompTugal.dinis**: signed record 2026-11-26__place-london-start (Site__Agent__Decisions 8ecec85; signature checked 16:31 UTC; endorsement widened, 991125a, to 30 Nov): Sonnet, limited "Default" environment, PrompTugal__Agent__Place__London only, no extra tools; first prompt states no add_repo, no create_session, no scheduled task, publishes its key first, does not write the website's place data; wakes 25 7,18 Lisbon set by cl-6.maestro. cl-6.abp policy v1.6.4 (abp/cl-6.place.london.md) adds: no write in the website (public clone only); board/keys.json only to add its key; hook label cl-6.place.london@PrompTugal.dinis. Started 16:38 UTC (session_016CrbJKifSCoGBhUJDMMjpN), wake trig_01VWwNuhgsJs23ehwqaaq1HT.
- 2026-11-26__strikes-site: no action until a later record names strike-day wakes.
- **cl-6.social@PrompTugal.dinis**: signed record 2026-11-26__social-start (Site__Agent__Decisions d14b5df; Dinis in the conductor's session 16:29:30 UTC, event 21f6da74; security's six conditions). Start when IaC #30 has created PrompTugal__Agent__Social and cl-6.security@dinis has reviewed cl-6.abp's grant. Sonnet, limited "Default" (never an environment holding OPEN_ROUTER_KEY), that repository only, no extra tools; first prompt states no connector, no posting, no login, no session, no schedule, no sub-agent; key first; brief PrompTugal__Agent__Conductor board/briefs/2026-11-26-video-abp-wrong-tab.md. Separate from cl-6.social@dinis (Sovereign Website, sgit, CBR).

## Wake changes waiting

- **cl-6.places, trig_0132oarAUsN5cwmgTAbj3GGk**: signed record 2026-11-26__abp-p11g (Site__Agent__Decisions 5b4b226) says run the places one after another, no sub-agents. 16:38 UTC: update_trigger refused by the platform (a wake's prompt can be changed only from the session it posts into); asking cl-6.places to apply it itself was refused by this session's permission check. Waits on Dinis: he changes it in cl-6.places' session (session_016CrbJJcoCJnQM6GGY1xC5K), or says how. 27 Nov 07:41 UTC: a replacement wake and disabling the old one were both refused by this session's permission check.

- **cl-6.onboarding@SovereignWebsite.dinis** (the web CMS for owners; Dinis asked about 16:50 UTC in cl-6.conductor-sw's session which agent does it; none does): Started 16:53 UTC at Dinis's yes here (session_016CrbJL9nXnBiLGoiXLGM2N). Sonnet, limited "Default", Site__Agent__Onboarding only, fictional demo owner, never a vault key.

## Resets in progress (Dinis: "reset them", 16:53 UTC)

Handover asked 16:55 UTC; then new session (same repository and model, limited environment), wake moved, old retitled "[ARCHIVED, replaced ...]" at once, archived after the new one confirms.
- cl-6.abp (session_016CrbJK3xXBhUMA6rucuPPd, 72.5%; wake trig_01UBF8M2222JWokDoFs2skhV)
- cl-6.journalist (session_016CrbJLhtarwbcbxJnrF3bP, 61.7%; wake trig_01HHZRxLqWpzNpKi7oURHNfF)
- cl-6.devops (session_016CrbJLNFt4cFTXMVgkqcCY, 54.0%; wake trig_01ABYHjvXT9THELBSgM2PaSg)
- cl-6.accountant@dinis (session_016CrbJJ7NP5eaJypGAHgdGi, 53.1%)
