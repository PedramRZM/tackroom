# Verification workflow v2 — 2026-11-17

This is a revision of the portable verification guidance, not a new executable gate or a
package release. The template remains the source for Claude Code, Codex and OpenCode.
The existing uncommitted local-testing/preview policy is retained. The owner subsequently
authorized committing and pushing this update to main; no other project is updated.

Source: Addy Osmani's [November 16 article](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/),
read in full and saved in [refs](../refs/articles/claude.dev/blog-how-the-claude-code-team-thinks-about-verification/meta.json).
[Research notes](../refs/notes/2026-11-17-verification-v2.md) distinguish the source's claims
from our judgments. The article's structured-generation result is not evidence of a coding
quality improvement here.

## What we already do, and what changes

| Area | Before this update | v2 |
|---|---|---|
| Define done before coding | Criteria mapped to examples, risks, tools and evidence; focused red/green checks | Retained; no second planning document required |
| Run the actual change | `verify` requires running UI/API/CLI behavior and nearby regressions | Emphasizes assembled flows and a repeatable boot/reset recipe with failure diagnostics |
| Test selection | Static/unit/integration/E2E chosen by risk; property/differential checks mentioned | Property domains, replay seeds and minimized failures; pinned old oracle, normalization and approved differences |
| Repair failures | Same fix twice in task/AGENTS; verify otherwise said restart full checks | Focused reruns, final full checks, cap of three failed repairs; stricter two-identical-fix limit retained |
| Review criteria | Task criteria, fixed reviewer brief, changed-test inspection | New project-owned `REVIEW.md` with incident-backed diff triggers; reviewer reads pinned base rubric |
| Reviewer rounds | Fresh reviewer and up to three rounds already present | Reuse reviewer, preserve findings, pin targets, distinguish pre-existing defects and stale evidence |
| Evidence identity | Revision/environment and dirty changes mentioned | Fixed commit or content-hashed snapshot including new files; verified/partial/none plus gaps |
| Test protection | `lock-tests`, guard hooks, no weakening/deletion, review of changed expectations | Existing controls retained; explicitly distinguish base-rubric procedure from trusted enforcement |
| Flaky checks | No retry/sleep to get green; quarantine language conflicted with no skipping | Fix or report; quarantine requires owner approval, repair task and expiry |
| Learn from failures | Inbox, dream proposals and pruning; prior synthetic evaluation | Diff triggers, owner/provenance, counterexamples, stable controls and stage-by-stage reviewer evaluation |
| New blocking gates | Quick Stop hook; no commit verification gate | Observe-first adoption guidance only; no new blocking hook |
| Where verification runs | Uncommitted policy: local machine/worker, final issue evidence, preview for humans | Preserved in workflow and verify; no implicit CI/preview testing requirement |

The existing quick Stop hook is a convenience feedback loop: it can skip unchanged work,
missing/unconfigured checks, timeouts and a repeated Stop invocation. It does not certify a
commit or replace the full check. Its fingerprint uses status and tracked diff, so new-file
content alone is not fully covered by its cached identity. v2's final evidence must not rely
on that cache. Hardening the hook is separate from this guidance revision.

## The resulting work loop

1. Run baseline checks; map criteria to concrete behavior and evidence.
2. Build against a focused failing example; use properties or old/new comparisons where useful.
3. Run cheap focused checks, then full local checks and the changed assembled journey.
4. Apply reliability rules selected from the pinned base's diff triggers. Record results/gaps.
5. Review a fixed target with one independent reviewer; carry findings through bounded repairs.
6. Record exact target, environment, criterion results and verified/partial/none. Refresh affected
   evidence after edits, publish through the existing task path, then hand over to the owner.

Changes live in `WORKFLOW.md`, `REVIEW.md`, `verify`, `write-tests`, `second-opinion`, the reviewer
brief, `dream` and the PR evidence template. Root native adapters are regenerated, not edited.
No new always-loaded AGENTS instructions, dependencies, service, CI job or test framework.

## What remains project-specific or deferred

- **Actual reliability rules:** the shipped rubric is deliberately empty. Each project needs
  its incidents, owner and exact checks. A made-up 39-rule list would create overhead without evidence.
- **Trusted enforcement:** base-file reads and mutable local hooks cannot prevent self-approved
  checks. A protected external verifier is needed when that assurance is required. This owner
  has not requested a new CI or deployment gate.
- **Commit stamps and observe/enforce implementation:** deferred. Record evidence in the
  existing task/PR first. Before adding a gate, measure false blocks, missing evidence, runtime
  and bypasses in observe mode. Merely invoking `/verify` must never count as passing evidence.
- **Project smoke harness:** the portable recipe needs real commands, seed data, health/reset
  behavior and useful failure output in each consuming project. No universal app driver is added.
- **Effectiveness evaluation:** existing [task-3 results](evidence/3-verification-workflow-evaluation/README.md)
  did not demonstrate a quality advantage for the previous longer guidance on its small fixture.
  v2 packaging/scenario checks cannot establish one either. A future evaluation should freeze
  unseen incidents and similar clean changes, score raw/verified/final findings separately, and
  compare correctness, false alarms, severity, cost and reviewer time before further expansion.

We deliberately do not adopt automatic flaky-test deletion, mass agent parallelism, or automatic
learning-rule installation. These conflict with current owner controls or lack local evidence.

## Validation and adoption

Acceptance: preserve the existing owner policy; implement the comparison's v2 behavior in shared
sources; regenerate adapters; pass repository checks; install in a scratch project and exercise
the revised guidance with adversarial scenarios (moving target, candidate rubric edits, repeated
failure, flaky tests, migration differences). Check installation includes the new rubric and
preserves a locally customized one on update. Retain exact results in
[validation evidence](evidence/verification-v2/README.md).

Use `tools/setup PROJECT --update` only for an explicitly selected project. It preserves local
customizations and memory and reports conflicts to merge. A customized verify skill may need
manual reconciliation. A clean install receives `REVIEW.md`; an existing customized rubric must
not be overwritten. v2 is a guidance identifier; source fingerprints/commit IDs remain installation
provenance. This revision uses the normal repository commit; no release tag is created.

On November 18 the owner requested early draft PRs and agent-run verification of a deployed
branch. Projects select their verification environments and scope their test data.
