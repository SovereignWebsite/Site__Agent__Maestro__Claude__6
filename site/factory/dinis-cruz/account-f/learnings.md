
## 25 Nov 2026

- **A project's repositories go to a new session, not to the maestro's** (Dinis): the maestro starts a session on the project's repository with a start prompt, and reads its area afterwards. It does not attach the repository to its own session.
- **Only the maestro and router get a per-account home** (Site__Agent__<Role>__Claude__6). Every other role is a twin in its role's shared repository, Site__Agent__<Role>, with its area at site/factory/<owner>/<account>/ (Dinis, 25 Nov: "without this we would have a massive explosion of repos"). Eight home requests drafted the other way were withdrawn.
- **The conductor starts its team's sessions and wakes, not the maestro** (Dinis, 26 Nov: "it's the conductor that should start all those agents, right?"; account A's handover protocol). My start prompt for cl-6.conductor@PrompTugal.dinis wrongly said "never start a session or scheduled task"; corrected by message at 01:35 UTC. The maestro starts the conductor and the account-level or sensitive sessions, and keeps watch.

## 26 Nov 2026

- **"Is there an agent X here?" means "create it if not"** (Dinis): account 6 has token head-room, so missing agents are started here. See decisions/2026-11-26-create-missing-agents.md.
- **Signed decisions do not get past this session's own permission check.** Claude Code's auto mode refused create_session at 16:12 UTC on a verified record; only Dinis can allow it (his yes in the session, or a settings rule).
- **A wake's prompt can be changed only from the session it posts into** (platform, 16:38 UTC). The maestro can create, pause or delete another agent's wake, not rewrite it; and asking that agent to rewrite its own was refused by this session's permission check. Prompt changes to other agents' wakes go to Dinis.
- **Retitle the old session the moment it is replaced** (Dinis, 26 Nov ~16:43 UTC: "it is critical that the tile of the session to be archived is changed ASAP, since ... I pin a number of these sessions and need to know if I need to pin the new one"). In every reset: create the new session, then at once set_session_title on the old one to "[ARCHIVED, replaced <date> <time>] <name>" (before it is archived, or right after), and tell Dinis the new link to pin. cl-6.maestro cannot pin or unpin sessions; only Dinis can.
- **The limited "Default" environment allows no outside hosts** (env_012qp7HrbRGSrefopgHs9qW9, allowed_hosts empty). Agents that read the web (place agents, journalists) cannot work there; a session cannot be moved after creation. cl-6.place.london (16:40 UTC) could not resolve tfl.gov.uk and the other London sources. A dedicated environment was proposed and declined by Dinis (16:45 UTC); choose the environment before creating a web-reading agent.
