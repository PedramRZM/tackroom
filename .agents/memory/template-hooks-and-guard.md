---
name: template-hooks-and-guard
description: The template's Claude Code and Codex hooks (guard, stop check, format, session context), the settings they ship with, their test commands, and the root-copy rule. Read before editing template/.claude, template/.codex or the root copies.
---

# Template hooks, guard and settings

## Files

- `template/.claude/hooks/guard.py`: PreToolUse for `Bash|Read|Edit|Write|NotebookEdit`, and for
  Codex `apply_patch` (the patch text names `*** Update File:` lines).
- `template/.claude/hooks/stop-check.py`: Stop. When the tree changed it runs
  `scripts/agent/check --quick` and blocks with `{"decision": "block"}` on failure. It lets the
  session stop when `stop_hook_active` is set. Exit code 3 from the check means "no checks configured".
- `template/.claude/hooks/format.py`: PostToolUse on Edit|Write. It uses only the project's own
  formatter (biome, prettier, rustfmt, gofmt) and never blocks.
- `template/.claude/hooks/session-context.sh`: SessionStart on startup|resume|compact. It prints
  the branch, the uncommitted count, the task id from a `task/<id>-<slug>` branch, the plan file,
  the task file, and the memory inbox count. At 15 or more inbox lines it suggests `/dream`.

## guard.py rules

- Always on: **secrets** (env files, private keys, registry credential files, and shell commands
  that name them; `*.example`, `*.sample`, `*.template`, `*.pub` are allowed), **wipe** (`rm -r`
  on the repo root, home, `/` or a parent; force pushes, while `--force-with-lease` is allowed),
  **main** (pushes to `main`, `master`, `production`, `release` are blocked; agents push task
  branches and the owner merges), **memory** (`.agents/memory/` is written only by the
  `memory-analyzer` and `memory-organizer` agents; `inbox.md` is open to all).
- Opt-in for a session: `--careful` (history and data destruction) and `--lock-tests` (test
  files). The `careful` and `lock-tests` skills set them.

## Tests and timing

- `template/.claude/hooks/tests/test_guard.sh` runs from anywhere. Count went 44, then 51 (protected
  branches), then 56 (Codex patch cases). The last run was 56 passed, 0 failed.
- Hooks call `/usr/bin/python3`, not the pyenv shim. Five guard calls took 1.09 s through the shim
  and 0.29 s with `/usr/bin/python3` (2026-11-10). The settings and skills were changed to match.

## Codex

- The same guard handles `apply_patch`. Only unit cases cover it. It has not run under Codex,
  which is not installed.
- A Codex Stop hook must print JSON on stdout when it exits 0, so `allow()` prints `{}`. Codex
  also asks for per-hook review, and again after a script changes.

## Shipped `settings.json` (template)

- Allow: `Bash(scripts/agent/check *)`, `Bash(scripts/agent/next-task *)`. Ask: `Bash(gh pr merge *)`.
- Deny reads: `.env` and `.env.*` (with `!` exceptions for `.example`, `.sample`, `.template`),
  `*.pem`, `id_rsa`, `id_ed25519`, `~/.aws/**`, `~/.gnupg/**`, `~/.kube/**`, `~/.netrc`,
  `~/.git-credentials`, `~/.docker/config.json`.
- Sandbox: `enabled` is removed (see [[live-testing-harnesses]]). `credentials.envVars` denies
  ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, ZAI_API_KEY, DEEPSEEK_API_KEY, MOONSHOT_API_KEY,
  KIMI_API_KEY. `network.allowedDomains` lists the npm, PyPI and crates registries.
- Hooks use `${CLAUDE_PROJECT_DIR}` paths.

## Docs facts behind the design (from `refs/notes/claude-code-docs-settings-security.md`)

- A project file cannot set `permissions.defaultMode` to `auto` or `bypassPermissions`. The
  `autoMode` keys are user-level only.
- Project allow rules, hooks, `env` values and `statusLine` wait for workspace trust. Deny and ask
  rules apply at once.
- On macOS, Linux and WSL, Glob and Grep are absent from the default tool set. Searches go through
  Bash, so matchers on `Grep|Glob` rarely fire.

## Root copies

- The repo's own `.claude/`, `CLAUDE.md`, and `scripts/agent/{check,next-task,claude-with,keys.example,github-labels}`
  are copies of `template/`. The root check `root-matches-template` fails on drift. Refresh them by
  copying from `template/` and re-running the check.
- `template/AGENTS.md` aims for under about 100 lines. `template/CLAUDE.md` is `@AGENTS.md` plus a
  comment. Claude Code reads CLAUDE.md, and the other harnesses read AGENTS.md.

## Checks

- Root `scripts/agent/check`: compile, config-parses, guard-tests, root-matches-template,
  instruction-size, skill-limits, skills-validate, agents-validate (`claude plugin validate`).
  Result on 2026-11-10: 8 of 8 passed. `--quick` skips the two validators (6 checks, passed).
- Template `scripts/agent/check` is a placeholder. It exits 3 until the project edits its
  CHECKS section.
- `stop-check.py` was exercised in a scratch repo: a clean tree is silent, a failing lint blocks,
  `stop_hook_active` allows, a fixed tree passes, and an unchanged tree is skipped through a marker
  file in the temp dir.

Related: [[task-management-design]], [[process-lessons]].
