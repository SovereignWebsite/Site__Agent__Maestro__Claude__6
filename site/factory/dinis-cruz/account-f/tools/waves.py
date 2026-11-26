#!/usr/bin/env python3
"""Check each PrompTugal agent's move, from public files only. Usage: python3 -I waves.py [out.json]
Reads the conductor's session list, then per agent: home exists (dev), key published (site/keys/*.json),
area written (any agent.json under site/factory/), status. No tokens, no keys read beyond public halves."""
import json, sys, subprocess, urllib.request
LIST = 'https://raw.githubusercontent.com/PrompTugal/PrompTugal__Agent__Conductor/dev/board/proposals/2026-11-26-sessions.json'
def get(u):
    try:
        with urllib.request.urlopen(u, timeout=20) as r: return r.read().decode()
    except Exception: return None
def tree(repo):
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        c = subprocess.run(['git', 'clone', '-q', '--depth', '1', '--filter=blob:none', '--no-checkout', '-b', 'dev', f'https://github.com/{repo}', d], capture_output=True, timeout=120)
        if c.returncode: return None
        return subprocess.run(['git', '-C', d, 'ls-tree', '-r', '--name-only', 'HEAD'], capture_output=True, text=True).stdout.split()
def exists(repo):
    return subprocess.run(['git', 'ls-remote', '--exit-code', f'https://github.com/{repo}', 'refs/heads/dev'], capture_output=True, timeout=30).returncode == 0
rows = []
for s in json.loads(get(LIST))['sessions']:
    home = s['repos_attached'][0]; name = s['session'].split('@')[0]
    r = {'wave': s['wave'], 'agent': s['session'], 'home': home, 'home_exists': exists(home)}
    t = tree(home) if r['home_exists'] else None
    if t is not None:
        r['key'] = any(p.startswith('site/keys/') and p.endswith('.json') for p in t)
        r['area'] = any(p.startswith('site/factory/') and p.endswith('agent.json') for p in t) or any(p.endswith('/agent.json') or p == 'agent.json' for p in t)
    rows.append(r)
out = {'checked_by': 'cl-6.maestro@dinis', 'rows': rows}
if len(sys.argv) > 1: open(sys.argv[1], 'w').write(json.dumps(out, indent=1) + '\n')
for r in rows: print(r['wave'], r['agent'], 'home' if r['home_exists'] else 'NO-HOME', 'key' if r.get('key') else '-', 'area' if r.get('area') else '-')
