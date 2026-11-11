---
name: repo-purpose-and-scope
description: What tackroom is for, what it deliberately does not do (no cross-project sync), the owner's rules for it, and the machine facts that shape it. Read first before changing structure or proposing tooling.
---

# Repo purpose and scope

- The repo is a personal library of agentic-coding setups. `template/` mirrors a project root and
  is copied into projects by hand, or with `tools/setup <dir>`. `refs/` holds the saved research.
  `docs/` explains the choices and cites refs. Source: `AGENTS.md`.
- **No cross-project orchestration.** On 2026-11-10 the owner said: "i dont want to make this a
  single source of truth among all projects, just a repo to keep my setups centralized and use
  manually in any projects, so i dont need orchestration over projects here." A sync engine with
  a project registry (`tools/projects.py`, plan/apply, conflict tracking, 11 passing tests) was
  built earlier that day and then deleted. Do not rebuild registry, sync, drift or fleet tooling
  unless the owner asks. See [[process-lessons]].
- **Global config is untouched.** Earlier the same day the owner asked for `~/.claude` to be
  emptied because the repo would be the only source of truth. That was put on hold. A backup
  exists at `~/.claude/backups/global-config-before-template-2026-11-10.tar.gz` (1,444 entries,
  includes `~/.config/opencode`). Ask before deleting or editing anything under `~/.claude` or
  `~/.config/opencode`.
- **Research-grounded.** Each rule, skill, hook or workflow should trace to a source in `refs/`.
  Anything that cannot be traced is labelled as a judgement call. The corpus and how it is
  fetched: [[refs-fetching]].
- **Machine facts (2026-11-10).** Ubuntu 24.04, zsh. Installed: uv 0.12.24, node 24.22.1 (nvm),
  pnpm, bun, gh 2.88.1, git, jq, rg, ffmpeg, Claude Code 2.1.322, OpenCode 1.3.10. Not installed:
  codex, gemini, aider, crush, kimi, qwen, yt-dlp, whisper, nvidia-smi (no GPU used).
  `python3` is the pyenv shim, 3.10.13, with no `tomllib`. Scripts that need 3.11 run through
  `uv run --python '>=3.11'`.
- **Owner's stack.** TypeScript (Next.js, React, Tailwind/shadcn, Prisma/Postgres), Rust, Python
  with uv. About 25 sibling repos under `~/Dev`. Several use hamgit or GitLab remotes, and some
  have no remote, so GitHub-only assumptions do not hold everywhere.
- Related: [[template-hooks-and-guard]], [[task-management-design]], [[model-routes-and-harnesses]],
  [[memory-dream-design]], [[live-testing-harnesses]].
