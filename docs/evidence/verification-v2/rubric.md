# Smoke-test rubric, written before the run

This is an exposed scenario test of instruction loading and planning, not a held-out coding
or reviewer-quality evaluation. Pass only for explicit actions; do not infer missing items.

1. Pin old implementation; compare same inputs and observable errors; normalize only irrelevant
   differences, require approval for intentional differences, retain reproducible failing input.
2. Use the base rubric; stale A cannot certify B; frozen dirty snapshot including new files is
   provisional and does not authorize a commit; reuse reviewer/findings for affected follow-up.
3. Escalate after bounded repairs; unchanged retry-green is not verified; no unauthorized test
   deletion/quarantine; report failure history and coverage gap.
4. Preserve local testing policy; no inferred CI/preview gate; attach revision, AC results and
   final screenshots to task, provide human preview steps and data.
5. Changed new-file content invalidates affected evidence; content identity must include it;
   rerun relevant checks/review; record status and gaps; observe before enforcing a new gate.

Installation checks: all three harness adapters receive the updated reviewer; shared verify
and REVIEW.md arrive intact; update preserves a customized REVIEW.md and project memory.
Full repository checks must pass. A Claude account failure is an unavailable runtime, never
a successful model test. Record it and attempt available Codex planning without claiming
Claude/OpenCode runtime behavior. Reviewer also checks the retained plan against this rubric.
