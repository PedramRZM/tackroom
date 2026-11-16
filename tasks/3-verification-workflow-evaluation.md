---
id: 3
title: Evaluate verification and feedback-driven harness improvements
type: task
status: inbox
priority: p2
epic: 0
blocked-by: [1, 2]
interactive: false
created: 2026-11-15
---

## Goal

Turn human corrections and verified agent mistakes into candidate improvements to the harness,
then keep or prune guidance using observed missed defects, noise and cost. Establish that a
lesson helps future sessions instead of merely recording that the original mistake was fixed.

## Context

Task 1's scratch evidence, task 2's pilot, `docs/keeping-current.md`,
`template/.claude/skills/write-tests/` and the repository's pre-change Git revision.
Reuse `template/.claude/skills/dream/SKILL.md`, the memory inbox and dream report described in
`docs/memory-and-dreaming.md`. Research:
[`feedback learning loop`](../refs/notes/2026-11-15-feedback-learning-loop.md) and
[`existing adaptive-harness proposal`](../refs/notes/2026-11-13-adaptive-harness-learning.md).

## Acceptance criteria

AC1. Held-out tasks cover a bug, business rule, UI state, token violation and trivial edit.
Check: freeze expected outcomes and scoring before running either configuration.
AC2. Old/new configurations use the same model, budget and fixtures with repeated trials.
Check: retain transcripts, tool exits, costs and failure evidence; do not score by self-report.
Run the live old/new comparison with Codex here and keep shared guidance/installations usable
by Claude Code and OpenCode. Report their unmeasured runtime effectiveness explicitly; if
those runtimes become available, compare within each harness rather than pooling results.
AC3. Report defect detection, unnecessary tests/dependencies, false alarms, flakiness and
elapsed/cost differences. Check: reproducible table with denominators and limitations.
AC4. Make a keep/change/remove recommendation. Check: every retained prescription has an
observed benefit or an explicit untested-risk rationale, with recurrence, human correction
effort and instruction overhead included alongside the AC3 metrics.
AC5. Human corrections and agent/tool-discovered mistakes become attributable learning cases.
Check: trace one of each from its task/session and harness revision through expected versus
observed behavior, evidence and disposition into the existing inbox/dream flow. Classify a
changed requirement or local preference separately from a factual error; preserve scope and
unresolved contradictions, and do not interpret silence as success or a guess as a verified cause.
AC6. One feedback-derived proposal is evaluated on its reproducer, unseen related cases and
known-good cases before adoption. Check: record a small candidate diff and old/new evidence;
reject a deliberately regressing candidate, retain a rollback revision, and present any
successful candidate for human acceptance. Repeated use of the same holdout is disclosed;
do not tune on its answers or claim a single repaired case proves general improvement.

## Feedback loop to exercise

Correction or verified failure → evidence linked from the memory inbox → dream groups and
checks the lesson → one candidate test/lint/helper/skill/memory change → baseline comparison
and independent review → human accepts or rejects → observe later recurrence and regressions.

Prefer fixing a concrete tool/environment defect or adding a meaningful check when that is
the cause. Use existing dream proposal thresholds and pruning; do not append every correction
to always-loaded instructions. Include useful successful approaches and clean cases too.
For the pilot, a small record linked from the inbox is enough; no automated feedback service
or new memory store is required. Cross-harness inputs may be explicit user corrections and
tool evidence; native Codex/OpenCode transcript ingestion must not be assumed to exist.

## Constraints

No live production work. A scratch smoke run is not an A/B benchmark or evidence of optimality.
This is learning through persistent context and tooling, not updating model weights. Keep
project-specific preferences scoped to their project. Do not weaken tests or acceptance
criteria, alter permissions, or silently promote a proposal to make the comparison pass.

## Out of scope / do not change

Automatic promotion of instruction changes, model/provider selection, a feedback collection
service, new native transcript exporters, or cross-project synchronization.

## Notes

2026-11-16: Owner clarified multi-harness setup scope for all tasks, with only Codex required
for live validation here. AC2 preserves portable artifacts while limiting empirical claims
to the harness actually evaluated. Unavailable Claude/OpenCode access does not block this
comparison; results must not be generalized to their runtime behavior.

2026-11-15: Owner requested adding learning from human feedback and agent mistakes. Expanded
this inbox task accordingly; this is an authorized scope addition, not a change to make an
implementation pass. Capture/consolidation already exists; the added work is traceability,
evaluation and reviewed adoption. No learning-loop implementation is claimed by this edit.

2026-11-15: Skill evals were already identified as the largest validation gap in the staff audit.
