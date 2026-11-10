---
title: "Specs - Features - Docs - Kiro"
date: "2026-10-15"
url: "https://kiro.dev/docs/specs/"
site: "Kiro"
type: "doc"
via: "direct"
---
Specs or specifications are structured artifacts that formalize the development process for features and bug fixes in your application. They provide a systematic approach to transform high-level ideas into detailed implementation plans with clear tracking and accountability.

| Capability | IDE | CLI | Web | Mobile | 
|---|---|---|---|---|
| Feature Specs | ✓ | ✓ | ✓ | — | 
| Bugfix Specs | ✓ | ✓ | ✓ | — | 
| Quick Spec | ✓ | ✓ | ✓ | — | 
| Parallel task execution | ✓ | ✓ | ✓ | — | 
| [Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/) | ✓ | ✓ | — | — | 
| [Correctness](https://kiro.dev/docs/specs/correctness/) (property-based testing) | ✓ | — | — | — | 

With Kiro's specs, you can:

- **Break down requirements** into user stories with acceptance criteria
- **Build design docs** with sequence diagrams and architecture plans
- **Track implementation progress** across discrete tasks
- **Collaborate effectively** between product and engineering teams

Every spec generates three key files that form the foundation of your specification:

- **requirements.md** (or **bugfix.md**) - Captures user stories, acceptance criteria, or bug analysis in structured notation
- **design.md** - Documents technical architecture, sequence diagrams, and implementation considerations
- **tasks.md** - Provides a detailed implementation plan with discrete, trackable tasks

All specs follow a three-phase workflow that transforms your idea into executable implementation:

**Requirements or Bug Analysis** - Define what needs to be built or fixed

- Feature Specs: User stories and acceptance criteria in `requirements.md`
- Bugfix Specs: Bug analysis with current/expected/unchanged behavior in `bugfix.md`

**Design** - Create technical architecture and implementation approach in `design.md`

- System architecture and component design
- Sequence diagrams and data flow
- Error handling and testing strategy

**Tasks** - Generate discrete, executable implementation tasks in `tasks.md`

- Trackable tasks with clear outcomes
- Real-time status updates as you implement
- Run tasks individually or all at once

Kiro provides a task execution interface for `tasks.md` files that displays real-time status updates. Tasks are updated as in-progress or completed, allowing you to efficiently track implementation progress.

When you run all tasks on a spec, Kiro analyzes your task list, figures out which tasks depend on each other, and runs independent tasks concurrently. For most feature specs, this cuts execution time significantly without any setup.

Kiro builds a **dependency graph** of the tasks in your `tasks.md` and groups independent tasks into **waves**:

- **Wave 1** - all tasks with no dependencies. These run concurrently.
- **Wave 2** - all tasks whose dependencies were satisfied by Wave 1. These run concurrently.
- **Wave N** - continues until all tasks are complete.

Waves execute sequentially; tasks within a wave execute concurrently.

Kiro supports two types of specs to match your development needs:

For building new features and capabilities in your application. Feature Specs guide you through requirements gathering, technical design, and implementation planning with two workflow variants: Requirements-First and Design-First. For well-understood features, you can also use [Quick Spec](https://kiro.dev/docs/specs/quick-spec/) to auto-generate all three artifacts without approval gates.

[Learn more about Feature Specs →](https://kiro.dev/docs/specs/feature-specs/)

For systematically diagnosing and fixing bugs with surgical precision while preventing regressions. Bugfix Specs help you identify root causes, design fixes, and validate that nothing else breaks.

[Learn more about Bugfix Specs →](https://kiro.dev/docs/specs/bugfix-specs/)

1. From the Kiro pane, click the `+` button under **Specs**. Alternatively, choose **Spec** from the chat pane.
2. Kiro will ask if you are developing a Feature or fixing a Bug
  - If you choose Feature, describe your feature and choose your workflow: **Requirements-First** or **Design-First**
  - If you choose Bug, describe your bug
3. As you move through each phase, select the floating **Review** button on requirements, design, bugfix, or behavior documents. It opens [Markdown Review](https://kiro.dev/docs/ide/editor/markdown-review/), where you can comment on exact passages and send your comments to Kiro at once.
4. Follow the workflow through each phase to implementation

Go deeper into Kiro's Spec system with these guides:

## Specs
