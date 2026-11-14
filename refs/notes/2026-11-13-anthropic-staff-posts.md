# Anthropic staff: additional setup posts

Research date: 2026-11-13. Seven new posts read in full. Public post text was saved
through `tools/refs post` (fxtwitter); linked images were not inspected. These are
self-reports, not measured comparisons of productivity.

## Questions

Which staff setup posts were absent from the existing corpus? Which show personal
use rather than announce features? Which details would change our template?

## Findings and sources

### Jarred Sumner — parallel bug fixing (2026-05-28)

Source: [Example prompt:](https://x.com/jarredsumner/status/2060050588574818763). Saved: [refs/posts/x/2060050588574818763/post.md](../posts/x/2060050588574818763/post.md).

Locator: the complete post, Steps 1–3. Split a bug report into separate files;
workers fix individual bugs and two reviewers challenge each fix. Workers and
reviewers avoid git/build commands on the shared branch. Only after they finish
are fixes integrated, built, tested and submitted. The parent post was already
saved; this concrete example was missing.

Affiliation: Anthropic's [migration article](https://claude.com/resources/articles/ai-code-migration)
names Sumner as Bun co-founder and Anthropic technical staff. That article is
already in the corpus.

Inference: add an explicit integration owner to parallel work. Worktrees remain
the safer default here; adopt the ownership rule without copying shared-branch
editing or automatically opening PRs. Relevance: high for parallel changes.

### Daisy Hollman — connected sessions and their cost (2026-08-07 to 2026-08-25)

Source: [Today we're releasing SendMessage tool for Claude Code, allowing it to message other Claude Code sessions dire](https://x.com/TheWholeDaisy/status/2085755692733079660). Saved: [refs/posts/x/2085755692733079660/post.md](../posts/x/2085755692733079660/post.md).

Locator: whole post. Hollman announces SendMessage and says the attached graph
shows her own connected sessions. This establishes personal use of cross-session
messaging, not the graph's unread details or a particular session count.

Source: [I 100% agree that my quote in the developer newsletter is indicative of the growing gap between unlimited toke](https://x.com/TheWholeDaisy/status/2092099546751082828). Saved: [refs/posts/x/2092099546751082828/post.md](../posts/x/2092099546751082828/post.md).

Locator: whole post. She explicitly distinguishes unlimited-token workflows from
economical token use. Relevance: high as a constraint on adopting staff workflows.

Source: [It's intersting (and slightly enjoyable?) to see the amount of doubt about my workflow on Reddit: https://www.](https://x.com/TheWholeDaisy/status/2092099544003871217). Saved: [refs/posts/x/2092099544003871217/post.md](../posts/x/2092099544003871217/post.md).

Locator: whole post. She defends her workflow's reality but supplies no benchmark.

Source: [@theo Hotter take: I don't want responses anymore. I just want evidence that the code works and a PR number.](https://x.com/TheWholeDaisy/status/2092093149095301438). Saved: [refs/posts/x/2092093149095301438/post.md](../posts/x/2092093149095301438/post.md).

Locator: whole reply. Her preferred output is evidence that code works and a PR
number. This reinforces our existing verification/reporting contract.

Affiliation: Anthropic's [May 6, 2026 session page](https://claude.com/code-with-claude/session/sf-beyond-the-basics-with-claude-code)
identifies her as a Member of Technical Staff. Saved posts identify her handle as
`@TheWholeDaisy`; some discovery mirrors use an older spelling.

Inference: try messaging only for dependent parallel work, measure its cost, and
keep the current small concurrency cap. Do not infer that many persistent agents
are necessary or economical. Relevance: medium.

### Felix Rieseberg — a different surface for coding (2026-01-12; 2026-09-27)

Source: [👋 Hi, I'm Felix and I work on Claude Cowork, bringing Claude Code closer to all kinds of knowledge work. It's ](https://x.com/felixrieseberg/status/2010851698550415826). Saved: [refs/posts/x/2010851698550415826/post.md](../posts/x/2010851698550415826/post.md).

Locator: whole post. First-person affiliation: he works on Claude Cowork.

Source: [Working on Claude, people often ask about my workflow.](https://x.com/felixrieseberg/status/2104304874062327970). Saved: [refs/posts/x/2104304874062327970/post.md](../posts/x/2104304874062327970/post.md).

Locator: whole post. His September account explicitly moves away from classic
Claude Code, local terminals and GitHub PRs. The linked blog is reviewed in
[the talks/articles note](2026-11-13-anthropic-staff-talks-articles.md).

This is relevant counter-evidence to the idea of one shared staff configuration;
it is not a Claude Code settings recipe. Relevance: medium.

## Recommendation and limits

Try explicit worker/reviewer/integrator ownership before increasing the number of
agents. Keep reporting evidence, which the template already requires. No new
always-loaded roles or messaging infrastructure is justified by these posts alone.

All seven IDs were absent from the initial metadata inventory. The search is not
an exhaustive account archive. Existing Boris, Thariq and Cat material is not
counted as new. A further Daisy talk, `shZgedW15vg`, was discovered but not fetched
or used as evidence. Third-party summaries were discovery leads only.
