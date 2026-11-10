---
title: "Beads | Technology Radar | Thoughtworks United States"
date: "2026-11-04"
url: "https://www.thoughtworks.com/en-us/radar/tools/beads"
site: "Thoughtworks"
type: "article"
via: "direct"
---
Technology Radar

**[Beads](https://github.com/gastownhall/beads)** is a Git-backed issue tracker that coding agents can share to coordinate their work. In place of ad hoc Markdown plans, it gives agents a persistent, structured task graph. Because Beads stores tasks and their dependencies alongside the code, agents retain their plans and newly discovered tasks across sessions and context compaction. Each agent can claim the next available task without colliding with others.

We're moving Beads to Trial because many of our developers now use it by default with coding agents. It complements team issue trackers such as [Linear](https://www.thoughtworks.com/en-us/radar/tools/linear), which teams use to plan, prioritize and track work. Beads holds the finer-grained tasks agents create as they work, and it syncs both ways with Linear, Jira and GitHub Issues.

Since we last featured it, Beads has reached 1.0 and moved to the Gas Town Hall organization. It’s maintained by Gas City, the company behind [Gas Town](https://github.com/gastownhall/gastown). [Dolt](https://github.com/dolthub/dolt) is now its only storage backend, and additions such as an HTTP API, work leases and synchronization between stores make Beads heavier than the lightweight tracker it started as. Upgrades migrate the schema in place, and clients running different versions can't share a store, so teams should pin a single version for each shared store and review the instructions Beads writes into [AGENTS.md](https://www.thoughtworks.com/en-us/radar/techniques/agents-md).

**[Beads](https://github.com/steveyegge/beads)** is a Git-backed issue tracker designed as a persistent memory layer for coding agents. Instead of relying on ad hoc Markdown plans, it gives agents a structured task graph with blocker relationships, ready-work detection and branch-friendly coordination for long-horizon work across sessions. It’s built on [Dolt](https://github.com/dolthub/dolt), a SQL database with built-in version control that supports branches, merging, diffs and table cloning similar to a Git repository. Beads represents a new category of agent-native project memory and task tracking tools. Other early projects in this space include [ticket](https://github.com/wedow/ticket) and [tracer](https://github.com/Abil-Shrestha/tracer). Unlike traditional ticketing systems such as GitHub Issues and Jira, Beads and similar tools enable new workflows for coordinating autonomous multi-agent execution, including agents assigning tasks to one another.
