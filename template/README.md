# template/

A project root in miniature. Copy what you want into a project (`tools/setup <project>` does it
without overwriting anything). This file is not copied.

## Every project

| File | What it is for | After copying |
|---|---|---|
| `AGENTS.md` | The instructions every harness reads at session start | Fill in; keep under about 100 lines |
| `CLAUDE.md` | One line that imports `AGENTS.md` for Claude Code | Leave as is |
| `WORKFLOW.md` | How a task moves from idea to merged | Keep the tracker line that applies |
| `scripts/agent/check` | The one command that says the repository is healthy | Replace the detection with real commands |
| `scripts/agent/next-task` | Picks the next ready task by a fixed rule | Nothing |
| `.agents/memory/` | Project memory: index, inbox, files written by the dream pass | Nothing |
| `docs/decisions/`, `docs/specs/`, `docs/plans/` | Decision records, specs for larger work, plans in flight | Nothing |
| `.github/pull_request_template.md` | Evidence per acceptance criterion, risk, how to revert | Nothing |
| `gitignore.additions` | Lines appended to the project's `.gitignore` | Nothing |

## Claude Code (`.claude/`)

| File | What it does |
|---|---|
| `settings.json` | Permission rules, sandbox configuration, the four hooks |
| `hooks/guard.py` | Blocks secret files, wide deletes, force-push, pushes to protected branches, writes to curated memory |
| `hooks/stop-check.py` | Runs the quick checks when a turn ends with changes, and sends failures back once |
| `hooks/format.py` | Formats an edited file with the project's own formatter, if it has one |
| `hooks/session-context.sh` | Prints branch, task id and plan file at session start |
| `hooks/tests/test_guard.sh` | Tests for the guard (not copied into projects) |
| `skills/verify` | Prove a change works: checks, behaviour, evidence per criterion |
| `skills/spec` | Turn a request into tasks with acceptance criteria |
| `skills/task` | Work one task through to a pull request |
| `skills/second-opinion` | Fresh-context review against the task |
| `skills/wrap-up` | Leave the work so a new session can continue |
| `skills/dream` | Review finished sessions, correct memory, propose instruction changes (you start it) |
| `skills/careful` | Block destructive commands for the session (you start it) |
| `skills/lock-tests` | Block edits to tests for the session (you start it) |
| `agents/reviewer.md` | The reviewer used by `second-opinion` |
| `agents/memory-analyzer.md`, `agents/memory-organizer.md` | The two workers of the dream pass |

## Task tracking: one of

| Files | For |
|---|---|
| `.github/ISSUE_TEMPLATE/task.yml`, `epic.yml`, `scripts/agent/github-labels` | Tasks as GitHub issues |
| `tasks/TEMPLATE.md`, `tasks/README.md` | Tasks as files in the repository |

## Optional

| Files | For | Status |
|---|---|---|
| `.codex/config.toml`, `hooks.json`, `agents/reviewer.toml` | Codex | From documentation; not run |
| `opencode.json`, `.opencode/agents/reviewer.md` | OpenCode | Config loads in 1.3.10; nothing else tried |
| `scripts/agent/claude-with`, `scripts/agent/keys.example` | Claude Code on GLM, DeepSeek or Kimi endpoints | From vendor documentation; not run |

Why each piece exists, and what it rests on: `../docs/principles.md`.
