# Verification before implementation

An agent should decide how it will know the change is right before producing the change.
The current template already has useful checks, bug-first tests, test locks and independent
review. The missing connection is a small pre-code plan that selects evidence for the task
and the project's actual risks.

Research: [source audit](../../refs/notes/2026-11-15-verification-workflow-audit.md),
[existing BDD research](../../refs/notes/2026-11-13-claude-team-bdd-e2e.md).
Tracker: [epic 0](../../tasks/0-verifiable-harness.md).

## Intended behavior

- The task contains concrete behavior examples and a criterion-to-check mapping. A small
  task needs a sentence, not another mandatory document.
- The agent inspects installed tools, existing commands and conventions before recommending
  missing checks. Each recommendation says what risk it catches, what it costs and what it
  cannot prove. No fixed stack or test percentage applies to every project.
- BDD clarifies the expected behavior; TDD iterates against a failing example; test levels
  choose the smallest boundary that proves the behavior. These are complementary decisions.
- Static checks enforce machine-checkable code and design constraints. UI correctness also
  needs browser interactions, visual review and appropriate accessibility/usability evidence.
- Final evidence names the revision/environment, expected result, actual check and gaps. A
  changed test expectation or visual baseline needs a reason tied to the task.

## Scope

Task 1 updates existing skills and templates with a conditional tool-selection reference,
source-backed documentation and scratch exercises. Later tasks trial a real project's setup
and compare outcomes; optional gate/parallel-work experiments require their own evidence.

Owner clarification, 2026-11-16: every task produces setups for Claude Code, Codex and OpenCode;
Codex is the available live validation harness here. Task 1 checks shared packaging and live
Codex planning; task 2 supplies a portable application recipe reproduced in Codex; task 3
compares old/new guidance in Codex without generalizing effectiveness to other runtimes.
Validate other harness configuration/installation statically and name untested behavior.
Unavailable model access is not a completion gate for portable setup work.

Task 3 also closes the feedback loop: human corrections and verified agent mistakes enter the
existing memory inbox/dream process with provenance, produce one small proposed improvement,
and are evaluated against the baseline, unseen related cases and clean cases before human
adoption. Record recurrence and regression after adoption. This extends existing memory and
evaluation work; it does not add a feedback service or retrain the model. Evidence and scope:
[feedback research](../../refs/notes/2026-11-15-feedback-learning-loop.md).

No new services, dependencies, hooks or always-loaded instruction blocks. No claim that a
second model, screenshot, coverage percentage or green suite proves a product is useful.
No universal token linter: enforcement must match the project's token API and style syntax.

## Acceptance

Use task 1's six criteria for the portable change. A live planning smoke test establishes
that the skills can be loaded and followed; task 3 measures whether they improve outcomes.
