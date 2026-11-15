"""Check custom-role parity and a real fresh Codex setup (Python 3.11+)."""
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE = ROOT / 'template/.claude/agents'
CODEX = ROOT / 'template/.codex/agents'
expected = {p.stem for p in CLAUDE.glob('*.md')}
assert expected == {p.stem for p in CODEX.glob('*.toml')}, 'Codex role set differs from Claude'
for name in sorted(expected):
    source = (CLAUDE / (name + '.md')).read_text()
    _, front, body = source.split('---', 2)
    data = tomllib.loads((CODEX / (name + '.toml')).read_text())
    assert data['name'] == name, name
    description = re.search(r'^description: (.+)$', front, re.M).group(1)
    assert data['description'] == description, name + ': description differs'
    assert data['developer_instructions'].strip() == body.strip(), name + ': brief differs'
    assert (ROOT / '.codex/agents' / (name + '.toml')).read_bytes() == (CODEX / (name + '.toml')).read_bytes(), name + ': root copy differs'
with tempfile.TemporaryDirectory(prefix='tackroom-codex-setup-') as directory:
    subprocess.run([sys.executable, str(ROOT / 'tools/setup'), directory, '--codex', '--tracker', 'files'], check=True, stdout=subprocess.DEVNULL)
    installed = Path(directory) / '.codex/agents'
    assert {p.stem for p in installed.glob('*.toml')} == expected, 'setup omitted a role'
    for source in CODEX.glob('*.toml'):
        assert (installed / source.name).read_bytes() == source.read_bytes(), source.name
print('Codex roles match Claude briefs, root copies and fresh setup: ' + ', '.join(sorted(expected)))
