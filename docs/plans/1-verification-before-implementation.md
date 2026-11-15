# Plan: 1 — verification before implementation

Task: [1](../../tasks/1-verification-before-implementation.md).

## Steps

- [x] Baseline checks and existing research/template audit.
- [x] Resolve named primary sources and save missing testing references.
- [x] Extend existing workflow/skills with a compact verification plan and tool reference.
- [x] Run full checks, bounded Codex planning exercises and independent review.
- [ ] Complete the scratch Claude behavior exercise (attempted; account verification blocks it).
- [x] Record evidence and leave uncommitted changes for owner review.

## Progress

2026-11-15: Added five shared-skill updates, conditional tool reference, task/PR fields,
research and cross-harness goal documentation. Fifteen new primary refs; index 1,817 items.
Independent reviewer checked sources, packaging, all changed copies and full checks. Codex
read-only planning succeeded; a first-run omission of explicit usability evidence prompted a
three-line reporting correction and a fresh successful planning exercise. Claude attempts
returned DNS failure, then account verification restriction after authorized network retry.
Task stays needs-human until that required exercise can run. No commit/push/PR created.

2026-11-15: Baseline all 10 checks passed. Branch created. Research is split between named
source verification and testing/tool evidence. Prior BDD note was research-only; avoid
duplicating existing write-tests/verify/lock-tests features.

## Dead ends

Sandbox blocked uv cache writes and Git ref creation; authorized escalated commands succeeded.
There was no root WORKFLOW.md or local tracker; created local tasks using the template format.
Claude's first scratch attempt could not reach the API; the network retry reached it but the
account could not receive replies. Both spent $0. Do not retry until the account state changes.

## Decisions

Owner requested implementation; task 1 is authorized without another ready-state question.
Use local task files. Preserve owner-only commits. Reuse skills; no new services or hooks.
User clarified cross-harness scope: native `/goal` exists in both Codex and Claude, so no
duplicate skill. Root `.agents/skills` are tracked copies; the five affected ones were mirrored
as well as `.claude`, preserving unrelated harness-specific differences.

## Evidence

Baseline and post-change: `scripts/agent/check` → all 10 checks passed. Final output lives in
[`checks.txt`](../evidence/1-verification-before-implementation/checks.txt).

| Criterion | Evidence and limits |
|---|---|
| AC1 | [Codex plan](../evidence/1-verification-before-implementation/codex-plan-recheck.md) maps success/failure/permission examples to checks/setup; no production code edited |
| AC2 | Plan selects CSS/JS/utility checks, valid/invalid fixtures, cost and coverage limits; no app-specific linter installed |
| AC3 | Recheck distinguishes visual inspection/baselines, accessibility and unverified representative-user usability; first-run omission retained for comparison |
| AC4 | Copy-only case adds no suite/dependencies; behavior case reuses ordinary tests without Cucumber |
| AC5 | [Audit](../../refs/notes/2026-11-15-verification-workflow-audit.md), primary metadata, source/locator checks and independent review |
| AC6 | Full local checks, YAML/skill validation and fresh setup pass; [Claude exercise](../evidence/1-verification-before-implementation/claude-attempt.md) blocked before model response |

[Execution record](../evidence/1-verification-before-implementation/codex-execution.md) proves
actual skill/reference reads. The Codex runtime disabled untrusted project configuration;
this does **not** validate Codex hooks, trust/permissions, automatic skill selection or goals
end to end. No application browser suite, vendor launcher endpoint or comparative benchmark
was run. This is a planning smoke test, not proof of optimized product outcomes.
