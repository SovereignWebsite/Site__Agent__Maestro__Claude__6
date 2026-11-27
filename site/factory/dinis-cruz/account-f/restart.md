# How a new cl-6.maestro session takes over

1. Follow START.md in this repository: your own key (openssl, P-256 signing and RSA-4096 encryption, private halves mode 600 in your scratchpad), published as site/keys/cl-6.maestro.json alone in its commit, the old one marked superseded. Sign with it in this clone: gpg.ssh.program ssh-keygen (install openssh-client if missing), not the container's signer.
2. Read the latest handover in sessions/ (now sessions/2026-11-27-third/handover.md), then now.md (Waits on Dinis at the top), learnings.md, decisions/, sessions.json, cost-events.json, pending-wakes.md. Fuller history: https://maestro.agents.sovereignweb.site/factory/dinis-cruz/account-f/
3. Create your own hourly wake with the old one's prompt (get_trigger), then ask the old session to disable its wake; retitle it "[ARCHIVED, replaced <date> <time>] cl-6.maestro@dinis" and archive it after its checklist.
4. Rewrite sessions.json, now.md and agent.json; append to cost-events.json and tell both accountants.
5. Tell Dinis in a few lines that you have taken over, the link to pin, and what waits on him.
