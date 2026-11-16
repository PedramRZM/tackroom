---
id: 1
title: Choose verification and quality tools before implementation
type: task
status: done
priority: p1
epic: 0
blocked-by: []
interactive: false
created: 2026-11-15
---

## Goal

Before coding a substantive change, the agent maps expected behavior and quality risks to
the smallest sufficient checks and recommends missing tools that fit the project. Its final
evidence distinguishes functional success, code constraints, UI regressions and UX judgment.

## Context

`template/.claude/skills/{write-tests,task,spec,verify,kickoff}/SKILL.md`,
`template/WORKFLOW.md`, task and PR templates, `docs/testing.md`,
`refs/notes/2026-11-13-claude-team-bdd-e2e.md`, and the 2026-11-15 audit.

## Acceptance criteria

AC1. Before implementation, guidance maps each substantive criterion to an expected result,
appropriate test level, setup and runnable check, reusing the task instead of requiring a
separate document. Check: scratch agent plans a feature with success, failure and permission
examples, using the shipped skills before writing implementation.
AC2. The agent selects tools from the project's existing stack and recommends missing quality
checks with limitations and cost. Check: scratch design-token scenario distinguishes CSS,
JS/TS and utility-class coverage and proposes known-good and known-bad rule fixtures.
AC3. UI verification separates interaction, visual comparison, automated accessibility and
human usability assessment. Check: scratch plan identifies evidence and limits for each.
AC4. The workflow stays proportional: BDD does not require Cucumber, TDD is a loop rather than
a test level, and trivial copy changes do not require new tests. Check: scratch responses for
a behavior change and a copy-only change; inspect the shipped reference.
AC5. New prescriptions trace to saved primary sources or are explicitly local judgments.
Check: audit source register, named-page resolution, gap table and `docs/testing.md` links.
AC6. Packaging remains valid. Check: `scripts/agent/check` passes all checks;
`tools/setup /tmp/<scratch> --codex --opencode` installs the shared skills and references,
followed by a bounded live Codex planning exercise with actual skill/reference reads.
Validate Claude Code and OpenCode setup through packaging/configuration checks and record
runtime limits separately. Unavailable model access is not a completion gate; do not present
static validation as successful live behavior in those harnesses.

## Edge cases and data changes

Existing failing checks, missing browser setup, flaky/retry-green tests, a changed expected
result, generated token definitions and third-party styles must be reported explicitly.

## Constraints

Edit template first, preserve dogfood copies, no new runtime dependencies or mandatory model
choice. Original no-commit constraint was superseded by the owner's 2026-11-16 request to
commit, merge into main and mark done. No push or publication was requested.

## Out of scope / do not change

Production app lint configurations, a new universal test runner, CI security boundaries,
new hooks and claimed optimality without measurements.

## Notes

2026-11-16: Owner accepted the reviewed result and explicitly requested commit, merge to
main and done status. AC1–6 evidence is in
`docs/evidence/1-verification-before-implementation/multi-harness.md`; all 11 checks passed
and independent review found no remaining issues under the clarified scope. Retired the
completed plan; lasting scope decision is in `docs/decisions/multi-harness-validation.md`.

2026-11-16: Owner clarified the scope: portable setups in every task; live validation here
uses Codex. AC6 now reflects that explicit instruction, superseding the original mandatory
Claude exercise and the agent's subsequently over-scoped all-harness live gate. Codex AC1–4
were demonstrated with executed reads and reviewed plans. Shared installation/configuration
checks cover all three targets; Claude runtime is unavailable. Exploratory OpenCode runs
completed but missed planning requirements; preserve this limitation, not a runtime guarantee.
An unsuccessful five-line guidance candidate was removed. Current branch:
`task/1-verification-portability`; evidence: `docs/evidence/1-verification-before-implementation/multi-harness.md`.
Implementation/evidence are ready for owner review; no commit, push or PR is authorized.

2026-11-16 (earlier, superseded by clarification above): resumed for epic 0 on `task/1-verification-claude-evidence`, based on
`main` at `9f88d9a`. The implementation is already committed in repository history; the
uncommitted description below is historical. Baseline all 11 checks passed. Fresh
`tools/setup --tracker files --codex` and the unchanged bounded scenario were retried;
Claude exited 1 with `is_error: true`, no model response and $0 cost because account
verification is still required. AC6 remains incomplete. Next: restore Claude account access,
then repeat the recorded exercise and inspect its actual reads and plans. Evidence:
`docs/evidence/1-verification-before-implementation/claude-attempt.md`. No commit or push.

2026-11-15: Implementation is present, uncommitted. Local checks and bounded Codex planning
exercise passed; independent review found no implementation defects. The initial exercise
omitted explicit usability limits; a focused reporting correction and identical fresh exercise
added them. Claude's live exercise could not reach a model response because the account
requires verification. AC6 therefore remains incomplete; no task/PR completion is claimed.
Evidence: `docs/evidence/1-verification-before-implementation/`. Next: restore Claude account
access and rerun the recorded scratch command, then owner review. No commit or push performed.

2026-11-15: Owner clarified that the setup is cross-harness and asked about Codex goals.
Extended supporting loop docs with native Codex/Claude entry points and a shared task/check
fallback. Codex CLI 0.169.0 reports goals stable/enabled; no duplicate goal skill is needed.

2026-11-15: Owner explicitly requested task creation and implementation; started on branch
`task/1-verification-before-implementation`. Baseline: all 10 checks passed. No root
`WORKFLOW.md` or task tracker existed; local tasks use the repository's own template format.
