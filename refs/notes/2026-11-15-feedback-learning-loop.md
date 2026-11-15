# Human feedback and verified mistakes as harness improvements

Research date: 2026-11-15. Follow-up to the verification workflow audit.

## Questions

1. Do Anthropic sources describe turning human corrections and agent-discovered failures into
   persistent improvements, and which accounts describe actual internal practice?
2. What already exists in this repository's memory/dream loop, and what is missing?
3. Which existing task should connect corrections to measured, reviewable harness changes?

## Findings

**Yes.** Sources explicitly describe learning from human corrections and from observed agent
failures. The evidence includes both reported Claude Code team practice and separate Anthropic
memory experiments. The mechanisms are persistent context, tests, rules and evaluation; these
sources do not say that an ordinary correction retrains the model's weights.

### Human feedback in the Claude Code team's workflow

The official power-user guide identifies its tips as practices collected from individual
Claude Code engineers. Under **CLAUDE.md and memory**, it recommends recording corrections in
the shared project instructions and using PR comments to request such updates. Its exact
example instruction is: “Update your CLAUDE.md so you don’t make that mistake again.” Auto
memory is described separately as retaining preferences, corrections and patterns. This is
direct evidence of the requested human-to-persistent-guidance pattern, not a guarantee that
every correction prevents recurrence. [S1]

The team's code-review account is stronger evidence of an internal operational loop. Recurring
automated findings prompt changes to skills, lint or instruction files. Past incident-causing
PRs become engineer-confirmed evaluation cases. Human responses to review comments are used
to distinguish actual fixes from wrong findings, intentional behavior and low-value comments;
known-clean changes test for harmful false positives. The article also recommends moving
repeated review comments into REVIEW.md. [S2]

### Agent mistakes, memory correction and proposed workflows

The dynamic-workflows article explicitly proposes mining sessions and review comments for
recurring human corrections, grouping them, checking whether a candidate rule would have
prevented a real mistake, then retaining the useful rules. This is a published workflow
recommendation; it is not evidence that every Anthropic engineer runs a scheduled version. [S3]

Anthropic's memory research describes incorrect answers followed by corrective feedback,
hypothesis testing and persistent rules. It also tests checking a mistaken memory note against
the original transcript and correcting it. The article explicitly distinguishes persistent
memory from weight updates. These are Managed Agents experiments, not proof of an identical
Claude Code engineering process. It also found that restricting memory to failures could hurt
performance, so a learning loop should retain useful successful strategies too. [S4]

The Warp case study on Anthropic's site describes another concrete human-feedback-to-skill
improvement loop. Attribute it to **Warp**, not to the Claude Code team's own infrastructure.
The earlier saved audit covers its public demo and limitations, including the danger of
interpreting silence as positive feedback. [S5, existing adaptive-harness note]

### What already exists here

- `template/AGENTS.md` and the task workflow route durable lessons to the memory inbox.
- The dream skill analyzes transcripts and inbox notes, corrects memory and proposes changes
  to checks, skills or instructions. It can propose removals, not only additions.
- Proposals already need recurrence in multiple sessions or one harmful incident, and human
  acceptance. These thresholds are this repository's judgment, not universal source rules.
- The missing connection is evaluation and traceability: which feedback led to which change,
  whether later sessions use it, whether the error recurs, and whether clean cases regress.
- Memory files are portable, but the existing native transcript exporter is Claude-specific.
  Codex/OpenCode corrections can be recorded explicitly or provided as plain-text logs; native
  ingestion is not assumed to work.

## Recommendation

**Extend task 3.** It already owns baseline comparisons and keep/change/remove decisions.
Tasks 1 and 2 supply behavior checks and real task evidence; task 3 should turn feedback into
an evaluated candidate improvement. Reuse the inbox/dream design rather than creating another
learning mechanism. The owner explicitly requested this scope addition.

The proposed sequence is our synthesis:

1. Link the correction or observed failure to its task/run and harness revision. Record what
   was expected, what happened, who reported it, the available evidence and its scope.
2. Distinguish factual bugs from preferences, new requirements, tool failures and unverified
   diagnoses. Preserve the user's intended correction without generalizing it beyond its scope.
3. Reuse dream to check recurring lessons and propose one small change to a test, lint rule,
   helper, skill or memory. Fix a broken tool directly rather than covering it with prose.
4. Evaluate the reproducer, unseen related cases and known-good cases against the baseline;
   include human correction effort, recurrence, overhead and cost. Never tune on holdout answers.
5. Present the diff and evidence for human adoption, keep a rollback revision, and record later
   regressions. A candidate that only fixes its training example has not established generality.

This is a task/spec update, not implementation of a new automatic collector or improver.
It does not require rewriting instructions after every complaint. Trade-off: reviewed,
evidence-based adoption is slower than automatic accumulation, but lets us reject harmful
lessons. Evidence that the records add overhead without reducing repeated mistakes would
favor simplifying or removing them.

## Source register and reading limits

All five primary URLs were opened live on 2026-11-15 and already have saved copies. Relevant
sections were rechecked against those copies and existing research; this was a focused
verification, not a new full-corpus reading or live memory experiment. No saved source was
edited, no external instructions were executed, and no new downloads were needed.

| Key | Author/date and primary URL | Saved file and locator; evidence type |
|---|---|---|
| S1 | Claude Help Center, living guide (saved date 2026-10-30): [power-user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips) | `refs/articles/support.claude.com/en-articles-14554000-claude-code-power-user-tips/article.md`; CLAUDE.md and memory; collected team practice |
| S2 | Addy Osmani, Morgan Westlee Lunt, Qing Wang, 2026-10-15: [team code review](https://claude.dev/blog/solving-code-review-at-anthropic/) | `refs/articles/claude.dev/blog-solving-code-review-at-anthropic/article.md`; Layer by layer / How we make the reviewer better; first-person internal workflow |
| S3 | Thariq Shihipar, Sid Bidasaria, 2026-06-02: [dynamic workflows](https://claude.dev/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code/) | `refs/articles/claude.dev/blog-a-harness-for-every-task-dynamic-workflows-in-claude-code/article.md`; Memory and rule adherence; recommended pattern |
| S4 | Anthropic Engineering, 2026-11-06: [components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) | `refs/articles/anthropic.com/research-components-of-agent-memory/article.md`; Memory notes / Memory can be a prediction / Steering Claude / Dreaming can correct memory; reported experiments |
| S5 | Michael Segner, 2026-08-26: [Warp case study](https://claude.com/resources/articles/how-warp-builds-self-improving-agents-on-claude) | `refs/articles/claude.com/resources-articles-how-warp-builds-self-improving-agents-on-claude/article.md`; skill-improvement loop; customer practice reported by Anthropic |

Existing synthesis: [adaptive-harness learning](2026-11-13-adaptive-harness-learning.md).
Implementation baseline: [memory and dreaming](../../docs/memory-and-dreaming.md).
Updated task: [task 3](../../tasks/3-verification-workflow-evaluation.md).
