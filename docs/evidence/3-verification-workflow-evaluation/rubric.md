# Frozen before trials

This is a synthetic package comparison, not a production benchmark. Five changes share one
session, so the experimental unit is a bundle, not five independent model observations.
Two repetitions per configuration, alternating old/new. No prompt or scorer tuning after
results. Same Codex 0.169.0, model `gpt-6.1-sol`, low reasoning, 180-second process deadline,
same task, fixtures and flags. Record tokens rather than estimating unavailable dollar cost.
The deadline is a common resource ceiling, not an equal number of output tokens.

Old guidance: `b8ce42c`; new: `9731d98`. Copy all files in write-tests, verify and ui-craft
when present at each revision into `.agents/skills`; no other repo guidance. This measures
the package, including added references, not a causal effect of any individual sentence.

## Outcome scoring

`score.py` is kept outside the model working directories. Seventeen frozen assertions cover
boundary repair, real SQLite storage after denial/success, optimistic failure, exact allowed
tokens, unchanged valid paths and exact copy. Count each of four defect categories as repaired
only if all its fault assertions pass. Report trivial edit separately, and all four clean
assertions separately. A clean assertion failure is a behavioral false alarm/regression proxy;
it does not measure every possible false-positive recommendation.

Human review records new tests solely checking the trivial heading (unnecessary for this
fixture), dependencies added, and weakened existing expectations. Count test methods and
inspect their purpose; the number alone is not usefulness. Run each final submitted suite
twice and report failures/inconsistency, not broad claims of flake freedom. Compare transcript
commands with final tests and retain nonzero exits, timeouts and unfinished attempts.

Report elapsed seconds, usage input/output/cached tokens, actual tool failures, lines/bytes
of delivered guidance, and final results. Add comparative interpretation only at bundle level.
No rendered browser, network, paid provider launcher or representative users are involved.

## Feedback candidate

Use the unchanged five-line omission reminder from task 1. Compare current guidance with and
without it, each once, same model/180s ceiling, on a planning bundle containing the original
invoice reproducer, two unseen related cases and a known-good trivial change. This repeats
the original case, not the related cases; do not tune on either result. Independent reviewer
scores actual plan text with these yes/no requirements per applicable scenario:

- invoice: direct viewer denial and persisted unchanged state; approver persisted success;
  failure unchanged; download contents; CSS/inline/utility enforcement fixtures and cost;
  visual comparison vs inspection, accessibility gaps, unverified user usability; setup unknown.
- archive: admin-only direct API and SQLite unchanged after denied/failed archive; archived
  state after success; exact deny/allow fixtures; unavailable service explicitly untested.
- profile: optimistic failed save preserves committed data and permits retry; CSS and inline
  token enforcement allow/deny fixtures and gaps; keyboard/error announcement checks; visual
  baseline and representative-user limits.
- clean: exact `Invoices` heading inspection plus existing checks; no new dependency or test
  suite solely for a copy edit; no claim of a browser check having run.

Adopt no reminder unless it repairs a missing applicable requirement without losing a clean
requirement. Equal passing outputs mean no demonstrated incremental benefit; reject extra
text. Any apparent success remains a proposal requiring human acceptance. Rollback is the
unmodified skill at `9731d98`. A deliberately faulty implementation control (unconditional
approval) must fail the frozen storage checks while the known-good control passes. This tests
the evaluation's ability to reject regression, not the effectiveness of the prose reminder.
