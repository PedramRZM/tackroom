"""Exercise shared skill installation for default, Codex and OpenCode setups."""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "template/.claude/skills"

for source in SKILLS.iterdir():
    shared = ROOT / "template/.agents/skills" / source.name
    assert shared.is_symlink(), f"template itself omitted shared skill {source.name}"
    assert shared.resolve() == source.resolve(), f"broken template skill link: {shared}"

for name in ("ui-craft", "verify", "write-tests"):
    for source in (SKILLS / name).rglob("*"):
        if source.is_file() and "__pycache__" not in source.parts:
            root_copy = ROOT / ".agents/skills" / source.relative_to(SKILLS)
            assert root_copy.read_bytes() == source.read_bytes(), f"root Codex skill differs: {root_copy}"


def setup(project, *flags):
    subprocess.run(
        [sys.executable, str(ROOT / "tools/setup"), str(project), *flags],
        check=True, stdout=subprocess.DEVNULL,
    )


with tempfile.TemporaryDirectory(prefix="tackroom-shared-skills-") as directory:
    base = Path(directory)
    copied = base / "manual-copy"
    shutil.copytree(ROOT / "template", copied, symlinks=True)
    for source in SKILLS.iterdir():
        skill = copied / ".agents/skills" / source.name
        assert skill.is_symlink() and skill.resolve() == copied / ".claude/skills" / source.name
        assert (skill / "SKILL.md").read_bytes() == (source / "SKILL.md").read_bytes()
    assert (copied / ".agents/skills/ui-craft/references/motion.md").is_file()
    for index, flags in enumerate(((), ("--codex",), ("--opencode",), ("--codex", "--opencode"))):
        project = base / str(index)
        project.mkdir()
        setup(project, *flags, "--dry-run")
        assert not list(project.iterdir()), "dry run wrote files"
        setup(project, *flags)
        for source in SKILLS.iterdir():
            installed = project / ".agents/skills" / source.name
            assert installed.is_symlink(), f"{flags}: missing shared skill {source.name}"
            assert installed.resolve() == project / ".claude/skills" / source.name
            for resource in source.rglob("*"):
                if resource.is_file() and "__pycache__" not in resource.parts:
                    assert (installed / resource.relative_to(source)).read_bytes() == resource.read_bytes(), resource
        assert (project / ".codex/config.toml").exists() == ("--codex" in flags)
        assert (project / "opencode.json").exists() == ("--opencode" in flags)
        # A copied project owns its files: rerunning setup must preserve local content.
        local_skill = project / ".claude/skills/ui-craft/SKILL.md"
        local_skill.write_text("project-specific craft\n")
        setup(project, *flags)
        assert local_skill.read_text() == "project-specific craft\n", "overwrote project skill"
    # Existing directories and dangling links are kept for manual comparison, not replaced.
    project = base / "existing"
    custom = project / ".agents/skills/ui-craft"
    custom.mkdir(parents=True)
    (custom / "SKILL.md").write_text("local override\n")
    dangling = project / ".agents/skills/verify"
    dangling.symlink_to("missing-local-skill")
    setup(project)
    assert (custom / "SKILL.md").read_text() == "local override\n"
    assert dangling.is_symlink() and not dangling.exists()

print("Shared skills: template copy, default, Codex, OpenCode, combined; references, dry run and existing files passed")
