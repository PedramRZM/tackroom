# Inbox

One dated line per thing a future session would otherwise have to rediscover: what is true, and
how you found out. The `dream` pass folds these into the memory files and empties this list.

- 2026-11-11: Renamed claude--template to tackroom (folder ~/Dev/tackroom) to publish it. Saved third-party texts are gitignored; only meta.json is tracked, and citations in docs/notes/prompts link to the source URL with the local path as link text.

- 2026-11-13: tools/refs article truncates URL path slugs to 80 characters, so different files under a commit-pinned GitHub repository can collide and be skipped as existing. Verify saved meta.json URLs; an explicit unique query parameter preserves distinct files without editing saved sources. See refs/notes/2026-11-13-anthropic-public-repo-configs.md.

- 2026-11-14: Codex custom roles must be added to template/.codex/agents first; root-only roles never reach tools/setup. The codex-agent-parity check covers role sets, Claude brief parity, root copies and a fresh install.

- 2026-11-15: Codex CLI 0.169.0 is installed and reports goals stable/enabled. Root .agents/skills are tracked copies (not setup symlinks); mirror affected portable skills there as well as .claude. Fresh tools/setup --codex uses symlinks. See docs/plans/1-verification-before-implementation.md for bounded skill probes and live-test limits.
