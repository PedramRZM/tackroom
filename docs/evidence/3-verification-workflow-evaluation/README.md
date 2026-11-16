# Verification guidance evaluation — 2026-11-16

Task [3](../../../tasks/3-verification-workflow-evaluation.md), branch
`task/3-verification-workflow-evaluation`, base `9731d98`. This is a small synthetic evaluation,
not evidence that the current guidance is optimal. No template instructions changed.

## Coding comparison

Two repeated five-case bundles per configuration, alternating old/new, Codex 0.169.0,
`gpt-6.1-sol` with low reasoning, 180-second process deadline, identical task and source files.
The model was discovered from the local app-server default and explicitly pinned for every
trial; no account, provider or global model setting was changed. This pins the configured
model ID, not an independently verified immutable backend snapshot. The common budget is
a wall-clock ceiling; there is no separate token or step cap. [Frozen manifest](frozen.json)
records the inputs and timestamp; [rubric](rubric.md) predates the runs. Old guidance is
`b8ce42c`, current is `9731d98`. Exact full revisions, delivered skill hashes, command lines,
exit codes and timing are in each run's metadata. Trials began from independent scratch roots
with `git init` and staged fixtures, but no HEAD commit.

| Run | Defect categories repaired | Clean paths preserved | Exact copy | Frozen assertions | Final suite, twice | Seconds | Input / cached / output tokens |
|---|---:|---:|---:|---:|---|---:|---|
| old 1 | 4/4 | 4/4 | 1/1 | 17/17 | 8 tests; pass/pass | 62.079 | 153456 / 129024 / 1924 |
| new 1 | 4/4 | 4/4 | 1/1 | 17/17 | 8 tests; pass/pass | 79.509 | 162480 / 119552 / 2506 |
| old 2 | 4/4 | 4/4 | 1/1 | 17/17 | 8 tests; pass/pass | 62.634 | 128393 / 111488 / 1695 |
| new 2 | 4/4 | 4/4 | 1/1 | 17/17 | 7 tests; pass/pass | 77.075 | 148343 / 129792 / 2521 |

All four exit 0. Each run's added tests produced red failures in all four bug categories
before implementation, then passed after repair. The known-good paths are ordinary delivery,
authorized approval, successful save and allowed token values. No run added a dependency,
a heading-only test or a retry to hide failure; original expectations remain. Zero clean-path
regressions in 8 opportunities per configuration is a narrow false-alarm proxy, not a general
false-positive rate. The token case is an exact string validator, not a CSS/JS/utility parser;
the UI case is a state reducer, not a browser or human usability test.

Old mean elapsed: 62.357s; new: 78.292s (+25.6%). Total output tokens old 3,619 vs new 5,027;
total input old 281,849 vs new 310,823, including cached input 240,512 vs 249,344. Usage is
reported cumulatively across turns, not unique prompt length or verified billing. Dollar
cost is unavailable. With two bundles each, timing/cache/provider variance is uncontrolled;
these observations do not establish a stable cost increase or a quality advantage.

Expected red results remain in transcripts (13 failures in each old run, 14 in each new).
New-1's shell command ended with `cat`, so its command exit is 0 despite the recorded failing
test output; the evaluation does not count that as green. Both new runs also tried to read
HEAD and received exit 128, then disclosed the missing revision. This is setup metadata
friction, not an application defect. No timeout or incomplete artifact is discarded.

All submitted final suites pass on two additional invocations (8/8 suite invocations).
That means no inconsistency observed in this tiny deterministic sample, not proven absence
of flakiness. The [summary](summary.json) includes raw command exits and final file/test lists;
the [runs](runs/) retain full JSONL transcripts, answers, stderr, final files, diffs and checks.
Final untracked files are in snapshots even when `git diff` does not include them.

## Scorer review and controls

The frozen [scorer](score.py) rejects broken fixtures and the deliberately broken approval
implementation; [controls](controls.json) show the known-good version passes 17/17.
Independent review found its same-connection assertion did not prove committed storage.
All four outputs also pass the separately labelled [persistence supplement](persistence.py),
which checks through another connection. [Its controls](persistence-controls.json) reject
a missing commit. This is post-freeze evidence, not a silently replaced held-out score.
See [deviations](deviations.md), including the runner's scoring-timeout limitation.

## Feedback and recommendation

Reuse the existing dream report and inbox. [Two attributable traces](feedback.md) distinguish
the owner's validation-scope requirement from a measured OpenCode output failure; neither
requires new capture machinery. [The recommendation inventory](recommendation.md) records
observed benefits or explicit untested risks for retained prescriptions, instruction overhead,
recurrence and the absence of measured human-time savings.

The [reminder comparison and independent scoring](planning-review.md) support a small proposal:
three planning omissions repaired, one still present, clean-case coverage retained in one pair.
No candidate may be silently adopted. The rollback is unchanged guidance at `9731d98`.

## Review and final checks

Independent task review reproduced the four outcome scores, persistence checks and submitted
suites, inspected red/green commands and unchanged expectations, and confirmed AC1–6 after
report corrections. It independently scored the planning outputs; successful candidate
acceptance remains with the owner. Final [repository output](checks.txt): `all 11 checks passed`.
Offline re-scoring reproduced retained results, frozen hashes and controls; all evaluation
scripts parse as Python 3.10 and local report links resolve. No template or settings file changed.
A separate fresh AI reviewer confirmed frozen/delivered guidance hashes, configured model and
bounds, usage/timing arithmetic, non-database assertions and planning conclusions. It made no
model calls or database writes. Its optional ai-features checklist was unavailable locally,
so this is a task/rubric review rather than certification against that missing checklist.

## Reproduce

Offline checks (no model use):

```sh
python3 docs/evidence/3-verification-workflow-evaluation/controls.py
python3 docs/evidence/3-verification-workflow-evaluation/summarize.py
scripts/agent/check
```

Live reruns spend model usage and need Codex access. `run.py old 3` or `run.py new 3` creates a
new run (existing run names fail rather than overwrite evidence); add `--planning` for the
planning bundle, and use `candidate` for the retained reminder. `negative.py` is an intentionally
bad evaluation-only policy, never a setup instruction. Review source before any live rerun.
New iterations on these exposed cases are development data, not a fresh holdout.

Shared installation and config checks cover Claude Code, Codex and OpenCode. Only Codex live
effectiveness was evaluated here. No Claude account run, OpenCode comparison, rendered UI,
representative-user study, full hook/permission lifecycle or vendor-launcher endpoint trial.
