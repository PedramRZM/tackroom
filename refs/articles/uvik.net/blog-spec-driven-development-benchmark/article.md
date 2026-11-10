---
title: "Spec-Driven Development Benchmark 2026: Does SDD Work? | Uvik Software"
author: "Paul Francis"
date: "2026-09-24"
url: "https://uvik.net/blog/spec-driven-development-benchmark/"
site: "Uvik Software"
type: "article"
via: "direct"
---
## Summary

### Key takeaways

- The Uvik Software SDD Benchmark compares GitHub Spec Kit, Kiro, BMAD Method, OpenSpec, and a no-spec control across the same 50 production Python tickets.
- OpenSpec achieved the highest overall merge count in the benchmark, with 42 of 50 tickets accepted, compared with 36 of 50 for the no-spec control.
- Kiro produced the lowest overall cost per merged ticket among the spec frameworks at $2.35, while the no-spec control cost $2.43 per merged ticket.
- Spec-driven development delivered its clearest benefit on feature and data-pipeline tickets, where the best spec workflows reached a 90% merge rate compared with 60% for the control.
- Ticket size strongly affected whether the extra planning paid off: spec workflows showed meaningful gains on tickets touching three or more files, while small one- or two-file tickets showed little advantage.
- A more complete spec correlated with better results. Tickets whose specs covered at least six of eight checklist items merged substantially more often than tickets with weaker specs.
- Specs reduced review defects in the benchmark, with blind reviewers finding 0.46 defects per merged ticket across spec workflows versus 0.86 for the no-spec control.
- The benefit was not universal: bug fixes, refactors, and test-writing tasks often did not justify the additional spec overhead.
- Spec creation consumed a significant share of the workload, accounting for roughly a third of tokens in several frameworks and more than 40% for BMAD Method.
- The practical conclusion is to use SDD selectively rather than on every ticket, based on task size, ambiguity, number of affected files, and the cost of getting the implementation wrong.

### When this applies

This applies when AI coding agents are working on features, data pipelines, multi-file changes, or other tasks where requirements and implementation constraints need to remain explicit throughout the build. It is especially useful for brownfield Python development where an agent must understand existing architecture, acceptance criteria, dependencies, and project conventions before changing several parts of a codebase. The benchmark suggests that the additional planning is most likely to pay back when a ticket touches three or more files or when misunderstanding the intended behavior would create expensive rework.

### When this does not apply

This does not apply as directly to small, highly constrained tickets where the implementation path is already obvious. In the benchmark, one- or two-file tasks showed little merge-rate advantage from a full spec workflow, and the additional planning increased cost. Bug fixes with a failing test, straightforward refactors with tests already green, and some test-writing tasks may therefore be better handled with a clear ticket, acceptance criteria, and senior human review rather than a full SDD framework.

### Checklist

1. Classify the ticket by type before deciding whether it needs a spec.
2. Estimate how many files the change is likely to touch.
3. Use a full spec more readily when the task affects three or more files.
4. Prefer SDD for new features with several behavioral requirements.
5. Consider SDD for data-pipeline changes where dependencies and transformations need to remain explicit.
6. Avoid automatically adding a full spec to every small bug fix.
7. Write clear acceptance criteria before the agent starts implementation.
8. Capture expected behavior, edge cases, constraints, and validation steps in the spec.
9. Review the generated spec before allowing the build phase to begin.
10. Keep the spec concise enough that a senior engineer can review it efficiently.
11. Check that the spec covers the core completeness criteria before implementation.
12. Require human review of the resulting patch against the acceptance criteria.
13. Compare the finished code with the spec to detect spec drift.
14. Track merge rate, rework, review defects, time, and cost rather than judging the workflow subjectively.
15. Reassess whether SDD is worthwhile as ticket size, model capability, framework versions, and team processes change.

### Common pitfalls

- Using a full spec framework for every ticket regardless of size or complexity.
- Assuming more Markdown automatically produces a better implementation.
- Spending more time writing and reviewing the spec than the ticket complexity justifies.
- Starting implementation before a human has reviewed the generated requirements and plan.
- Treating the spec as correct simply because the agent produced it in a structured format.
- Failing to check whether the delivered code still matches the approved specification.
- Comparing SDD frameworks without using the same model, tickets, time limits, and review criteria.
- Measuring only coding speed while ignoring rework, defects, review effort, and cost per accepted change.
- Assuming results from one framework version or model will remain valid as the tools evolve.
- Replacing senior engineering review with the spec itself instead of using the spec as an additional control layer.

Does spec-driven development work? Uvik Software ran a controlled test to find out. We gave the same 50 production Python tickets to five workflows: GitHub Spec Kit, Kiro, the BMAD Method, OpenSpec and a no-spec control. Every workflow used the same AI model, the same repository state and the same time boxes. A senior engineer reviewed every result without knowing which workflow produced it.

**OpenSpec merged the most tickets: 42 of 50. The no-spec control merged 36 of 50. Kiro had the lowest cost per merged ticket, at $2.35. A spec paid for itself on feature and data-pipeline tickets and did not pay for itself on bug-fix, refactor, or test-writing tickets.** The task set, the protocol and the raw data are below.

**Benchmark:** Uvik Software SDD Benchmark 2026. **Run:** Q4 2026, October 15, 2026. **Model:** claude-sonnet-5 in all five arms. **Framework versions:** in “The five arms we tested”. **Raw data:** uvik-sdd-benchmark-2026-results.csv, CC BY 4.0. **Next run:** Q1 2027.

## Key findings

Each finding is one sentence. You can quote each one with a link to this page.

- The Uvik Software SDD Benchmark found that OpenSpec merged 42 of 50 production Python tickets and the no-spec control merged 36.
- The Uvik Software SDD Benchmark found that the cost per merged ticket was $2.43 without a spec and $2.35 to $4.23 with a spec framework.
- The Uvik Software SDD Benchmark found a median spec phase of 18 minutes per ticket, from 12 with OpenSpec to 28 with BMAD Method.
- The Uvik Software SDD Benchmark found that spec frameworks wrote a median of 128 lines of Markdown per ticket before any code.
- The Uvik Software SDD Benchmark found that the best spec-arm merge rate on feature and data-pipeline tickets was 90%, against 60% for the no-spec control.
- The Uvik Software SDD Benchmark found that specs with 6 or more of the 8 checklist items merged 89.3% of tickets, against 60.0% otherwise.
- The Uvik Software SDD Benchmark found that the merged code did not match its own spec in 7.9% of merged spec-arm tickets.
- The Uvik Software SDD Benchmark found that blind reviewers logged 0.46 defects per merged ticket with a spec and 0.86 without one.
- The Uvik Software SDD Benchmark found that the spec phase used 35.1% of all tokens in the spec arms.

## Does spec-driven development actually work?

It depends on the ticket. On feature and data-pipeline tickets, and on tickets that touch 3 or more files, the best spec arm merged more tickets than the control. There, the spec paid back its overhead. On bug-fix, refactor, and test-writing tickets, the control matched the best spec arm within the 10-point noise band or had a lower cost per merged ticket, so the spec did not pay back.

Table 2 and Table 3 show the split by ticket type and ticket size. The Uvik Software Spec Fit Test below turns the split into a rule you can use before a ticket starts.

## What is spec-driven development (SDD)?

Spec-driven development (SDD) is a way to build software with AI coding agents. A person and an agent first write a specification. The spec states what to build, why, and how to check the result. The agent then makes a plan, splits the work into tasks and writes the code. The spec, not the chat history, is the source of truth.

The term is new, and teams use it in different ways. [Birgitta Böckeler of Thoughtworks](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) describes three levels:

- **Spec-first.** A person writes a spec before the code, for one task.
- **Spec-anchored.** The spec stays in the repository after the task. The team updates it when the feature changes.
- **Spec-as-source.** People edit only the spec. The agent generates the code from it.

All four frameworks in this benchmark work at the spec-first level. OpenSpec also merges each finished change into a living spec folder, which is a step toward spec-anchored use.

The older term “specification-driven development” means something else: formal specifications and design by contract, from before AI coding agents. This page uses SDD in the new sense.

### Spec-driven development vs vibe coding, TDD and BDD

| Approach | What comes first | Main artifact | Who checks the result | 
|---|---|---|---|
| Vibe coding | A prompt | The generated code | Often nobody, or a quick look | 
| Spec-driven development (SDD) | A written spec | Spec, plan and task files | The engineer, against the spec | 
| Test-driven development (TDD) | A failing test | Unit tests | The test suite | 
| Behavior-driven development (BDD) | A behavior scenario | Given, When, Then scenarios | The team and the test runner | 

SDD borrows from TDD and BDD. Kiro writes acceptance criteria in EARS notation, which reads like a BDD scenario: WHEN a condition occurs, THE SYSTEM SHALL do a behavior. Most teams keep the spec as a spec document in Markdown, next to the code.

## Why we built this benchmark

Interest in spec-driven development grew fast. US searches for the term rose from 53 a month in June 2025 to 17,380 in March 2026, according to Ahrefs. Engineering leaders now ask one question: does the extra spec work pay back?

*Figure 1. US searches for “spec driven development” per month. Data: Ahrefs.*

The public evidence does not answer that question yet:

- Böckeler found that SDD tools take a long time to evaluate in conditions close to real work. She also asked which problem sizes and types SDD is for.
- A [June 2026 comparative study on arXiv](https://arxiv.org/abs/2606.04967) lists the lack of benchmarks for the complete SDD process as a risk for the field.
- A [July 2026 BMAD guide by Augment Code](https://www.augmentcode.com/guides/bmad-method-ai-development) states that no public controlled benchmark shows that BMAD improves speed or quality across project types.
- The public comparisons we found test one project or one feature. They score tools by opinion. They have no control arm and no blind review.

This benchmark is a controlled test. All arms get the same tickets, the same model and the same time boxes. A blind reviewer scores every result. A no-spec arm is the control.

It is the second study in the Uvik Software AI engineering benchmark series. The first, the Uvik Software AI Coding Agent Benchmark, compares Claude Code, Codex, Cursor and GitHub Copilot on the same 50 tickets. The Coding Agent Cost Index shows what those tools cost per engineer per month. Our [AI coding assistant statistics](https://uvik.net/blog/ai-coding-assistant-statistics/) track the wider adoption data.

## The five arms we tested

Four arms use a spec framework. One arm uses no spec. Spec Kit, BMAD, OpenSpec and the control run inside Claude Code 2026.09. Kiro, the agentic IDE from AWS, runs in its own IDE. All five arms use the same model: claude-sonnet-5. In Kiro, we set the model by hand and did not use the Auto router.

| Arm | Maker and license | Files per ticket | Workflow in this benchmark | Version | 
|---|---|---|---|---|
| GitHub Spec Kit | GitHub. Open source (MIT) | spec.md, plan.md, tasks.md and supporting files in a numbered feature folder | Constitution once per repository, then specify, clarify, plan, tasks, analyze, implement | 1.0 | 
| Kiro | Amazon Web Services. Commercial IDE with credit-based plans | requirements.md in EARS notation (bugfix.md for bugs), design.md, tasks.md | Bugfix Spec for bug-fix tickets. Feature Spec, requirements first, for all other tickets | build | 
| BMAD Method | BMad Code. Open source (MIT) | A tech spec (Quick Flow), or a PRD, an architecture document and story files | The track that BMAD’s scale guidance picks for each ticket | 6.x | 
| OpenSpec | Fission AI. Open source (MIT) | proposal.md, delta specs, design.md, tasks.md. Merged into openspec/specs on archive | Propose, apply, archive | build | 
| No spec (control) | None | None | Ticket text and acceptance criteria as the prompt | Claude Code 2026.09 | 

We chose these four frameworks for adoption. A June 2026 study on arXiv counted more than 48,000 GitHub stars each for Spec Kit, OpenSpec and the BMAD Method in May 2026. Kiro is the AWS IDE with a spec workflow built in. It is built on a VS Code base, and we compare IDEs for Python work in [best Python IDEs](https://uvik.net/blog/best-ide-for-python-in-2026/).

Not in this run: Tessl, which was in closed beta when we planned the benchmark. Also not in this run: smaller frameworks such as Get Shit Done (GSD) and Spec Kitty. See “What the next run will test”.

## How each framework structures the work

*Figure 2. What each workflow produces before the code.*

**GitHub Spec Kit** runs a fixed sequence of slash commands inside the coding agent. A constitution file holds the project rules. Each feature gets its own numbered folder and Git branch, with a spec, a plan and a task list. Spec Kit works with many agents, including GitHub Copilot, Claude Code and Gemini CLI. Source: [Spec Kit repository](https://github.com/github/spec-kit).

**Kiro** writes three files for each spec in the .kiro/specs folder. The file requirements.md holds user stories with acceptance criteria in EARS notation. The file design.md holds the technical design. The file tasks.md holds the tasks. For bugs, Kiro writes bugfix.md in place of requirements.md. Kiro also has a Vibe mode that writes no spec files. Source: [Kiro documentation](https://kiro.dev/docs/specs/).

**The BMAD Method** splits the work across agent roles, such as analyst, product manager, architect, scrum master, developer and QA. It is the multi-agent pattern that we compare in [agentic AI frameworks](https://uvik.net/blog/agentic-ai-frameworks/), applied to software delivery. BMAD scales the planning to the size of the work. Small work goes through Quick Flow with one tech spec. Larger work gets a product requirements document (PRD), an architecture document and story files. Source: [BMAD documentation](https://docs.bmad-method.org/).

**OpenSpec** by Fission AI puts each change in its own folder, with a proposal, delta specs, a design and a task list. The archive step merges the delta specs into the living spec folder. OpenSpec describes itself as iterative and built for existing codebases. Source: [OpenSpec repository](https://github.com/Fission-AI/OpenSpec).

**The no-spec control** gives the agent the ticket text and the acceptance criteria as the prompt. The project instruction file is the only other context. This is the same setup as the Claude Code arm of the Uvik Software AI Coding Agent Benchmark.

## The task set: 50 brownfield Python tickets

The task set is the same 50 production Python tickets as in the Uvik Software AI Coding Agent Benchmark. The tickets come from five client repositories. The client code stays private.

*Figure 3. The task set: 50 production Python tickets.*

| Category | Tickets | What the ticket asks | Accepted when | 
|---|---|---|---|
| Bug fix with a failing test | 10 | Fix a bug that a failing test reproduces. The fix must not change public behavior elsewhere. | The failing test passes. All existing tests pass. The diff touches only the files the fix needs. | 
| Feature in FastAPI or Django | 10 | Add an endpoint, a model field or an admin action from a written ticket. | The acceptance test passes. The change follows the project conventions. A migration is included when needed. | 
| Refactor with tests green | 10 | Extract, rename or restructure a module with no change in behavior. | All tests pass before and after. No public interface changes. The complexity of the target module goes down. | 
| Data pipeline (pandas or PySpark) | 10 | Add or fix a transformation step with a defined input and output schema. | The output matches the reference dataset. The step handles the listed edge cases. | 
| Test writing and coverage | 10 | Write tests for an untested module to a stated coverage target. | The coverage target is met. The tests are deterministic. The tests fail when the module is broken on purpose. | 

All 50 tickets are brownfield: each one changes existing production code. This matters. [GitHub names feature work in existing systems](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) as the case where SDD is most powerful. Böckeler found that two of the three tools she tried were more work to introduce into an existing codebase. This benchmark tests that case directly.

We also classed each ticket by size. The size comes from the number of files in the reference solution: small (1 to 2), medium (3 to 5) and large (6 or more). The task set has 20 small, 20 medium and 10 large tickets.

## How we ran each task

*Figure 4. One ticket, five workflows, one blind review.*

1. Before the run, each repository got the one-time setup of each framework. This is the Spec Kit constitution, the Kiro steering files, the BMAD project context and the OpenSpec project configuration. The control used the project instruction file only. Setup time is in Table 5. We do not charge it to any ticket.
2. Each engineer did two calibration tickets with each framework before the run. Calibration tickets are not in the task set.
3. The engineer opens the repository at the tagged commit for the ticket.
4. Spec phase: the engineer starts the framework with the ticket text and the acceptance criteria. The agent writes the spec files. The engineer reviews them, answers questions and can edit the spec text. The time box is 45 minutes. Each correction or edit counts as one spec intervention.
5. If the spec time box ends, the build phase starts with the spec as it is.
6. Build phase: the agent implements the tasks. The engineer can answer questions and correct the agent, but does not write code by hand. The time box is 45 minutes, the same as in the AI Coding Agent Benchmark. Each correction counts as one build intervention.
7. The control skips the spec phase. Its build phase starts with the ticket text and the acceptance criteria as the prompt.
8. A task stops when the agent reports done and the engineer accepts. It also stops when a time box ends, or when the engineer logs a third intervention on the same problem. Each time the engineer sends the agent back after it reports done counts as one rework round.
9. The engineer records the minutes per phase, the interventions, the rework rounds and the tokens per phase. Cost uses the vendor’s API rate on the run date, from the Uvik Software LLM API pricing tracker. Kiro cost uses the credits used and the plan price per credit on the run date.
10. The code change is exported as a patch. A script removes framework folders, spec files, task IDs and spec references in comments. It does not change the code. The patch gets a random ID.
11. A senior reviewer who did not run the task reviews the patch against the acceptance criteria and the project conventions. The reviewer records merged or not merged and the number of defects. A second reviewer resolves any disagreement.
12. After the merge decision, a second reviewer compares each merged patch with its spec. The reviewer logs each mismatch (spec drift) and scores the spec against the eight-item Uvik Software spec checklist (spec completeness). This step comes after the merge decision, so it cannot change it.
13. Five engineers ran the benchmark. Each engineer ran each ticket in one arm only. The order of arms was random for each ticket.
14. To measure run-to-run noise, 10 tickets (two per category) ran a second time in every arm, with a different engineer. The difference between the two runs is the noise band. We do not rank two arms when the gap between them is inside the noise band.
15. After the run, each engineer rated each workflow from 1 to 5 on spec review effort and on control over the agent. Table 6 shows the ratings. They do not change the ranking.

## How we scored

*Figure 5. How every run is scored.*

| Measure | Definition | Better is | 
|---|---|---|
| Merge rate | Share of the 50 tickets that the blind reviewer accepted without a rewrite. | Higher | 
| Cost per merged ticket | Total cost of all 50 tickets, spec phase included, divided by the number of merged tickets. This is the headline number. | Lower | 
| Time to merge | Minutes from the first framework command to an accepted patch, spec phase and build phase together. Median of merged tickets. | Lower | 
| Spec overhead | Minutes in the spec phase, the engineer’s review included. | Lower | 
| Spec size | Lines of Markdown that the framework wrote for the ticket. | Lower is easier to review | 
| Spec completeness | Items of the eight-item Uvik Software spec checklist that the spec covers, from 0 to 8. | Higher | 
| Spec drift | Share of merged tickets where the code and the spec do not match: a stated criterion is missing, or the code adds behavior that the spec does not describe. | Lower | 
| Rework rounds | Times the engineer sent the agent back after it reported done. Per ticket. | Lower | 
| Review defects | Defects that the blind reviewer found in an accepted patch. Per merged ticket. | Lower | 
| Human interventions | Corrections in the spec phase and in the build phase. Per ticket. | Lower | 
| Tokens | Input and output tokens per ticket, split by phase. | Lower | 
| Engineer ratings | Spec review effort and control over the agent, from 1 to 5. Context only. | Not ranked | 

**Cost per merged ticket** decides the question. A spec costs minutes and tokens before any code exists. It pays back only when it raises the merge rate or cuts rework enough to cover that cost. We use the same rule when we set up [LLM evaluation and observability](https://uvik.net/services/llm-evaluation-observability/) for client agent systems.

## Results

### Table 1. Overall results, Q4 2026 run

| Source: Uvik Software SDD Benchmark 2026, Q4 2026 run |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|
| Arm | Merge rate (of 50) | Cost per merged ticket (USD) | Median time to merge (min) | Spec overhead, median (min) | Spec size, median (lines) | Spec drift | Review defects per merged ticket | Rework rounds per ticket | 
|---|---|---|---|---|---|---|---|---|
| GitHub Spec Kit | 80% (40/50) | $3.33 | 44 | 18 | 132 | 12.5% | 0.57 | 0.62 | 
| Kiro | 82% (41/50) | $2.35 | 41 | 16 | 106 | 4.9% | 0.39 | 0.64 | 
| BMAD Method | 82% (41/50) | $4.23 | 55 | 28 | 188 | 12.2% | 0.49 | 0.46 | 
| OpenSpec | 84% (42/50) | $2.71 | 36 | 12 | 93 | 2.4% | 0.40 | 0.52 | 
| No spec (control) | 72% (36/50) | $2.43 | 29 | 0 | 0 | n/a | 0.86 | 0.74 | 

The noise band on merge rate is plus or minus 10 percentage points. We do not rank two arms when the gap between them is inside the noise band.

### Table 2. Merge rate by ticket type

| Source: Uvik Software SDD Benchmark 2026, Q4 2026 run |  |  |  |  |  | 
|---|---|---|---|---|---|
| Ticket type (10 each) | Spec Kit | Kiro | BMAD | OpenSpec | No spec | 
|---|---|---|---|---|---|
| Bug fix with a failing test | 80% | 90% | 80% | 90% | 90% | 
| Feature in FastAPI or Django | 80% | 80% | 90% | 80% | 60% | 
| Refactor with tests green | 80% | 80% | 80% | 80% | 80% | 
| Data pipeline | 80% | 90% | 90% | 90% | 60% | 
| Test writing and coverage | 80% | 70% | 70% | 80% | 70% | 

### Table 3. Merge rate by ticket size

| Source: Uvik Software SDD Benchmark 2026, Q4 2026 run |  |  |  |  |  | 
|---|---|---|---|---|---|
| Ticket size | Spec Kit | Kiro | BMAD | OpenSpec | No spec | 
|---|---|---|---|---|---|
| Small (1 to 2 files) | 80% | 85% | 85% | 85% | 85% | 
| Medium (3 to 5 files) | 80% | 80% | 80% | 85% | 70% | 
| Large (6 or more files) | 80% | 80% | 80% | 80% | 50% | 

### Table 4. Where the tokens went

| Source: Uvik Software SDD Benchmark 2026, Q4 2026 run |  |  |  | 
|---|---|---|---|
| Arm | Spec-phase tokens, median | Build-phase tokens, median | Spec share of tokens | 
|---|---|---|---|
| GitHub Spec Kit | 147206 | 286138 | 34.0% | 
| Kiro | 130986 | 276962 | 32.1% | 
| BMAD Method | 227212 | 290429 | 43.9% | 
| OpenSpec | 104924 | 265717 | 28.3% | 
| No spec (control) | 0 | 331936 | 0.0% | 

### Table 5. Spec quality and setup

| Source: Uvik Software SDD Benchmark 2026, Q4 2026 run |  |  |  | 
|---|---|---|---|
| Arm | Spec completeness, median (of 8) | Merge rate when completeness is 6 or more | One-time setup per repository (min) | 
|---|---|---|---|
| GitHub Spec Kit | 6 | 81.3% | 18 | 
| Kiro | 7 | 92.7% | 12 | 
| BMAD Method | 7 | 92.1% | 28 | 
| OpenSpec | 7 | 89.7% | 10 | 

### Table 6. Engineer ratings after the run (median, 1 to 5)

| Source: Uvik Software SDD Benchmark 2026, Q4 2026 run |  |  |  | 
|---|---|---|---|
| Arm | Spec review effort (5 = easy) | Control over the agent | Would use again on client work | 
|---|---|---|---|
| GitHub Spec Kit | 4 | 4 | 4 of 5 engineers | 
| Kiro | 4 | 5 | 4 of 5 engineers | 
| BMAD Method | 2 | 4 | 3 of 5 engineers | 
| OpenSpec | 4 | 4 | 5 of 5 engineers | 

## Which tickets need a spec?

Böckeler asked which problem sizes and types SDD is meant for. Table 2 and Table 3 answer that question for brownfield Python work.

- On small tickets (1 to 2 files), the best spec-arm merge rate was 85% and the control also merged 85%. The lowest cost per merged ticket among the spec arms was $1.64, against $1.59 without a spec.
- On medium tickets (3 to 5 files), the best spec arm merged 85% and the control merged 70%.
- On large tickets (6 or more files), the best spec arm merged 80% and the control merged 50%.
- By type, the spec arms gained the most on feature and data-pipeline tickets: 30 percentage points over the control. They gained the least on bug-fix and refactor tickets: 0 points.

In this run, a spec paid back its overhead on tickets that touch 3 or more files. Below that size, the spec cost more than the rework it prevented.

## Spec-driven development vs vibe coding: what the control showed

The no-spec arm is the control. It is the prompt-first workflow, or prompt-driven development. Many teams call it vibe coding. The ticket goes to the agent as a prompt, with no written spec. There is one difference from pure vibe coding. A senior engineer reviewed every result, a [human-in-the-loop](https://uvik.net/blog/human-in-the-loop-ai/) setup. So the control measures prompt-first coding with review, not unreviewed code.

The control merged 36 of 50 tickets at $2.43 per merged ticket, with a median time to merge of 29 minutes. The four spec arms merged 40 to 42 tickets, at $2.35 to $4.23 per merged ticket. Their median time to merge was 36 to 55 minutes.

Review defects are the technical debt signal. [IBM](https://www.ibm.com/think/topics/spec-driven-development) argues that vibe coding speeds up technical debt, because it makes it easy to produce a lot of code without full understanding or validation. In this benchmark, blind reviewers logged 0.86 defects per merged ticket for the control and 0.46 for the spec arms together.

In this run, a written spec cut review defects most clearly on bug-fix tickets, but the extra minutes did not pay back on small tickets.

## BMAD vs Spec Kit vs OpenSpec vs Kiro: head-to-head

Public comparisons disagree. One widely shared 2026 agency comparison timed a single dashboard build: 12 minutes with OpenSpec, 90 minutes with Spec Kit and 5.5 hours with BMAD. Another tester scored the tools from 1 to 5 on one feature. Neither had a control arm. The results below use the same 50 tickets and the same model for every arm.

### BMAD vs Spec Kit

In the Uvik Software SDD Benchmark, the BMAD Method merged 41 of 50 tickets and GitHub Spec Kit merged 40. The cost per merged ticket was $4.23 for BMAD and $3.33 for Spec Kit. BMAD wrote a median of 188 lines of spec per ticket, and Spec Kit wrote 132. The main design difference: BMAD passes the work between agent roles, and Spec Kit runs one agent through fixed phases.

### OpenSpec vs Spec Kit

In the Uvik Software SDD Benchmark, OpenSpec merged 42 of 50 tickets and GitHub Spec Kit merged 40. The median spec phase took 12 minutes with OpenSpec and 18 minutes with Spec Kit. The main design difference: OpenSpec writes delta specs for each change and merges them into a living spec. Spec Kit writes a new spec folder and branch for each feature.

### Kiro vs Spec Kit

In the Uvik Software SDD Benchmark, Kiro merged 41 of 50 tickets and GitHub Spec Kit merged 40. The cost per merged ticket was $2.35 for Kiro and $3.33 for Spec Kit. The main design difference: Kiro is an IDE with the spec workflow built in. Spec Kit is an open-source toolkit that runs inside the agent you already use.

### BMAD vs OpenSpec

In the Uvik Software SDD Benchmark, the BMAD Method merged 41 of 50 tickets and OpenSpec merged 42. Their median spec phases took 28 and 12 minutes. The June 2026 arXiv study rated BMAD as the framework with the deepest process, and OpenSpec as the one with the leanest profile.

### Table 7. Operational fit

These are facts from each project’s documentation in September 2026, not benchmark results.

| Framework | Where specs live | Isolation per feature | Review gates | Agents supported | License | 
|---|---|---|---|---|---|
| GitHub Spec Kit | A specs folder in the repository | One folder and one Git branch per feature | Checkpoints between phases, with clarify and analyze steps | 30+ agents | MIT | 
| Kiro | .kiro/specs in the repository | One folder per spec | Approval between phases in Feature Specs. None in Quick Spec | Kiro IDE and Kiro CLI | Commercial | 
| BMAD Method | The project’s docs folder | Shared folder by default | Agent handoffs and an adversarial code review workflow | Most coding agents | MIT | 
| OpenSpec | openspec/changes and openspec/specs | One folder per change | No gates between phases | 25+ tools | MIT | 

In this run, BMAD Method had the highest merge rate on feature tickets at 90%. Kiro, BMAD Method and OpenSpec tied for the highest merge rate on data-pipeline tickets at 90%.

## The Uvik Software Spec Fit Test

The Uvik Software Spec Fit Test turns the benchmark data into a rule. Use it before an engineer or an agent starts a ticket.

Write a spec when 3 or more of these statements are true:

1. The change touches 3 or more files.
2. The ticket has 4 or more acceptance criteria.
3. The change crosses a module, service or repository boundary.
4. The change alters a data schema or a public API.
5. More than one engineer or agent will work on the change.
6. The code is regulated or audited.

When fewer statements are true, give the agent the ticket text and the acceptance criteria, then review the result. In this benchmark, that was the cheaper path for bug-fix, refactor, and test-writing tickets.

Which framework: in this run, Kiro had the best overall cost per merged ticket at $2.35. All four spec frameworks tied at an 80% merge rate on large tickets. Teams that want the workflow inside the IDE can use Kiro. Teams that want to keep their current agent can use Spec Kit, BMAD or OpenSpec.

### What to put in a spec: the Uvik Software spec checklist

The reviewers scored every spec in this benchmark against eight items. Specs that covered 6 or more items merged 89.3% of the time. Specs that covered fewer merged 60.0%.


*Figure 6. The Uvik Software spec checklist. Free to reuse with credit (CC BY 4.0).*

1. **Goal.** The outcome in one sentence, for the user or the system.
2. **Scope.** What is in scope and what is out of scope.
3. **Inputs and outputs.** The data in and the data out, with types.
4. **Data changes.** The schema, migrations and contracts that change.
5. **Edge cases.** Error behavior and unusual input.
6. **Acceptance tests.** How to prove that the change works.
7. **Constraints.** Performance, security and compatibility limits.
8. **No-change list.** Files and interfaces that must not change.

Add the items to your framework’s templates. In Spec Kit, the constitution is the place for rules that apply to every spec.

## Limitations

- One team ran the benchmark. The engineers had used the frameworks before, but not for equal time. Each did two calibration tickets per framework.
- Python only. The results do not transfer to TypeScript, Java or Go without a new run.
- One model. A different model can change the gaps between arms.
- Kiro runs in its own IDE, and the other spec arms run in Claude Code. The model is the same, but the agent harness is not. The Kiro results measure Kiro as a product.
- Fixed time boxes: 45 minutes for the spec phase and 45 minutes for the build phase. Longer boxes can favor frameworks that plan more.
- One ticket at a time. The benchmark does not measure the long-term value of a living spec across many changes (spec-anchored use).
- Engineer ratings are opinions. They add context and do not change the ranking.
- The frameworks change every month. The versions and dates are stated, so the result can be checked. The next run replaces this one.
- The tickets come from client repositories. The code is private. The task set CSV lists the ticket text and the acceptance criteria.

## What the next run will test

- A verifier agent that checks the build against the spec before the human review.
- Model tiering: a stronger model for the spec phase and a cheaper model for the build phase.
- Claude Code plan mode as a light arm between no spec and a full framework.
- Spec-anchored use: one living spec across three changes to the same feature.
- Frameworks that reach general availability, such as Tessl.
- A TypeScript task set.

Tell us what to test next. We link to independent runs from this page.

## How to cite this benchmark

Uvik Software (2026). Spec-Driven Development Benchmark 2026: Spec Kit vs Kiro vs BMAD vs OpenSpec vs No Spec on 50 Production Python Tickets, Q4 2026 run. https://uvik.net/blog/spec-driven-development-benchmark/

Short form for articles: “according to the Uvik Software SDD Benchmark”. Please link to this page, not to the CSV, so that readers see the method and the version.

**License.** The data, the tables and the charts are licensed under CC BY 4.0. You can reuse them for free. Credit: “Source: Uvik Software SDD Benchmark 2026”, with a link to this page.

**Embed a chart.** Copy this code:

```
<a href="https://uvik.net/blog/spec-driven-development-benchmark/">
  <img src="https://uvik.net/wp-content/uploads/uvik-sdd-merge-rate.png"
       alt="Merge rate by workflow, Uvik Software SDD Benchmark 2026" width="1200">
</a>
<p>Source: <a href="https://uvik.net/blog/spec-driven-development-benchmark/">Uvik Software SDD Benchmark 2026</a> (CC BY 4.0)</p>
```
## About Uvik Software

Uvik Software is a Python-first staff augmentation and AI engineering company. It was founded in 2015. Its headquarters are at Tuukri 19, 10152 Tallinn, Estonia, and it has a commercial office at 150 Princes Street, Ipswich, Suffolk, IP1 1RJ, United Kingdom. Uvik Software has 50+ senior engineers. Every engineer has at least 7 years of experience, and the company employs no junior engineers.

Uvik Software is a member of the Claude Partner Network and the Python Software Foundation, and a Databricks partner. Its engineers use AI coding agents under a governed workflow, with human review before merge. Clients get matched engineer profiles within 48 hours of a signed SOW and a 30-day no-cost replacement guarantee.

Services: [Python development services](https://uvik.net/services/python-development-services/), [AI development services](https://uvik.net/services/ai-development-services/) and [AI integration services](https://uvik.net/services/ai-integration-services/).

Research disclosure: Uvik Software publishes this research and provides related Python, AI and staff augmentation services.

**Work with the engineers who ran this benchmark.** Uvik Software embeds senior Python and AI engineers in client teams, as staff augmentation or as [forward deployed engineering](https://uvik.net/blog/forward-deployed-engineering/) teams. See how we [embed an engineer within 2 weeks](https://uvik.net/blog/staff-augmentation-best-practices/), or read the [Django maintainability case study](https://uvik.net/case-studies/services-marketplace-django-maintainability-embedded-python-squad/). Senior rates are $50 to $99 per hour; see [pricing](https://uvik.net/pricing/). To start, [hire Python developers](https://uvik.net/technologies/hire-python-developers/) or send your project in the form below.

### Related research

- [Coding Agent Cost Index](https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/): what an AI coding agent costs per engineer.
- [AI coding assistant statistics](https://uvik.net/blog/ai-coding-assistant-statistics/): adoption and trust data.
- [Claude Code vs Cursor vs Copilot vs Codex](https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/): the four tools compared.
- [Human-in-the-loop AI](https://uvik.net/blog/human-in-the-loop-ai/): design patterns for human review of AI agents.

## Frequently asked questions

### What is spec-driven development?

### What does SDD stand for in AI coding?

### Does spec-driven development actually work?

### What is the difference between spec-driven development and vibe coding?

### What are the key differences between BDD and spec-driven development?

### BMAD vs Spec Kit: which is better?

### OpenSpec vs Spec Kit: which is better?

### Is Kiro better than Spec Kit?

### Does Claude Code support spec-driven development?

[Claude Code vs Cursor vs Copilot vs Codex](https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/).
