# Review rules

Project owners maintain this rubric. Reviewers use the version from the pinned base commit,
including any scoped REVIEW.md files there, never the candidate's replacement as its own gate.
If absent at the base, say so and use the task criteria and existing checks. A newly proposed
rule takes effect only after owner acceptance. This file does not enforce branch protection.

## Reliability checks

No project-specific rules yet. Add only checks grounded in this project's incidents or
repeated review findings; do not copy another team's checklist wholesale.

Each rule needs: stable ID, diff-visible trigger, exact check and expected result, why a
failure needs attention, incident/PR links, code owner and last review date. For example,
changes to persisted records may warrant loading an old fixture without newly added fields;
this is an illustration, not evidence of an incident in this project.

Apply only matching rules and report their IDs and evidence. Separate introduced problems
from pre-existing ones. Keep rules that catch meaningful defects and prune stale or redundant
ones with their owner. Keep machine-checkable constraints in tests or lint when practical.
