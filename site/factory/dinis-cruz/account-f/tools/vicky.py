"""Vicky's team at a glance, from the public record only (git history of PrompTugal__News__Website).
Usage: python3 -I tools/vicky.py <clone of PrompTugal__News__Website> > vicky.md
Lists every agent named *.vicky (and her web-summit conductor) by its last commit on dev, then the last 48 hours of their commits.
Reads commit subjects and dates; never a transcript, a key or a token."""
import subprocess, sys, re, collections, datetime
repo = sys.argv[1]
def git(*a): return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True).stdout
git('fetch', '-q', 'origin', 'dev')
log = git('log', 'origin/dev', '--since=14 days ago', '--format=%H\x1f%cI\x1f%s')
pat = re.compile(r'^([A-Za-z0-9._-]+@[A-Za-z0-9._-]*vicky)\b')
last, recent = {}, []
now = datetime.datetime.now(datetime.timezone.utc)
for line in log.splitlines():
    h, at, s = line.split('\x1f', 2)
    m = pat.match(s)
    if not m: continue
    a = m.group(1); t = datetime.datetime.fromisoformat(at)
    last.setdefault(a, (t, h[:9], s))
    if now - t < datetime.timedelta(hours=48): recent.append((t, a, h[:9], s))
head = git('log', '-1', 'origin/dev', '--format=%h %cI').strip()
print(f"# Vicky's team: what it did (generated {now:%Y-%m-%d %H:%M} UTC from PrompTugal__News__Website dev {head})\n")
print("Public record only: commit subjects on dev. Her sessions run on her own account, so their status is not visible from account 6.\n")
print("## Each agent's last commit (last 14 days)\n\n| Agent | Last commit (UTC) | Hours ago | Commit | What |\n|---|---|---|---|---|")
for a, (t, h, s) in sorted(last.items(), key=lambda x: x[1][0], reverse=True):
    w = s[len(a):].lstrip(': ').replace('|', '/')[:110]
    print(f"| {a} | {t:%d %b %H:%M} | {int((now - t).total_seconds() // 3600)} | [{h}](https://github.com/PrompTugal/PrompTugal__News__Website/commit/{h}) | {w} |")
print("\n## The last 48 hours\n")
for t, a, h, s in recent:
    print(f"- {t:%d %b %H:%M} [{h}](https://github.com/PrompTugal/PrompTugal__News__Website/commit/{h}) {s.replace('|', '/')[:160]}")
if not recent: print("- nothing")
