# Verification workflow v2: source audit

Source read in full: Addy Osmani, **How the Claude Code team thinks about verification**,
2026-11-16, [original](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/).
Saved with `tools/refs article ... --collection verification --via jina` in
`refs/articles/claude.dev/blog-how-the-claude-code-team-thinks-about-verification/`.
The saved Markdown retains section headings and links. The supplied X link returned 403;
the official article matches the supplied text and restores its missing linked phrases.

## Source findings and locators

- **Opening:** the author reports roughly 90% of team code written and reviewed by Claude.
  The separate-grader result is up to ten points on structured file generation, not a measured
  improvement in this repository's coding accuracy. No such uplift is claimed here.
- **E2E tests / Verification means running the change:** prioritize executable user journeys,
  useful failure artifacts and a project-specific boot/drive/reset recipe. A feature map can
  supply expectations. A green unit suite alone does not establish integrated behavior.
- **Property tests / Differential tests:** generate inputs for invariants and compare old/new
  behavior for migrations. Normalize irrelevant differences and identify approved deviations.
- **Failing tests require human attention:** three failed repair rounds lead to a person.
- **Code owners write their own checks / Reliability checks trigger on the diff:** owners
  maintain incident-backed trigger/check/rationale entries and run the matching subset.
  Their 39 entries and typical 3–10 matches describe their project, not a template target.
- **One reviewer, multiple rounds / Changes can't modify their own checks:** improve one
  reviewer, retain earlier findings, use base-branch rubrics and fixed commit targets, and run
  local checks before consuming shared review resources.
- **Start a new gate in observe mode:** the team records verification, including absence, and
  trials blocking policy without blocking first. Their gate permits explained bypasses and
  eventually allows a repeatedly blocked commit; that escape is not proof of verification.
- **Test your checks on what actually matters:** replay incidents with answer keys, use stable
  size-matched controls, separate tuning from evaluation, and score successive review stages.
- **Turn misses into rules:** recurrent findings or reproducible incident misses become
  candidate rules, challenged before human acceptance. They also prune accumulated guidance.

## Inference and deliberate differences

Inference: strengthen the existing skills instead of installing another verification framework.
Replay seeds, minimized counterexamples, snapshot manifests and approval/expiry for quarantine
are local implementation judgments. Base-rubric reads help procedural independence but do not
make writable tests or hooks an independent trust boundary.

Retain the project's stricter stop after the same fix fails twice, alongside a cap on three
unsuccessful repair rounds. Retain owner-controlled test deletion/quarantine rather than the
article's permission to delete unresolved flaky tests. Keep risk-based test scope and a few
assembled journeys rather than requiring every edge case to use E2E. Preserve the owner's
local verification and human-preview policy. Do not infer permission for CI, production replay,
automatic rule adoption, increased concurrency or a new commit gate from this article.

Their three-agent challenges are a team procedure, not a portable requirement. The template
uses its existing reviewer and dream proposal process with counterexamples and clean controls.
Existing task-3 evaluation is useful precedent, but its exposed cases are development data;
v2 has no new controlled effectiveness comparison yet.

Implementation and before/after comparison: [verification v2](../../docs/verification-v2.md).
