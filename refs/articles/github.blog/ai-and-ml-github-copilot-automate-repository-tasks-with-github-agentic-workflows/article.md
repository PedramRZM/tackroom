---
title: "Automate repository tasks with GitHub Agentic Workflows"
author: "Don Syme; Peli de Halleux"
date: "2026-02-13"
url: "https://github.blog/ai-and-ml/github-copilot/automate-repository-tasks-with-github-agentic-workflows/"
site: "The GitHub Blog"
type: "article"
via: "direct"
---
**Try GitHub Agentic Workflows in a repo today**! Install `gh-aw`, add a starter workflow or create one using AI, and run it. Then, [share what you build (and what you want next)](https://gh.io/aw-tp-community-feedback).

Imagine visiting your repository in the morning and feeling calm because you see:

- Issues triaged and labelled
- CI failures investigated with proposed fixes
- Documentation has been updated to reflect recent code changes.
- Two new pull requests that improve testing await your review.

All of it visible, inspectable, and operating within the boundaries you’ve defined.

That’s the future powered by [GitHub Agentic Workflows](https://github.github.com/gh-aw/?utm_source=blog-agentic-workflows-cta&utm_medium=blog&utm_campaign=agentic-workflows-tech-preview-feb-2026): automated, intent-driven repository workflows that run in GitHub Actions, authored in plain Markdown and executed with coding agents. They’re designed for people working in GitHub, from individuals automating a single repo to teams operating at enterprise or open-source scale.

At GitHub Next, we began GitHub Agentic Workflows as an investigation into a simple question: what does repository automation with strong guardrails look like in the era of AI coding agents? A natural place to start was GitHub Actions, the heart of scalable repository automation on GitHub. By bringing automated coding agents into actions, we can enable their use across millions of repositories, while keeping decisions about when and where to use them in your hands.

GitHub Agentic Workflows are now available in [technical preview](https://github.github.com/gh-aw/?utm_source=blog-agentic-workflows-cta&utm_medium=blog&utm_campaign=agentic-workflows-tech-preview-feb-2026). In this post, we’ll explain what they are and how they work. We invite you to put them to the test, to explore where repository-level AI automation delivers the most value.

## AI repository automation: A revolution through simplicity

The concept behind GitHub Agentic Workflows is straightforward: you describe the outcomes you want in plain Markdown, add this as an automated workflow to your repository, and it executes using a coding agent in GitHub Actions.

This brings the power of coding agents into the heart of repository automation. Agentic workflows run as standard GitHub Actions workflows, with added guardrails for sandboxing, permissions, control, and review. When they execute, they can use different coding agent engines—such as Copilot CLI, Claude Code, or OpenAI Codex—depending on your configuration.

The use of GitHub Agentic Workflows makes entirely new categories of repository automation and software engineering possible, in a way that fits naturally with how developer teams already work on GitHub. All of them would be difficult or impossible to accomplish traditional YAML workflows alone:

1. **Continuous triage**: automatically [summarize, label, and route new issues](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows/).
2. **Continuous documentation**: keep [READMEs and documentation aligned with code changes](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/).
3. **Continuous code simplification**: [repeatedly identify code improvements](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-continuous-simplicity/) and open pull requests for them.
4. **Continuous test improvement**: [assess test coverage and add high-value tests](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-testing-validation/).
5. **Continuous quality hygiene**: proactively [investigate CI failures and propose targeted fixes](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-quality-hygiene/).
6. **Continuous reporting**: [create regular reports on repository health, activity, and trends](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-metrics-analytics/).

These are just a few examples of repository automations that showcase the power of GitHub Agentic Workflows. We call this [Continuous AI](https://githubnext.com/projects/continuous-ai/): the integration of AI into the SDLC, enhancing automation and collaboration similar to continuous integration and continuous deployment (CI/CD) practices.

GitHub Agentic Workflows and Continuous AI are designed to augment existing CI/CD rather than replace it. They do not replace build, test, or release pipelines, and their use cases largely do not overlap with deterministic CI/CD workflows. Agentic workflows run on GitHub Actions because that is where GitHub provides the necessary infrastructure for permissions, logging, auditing, sandboxed execution, and rich repository context.

In our own usage at GitHub Next, we’re finding new uses for agentic workflows nearly every day. Throughout GitHub, teams have been using agentic workflows to create custom tools for themselves in minutes, replacing chores with intelligence or paving the way for humans to get work done by assembling the right information, in the right place, at the right time. A new world of possibilities is opening for teams and enterprises to keep their repositories healthy, navigable, and high-quality.

## Let’s talk guardrails and control

Designing for safety and control is non-negotiable. GitHub Agentic Workflows implements a defense-in-depth security architecture that protects against unintended behaviors and prompt-injection attacks.

Workflows run with read-only permissions by default. Write operations require explicit approval through [safe outputs](https://github.github.com/gh-aw/introduction/architecture/), which map to pre-approved, reviewable GitHub operations such as creating a pull request or adding a comment to an issue. Sandboxed execution, tool allowlisting, and network isolation help ensure that coding agents operate within controlled boundaries.

Guardrails like these make it practical to run agents continuously, not just as one-off experiments. See our [security architecture](https://github.github.com/gh-aw/introduction/architecture/) for more details.

One alternative approach to agentic repository automation is to run coding agent CLIs, such as Copilot or Claude, directly inside a standard GitHub Actions YAML workflow. This approach often grants these agents more permission than is required for a specific task. In contrast, GitHub Agentic Workflows run coding agents with read-only access by default and rely on safe outputs for GitHub operations, providing tighter constraints, clearer review points, and stronger overall control.

## A simple example: A daily repo report

Let’s look at an agentic workflow which creates a daily status report for repository maintainers.

In practice, you will usually use AI assistance to [create your workflows](https://github.github.io/gh-aw/setup/creating-workflows/). The easiest way to do this is with an interactive coding agent. For example, with your favorite coding agent, you can enter this prompt:

`Generate a workflow that creates a daily repo status report for a maintainer. Use the instructions at https://github.com/github/gh-aw/blob/main/create.md`
The coding agent will interact with you to confirm your specific needs and intent, write the Markdown file, and check its validity. You can then review, refine, and validate the workflow before adding it to your repository.

This will create two files in `.github/workflows`:

- `daily-repo-status.md` (the agentic workflow)
- `daily-repo-status.lock.yml` (the corresponding agentic workflow lock file, which is executed by GitHub Actions)

The file `daily-repo-status.md` will look like this:

```
--- 
on: 
  schedule: daily 
 
permissions: 
  contents: read 
  issues: read 
  pull-requests: read 
 
safe-outputs: 
  create-issue: 
    title-prefix: "[repo status] " 
    labels: [report] 
 
tools: 
  github: 
---  
 
# Daily Repo Status Report 
 
Create a daily status report for maintainers. 
 
Include 
- Recent repository activity (issues, PRs, discussions, releases, code changes) 
- Progress tracking, goal reminders and highlights 
- Project status and recommendations 
- Actionable next steps for maintainers 
 
Keep it concise and link to the relevant issues/PRs.
```
This file has two parts:

1. **Frontmatter** (YAML between `---` markers) for configuration
2. **Markdown instructions** that describe the job in natural language in natural language

The Markdown is the intent, but the trigger, permissions, tools, and allowed outputs are spelled out up front.

If you prefer, you can add the workflow to your repository manually:

1. **Create the workflow**: Add `daily-repo-status.md` with the frontmatter and instructions.
2. **Create the lock file**:
  - `gh extension install github/gh-aw`
  - `gh aw compile`
3. **Commit and push**: Commit and push files to your repository.
4. **Add any required secrets**: For example, [add a token or API key for your coding agent](https://github.github.com/gh-aw/reference/engines/).

Once you add this workflow to your repository, it will run automatically or you can trigger it manually using GitHub Actions. When the workflow runs, it creates a status report issue like this:

## What you can build with GitHub Agentic Workflows

If you’re looking for further inspiration [Peli’s Agent Factory](https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/) is a guided tour through a wide range of workflows, with practical patterns you can adapt, remix, and standardize across repos.

A useful mental model: if repetitive work in a repository can be described in words, it might be a good fit for an agentic workflow.

If you’re looking for design patterns, check out [ChatOps](https://github.github.com/gh-aw/patterns/chatops/), [DailyOps](https://github.github.com/gh-aw/patterns/dailyops/), [DataOps](https://github.github.com/gh-aw/patterns/dataops/), [IssueOps](https://github.github.com/gh-aw/patterns/issueops/), [ProjectOps](https://github.github.com/gh-aw/patterns/projectops/), [MultiRepoOps,](https://github.github.com/gh-aw/patterns/multirepoops/) and [Orchestration](https://github.github.com/gh-aw/patterns/orchestration/).

Uses for agent-assisted repository automation often depend on particular repos and development priorities. Your team’s approach to software development will differ from those of other teams. It pays to be imaginative about how you can use agentic automation to augment *your* team for *your* repositories for *your* goals.

## Practical guidance for teams

Agentic workflows bring a shift in thinking. They work best when you focus on goals and desired outputs rather than perfect prompts. You provide clarity on what success looks like, and allow the workflow to explore how to achieve it. Some boundaries are built into agentic workflows by default, and others are ones you explicitly define. This means the agent can explore and reason, but its conclusions always stay within safe, intentional limits.

You will find that your workflows can range from very general (“Improve the software”) to very specific (“Check that all technical documentation and error messages for this educational software are written in a style suitable for an audience of age 10 or above”). You can choose the level of specificity that’s appropriate for your team.

GitHub Agentic Workflows use coding agents at runtime, which incur billing costs. When using Copilot with default settings, each workflow run typically incurs two [premium requests](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-premium-requests): one for the agentic work and one for a guardrail check through safe outputs. The models used can be configured to help manage these costs. Today, automated uses of Copilot are associated with a user account. For other coding agents, refer to our [documentation](https://github.github.com/gh-aw/reference/engines/) for details. Here are a few more tips to help teams get value quickly:

- Start with **low-risk outputs** such as comments, drafts, or reports before enabling pull request creation.
- For coding, start with **goal-oriented improvements** such as routine refactoring, test coverage, or code simplification rather than feature work.
- For reports, use instructions that are **specific about what “good” looks like**, including format, tone, links, and when to stop.
- Agentic workflows create an agent-only, sub-loop that’s able to be autonomous because agents are acting under defined terms. But it’s important that **humans stay in the broader loop** of forward progress in the repository, through reports, issues, and pull requests. With GitHub Agentic Workflows, **pull requests are never merged automatically**, and humans must always review and approve.
- Treat the workflow Markdown as code. Review changes, keep it small, and evolve it intentionally.

Continuous AI works best if you use it in conjunction with CI/CD. Don’t use agentic workflows as a replacement for GitHub Actions YAML workflows for CI/CD. This approach extends continuous automation to more subjective, repetitive tasks that traditional CI/CD struggle to express.

## Build the future of automation with us

GitHub Agentic Workflows are available now in technical preview and are a collaboration between GitHub, Microsoft Research, and Azure Core Upstream. We invite you to try them out and help us shape the future of repository automation.

We’d love for you to be involved! [Share your thoughts in the Community discussion](https://gh.io/aw-tp-community-feedback), or join us (and tons of other awesome makers) in the #agentic-workflows channel of the [GitHub Next Discord](https://gh.io/next-discord). We look forward to seeing what you build with GitHub Agentic Workflows. Happy automating!

## Tags:

## Written by

## Related posts

### 
					[Beyond code generation: A developer’s guide to agentic engineering](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/)				

Writing code got faster. The work around it didn’t. See how you can plan, write code, review changes, and investigate production issues with GitHub Copilot, and what work still needs your judgment.

### 
					[How 3 Java Champions are using GitHub Copilot for increased productivity](https://github.blog/ai-and-ml/github-copilot/how-3-java-champions-are-using-github-copilot-for-increased-productivity/)				

Three Java Champions share how they use GitHub Copilot to solve problems, accelerate development, and keep humans responsible for the results.

### 
					[How to continue a GitHub Copilot app session in VS Code](https://github.blog/ai-and-ml/github-copilot/how-to-continue-a-github-copilot-app-session-in-vs-code/)				

Learn how to move an agent session from the GitHub Copilot app into VS Code without losing the conversation, code changes, or working context.
