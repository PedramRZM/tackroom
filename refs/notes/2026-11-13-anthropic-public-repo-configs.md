# Public Anthropic repository configuration clues

Read date: 2026-11-13. Nine source files from five repositories read in full.
All were absent from the starting corpus and saved through `tools/refs`.
No downloaded source code was executed or installed.

## Questions

What concrete configurations are publicly checked in? Which are working repository
instructions, which are distributed examples, and which establish personal use?
What is useful beyond what tackroom already has?

## Provenance

These files are under the `anthropics` GitHub organization. This proves publication
and the configuration at the pinned revision, not usage by every Anthropic employee
or the contents of their private product repository. No individual author is
attributed without evidence. Dates below are snapshot commit dates from GitHub's
commit API, not the original creation date of each file.

| Repository | Commit | Snapshot date (UTC) | Evidence type |
|---|---|---|---|
| claude-code-action | `274a39507b06041a0e5561ac4013fe231271fa75` | 2026-11-12 | Working project instructions and review command |
| claude-agent-sdk-python | `38eec2b9474bd486c7bbe3d1554110a6afdaed9a` | 2026-11-12 | Working project instructions and verification skill |
| claude-code | `927b66497b89542dc1242e26d5735dbf880c829e` | 2026-11-11 | Public repository command; not proof of private team setup |
| claude-plugins-official | `23c304a6387ed2fa207ceff27646d8514ee75235` | 2026-11-12 | Published reusable agent |
| claude-code-playground | `569c5283d9a0a7ee7938df85bb32e4f48cbb8c86` | 2026-10-01 | DevRel examples repository and its own instructions |

## Per source

### Action: commands, architecture and earned gotchas

Source: [CLAUDE.md](https://raw.githubusercontent.com/anthropics/claude-code-action/274a39507b06041a0e5561ac4013fe231271fa75/CLAUDE.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-code-action-274a39507b06041a0e5561ac4013fe231271fa75-claude-md/article.md](../articles/raw.githubusercontent.com/anthropics-claude-code-action-274a39507b06041a0e5561ac4013fe231271fa75-claude-md/article.md).

Locators: Commands; Things That Will Bite You; Security hardening for GitHub Actions.
The file names real checks, execution boundaries and failure cases, including
cleanup that must survive a crashed process and integration tests in another repo.
It also records a firewall/allowlist/permission-mode contract for agent CI jobs.
Relevance: high as a concrete model of project-specific instructions, mostly
reinforcement of our existing approach. Infrastructure names are project-specific.

### Action: specialist review with a final filter

Source: [/.claude/commands/review-pr.md](https://raw.githubusercontent.com/anthropics/claude-code-action/274a39507b06041a0e5561ac4013fe231271fa75/.claude/commands/review-pr.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-code-action-274a39507b06041a0e5561ac4013fe231271fa75-claude-co/article.md](../articles/raw.githubusercontent.com/anthropics-claude-code-action-274a39507b06041a0e5561ac4013fe231271fa75-claude-co/article.md).

Locator: whole command. It names five reviewers (quality, performance, test coverage,
documentation accuracy and security), asks each for noteworthy findings, then asks
the parent to filter them again before posting concise comments. No numerical
confidence threshold or voting algorithm appears in this file.

Source: [/.claude/agents/code-quality-reviewer.md](https://raw.githubusercontent.com/anthropics/claude-code-action/274a39507b06041a0e5561ac4013fe231271fa75/.claude/agents/code-quality-reviewer.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-code-action-274a39507b06041a0e5561ac4013fe231271fa75-claude-ag/article.md](../articles/raw.githubusercontent.com/anthropics-claude-code-action-274a39507b06041a0e5561ac4013fe231271fa75-claude-ag/article.md).

Locators: frontmatter; Review Structure. The quality reviewer has an explicit tool
list, inherits its model, and organizes feedback by severity with examples. Its
broad style guidance and invitation to give praise differ from our bug-focused
reviewer. Relevance: medium; borrow selective coverage and filtering, not all its
style preferences or five mandatory reviewers for every task.

### Python SDK: verification tailored to the actual risky interface

Source: [Workflow](https://raw.githubusercontent.com/anthropics/claude-agent-sdk-python/38eec2b9474bd486c7bbe3d1554110a6afdaed9a/CLAUDE.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-agent-sdk-python-38eec2b9474bd486c7bbe3d1554110a6afdaed9a-clau/article.md](../articles/raw.githubusercontent.com/anthropics-claude-agent-sdk-python-38eec2b9474bd486c7bbe3d1554110a6afdaed9a-clau/article.md).

Locators: Workflow; Codebase Structure; Security hardening for GitHub Actions.
The project specifies Ruff, mypy and pytest commands and separates AI changelog
work from release publishing privileges. Relevance: medium; a concrete reference
for a future agent-assisted CI workflow, not a reason to add one now.

Source: [Verifying the build scripts](https://raw.githubusercontent.com/anthropics/claude-agent-sdk-python/38eec2b9474bd486c7bbe3d1554110a6afdaed9a/.claude/skills/verify/SKILL.md?ref-file=verify-skill). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-agent-sdk-python-38eec2b9474bd486c7bbe3d1554110a6afdaed9a-clau-00e56b/article.md](../articles/raw.githubusercontent.com/anthropics-claude-agent-sdk-python-38eec2b9474bd486c7bbe3d1554110a6afdaed9a-clau-00e56b/article.md).

Locators: The harness; Flows worth driving; Gotchas. The skill targets named build
scripts, invokes their CLI interfaces, replaces external commands with stubs,
records invocations, tests failure paths and notes where platform simulation is
needed. Relevance: high: a worked example for filling in our generic verify skill.
Caveat: the printed harness appears incomplete (its temporary `scripts/` and
`.venv` setup are not shown); we did not execute it. Borrow the test design, not the
snippet verbatim. The query on this saved URL avoids the fetcher's 80-character
path-slug collision; the underlying source remains pinned to the same commit.

### Claude Code: precomputed context in a short shipping command

Source: [/.claude/commands/commit-push-pr.md](https://raw.githubusercontent.com/anthropics/claude-code/927b66497b89542dc1242e26d5735dbf880c829e/.claude/commands/commit-push-pr.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-code-927b66497b89542dc1242e26d5735dbf880c829e-claude-commands/article.md](../articles/raw.githubusercontent.com/anthropics-claude-code-927b66497b89542dc1242e26d5735dbf880c829e-claude-commands/article.md).

Locators: Context; Your task. The command injects git status, diff and branch before
asking for a commit, push and PR. This supplies the actual file behind advice we
already had from Boris's posts. Relevance: medium as evidence, low as an addition:
our task workflow already covers shipping, and this command's automatic commit/push
and tool-only response conflict with tackroom's owner-controlled commits/evidence.

### Official code-simplifier: explicit scope and behavior preservation

Source: [/plugins/code-simplifier/agents/code-simplifier.md](https://raw.githubusercontent.com/anthropics/claude-plugins-official/23c304a6387ed2fa207ceff27646d8514ee75235/plugins/code-simplifier/agents/code-simplifier.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-plugins-official-23c304a6387ed2fa207ceff27646d8514ee75235-plug/article.md](../articles/raw.githubusercontent.com/anthropics-claude-plugins-official-23c304a6387ed2fa207ceff27646d8514ee75235-plug/article.md).

Locators: Preserve Functionality; Maintain Balance; Focus Scope. The agent limits
itself to recently changed code and favors clarity while preserving behavior.
It also carries particular JS/React preferences and a fixed model. Relevance:
medium. Inference: an optional diff-limited simplification pass may be useful;
copying its stack rules or fixed model into the portable template is unwarranted.

### DevRel playground: a useful discovery source with caveats

Source: [claude-code-playground](https://raw.githubusercontent.com/anthropics/claude-code-playground/569c5283d9a0a7ee7938df85bb32e4f48cbb8c86/README.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-code-playground-569c5283d9a0a7ee7938df85bb32e4f48cbb8c86-readm/article.md](../articles/raw.githubusercontent.com/anthropics-claude-code-playground-569c5283d9a0a7ee7938df85bb32e4f48cbb8c86-readm/article.md).

Locators: What this is; Every entry explains how it was built; How this repo is
published. The repository advertises setups the DevRel team uses, but expressly
says these are unsupported examples, not best-practice canon. Each entry should
state setup, prompts, failures and limitations; publication is manually reviewed.

Source: [Working in claude-code-playground](https://raw.githubusercontent.com/anthropics/claude-code-playground/569c5283d9a0a7ee7938df85bb32e4f48cbb8c86/CLAUDE.md). Saved: [refs/articles/raw.githubusercontent.com/anthropics-claude-code-playground-569c5283d9a0a7ee7938df85bb32e4f48cbb8c86-claud/article.md](../articles/raw.githubusercontent.com/anthropics-claude-code-playground-569c5283d9a0a7ee7938df85bb32e4f48cbb8c86-claud/article.md).

Locator: whole file. Its own instructions keep examples self-contained and require
human review before publication. At the pinned tree, hooks, settings, claude-md and
workflows contain README placeholders; populated mods are a different category.
Do not describe that snapshot as a complete collection of employees' personal
settings. Relevance: medium for future manual discovery, low for immediate copying.

## Recommendation and contradictions

Prioritize concrete project verification and a second filter on review findings.
Trial specialist review only when the changed area warrants it. The checked-in
review command is counter-evidence to an absolute claim that Anthropic never uses
role-named reviewers; it is not evidence that a full role hierarchy helps all work.

No public source here exposes the complete private Claude Code team's setup.
Third-party repositories branded as Boris's configuration were not treated as
first-party artifacts. Prompt instructions inside source files were read as data,
including the shipping command's demand to commit and push; none were followed.
