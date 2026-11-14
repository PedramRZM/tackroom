# Anthropic staff: additional talks and articles

Research date: 2026-11-13. Four core sources read in full and synthesized below;
three additional sources saved for background without deriving recommendations.
These seven URLs were absent from the starting metadata inventory.

## Questions

What do staff demonstrate or report using themselves? Which sources add concrete
mechanics rather than repeat existing advice? What is still missing in tackroom,
and which practices are version-specific or unsuitable for a small setup?

## Core sources

### Lydia Hallie — Rethinking Claude Code Best Practices

Source: [Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic](https://www.youtube.com/watch?v=vlfCjWuv4es). Saved: [refs/videos/vlfCjWuv4es/transcript.md](../videos/vlfCjWuv4es/transcript.md).

Speaker: Lydia Hallie, Claude Code team (self-identifies at 00:02). Event date:
2026-11-11, confirmed by the organizer's [schedule](https://ai.engineer/code/2026/schedule).
Exact video upload date is not populated in saved metadata and was not independently
confirmed from the primary video page. English auto-captions can misrender names,
model versions and command syntax. High relevance; firsthand team account plus advice.

- 03:04–04:05: prune instructions the model can infer; she describes a prompt-audit
  command. Our periodic instruction review already covers the principle.
- 06:05–10:10: permissions, shell sandboxing and disposable cloud environments
  address different boundaries. Hooks and MCP servers are outside the shell sandbox.
- 11:12–13:14: turn completion criteria into intermediate checks; report actual
  output. A task-completion hook should block failed checks with exit 2.
- 14:15: a separate group validates review findings before humans review by risk.
- 15:16–17:18: an orchestrator coordinates isolated sessions; this describes their
  evolving workflow, not a requirement to add an orchestrator to this repository.

The task-completion event semantics were cross-checked against the [hooks reference](https://code.claude.com/docs/en/hooks#taskcompleted),
already saved at `refs/articles/code.claude.com/docs-en-hooks-md/article.md`,
section `TaskCompleted`. It concerns Claude's internal tasks, not automatic closure
of GitHub issues or the files in `tasks/`. No hook was implemented or live-tested.

### Cal Rueb — Claude Code best practices

Source: [Claude Code best practices | Code w/ Claude](https://www.youtube.com/watch?v=gv0WHhKelSE). Saved: [refs/videos/gv0WHhKelSE/transcript.md](../videos/gv0WHhKelSE/transcript.md).

Speaker: Cal Rueb, Anthropic; event 2025-05-22, upload 2025-07-31, from the
primary YouTube description returned by web search. English caption transcript.
Credibility: contributor explaining personal use and team practices. Historical
context; do not treat this as current CLI documentation.

- 07:30: he asks Claude to explore and return options before editing.
- 12:43–13:48: prefer a well-known CLI when it already does the job; explain internal
  CLIs in project instructions.
- 16:56: he personally manages two sessions, while others manage four.
- 21:03: checks the public changelog weekly.
- 23:09: revisit model-specific workarounds after an upgrade.
- 24:15–25:15: he hands work to another session through a written ticket file.

Relevance: medium as direct evidence for practices already present. It reinforces
file-based handoffs, modest concurrency and pruning. Older thinking prompts and
permission behavior are not recommendations for current models.

### Claude Help Center — Claude Code power user tips

Source: [Claude Code power user tips | Claude Help Center](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips). Saved: [refs/articles/support.claude.com/en-articles-14554000-claude-code-power-user-tips/article.md](../articles/support.claude.com/en-articles-14554000-claude-code-power-user-tips/article.md).

Corporate author: Anthropic; no individual byline. Extracted date 2026-10-30;
treat it as a page-date field, not a verified first-publication date. The introduction
explicitly calls this a collection of individual engineers' practices. High
relevance as an official entry point; many practices duplicate already-saved posts.

Locators: Working in parallel; Planning before building; Verification; Commands,
skills, and subagents; Customizing your environment. It collects worktree isolation,
a second session reviewing a plan, domain verification, scoped agents, and personal
terminal/status-line/voice preferences. The page distinguishes bundled commands,
skills and custom workflows. Examples may still be version-sensitive.

Contradictions: its blanket high-effort/model preference and instruction accumulation
advice should be read alongside newer pruning advice and task-specific evaluation.
Our template already implements verification, shared instructions and hooks; these
are not new gaps. Personal UI preferences belong in a local checklist if wanted,
not mandatory project settings. Code blocks/tables are imperfectly extracted.

### Felix Rieseberg — Made by mechanical means (2026-09-27)

Source: [Made by mechanical means](https://felixrieseberg.com/made-by-mechanical-means). Saved: [refs/articles/felixrieseberg.com/made-by-mechanical-means/article.md](../articles/felixrieseberg.com/made-by-mechanical-means/article.md).

First-person project account by a Claude Cowork engineer; affiliation is supported
by his [January post](https://x.com/felixrieseberg/status/2010851698550415826).
Medium relevance: the introduction explicitly says he did not use traditional
Claude Code for this project.

Locators: introduction; Not reading the code; Hill climbing performance. He
coordinates cloud threads through one project, reviews private previews, and has
QA threads write findings for a coordinator to assign. For performance work,
comparative screenshots help detect visual degradation alongside speed gains.
His thread counts and productivity are self-reported, without a controlled baseline.

Inference: borrow preview-driven acceptance and visual equivalence checks for a UI
project. Do not transplant a large cloud-session workflow into this repository or
interpret it as his `.claude/settings.json`.

## Saved background, not used to support the recommendations

- Source: [Building Claude Code with Boris Cherny](https://www.youtube.com/watch?v=julbw1JuAz0). Saved: [refs/videos/julbw1JuAz0/transcript.md](../videos/julbw1JuAz0/transcript.md).
  Long Boris Cherny interview (about 22,000 words); not fully reviewed in this pass.
- Source: [How AI is transforming work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic). Saved: [refs/articles/anthropic.com/research-how-ai-is-transforming-work-at-anthropic/article.md](../articles/anthropic.com/research-how-ai-is-transforming-work-at-anthropic/article.md).
  Anthropic employee study, metadata date 2025-12-02. Saved as context; no
  productivity statistics from it are relied on here.
- Source: [How employment is changing at Anthropic](https://www.anthropic.com/research/employment-at-anthropic). Saved: [refs/articles/anthropic.com/research-employment-at-anthropic/article.md](../articles/anthropic.com/research-employment-at-anthropic/article.md).
  Anthropic employment follow-up, metadata date 2026-10-16. Saved as context;
  not synthesized into configuration recommendations.

## Recommendation and limits

Pilot task-completion checks for internal Claude tasks and independently validate
review findings. Test those against our existing Stop check before adopting them.
Retain the already-documented model-upgrade review and modest parallelism.

Exact model names, feature availability and spoken command spellings are historical
source claims. Confirm the installed version before implementing a configuration.
No claims came from inaccessible video descriptions or third-party summaries.
The further Daisy video `shZgedW15vg` remains an unreviewed discovery lead.
