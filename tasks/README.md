# Tackroom tasks

This repository uses local task files, with the format in
[`template/tasks/TEMPLATE.md`](../template/tasks/TEMPLATE.md) and states explained in
[`docs/tasks.md`](../docs/tasks.md). These are work on tackroom, not sample tasks to copy into
other projects. No issue tracker or cross-project management service is being introduced.

The owner requested the 2026-11-15 harness audit, task breakdown and implementation. That
authorizes starting task 1; other proposals stay in the inbox for prioritization. No task is
marked done until the owner accepts it. Work remains uncommitted until requested.

All current and future tasks target setups for Codex, Claude Code and OpenCode. Keep shared
workflow/skills harness-neutral and add only supported per-harness configuration where needed.
Codex is the available live validation harness on this machine. Validate the other targets
through installation, shared-file parity and configuration checks, and name untested runtime
behavior. Do not block portable setup work on unavailable model access or claim runtime
equivalence from static checks. This scope is the owner's 2026-11-16 clarification.

| Task | Scope | State |
|---|---|---|
| [0](0-verifiable-harness.md) | Epic: verification before implementation | in-progress |
| [1](1-verification-before-implementation.md) | Portable verification planning and tool selection | done |
| [2](2-project-verification-pilot.md) | agent-dev-infra readiness CLI verification pilot | done |
| [3](3-verification-workflow-evaluation.md) | Reuse dream feedback; evaluate old/new guidance | done |
| [4](4-task-completion-gate-trial.md) | Evaluate an opt-in deterministic completion gate | inbox |
| [5](5-parallel-integration-ownership.md) | Integration ownership and review-finding validation | inbox |
| [6](6-hard-limits-for-goal-examples.md) | Correct misleading prose limits in the loop recipe | done |
| [7](7-selective-harness-installation.md) | Epic: shared template and selective GitHub installation | done |
| [8](8-centralize-harness-template.md) | One canonical harness source, adapters and capability catalog | done |
| [9](9-selective-local-installation.md) | Select agents and optional app capabilities during installation | done |
| [10](10-github-harness-bootstrap.md) | Bootstrap from GitHub in an app without a local checkout | done |
| [11](11-safe-harness-updates.md) | Explicit updates preserving local edits and project knowledge | done |

Suggested order: 1, 6, 2, 3. Evaluate 4 and 5 only if the pilot demonstrates the corresponding
problem. Their existence is not a decision to install more hooks or agents.

Selective-installation work follows 8 → 9 → 10 → 11 under epic 7. The owner requested
implementation of the entire epic, then added explicit updates preserving project knowledge. See the [spec](../docs/specs/selective-harness-installation.md)
and [owner-directed scope decision](../docs/decisions/0001-selective-harness-installation.md).

Epic 7 and tasks 8–11 are complete and published on main, as requested by the owner.
See [installation](../docs/installation.md) and [acceptance evidence](../docs/evidence/7-selective-harness/README.md).
