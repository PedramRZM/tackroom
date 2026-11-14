# Anthropic staff Claude Code setups: additions and gaps

Research date: 2026-11-13. Scope: publicly shared personal/team workflows and public
repositories; recommendations for tackroom, not changes to the shipped setup.

## Questions

1. What do Anthropic staff say they actually use to configure and operate Claude Code?
2. Which primary sources are missing from the existing references, after checking equivalent
   URLs, reposts and already-saved threads?
3. What can public repository files establish, and what would be an inference about private
   Anthropic development practices?
4. Which useful practices are absent from `template/`, rather than merely absent from the
   research corpus? What is worth trying first, and how would we judge it?
5. Where do dates, missing transcripts, inaccessible posts or contradictory advice limit the
   conclusion?

## Baseline and method

The starting corpus contains 1,654 saved items: 785 posts, 419 articles, 355 docs and 95
videos (counted from `meta.json`, before this pass). Existing notes already cover Boris
Cherny's January and March 2026 setup threads, Thariq Shihipar, Cat Wu and many colleagues,
official guidance, and interviews. A familiar recommendation is not a new discovery.

Searches are split across staff posts, official articles/talks and public repository
artifacts. New saved sources go through `tools/refs`. Each finding distinguishes a direct
account of use, official advice/example code and our inference. Repository revisions are
pinned when available. Publication dates and retrieval dates are kept separate.

## Result

**23 new reference items saved:** seven X posts, three video transcripts, four
articles and nine commit-pinned repository files from five Anthropic repositories.
Twenty were read in full and synthesized; the long Boris interview and two employee
studies are retained as background, not used for recommendations. The new total is
1,677 items. These are new to this corpus, not necessarily newly published.

The strongest additions are Lydia Hallie's November 11 talk, Jarred Sumner's concrete
parallel-fix prompt, and the working review/verification files in Anthropic's Action
and Python SDK repositories. The official power-user guide is a useful consolidated
reference, but mostly reinforces practices we already have.

Detailed evidence, author/date caveats and saved-file locators:

- [Staff X posts](2026-11-13-anthropic-staff-posts.md).
- [Talks and articles](2026-11-13-anthropic-staff-talks-articles.md).
- [Public repository configurations](2026-11-13-anthropic-public-repo-configs.md).
- [Exact new-source URL manifest](../sources/anthropic-staff-setups-2026-11-13.txt).

## What their setups actually look like

There is no single staff configuration to copy. The evidence ranges from personal
self-report to checked-in project instructions and reusable examples.

| Person or team | Supported practice | Evidence and novelty |
|---|---|---|
| Boris Cherny / Claude Code team | Shared project instructions, recurring commands, formatting hook, verification, parallel checkouts/worktrees | Already saved January 2026 posts; not a new finding. The actual public `commit-push-pr.md` is a new artifact. |
| Lydia Hallie | Intermediate verification, task-completion checks, independent validation of review findings, fewer stale instructions | [November talk](https://www.youtube.com/watch?v=vlfCjWuv4es), especially 11:12–14:15. New source; some practices already covered. |
| Jarred Sumner | Parallel fixes/reviews; a later integration stage owns builds and git operations | [May 28 example](https://x.com/jarredsumner/status/2060050588574818763). Missing reply to an already-saved parent post. |
| Daisy Hollman | Sessions message each other; output emphasizes evidence; unlimited-token workflows have different economics | [August 7 personal-use post](https://x.com/TheWholeDaisy/status/2085755692733079660) and [August 25 cost caveat](https://x.com/TheWholeDaisy/status/2092099546751082828). New sources, not a costed recommendation. |
| Felix Rieseberg | Cloud project coordination and preview/QA feedback, explicitly outside traditional Claude Code | [September account](https://felixrieseberg.com/made-by-mechanical-means). New source; adjacent workflow, not a settings file. |
| Cal Rueb | Explore before editing, known CLIs, two concurrent sessions personally, written handoffs | [May 2025 talk](https://www.youtube.com/watch?v=gv0WHhKelSE). New source, mostly established practices. |
| Anthropic public projects | Project-specific checks/gotchas, five named review perspectives plus a parent filter, a focused CLI verification skill | Nine [pinned files](2026-11-13-anthropic-public-repo-configs.md). Strong evidence of checked-in configuration, not proof of every employee's private setup. |

### Already in the template

These should not be added again under new names:

| Practice | Existing implementation |
|---|---|
| Shared, short project instructions | `template/AGENTS.md`, imported by `template/CLAUDE.md` |
| Automatic formatting | `template/.claude/hooks/format.py` |
| Verification and output as evidence | `template/.claude/skills/verify/SKILL.md` |
| Fresh-context review and suppression of nits | `template/.claude/skills/second-opinion/SKILL.md`, `agents/reviewer.md` |
| Task acceptance criteria and handoff files | `template/WORKFLOW.md`, `template/tasks/TEMPLATE.md`, task/wrap-up skills |
| Memory curation rather than unlimited accumulation | The dream skill and `.agents/memory/` |
| Model-upgrade pruning and skill evals as a known gap | `docs/keeping-current.md` |
| Modest concurrency | `template/WORKFLOW.md`: at most three supervised sessions, one hard task |

These comparisons were made against `template/`, not personal skills on this machine.

## Recommendation

Keep the template small. Trial the following individually; the implementation and
success criteria below are **our judgement**, not claims that Anthropic uses this
exact design. Nothing in the shipped setup was changed by this research.

| Priority | Proposal and exact gap | Small trial and acceptance evidence | Trade-off |
|---|---|---|---|
| 1 | **A project-specific verification recipe.** Our verify skill has a deliberate placeholder; the Python SDK supplies a concrete example of driving real CLI boundaries with isolated stubs and failure cases. | Fill that section in one real project with startup/seed/reset steps and one repeatable critical-path check. A fresh session must reproduce success and a deliberate failure without inventing setup. For UI work, include a preview and state assertions. | Project work is required; another generic paragraph would not fill the gap. |
| 2 | **Explicit integration ownership for parallel work.** The workflow caps sessions but does not assign who owns shared builds, git state and final verification. | Add a short optional parallel-work recipe: independent scopes/worktrees, evidence from each worker, one integration owner, one final combined check. Demonstrate two simultaneous changes without overlapping writes or competing builds. | Some integration is serialized. This is local project coordination, not cross-project orchestration. |
| 3 | **An opt-in `TaskCompleted` check.** The template has a `Stop` check, not an internal-task completion gate. | On a scratch project, map a task to a deterministic check; prove failure leaves it incomplete and success permits completion. Test irrelevant tasks, missing check commands and repeated failures. Only then consider adding a hook. | Extra test runs and Claude-specific behavior. This does not enforce tracker issue closure or task-file status. |
| 4 | **Selective review perspectives plus finding validation.** We already have independent review; we lack an explicit optional second pass to validate candidate findings before reporting. | For a risky change, add only the relevant perspective (e.g. performance or security), then have the parent reproduce/deduplicate findings. Compare useful findings, false positives, time and cost against the current reviewer. | More model calls; do not install five mandatory reviewers or replace evidence with agent agreement. |
| 5 | **Optional simplification of the changed diff.** We have correctness/performance skills, but no dedicated clarity pass. | Try the available simplification capability on a messy diff; constrain it to touched code and re-run behavior checks. Keep it only if the result is easier to review without unrelated edits. | More churn; avoid copying the published agent's fixed model and JS/React style preferences into every project. |

The per-task idea needs one important distinction: `Stop` fires when Claude finishes
responding, not only when a whole project is complete. Our hook deliberately runs
quick checks and allows an eventual stop after a failed continuation. A task gate
adds a different checkpoint; it is not a replacement for full verification or CI.
The [official event reference](https://code.claude.com/docs/en/hooks#taskcompleted)
documents exit 2 as blocking internal task completion. Runtime-error behavior still
needs live testing; do not market a hook as an unbreakable guarantee.

**The largest existing validation gap remains skill evals.** `docs/keeping-current.md`
already says this. Use a few real tasks to compare each proposed addition with the
current setup; otherwise extra configuration is unmeasured overhead. Evidence of
equal results with less cost or fewer instructions would favor deleting the addition.

## What not to copy, and disagreements worth retaining

- Large session counts are not a target. Daisy explicitly notes the economics of
  unlimited tokens; Cal's personal limit was two. Keep our current cap until measured
  work justifies more.
- The public shipping command commits and pushes automatically. That conflicts with
  this repository's owner-controlled commits; use it as reference, not an installed workflow.
- The official power-user guide collects historical preferences. Its advice to keep
  adding corrections to `CLAUDE.md` must be balanced with Lydia's pruning advice and
  our curated-memory process. No new fixed model/effort default is recommended.
- The Action repository does use role-named specialist reviewers. This qualifies any
  blanket claim that such agents never occur in frontier teams. It does not establish
  that planner/architect/tester hierarchies improve ordinary work.
- The DevRel playground is worth checking manually, but its setup categories at the
  inspected revision mostly have placeholders. Its README is not proof that those
  personal configurations are already available.
- Shell sandboxing, permissions and external publishing boundaries are different.
  Public CI runner names/settings are project-specific, and our known local sandbox
  limitation has not been fixed or retested by this research.

## Coverage and validation limits

The 23 additions were compared with the initial 1,654 metadata records and relevant
existing notes. Exact X IDs, video IDs and repository-file identities were checked;
this is a focused search, not an exhaustive scrape of every staff account. Most
official guides and famous setup threads were already present.

X text came through the repository's public-post fetcher; images were not inspected.
Video evidence is caption-derived. Repository files are pinned to commits with dates
verified through GitHub; they were read, never executed. A query parameter was needed
for one raw URL because the current fetcher truncates long paths to colliding slugs.
The long Boris interview and two employee studies remain background-only; the Daisy
video `shZgedW15vg` remains a discovery lead, not evidence.

Only reference files, research documentation and a fetching lesson in the memory
inbox changed. No new hook, skill, settings
file, live model experiment, Codex harness test or vendor endpoint test was run. A
scratch Claude project is therefore not claimed as validation of these proposals.

## Validation output

`UV_CACHE_DIR=/tmp/tackroom-research-uv scripts/agent/check`:

```text
ok    compile (1s)
ok    config-parses (0s)
ok    guard-tests (8s)
ok    root-matches-template (0s)
ok    instruction-size (0s)
ok    skill-limits (0s)
ok    prompts-verbatim (0s)
ok    skills-validate (0s)
ok    agents-validate (0s)
all 9 checks passed
```

The source manifest has 23 unique URLs, all with saved metadata. All relative links
in the four new notes resolve. `tools/refs index` reports 1,677 items;
`git diff --check` passes.

`tools/refs watch` completed with six additional discoveries in the Claude articles
feed; the other configured lists reported zero new URLs and the changelog was
unchanged. The watch baseline was not marked. These are **unreviewed discovery
leads**, not additional evidence for the recommendations:

- https://claude.com/resources/articles/claude-for-manufacturing
- https://claude.com/resources/articles/claude-meetings
- https://claude.com/resources/articles/claude-tag-guide-for-startups
- https://claude.com/resources/articles/j-crew-style-advisor-with-claude
- https://claude.com/resources/articles/self-hosted-claude-managed-agents
- https://claude.com/resources/articles/using-claude-opus-5-5-as-your-daily-driver-for-knowledge-work
