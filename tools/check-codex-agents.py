"""Check generated native config/roles and the common brief source (Python 3.11+)."""
import json
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEFS = ROOT / 'template/.agents/briefs'
expected = {p.stem for p in BRIEFS.glob('*.md')}
with tempfile.TemporaryDirectory(prefix='tackroom-native-config-') as directory:
    project = Path(directory)
    subprocess.run([sys.executable, str(ROOT / 'tools/setup'), directory, '--agents', 'claude,codex,opencode', '--tracker', 'files'], check=True, stdout=subprocess.DEVNULL)
    for name in expected:
        meta = json.loads((BRIEFS / (name + '.json')).read_text())
        body = (BRIEFS / (name + '.md')).read_text().strip()
        native = project / '.codex/agents' / (name + '.toml')
        data = tomllib.loads(native.read_text())
        assert data['name'] == name and data['description'] == meta['description'], name
        assert data['developer_instructions'].strip() == body, name
        assert (ROOT / '.codex/agents' / native.name).read_bytes() == native.read_bytes(), name
        for agent in ('claude', 'opencode'):
            if agent in meta:
                _, _, instructions = (project / ('.' + agent) / 'agents' / (name + '.md')).read_text().split('---', 2)
                assert instructions.strip() == body, (agent, name)
    for path in (project / '.codex').rglob('*.toml'):
        tomllib.loads(path.read_text())
    for rel in ('.claude/settings.json', '.codex/hooks.json', 'opencode.json'):
        data = json.loads((project / rel).read_text())
        assert data, rel
    for rel in ('.claude/settings.json', '.codex/hooks.json'):
        text = (project / rel).read_text()
        assert '.claude/hooks/' not in text, rel
        for hook in ('guard.py', 'stop-check.py'):
            assert (project / '.agents/hooks' / hook).is_file()
print('Generated native configuration parses; all role bodies match canonical briefs and root outputs')
