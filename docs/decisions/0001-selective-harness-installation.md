# One shared template with selective installation

Accepted scope from the owner's 2026-11-16 request to create this work.

`template/` remains the source of the distributable harness. Shared instructions, skills,
reviewer briefs and hook logic are authored once, with only supported configuration and
discovery adapters specific to Codex, Claude Code and OpenCode. Generated or linked agent
entry points are acceptable; separately maintained copies of common content are not.

Installation provides a common base and explicitly selectable capabilities for particular
stacks or kinds of application. UI craft is the initial example of an optional capability.
Users select the agents they use; installing Codex must not require installing Claude's setup.

An installer runs in the destination application and obtains the selected harness from this
repository on GitHub. The owner authorized publishing to `main` and using GitHub raw files.
Projects still own the installed files. This extends the existing one-time copy workflow;
it does not introduce a registry, fleet management, automatic updates or drift tracking.

These are owner-directed requirements. The exact command, runtime, catalog format and adapter
generation mechanism are not selected by this decision. Keep those proposals small and
review them before implementation commits to a public interface or new dependency.

Related: [spec](../specs/selective-harness-installation.md),
[multi-harness validation](multi-harness-validation.md), and
[existing setup rationale](../principles.md). The selective distribution design is a product
judgement call, not a measured conclusion from the research corpus.
