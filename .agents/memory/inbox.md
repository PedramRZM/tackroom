# Inbox

One dated line per thing a future session would otherwise have to rediscover: what is true, and
how you found out. The `dream` pass folds these into the memory files and empties this list.

- 2026-11-11: Renamed claude--template to tackroom (folder ~/Dev/tackroom) to publish it. Saved third-party texts are gitignored; only meta.json is tracked, and citations in docs/notes/prompts link to the source URL with the local path as link text.

- 2026-11-13: tools/refs article truncates URL path slugs to 80 characters, so different files under a commit-pinned GitHub repository can collide and be skipped as existing. Verify saved meta.json URLs; an explicit unique query parameter preserves distinct files without editing saved sources. See refs/notes/2026-11-13-anthropic-public-repo-configs.md.

- 2026-11-14: Codex custom roles must be added to template/.codex/agents first; root-only roles never reach tools/setup. The codex-agent-parity check covers role sets, Claude brief parity, root copies and a fresh install.

- 2026-11-15: Codex CLI 0.169.0 is installed and reports goals stable/enabled. Root .agents/skills are tracked copies (not setup symlinks); mirror affected portable skills there as well as .claude. Fresh tools/setup --codex uses symlinks. See docs/plans/1-verification-before-implementation.md for bounded skill probes and live-test limits.

- 2026-11-15: Portable UI guidance is `ui-craft` (avoids personal `ui-design` name collision); its source register records misleading extracted dates. Claude scratch trial hit provider account verification; do not treat validators or the independent static rehearsal as a live skill run. See docs/ui-craft.md and docs/evidence/ui-craft/README.md.
- 2026-11-15 follow-up: The template itself now ships all shared skills in `.agents/skills/` and setup installs them without flags. Live Codex CLI 0.169 read UI craft and its references and reviewed the fixture; OpenCode debug confirmed discovery. This supersedes the earlier no-live-Codex limitation for that narrow trial only.
2026-11-16: Task 6 verified Claude Code 2.1.323 accepts/enforces hidden `--max-turns`: local synthetic `/goal` probes with caps 1/2 made 1/2 requests then exited 1 (`error_max_turns`), while `num_turns` reported 2/3. Prose goal limits remain model-judged; budget estimates can overshoot. See `refs/notes/2026-11-16-headless-goal-limits.md`; no provider calls or live goal evaluation were tested.

- 2026-11-16: Task 6 cross-harness follow-up: actual Codex 0.169/OpenCode 1.3.10 discovery finds all 12 shared skills; Codex skill visibility does not imply trusted project config. Native goal budget/steps parsing passed, exhaustion was not tested. GNU timeout stopped real headless clients against stalled local endpoints (exit 124); see refs/notes/2026-11-16-headless-goal-limits.md. No provider calls or persistent config changes.

2026-11-16: Owner clarified all tackroom tasks must produce Codex/Claude Code/OpenCode setups, but live validation here uses Codex; validate other targets with shared packaging/configuration checks and explicit runtime limits, not mandatory unavailable model access. See tasks/README.md and docs/evidence/1-verification-before-implementation/multi-harness.md.

- 2026-11-16: Task 3 reuses the existing dream report for human feedback; no new collector. Human multi-harness scope clarification and measured OpenCode plan omission are traced separately (requirement vs observed error) in `docs/evidence/3-verification-workflow-evaluation/feedback.md`; the linked bounded evaluation retains failed candidates, limits and rollback. Native Codex/OpenCode transcript ingestion remains unimplemented.

- 2026-11-16: Owner requested a task for one canonical template with shared base, optional app/stack skills and independently selectable agent adapters, installable from GitHub inside any app. Epic 7/tasks 8–10 and decision 0001 record it; this authorizes selective distribution, not cross-project sync or registry management.

- 2026-11-16: During epic 7 the owner explicitly added easy project-local sync/update with memory and dream reports untouched. Task 11 supersedes the prior no-update scope, while no central registry/background service remains. Shared sources now live in template/.agents; regenerate adapters/catalog/root links with tools/render-harness --write --dogfood.

- 2026-11-16: Owner rejected even checked-in generated per-agent template outputs. Final epic 7 uses no native template directories or catalog: skill folders include install.json, brief bodies have sibling metadata, adapters.json defines native config, CLI generates destination files. Root native outputs are gitignored; .agents/skills points to canonical template skills. GitHub installs inventory only the pinned template tree.
