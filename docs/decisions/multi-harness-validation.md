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
