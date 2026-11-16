# Portable setups with available runtime validation

Accepted by the owner on 2026-11-16 while completing task 1.

All current and future tackroom tasks target Codex, Claude Code and OpenCode setups. Shared
workflow and skills stay harness-neutral; per-harness configuration uses supported controls.
Native goals and execution limits remain harness-specific rather than a duplicate goal skill.

Codex is the available live validation harness on this machine. Other targets receive
installation, shared-file parity and configuration checks, with untested runtime behavior
explicitly reported. Unavailable model access does not block portable setup work, and static
checks do not establish runtime equivalence or effectiveness.

This is an owner-directed scope decision. It supersedes task 1's original mandatory Claude
exercise and the agent's mistaken requirement for live trials in every harness. Evidence:
[task 1](../../tasks/1-verification-before-implementation.md),
[trial results and limits](../evidence/1-verification-before-implementation/multi-harness.md),
and [native loop controls](../loops.md).

Task 2 applied this scope to the owner-selected agent-dev-infra CLI: isolated external-provider
fixtures and actual CLI output are appropriate evidence for command behavior. They do not
establish live company infrastructure or browser-application behavior. The accepted
[pilot recipe and limits](../evidence/2-project-verification-pilot/README.md) remain the record.

Task 3's accepted [evaluation](../evidence/3-verification-workflow-evaluation/README.md) reuses
existing dream reports and inbox entries for feedback; no additional collector or memory
format is needed. The small Codex comparison does not establish coding superiority or runtime
effectiveness in other harnesses. The evaluated five-line reminder remains a separate
human-review proposal; accepting the evidence does not silently install it. Retain current
shared guidance provisionally and use new cases for future comparisons, because the retained
fixtures are now exposed. Synthetic controls and the separately labelled persistence
supplement remain evidence, not production checks added to copied projects.
