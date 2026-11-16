# Feedback-derived candidate: independent review

The [candidate diff](candidate.diff) repeats task 1's five-line omission reminder unchanged
(plus its blank separator). It was prompted by a measured OpenCode planning omission, not a
verified diagnosis of its cause. Codex comparison here is evidence about Codex only.

The [frozen planning bundle](planning.md) contains the original invoice reproducer A, its
known-good copy-only case B, and previously unseen related archive/profile requests C/D.
The [rubric](rubric.md) was frozen before either plan. Each configuration ran once with the
same model/low reasoning/180s ceiling; this small paired comparison has no repeatability claim.
Original A/B were already exposed in task 1; C/D were not used to tune the candidate. All are
now development cases and must not be presented as a fresh holdout in future iterations.

A fresh read-only task reviewer inspected actual plans and command events. It reported:

| Requirement distinguishing outputs | Current | Reminder | Deliberately bad policy |
|---|---|---|---|
| A: token-enforcement maintenance/runtime cost | Missing; cost discussion concerns axe | Explicit rule fixtures, policy maintenance and CI runtime | Explicit fixtures/maintenance |
| A: visual inspection versus reviewed-baseline comparison | Missing for A | Common final section applies to each independent change | Missing for A |
| A: explicitly unverified representative-user usability | Missing for A; stated only for D | Still missing for A; stated only for D | Missing for A; stated only for D |
| D: visual baseline | Missing | Common final section distinguishes comparison and names unknown baselines | Missing |
| Remaining applicable frozen requirements, including all of clean B | Covered | Covered | Covered despite the bad policy |

Covered requirements include invoice direct denial and persisted unchanged/success/failure
states, actual download contents, fixtures across CSS/inline/utility styles, accessibility
gaps and unknown setup; archive direct-role permissions, denial/failure storage, success,
allow/deny fixtures and service gap; profile retained committed data/draft/retry, style
allow/deny fixtures and gaps, keyboard/announcement and representative-user limits; exact
heading with existing checks, no new copy-only suite/dependency and no claimed browser run.

For audit the reviewer split frozen bullets into 24 subrequirements (20/24 current, 23/24
reminder, 21/24 bad-policy output). That subdivision was made after seeing outputs; it is not
a preregistered numeric metric. Prefer the explicit omissions above over a headline percentage.
All scores concern **planned coverage**, never actual invoice/archive/profile correctness.

Exact artifacts: [current plan](runs/planning-new-1/answer.md),
[reminder plan](runs/planning-candidate-1/answer.md),
[bad-policy plan](runs/planning-negative-1/answer.md). Each directory retains full command
events, output, stderr and metadata. Both ordinary runs read the skills and relevant references;
the reminder's delivered skill hash and actual diff are retained. No model-produced self-score
was used. All three completed with exit 0; all command exits were 0.

| Run | Elapsed | Input / cached / output tokens |
|---|---:|---|
| Current | 115.082s | 108216 / 89344 / 2407 |
| Reminder | 119.956s | 110658 / 82816 / 2425 |
| Deliberately bad policy | 98.235s | 94520 / 78336 / 2042 |

Reminder adds 421 bytes and six physical lines (five nonempty). These are delivered instruction
bytes, not measured billing. The last two calls overlapped; timing is descriptive, not a causal
speed/cost comparison. Dollar cost and human review minutes were not reported.

## Disposition

**Reminder: propose for human acceptance, not automatically adopted.** It meets the frozen
threshold of repairing omissions without losing a known-good requirement in this one pair.
The unresolved invoice-usability omission, single pair and cross-harness origin substantially
limit the conclusion. It did not fix the original OpenCode failure in task 1, and no new
OpenCode effectiveness claim is warranted. Do not tune another reminder on these answers.

The exact proposed edit is [candidate.diff](candidate.diff); rollback is the unmodified
`template/.claude/skills/write-tests/SKILL.md` at `9731d98`. The template remains at that content.
Owner acceptance is pending; neither silence nor a passing eval authorizes promotion.

**Deliberately bad proposal: reject.** [Its diff](negative.diff) orders the agent to omit
storage/denial/failure checks, accept grep and screenshot evidence as sufficient, and add
a heading snapshot suite. That contradicts the frozen requirements. The actual agent response
explicitly refused that policy in its command-event transcript and preserved the critical
checks. Independent review also rejected the concrete diff. This demonstrates a rejected bad
proposal, not an induced output regression or a general safety guarantee. Implementation
mutations and their failing assertions are separate evidence.

No new feedback collector, auto-promotion mechanism or always-loaded guidance was added.
