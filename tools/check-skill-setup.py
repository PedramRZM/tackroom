"""Exercise canonical skill resources, discovery adapters and legacy setup compatibility."""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / 'template/.agents/skills'
for source in SKILLS.iterdir():
    assert (ROOT / '.agents/skills' / source.name).resolve() == source.resolve(), source


def setup(project, *flags, ok=True):
    result = subprocess.run([sys.executable, str(ROOT / 'tools/setup'), str(project), *flags],
                            text=True, capture_output=True)
    assert (result.returncode == 0) == ok, result.stdout + result.stderr
    return result


with tempfile.TemporaryDirectory(prefix='tackroom-shared-skills-') as directory:
    base = Path(directory)
    copied = base / 'manual-copy'
    copied.mkdir()
    setup(copied, '--legacy')
    assert (copied / '.agents/skills/ui-craft/references/motion.md').is_file()
    for index, flags in enumerate((('--legacy',), ('--codex',), ('--opencode',), ('--codex', '--opencode'))):
        project = base / str(index)
        project.mkdir()
        setup(project, *flags, '--dry-run')
        assert not list(project.iterdir()), 'dry run wrote files'
        setup(project, *flags, '--tracker', 'files')
        for source in SKILLS.iterdir():
            installed = project / '.agents/skills' / source.name
            assert installed.is_dir() and not installed.is_symlink(), installed
            assert (project / '.claude/skills' / source.name).resolve() == installed
            for resource in source.rglob('*'):
                if resource.is_file() and '__pycache__' not in resource.parts and resource.name != 'install.json':
                    assert (installed / resource.relative_to(source)).read_bytes() == resource.read_bytes(), resource
        assert (project / '.codex/config.toml').exists() == ('--codex' in flags)
        assert (project / 'opencode.json').exists() == ('--opencode' in flags)
        local = project / '.agents/skills/ui-craft/SKILL.md'
        local.write_text('project-specific craft\n')
        result = setup(project, *flags, ok=False)
        assert result.returncode == 2 and 'conflict (kept local)' in result.stdout
        assert local.read_text() == 'project-specific craft\n'
    project = base / 'existing'
    custom = project / '.agents/skills/ui-craft'
    custom.mkdir(parents=True)
    (custom / 'SKILL.md').write_text('local override\n')
    dangling = project / '.agents/skills/verify'
    dangling.symlink_to('missing-local-skill')
    setup(project, '--legacy', ok=False)
    assert (custom / 'SKILL.md').read_text() == 'local override\n'
    assert dangling.is_symlink() and not dangling.exists()
print('Shared skills: canonical sources, generated adapters, legacy selections, resources, dry run and preservation passed')
