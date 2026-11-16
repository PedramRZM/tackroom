# Reuse the existing feedback flow

The [2026-11-11 dream report](../../../.agents/dream-report.md) already connects an owner's
quoted correction to session `20261110-1849-c6618e80.txt`, observed rework and disposition.
Its second proposal declines new guidance because the no-registry rule already exists.
The first catches a conflicting hook workaround. That is sufficient capture for this pilot;
neither a new collector nor another memory format is needed. Report introduced at `23ff57c`.
This inspection did not run dream again, rewrite its report or claim long-term effectiveness.

## Human correction: validation scope

- Source: owner messages in the task 1–2 conversation on 2026-11-16: multi-harness setups
  throughout, but only Codex live validation is required on this machine. Task 1 base was
  `9f88d9a`; correction and evidence merged at `a82eacc`.
- Classification: owner requirement/local validation policy, not a universal factual claim
  that other runtimes never work. The earlier agent had expanded the completion gate to
  all three live harnesses. Expected: portable packages plus bounded claims from actual runs.
- Evidence: [task 1 scope and results](../1-verification-before-implementation/multi-harness.md)
  preserves Codex success, Claude account failure and deficient exploratory OpenCode plans.
  The owner clarified the requirement across several messages; no timed estimate of human
  effort exists. These messages are one correction episode, not independent recurrences.
- Disposition: [scoped decision](../../decisions/multi-harness-validation.md), task criteria
  clarified, existing dated inbox entry. No new always-loaded instruction or feedback system.
  No later recurrence observed in task 2's Codex pilot; this is one follow-up, not a rate.

## Verified agent mistake: omitted verification evidence

- Source: task 1 OpenCode initial planning run, harness 1.3.10, recorded model
  `google/gemini-3-flash-preview`; base `9f88d9a`. Full provenance and tool reads in the
  [retained run record](../1-verification-before-implementation/multi-harness.md).
- Expected: permission checks at storage, enforcement fixtures for all used style forms,
  maintenance costs and distinct visual/accessibility/usability limits.
- Observed: [initial output](../1-verification-before-implementation/opencode-plan-20261116-first.md)
  omitted these despite reading relevant guidance. This is an observed output deficiency;
  its internal cause is unknown. Do not generalize it to all models or harnesses.
- Disposition: the [five-line reminder](../1-verification-before-implementation/rejected-omission-audit.diff)
  was tried, omissions recurred in one additional OpenCode run, and the reminder was removed.
  The two results reuse one scenario. The Codex comparison here tests transfer to new cases;
  it cannot establish a fix for OpenCode. Rollback: skill content at `9731d98`.
- Correction effort: one candidate drafted, one additional run per harness in task 1, then
  removal. Human review minutes were not recorded; do not invent a savings estimate.

The current evaluation's linked inbox note supplies both traces to a future dream pass.
Native transcript export remains Claude-specific; explicit notes and supplied plain-text
logs are the existing portable route. Nothing silently ingests Codex or OpenCode sessions.
Any successful proposal still needs human acceptance; silence is not approval.

This use of existing records follows the [feedback research synthesis](../../../refs/notes/2026-11-15-feedback-learning-loop.md).
The exact small-case rubric and adoption threshold are local judgment calls, not universal
research results. Their predictive value remains limited by the pilot size.
