# X posts: how the people who build and shape coding agents say they work with them

Sources read: 787 (784 X posts and X articles under `refs/posts/x/`: 783 saved for this assignment in
collection `x-posts` and one that was already there; plus 3 press pages saved under `refs/articles/`,
collection `x-posts-secondhand`, as secondhand evidence for Dario Amodei). All were read in full, including
the long X articles. Could not fetch: post `2038552880018538749` (@bcherny, linked from a GitHub README; the
public post API returned 404, probably deleted). No instructions aimed at the reader were found in any source.

Conventions used in this file

- `[2007179833990885678, 2026-01-02]` means the file [`refs/posts/x/2007179833990885678/post.md`](https://x.com/bcherny/status/2007179833990885678), posted on
  that date. Author and date were checked against each file's front matter. `[id]` alone repeats a post
  already dated nearby.
- Text in double quotes followed by a post reference is copied verbatim from that file. Anything else is
  paraphrase. "Inference:" marks my own reading. "Secondhand:" marks something I saw on a page that is not
  the person's own post.
- The posts run to 2026-11-10. Model names in them (Opus 4.5 to 5.5, Fable 5 to 5.2, Sonnet 5.5) are the
  authors' own; advice is tied to the model that was current on the post date, so dates matter.
- How the posts were found: index pages that link them (howborisusesclaudecode.com, threadreaderapp user
  pages, simonwillison.net tag pages, a GitHub best-practice README), then the same public, no-login post API
  that `tools/refs post` uses, through its search and thread endpoints. ID lists and the save log are in
  `refs/sources/batches/x-posts-*.txt|log`. No account, cookie or login was used.

Counts per person (posts saved): Boris Cherny 183; Thariq Shihipar 93; @ClaudeDevs 54; Ado Kukic 46;
Andrej Karpathy 40; Cat Wu 39; Alex Albert 32; Geoffrey Huntley 25; Peter Steinberger 22; @claudeai 21;
Addy Osmani 21; Noah Zweben 20; Simon Willison 18; Lydia Hallie 17; Mitchell Hashimoto 17; Ryan Lopopolo 13;
swyx 12; Steve Yegge 11; Guillermo Rauch 11; Sid Bidasaria 10; Adam Wolff 10; Delba de Oliveira 8;
Dario Amodei 7; Dickson Tsai 6; Alexander Embiricos 5; @AnthropicAI 5; Tibo Sottiaux 3; 35 context posts by
others (people being replied to or quoted). Claude Code team and official Anthropic accounts: 544.

## Cross-cutting findings

1. Verification is the one tip the Claude Code team calls most important, repeatedly and across model
   generations: give the agent a way to check its own work end to end (tests, a browser, a simulator, a way
   to start the server), and encode your manual checks as a skill. Boris [2007179861115511237, 2026-01-02],
   [2038454347156398333, 2026-03-30], [2044847858634064115, 2026-04-16], [2063792263067754658, 2026-06-08];
   Cat Wu [2044808538351100377, 2026-04-16]; Delba [2062203743387459836, 2026-06-03]; ClaudeDevs
   [2074208949205881033, 2026-07-06]; Karpathy [2015883857489522876, 2026-01-26]; Osmani
   [2111604705340326393, 2026-10-17]; Steinberger [2073214429655883814, 2026-07-04].
2. Review with a second, fresh context. The agent that wrote the code is a poor judge of it; a separate
   context window (subagent, `claude -p`, `/code-review`, managed Code Review) finds what the author missed.
   Boris [2015979257038831967, 2026-01-27], [2031151689219321886, 2026-03-09]; Sid [2060120459916750995,
   2026-05-28]; Thariq [2061907337154367865, 2026-06-02]; Delba [2062203743387459836]; Osmani
   [2066595308629594363, 2026-06-15]; Hashimoto [2089111740395270615, 2026-08-16]. Disputed late 2026, see
   Contradictions.
3. Keep project instructions short and made of earned, non-obvious rules; add a rule when the agent makes a
   mistake, prune regularly, split by directory, move detail into skills. Boris [2007179840848597422,
   2026-01-02], [2007212366094811401, 2026-01-02], [2007569961796153649, 2026-01-03], [2016339448863355206,
   2026-01-28]; Thariq [2080710971228918066, 2026-07-24]; Osmani [2026172457233829922, 2026-02-24],
   [2053231239721885918, 2026-05-09]; Lopopolo [2099585474218385614, 2026-09-14].
4. Remove permission prompts safely instead of approving by hand: first an allowlist in shared settings,
   then a sandbox, then (from March 2026) auto mode with a classifier. Boris [2007179854077407667,
   2026-01-02], [2021700506465579443, 2026-02-11], [2044847849662505288, 2026-04-16], [2058519809214607704,
   2026-05-24], [2085807103382519872, 2026-08-07]; Cat Wu [2044808535385772521, 2026-04-16]; Delba
   [2065106020347613598, 2026-06-11]; Lydia [2090134982161502394, 2026-08-19]. Counter-evidence that running
   with checks off bites: Yegge [1946360175339974807, 2025-07-19], Sottiaux [2077630111499882637,
   2026-07-16], [2107621483392446572, 2026-10-06].
5. Run work in parallel, isolated by git worktrees, and use a view that lists sessions. Boris
   [2007179833990885678, 2026-01-02], [2017742743125299476, 2026-01-31], [2025007394967957720, 2026-02-21],
   [2038454353787519164, 2026-03-30]; Cat Wu [2053999857799672111, 2026-05-12]; Osmani [1946676964804399125,
   2025-07-19]; Karel Doostrlnck (OpenAI) [2019477361557926281, 2026-02-05]. The limit is human review
   capacity, not the tool: Osmani [2059844244907696186, 2026-05-28], Thariq [2112219173288120531,
   2026-10-19].
6. Settle intent before code: plan mode, a spec written by having the agent interview you, then a new
   session to implement. Boris [2007179845336527000, 2026-01-02]; team [2017742745365057733, 2026-01-31];
   Thariq [2005315275026260309, 2025-12-28], [2073100352921215386, 2026-07-03]; ClaudeDevs
   [2064394924292997187, 2026-06-09]; Yegge [1946360175339974807]; Huntley [1914271213331058924, 2025-04-21].
   The ritual shrank with newer models, see Contradictions.
7. Turn anything repeated into a skill or slash command checked into git; put scripts and a gotchas section
   in the skill folder; write the description as a trigger. Boris [2007179847949500714, 2026-01-02],
   [2017742748984742078, 2026-01-31]; Thariq [2033949937936085378, 2026-03-17]; Alex Albert
   [1978877575767478633, 2025-10-16]; Lydia [2033603164398883042, 2026-03-16]. Dissent: Lopopolo
   [2094254379209732164, 2026-08-31].
8. Use hooks for what must always happen (formatting, blocking destructive commands, notifications, keep
   going at Stop) and prompts for what is a preference. Boris [2007179852047335529, 2026-01-02],
   [2021701059253874861, 2026-02-11], [2038454343519932844, 2026-03-30]; Alex Albert [1940480979141021781,
   2025-07-02]; Thariq [2033949937936085378]; Osmani [2119332146485891501, 2026-11-08].
9. Manage context deliberately: one task per session, rewind instead of correcting, compact proactively
   with a steer, send noisy work to subagents. Thariq [2044548257058328723, 2026-04-15],
   [2044653085415604473, 2026-04-16]; Huntley [1914271223489724588, 2025-04-21]; Sottiaux
   [2108778939057664357, 2026-10-10]; Lydia [2110484840256819380, 2026-10-14].
10. Automate recurring work with loops that have a stop condition: `/loop`, `/schedule` and routines,
    `/goal`, dynamic workflows. Boris [2030193932404150413, 2026-03-07], [2038454341884154269, 2026-03-30],
    [2088014489438621990, 2026-08-13]; Noah [2044093913376706655, 2026-04-14]; ClaudeDevs
    [2074208949205881033]; Steinberger [2063697162748260627, 2026-06-07]; Osmani [2064127981161959567,
    2026-06-08]; Karpathy [2030371219518931079, 2026-03-07]. Codex has the same primitive: [2049917871799636201,
    2026-04-30].
11. Each new model made earlier scaffolding a constraint: delete rules, examples, emphasis and repeated
    instructions, and re-test features that used to fail. Cat Wu [2035104388541473275, 2026-03-20]; Alex
    Albert [1993365987773890941, 2025-11-25]; ClaudeDevs [2064394926469840957, 2026-06-09]; Thariq
    [2080710971228918066]; Boris [2107565388250874193, 2026-10-06]; Lopopolo [2090990833675939875,
    2026-08-22].
12. Pick effort by how much verification and autonomy the task needs, and change model only when the model
    does not know enough. ClaudeDevs [2074900291062034618, 2026-07-08]; Thariq [2103576349499855160,
    2026-09-25]; Boris [2044847856872546639, 2026-04-16]. By autumn 2026 most of the people quoted here had
    medium as their default, see Contradictions.
13. Use the filesystem and plain CLIs as the agent's memory and tool surface; prefer a CLI plus one line in
    the agents file over loading many tool schemas. Thariq [1970243253061783669, 2025-09-22],
    [1982869394482139206, 2025-10-27]; Steinberger [1986968745504334300, 2025-11-08]; Karpathy
    [2026360908398862478, 2026-02-24], [2040572272944324650, 2026-04-04]; Rauch [2081103993917649134,
    2026-07-25]; Hashimoto [2046319366489407803, 2026-04-20].
14. Ask the agent to keep a running notes or progress file while it works, so decisions and deviations are
    visible and work can resume. Thariq [2056418157305454805, 2026-05-18]; Steinberger [1986799989775810955,
    2025-11-07]; Karel Doostrlnck [2019477361557926281]; Huntley [1914271208058864039, 2025-04-21]; team tip
    [2017742747067945390, 2026-01-31].
15. Keep changes small enough to review and keep a human accountable for what ships; how much you read
    scales with blast radius. Hashimoto [2066645959539556852, 2026-06-15], [2100249348345057389, 2026-09-16];
    Osmani [2066595308629594363], [2097027173941141799, 2026-09-07]; Boris [2098217573276131577, 2026-09-11];
    Willison [2029260505324412954, 2026-03-04].
16. A clean, well-structured codebase is itself agent configuration, because agents copy the patterns they
    find. ClaudeDevs [2074208949205881033]; Huntley [2111161924683456867, 2026-10-16]; Boris
    [2077460395279692197, 2026-07-15]; Lopopolo [2106110500719501413, 2026-10-02].

### (a) Boris Cherny's stated setup, item by item

He opens with "My setup might be surprisingly vanilla!" [2007179832300581177, 2026-01-02]. Later posts
changed several items; the newer state is noted on the same line.

1. Parallel local sessions: "I run 5 Claudes in parallel in my terminal", tabs numbered 1 to 5, system
   notifications when one needs input [2007179833990885678, 2026-01-02]. Uses separate git checkouts
   himself while most of the team uses worktrees [2017742743125299476, 2026-01-31]. By March: "I have
   dozens of Claudes running at all times" [2038454353787519164, 2026-03-30], started with `claude -w`.
2. Cloud and phone sessions: 5 to 10 more on claude.ai/code; hands local sessions to the web with `&`,
   uses `--teleport`, starts sessions from the iOS app each morning [2007179836704600237, 2026-01-02].
   Writes much of his code from the iOS app [2038454337811386436, 2026-03-30]; has "Enable Remote Control
   for all sessions" set in `/config` [2038454339933548804, 2026-03-30].
3. Model and effort: "I use Opus 4.5 with thinking for everything." [2007179838864666847, 2026-01-02];
   "Personally, I use High for everything." [2021699860869902424, 2026-02-11]; "I use xhigh effort for most
   tasks, and max effort for the hardest tasks." [2044847856872546639, 2026-04-16]; still xhigh on
   2026-09-01 [2094865488706973739]; Opus 5.5 was his daily driver in September [2102439069053747549,
   2026-09-22].
4. Shared CLAUDE.md: one file for the repo, checked into git, edited by the whole team several times a
   week; a mistake by Claude becomes a line in it [2007179840848597422, 2026-01-02]. Size and contents:
   "Our checked in http://CLAUDE.md is 2.5k tokens." [2007212366094811401, 2026-01-02], covering common bash
   commands, code style, UI and content guidelines, state management, logging, error handling, gating,
   debugging, and the PR template. Claude writes all of it [2006866138756796730, 2026-01-01]. On 2026-10-06,
   asked for his system instructions: "I don't use a custom CLAUDE.md" [2107591357170950471]. Inference:
   this is about a personal file; nothing he posted says the team's checked-in file was removed.
5. CLAUDE.md updates through code review: tags `@.claude` on coworkers' PRs to add a rule as part of the
   PR, using the GitHub action installed with `/install-github-action` [2007179842928947333, 2026-01-02].
6. Planning: most sessions start in plan mode (shift+tab twice); he iterates on the plan, then switches to
   auto-accept edits and Claude "can usually 1-shot it" [2007179845336527000, 2026-01-02]. By June he
   describes "why I use auto mode instead of plan mode" [2064034799711588805, 2026-06-08].
7. Slash commands and skills for the inner loop, in `.claude/commands/`, checked in; `/commit-push-pr`
   precomputes git status with inline bash [2007179847949500714, 2026-01-02]. Later a `/go` skill that
   tests end to end, runs `/simplify` and opens a PR [2044847858634064115, 2026-04-16]; `/simplify` and
   `/batch` used daily [2027534984534544489, 2026-02-28].
8. Subagents: `code-simplifier` after Claude finishes and `verify-app` with detailed end-to-end test
   instructions [2007179850139000872, 2026-01-02].
9. Formatting hook: a PostToolUse hook formats Claude's code to avoid CI formatting failures
   [2007179852047335529, 2026-01-02].
10. Permissions: "I don't use --dangerously-skip-permissions." He pre-allows safe bash commands with
    `/permissions`, mostly checked into `.claude/settings.json` [2007179854077407667, 2026-01-02]. From
    spring: "These days my #1 tip is: use auto mode" [2058519809214607704, 2026-05-24] and "The team and I
    use Auto mode exclusively, and have been for many months." [2085807103382519872, 2026-08-07].
11. Tools: Slack through an MCP server configured in a checked-in `.mcp.json`, BigQuery through the `bq`
    CLI, Sentry for error logs [2007179856266789204, 2026-01-02].
12. Long-running work: asks Claude to verify with a background agent, or uses an agent Stop hook, or the
    ralph-wiggum plugin; runs with `--permission-mode=dontAsk`, or skip-permissions only inside a sandbox
    [2007179858435281082, 2026-01-02]. From March he runs loops: `/loop 5m /babysit`, `/loop 30m
    /slack-feedback`, `/loop /post-merge-sweeper`, `/loop 1h /pr-pruner` [2038454341884154269, 2026-03-30],
    plus a loop that removes stale worktrees [2087024157196489117, 2026-08-11].
13. Verification: Claude tests every change he lands to claude.ai/code with the Chrome extension
    [2007179861115511237, 2026-01-02]; he uses the extension for all web work [2038454347156398333,
    2026-03-30].
14. Review: `claude -p` reviews every PR in a fresh context [2015979257038831967, 2026-01-27]; later Claude
    Code Review runs on all his PRs [2111158313463525518, 2026-10-16]. He reads diffs selectively: "I read
    diffs when it's touching critical code, or code that's important to get right." [2098210496109572123,
    2026-09-11].
15. Input and environment: "I do most of my coding by speaking to Claude, rather than typing."
    [2038454362226467112, 2026-03-30]; no IDE since Opus 4.5 [2064431111154053187, 2026-06-09]; `/btw` for
    side questions [2038454351849787485], `--add-dir` across repos [2038454359047156203], focus mode
    [2044847855006024147, 2026-04-16].
16. Since September 2026: Projects. "I stopped managing sessions." [2100669598995816511, 2026-09-17]. Claude
    Tag writes more than half his PRs [2103538666597691552, 2026-09-25].
17. Prompting: plain, short, coworker-style; say what to do, how much effort to spend, and how to verify
    [2107565388250874193, 2026-10-06]. A real prompt sequence is in [2042352725481177315, 2026-04-09].

### (b) The Claude Code team's recurring advice, ranked

Ranking method: a keyword count over the 551 saved posts by team members and official accounts (quoted text
excluded; Osmani counted only from 2026-09-08, the day he says he joined [2097210828659564642]). The count
is of posts that mention the topic, so product announcements inflate the feature-named rows. It is a crude
measure; the second column is my reading of how strongly it is advised.

| Rank | Topic | Posts, authors | How it is framed |
|---|---|---|---|
| 1 | Subagents, fresh context, automated code review | 67, 12 | Advice: separate context windows for review and for noisy work |
| 2 | Skills and slash commands | 60, 12 | Advice: turn repeated work into skills; much of the count is launches |
| 3 | Loops, schedules, routines, goals | 47, 10 | Advice from March 2026 on; before that, Stop hooks |
| 4 | Verification and feedback loops | 40, 8 | The only topic repeatedly called the most important tip |
| 5 | Effort level and model choice | 37, 11 | Personal defaults differ by person and date |
| 5 | Plan mode, specs, interviews | 37, 6 | Strong advice early 2026, softened later |
| 7 | Hooks | 36, 8 | Advice: determinism, guardrails, notifications |
| 8 | Parallel sessions and worktrees | 34, 9 | Called the team's top tip on 2026-01-31 |
| 9 | CLAUDE.md and AGENTS.md | 31, 7 | Advice: shared, short, updated after mistakes |
| 10 | Auto mode, allowlists, permission prompts | 30, 9 | Boris's top tip from 2026-05-24 [2058519809214607704] |
| 11 | Compaction, rewind, session hygiene | 21, 7 | Mostly Thariq |
| 12 | HTML artifacts and playgrounds | 18, 5 | Mostly Thariq, then Boris and Delba |
| 13 | Voice input | 8, 2 | Boris and Thariq |
| 14 | Simplify prompts, remove scaffolding | 7, 4 | Few posts by keyword, but the theme of mid-2026 (finding 11) |

### (c) Disagreement and change over time (dated)

- Permission prompts. 2026-01-02: no skip-permissions, hand-built allowlist [2007179854077407667].
  2026-03-24: auto mode ships with the caveat "We recommend using it in isolated environments."
  [2036503583667933400]. 2026-05-24: Boris's top tip [2058519809214607704]. 2026-08-14: default for Pro, Max
  and Team; the announcement quoted in Boris's post says "it caught 89% of dangerous commands. Manual
  approval caught 14%." [2085807103382519872, 2026-08-07]. Cat Wu's farewell sums up the shift: at launch
  people approved every prompt by hand, now the default is to trust the classifier [2117731934340337676,
  2026-11-03].
- Plan mode. 2025-12-27: "Almost always use Plan mode" [2004711722926616680]. 2026-01-31: start every
  complex task in plan mode [2017742745365057733]. 2026-06-08: Boris on auto mode instead of plan mode
  [2064034799711588805]. 2026-09-23: Thariq, "I don’t think the models need plan mode anymore"
  [2102813194196758746]; the next day, after feedback, plan mode stays as a built-in mod
  [2103212051065921632]. Osmani still lists "Plan before it builds" on 2026-11-08 [2119332146485891501]
  while saying on 2026-09-12 that a long planning ritual is not needed on the latest models
  [2098662421644853433].
- Instruction files. January 2026: add a line for every mistake; "Invest in your http://CLAUDE.md"
  [2017742747067945390, 2026-01-31]. 2026-06-09: prompts and skills written for older models are "often too
  prescriptive for Fable" [2064394926469840957]. 2026-07-08: `/checkup` dedups and splits the root file
  [2074997570317779038]. 2026-07-24: the team cut most of its own system prompt and advises a lightweight
  file that spends "most of the tokens on gotchas inside of the codebase" [2080710971228918066].
  2026-08-08: if the model rabbit-holes, test with `claude --safe-mode`; if that fixes it, the cause is
  your CLAUDE.md or skills [2085954130435248621]. 2026-09-18: Claude Code reads AGENTS.md when a folder has
  no CLAUDE.md [2101009392611278961].
- Memory. 2026-01-01: Boris says one file is enough and automatic memory is not supported
  [2006866138756796730], [2006877177040781767]; the `#` shortcut for writing to CLAUDE.md had just been
  removed [2006802351378805121]. 2026-07-24: the article lists "Then: Memory in CLAUDE.md files" and
  "Now: Auto-memory" [2080710971228918066].
- Effort defaults moved down as models improved. Boris: thinking on for everything (Jan), High (Feb), xhigh
  (Apr to Sep). Opus 4.7 defaulted to xhigh [2044808539663978970, 2026-04-16]; Opus 4.8 to high
  [2060048875918930045, 2026-05-28]; Opus 5.5 to medium [2102438806465245246, 2026-09-22]. Medium as a
  personal default: Lydia [2096024729496994303, 2026-09-04], Ado [2109671905733341559, 2026-10-12], Adam
  Wolff [2115614417689944066, 2026-10-29], Karpathy [2116957135661945283, 2026-11-01]. Boris is the outlier:
  "I use xhigh, but many people actually prefer medium" [2094865488706973739, 2026-09-01].
- Thinking keywords. December 2025: `think`, `think hard`, `ultrathink` set thinking budgets, with a note
  that only ultrathink still worked [2006802366750929004, 2026-01-01]. April 2026: adaptive thinking and an
  effort setting replace budgets [2044847856872546639]. 2026-10-29: ultrathink is back in the CLI as a
  per-turn boost [2115614417689944066]. Osmani lists "think harder" and ALL CAPS rules as habits to stop
  [2119332146485891501, 2026-11-08].
- Aggressive wording. Already on 2025-11-25 the Opus 4.5 guidance was to dial back "CRITICAL: You MUST use
  this tool" because it now over-triggers [1993365987773890941].
- Tool examples. 2025-11-24: a "Tool Use Examples" API feature to improve tool accuracy
  [1993038680177754574]. 2026-07-24: "giving examples actually constrains them" [2080710971228918066].
- Built-in tools shrink. TodoWrite and its reminders were replaced by Tasks [2014480496013803643,
  2026-01-22]; the dedicated Grep and Glob tools gave way to Bash in 2.1.117 [2047105823890166170,
  2026-04-23]. The February article still describes giving Claude a Grep tool [2027463795355095314,
  2026-02-27].
- Adversarial review. Promoted by the team from March to August 2026 [2031089411820228645],
  [2060120459916750995], [2087284684103537011, 2026-08-11]. 2026-08-26, Lopopolo: "You don’t want
  adversarial code review. You want collaborative code review." [2092498261307511034]. 2026-11-03, Thariq
  (after leaving Anthropic) endorses a post calling adversarial reviews mostly a waste of tokens next to
  empirical and formal verification [2117670540148347273]. Thariq's own workflow article had already warned
  that "most traditional coding tasks do not need a panel of 5 reviewers" [2061907337154367865, 2026-06-02].
  Osmani's cited four-reviewer experiment found 93.4% of flagged locations were caught by only one tool
  [2066595308629594363].
- Skills. Anthropic: hundreds in use internally [2033949937936085378, 2026-03-17]. Lopopolo: "Zero skills
  in my repos." [2094254379209732164, 2026-08-31], and after deleting hundreds of skills in favour of a few
  skills plus docs his team saw lower token use and higher eval scores [2099585474218385614, 2026-09-14].
  Adam Wolff: most of what bespoke tools, custom agents and elaborate skills do can be done with a prompt
  [2006035614806802820, 2025-12-30]. Thariq's later line is close to Lopopolo's: "thin skills"
  [2077539537992229076, 2026-07-15].
- How many agents. Boris runs dozens; Yegge reports 20+ concurrent [2077475727327604932, 2026-07-15].
  Osmani: "The right number of parallel agents is how many you can actually code review properly."
  [2059844244907696186, 2026-05-28]. Thariq: "most people multi-tasking with agents could benefit from
  slowing down" [2112219173288120531, 2026-10-19] and a warning about agent "mania" [2115937378674372783,
  2026-10-29]. Karpathy went from one instance being hard enough [1959703967694545296, 2025-08-24] to
  managing parallel agents [2026731645169185220, 2026-02-25].
- Reading the code. Karpathy: "I would watch them like a hawk" [2015883857489522876, 2026-01-26], then
  with Fable 5 "it's never felt this tempting to stop looking at the code at all (but don't do this in
  prod!)" [2064409694761054332, 2026-06-09]. Delba: "You don't need to read code anymore." read
  architecture changes first [2073467304491233543, 2026-07-04]. Boris reads diffs for critical code only
  [2098210496109572123]. Hashimoto's bar is being able to explain and defend any customer-facing system
  [2100249348345057389]. Adam Wolff predicted in 2025 that soon nobody would check generated code
  [1993036664428806145].
- Headless loops. Boris used the ralph-wiggum plugin in January [2007179858435281082]; Karpathy: "I really
  dislike the -p + ralph loop pattern of running agents" [2031083551387701698, 2026-03-09], preferring
  interactive sessions in tmux; Huntley wants deterministic workflow engines mixed in rather than relying
  on the agent loop alone [2092975233556996212, 2026-08-27].
- Worktrees. The team's top tip in January; swyx: "worktrees must die", citing 20GB of repeated
  node_modules [2086962980235939920, 2026-08-10]; Boris agrees they pile up [2087024157196489117].
- Model switching mid-session. February 2026: do not switch models mid-session because the cache is per
  model [2024574133011673516]; September 2026: switching effort mid-session on Opus 5.5 keeps the cache
  [2102513987699212344].
- Is it working at the labs? Hashimoto: the labs' own products are "buggy, resource hungry messes"
  [2025350212014014564, 2026-02-21]; a user post saved for context calls the release pace performative
  [2041472013215076519, 2026-04-07]; Boris's reply lists the bottlenecks they hit (review, CI, merge queues)
  and admits the source leak was human error [2041592252661919939, 2026-04-07].
- People moved. Osmani wrote for Google in April [2043812343508021460] and joined Anthropic on 2026-09-08
  [2097210828659564642]. Thariq left Anthropic on 2026-10-24 [2113844051938054167]. Cat Wu's last day was
  the Friday before 2026-11-03 [2117731934340337676] and she joined OpenAI [2118137612577968402,
  2026-11-05]. Read their later posts with that in mind.

### (d) Leaders' claims and predictions, kept apart from practitioner tips

These are statements about where things are or are going. They are not practices and several are disputed.

- Dario Amodei. None of his 7 saved posts is about coding practice; they announce essays and policy
  positions [2015833046327402527, 2026-01-26], [2098773920774074715, 2026-09-12], and one usage figure:
  Claude Code use in India "up 5× since June" [1977010693460443151, 2025-10-11]. He says "I don't usually
  spend much time on social media" [2088758816376807762, 2026-08-15]. Secondhand, from saved press pages:
  at Davos in January 2026 he said models could do "most, maybe all" of what software engineers do within
  six to twelve months, and "I have engineers within Anthropic who say I don’t write any code anymore"
  ([`refs/articles/entrepreneur.com/business-news-ai-ceo-says-software-engineers-could-be-replaced-in-months-502087/article.md`](https://www.entrepreneur.com/business-news/ai-ceo-says-software-engineers-could-be-replaced-in-months/502087),
  2026-01-21). In March 2025 he predicted AI writing 90% of code in three to six months and essentially all
  in twelve; John Gruber's one-year check calls that not exactly right but mainly "too facile"
  ([`refs/articles/daringfireball.net/linked-2026-03-13-amodei-ai-code-claim-chowder/article.md`](https://daringfireball.net/linked/2026/03/13/amodei-ai-code-claim-chowder),
  2026-03-13). Fortune reports an Anthropic spokesperson putting the company-wide share at 70% to 90% while
  Boris claimed 100% for himself
  ([`refs/articles/fortune.com/2026-01-29-100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-c/article.md`](https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/),
  2026-01-29).
- Boris Cherny. "Pretty much 100% of our code is written by Claude Code + Opus 4.5." and a forecast that
  most of the industry would see similar numbers within months [2015979257038831967, 2026-01-27]; 259 PRs
  in 30 days, all written by Claude [2004887829252317325, 2025-12-27]; code output per Anthropic engineer
  up 200% in a year [2031089411820228645, 2026-03-09]; a three-stage timeline in which coding is solved for
  his kind of work but engineering is not [2091589188298891264, 2026-08-23], a framing others mocked
  [2091434155561107647, 2026-08-23]; prompt injection "largely solved" in practice with layered defences
  [2086520950259118464, 2026-08-09].
- Anthropic accounts (company-reported numbers, unverified here). Over 80% of merged code written by
  Claude and 8x code per engineer versus 2024 [2062580571214389510, 2026-06-04]; Claude writes about 90% of
  Claude Code and merged PRs doubled from June to September while the reverted share fell by more than 40%
  [2111168901723906176, 2026-10-16]; merged changes went from about 2,500 to more than 30,000 per day
  between May and September [2110047081414987957, 2026-10-13]; tests grew 10x and CI jobs 25x in six months
  [2099577600159158765, 2026-09-14]; Code Review raised PRs with substantive comments from 16% to 54%, at
  $15 to $25 per review [2031088173510701125], [2031088175456903667, 2026-03-09].
- Adam Wolff. "software engineering is done" possibly by the first half of 2026, and generated code will
  go unchecked like compiler output [1993036664428806145, 2025-11-24]; softened a month later to coding,
  with engineering given at least 18 more months [2006403495738622040 was seen in a search listing only and
  is not saved; Secondhand].
- Andrej Karpathy. A threshold was crossed in December 2025: "coding agents basically didn’t work before
  December and basically work since" [2026731645169185220, 2026-02-25]; 2026 as a year of slop
  [2015883857489522876]; a widening gap between heavy professional users and everyone else
  [2109361546505966046, 2026-10-11]. Earlier he was far more cautious [1979644538185752935, 2025-10-18].
- Thariq Shihipar. The smartest models "won't need to verify their work or check it for bugs, they will
  just be right" [2117670540148347273, 2026-11-03]. This contradicts the team's standing advice and is a
  forecast, not a present-day practice.
- Guillermo Rauch. Projects will become "agentic software factories" with an issue to agent to PR to
  release loop [2083208578526314513, 2026-07-31]; markdown as the next programming language
  [2068165988005380478, 2026-06-20].
- Steve Yegge and Geoffrey Huntley. Adoption is far behind what insiders assume, with roughly 20% power
  users, 20% refusers and 60% on chat-style tools [2043747998740689171, 2026-04-13] (disputed for Google by
  Osmani [2043812343508021460]); per-seat SaaS and ticket-driven jobs are at risk [2070378458148970731,
  2026-06-26]; software factories are real but not yet cracked [2082525589416923314, 2026-07-29].
- Counterweights from practitioners. Hashimoto on "AI psychosis" and automating into "a very resilient
  catastrophe machine" [2055380239711457578, 2026-05-15]; Willison: agents "make software engineering even
  harder" [2103288927805476900, 2026-09-25]; Osmani's cited data on churn, defects and unreviewed merges
  [2066595308629594363].

### Contradictions and open questions

- Does more review by agents help or just cost tokens? The team says fresh-context review catches real bugs;
  Thariq (November 2026) and the post he quotes say verification by running things beats review in the
  abstract. Nobody in these posts publishes a controlled comparison on the same codebase.
- How much instruction is right? Investing in CLAUDE.md and deleting it to add lines back one at a
  time are both Boris's advice, within the same month (January 2026) [2017742747067945390],
  [2007569961796153649]. The later guidance (gotchas only,
  progressive disclosure, `/checkup`, `/doctor`) resolves it toward small files, but Karpathy reports that
  agents ignore style rules in his instruction files anyway [2035173492447224237, 2026-03-21].
- Context window size. Anthropic: context rot shows around 300 to 400k tokens on a 1M model and a 400k
  auto-compact setting is a good compromise [2044548257058328723], [2044653085415604473]. OpenAI's Codex
  lead: 300k was chosen as the default because the numbers were better [2108778939057664357]. A user estimates
  a 400k auto-compact setting would have saved 29% of weekly usage [2108277836285161798, 2026-10-08]. These agree with each other more than
  with the marketing of 1M windows.
- Plan mode's future is unsettled inside the team itself (see (c)).
- Effort: Boris stays on xhigh while colleagues default to medium; Thariq's tests suggest low or medium for
  implementing and high for verifying [2103576349499855160]. There is no single recommended setting.
- Open: nothing here says how a solo developer should size automated review. Osmani's answer is to scale
  layers by blast radius [2066595308629594363]; Boris's is guardrails plus a higher bar for production code
  [2098217573276131577].

## Per person

### Boris Cherny (@bcherny, creator of Claude Code, Anthropic; 183 posts, 2025-12-24 to 2026-10-22)

Files: `refs/posts/x/<id>/post.md` for the IDs below. Main threads: setup [2007179832300581177] (15 posts),
team tips [2017742741636321619] (11), customisation [2021699851499798911] (13), worktrees
[2025007393290272904] (7), hidden features [2038454336355999749] (16), Opus 4.7 tips [2044847848035156457]
(8), adoption steps [2077929379661844559] (5).

Thesis: The default product needs little customisation; results come from parallel sessions, a short shared
instruction file, and above all a way for Claude to verify its own work. As models improved he moved from
plan-then-approve to auto mode, loops and background routines, and argues that domain knowledge should be
encoded as checked-in infrastructure so anyone, or any agent, can contribute.

Practices
- Setup: see (a) above.
- Verification first. "give Claude a way to verify its work" and "it will 2-3x the quality of the final
  result" [2007179861115511237, 2026-01-02]. By domain: backend, make sure Claude can start the service;
  frontend, the Chrome extension; desktop, computer use [2044847858634064115, 2026-04-16]; mobile, an iOS or
  Android simulator MCP [2063792263067754658, 2026-06-08].
- Answer to how he trusts hundreds of PRs: plan mode, a way to verify output, and "Hold the same bar for
  human and Claude code." with `/code-review` [2004711722926616680, 2025-12-27].
- CLAUDE.md pruning: "add it back an instruction at a time as you see Claude making mistakes", repeated
  every few months [2007569961796153649, 2026-01-03]. Ancestor files load at startup; files in
  subdirectories load lazily when Claude touches that folder [2016339448863355206, 2026-01-28]. A separate
  memory file can be pulled in with an @-mention [2006874946904154562, 2026-01-01]. One-line fixes are
  appended to the file, for example to stop over-commenting [2080731329990377755, 2026-07-24].
- Team tips he relays (2026-01-31): 3 to 5 worktrees with shell aliases (`za`, `zb`, `zc`) and a dedicated
  analysis worktree [2017742743125299476]; a second Claude reviews the plan "as a staff engineer", and
  re-plan the moment something goes sideways [2017742745365057733]; end corrections by asking Claude to
  update CLAUDE.md, and keep a notes directory per task [2017742747067945390]; a `/techdebt` command at the
  end of each session and anything done more than once a day becomes a skill [2017742748984742078]; paste a
  Slack bug thread and say "fix", or "Go fix the failing CI tests." without micromanaging
  [2017742750473720121]; prompts such as "Grill me on these changes and don't make a PR until I pass your
  test." and "Knowing everything you know now, scrap this and implement the elegant solution"
  [2017742752566632544]; append "use subagents" to spend more compute and keep the main context clean, and
  route permission requests to a model through a hook [2017742755737555434]; Explanatory or Learning output
  style for unfamiliar code [2017742759218794768].
- Configuration worth checking into the repo: `settings.json` with permissions (wildcards such as
  `Bash(bun run *)`, `Edit(/docs/**)`) [2021700332292911228], plugin marketplaces [2021699862522364149],
  custom agents as `.md` files in `.claude/agents` with tools, permission mode and model
  [2021700144039903699], the `agent` setting or `--agent` flag to change the main agent
  [2038454360418787764], `/sandbox` [2021700506465579443], `/statusline` showing context use and branch
  [2021700784019452195], hooks [2021701059253874861] (all 2026-02-11).
- Hooks he names: SessionStart to load context, PreToolUse to log bash commands, PermissionRequest to route
  approvals, Stop to keep going [2038454343519932844, 2026-03-30]; agent frontmatter can carry hooks
  [2005013956818337846, 2025-12-27].
- Worktrees: `claude --worktree` (optionally `--tmux`), worktree isolation for subagents, `isolation:
  worktree` in agent frontmatter, worktree hooks for non-git VCS [2025007394967957720],
  [2025007398537380028], [2025007400235987300], [2025007401766948935] (2026-02-21).
- Long autonomous runs, five tips: auto mode, dynamic workflows, `/goal` or `/loop`, cloud sessions,
  end-to-end self-verification [2063792263067754658, 2026-06-08]. Dynamic workflows are token-heavy: keep
  them for migrations, refactors, performance work and batch bug fixes [2060048877944778995, 2026-05-28].
- Opus 4.7 habits: `/fewer-permission-prompts` to build an allowlist from history [2044847851591856461],
  recaps [2044847853030580247], `/focus` [2044847855006024147], `/effort` [2044847856872546639].
- Maintenance by routine: daily Claude Tag routines in a Slack channel (crash fuzzer, duplicate unifier,
  dead-code remover, abstraction police) opened 388 PRs in a few weeks, 180 merged after Code Review plus
  human review; routines are tuned when a PR is wrong [2088014489438621990, 2026-08-13].
- Encode knowledge as infrastructure: lint rules, CI steps and routines instead of fixing a class of issue
  by hand each time; every team should write the CLAUDE.md, REVIEW.md, skills and docs that let an agent
  work with no extra context; "automate, and encode domain knowledge as infrastructure"
  [2077460395279692197, 2026-07-15].
- Quality bar: "Production code written by Claude should have a higher bar than if it was written by a
  human." Guardrails listed: lint rules, tests, Claude-driven end-to-end tests, daily fuzzers, automated
  code and security review, automated refactoring. If output is below the bar: latest model, higher effort,
  better CLAUDE.md and skills, then pay down debt [2098217573276131577, 2026-09-11]. Throwaway code can be a
  black box; their terminal renderer is treated as one, guarded by property-based tests and benchmarks
  [2098210282464247871, 2026-09-11].
- Bug finding: adversarial review via a dynamic workflow or `/code-review` at a chosen level
  [2087284684103537011, 2026-08-11]; formal modelling with Lean and TLA+ produced 16 bug-fix PRs on the
  Agent SDK [2102543349102338309, 2026-09-22].
- `/checkup`: removes unused skills, MCPs and plugins, dedups local against checked-in CLAUDE.md, splits
  the root file into nested files plus skills, turns off slow hooks, enables auto mode, pre-approves
  frequently denied read-only commands [2074997570317779038, 2026-07-08].
- SDK and scripts: `--bare` skips loading local CLAUDE.md, settings and MCPs for `claude -p`
  [2038454357088457168, 2026-03-30].
- Why multiple context windows work: "multiple uncorrelated context windows tends to be a good approach"
  [2031151689219321886, 2026-03-09]. Nested subagents, depth capped at 5 [2064327225504403752, 2026-06-09];
  subagents run in the background by default [2071647677591466098, 2026-06-29].

Evidence and numbers: 259 PRs, 497 commits in 30 days [2004887829252317325]; 22 and 27 PRs on two days
[2015979257038831967]; a Rust-to-TypeScript port of the file indexer made @-mentions 3x faster at P99
[2042352726613639570, 2026-04-09]; Opus 5.5 ported HAProxy from C to Rust in 9.5 hours versus 12 for Fable
5.1 at 51% less cost [2102439069053747549]; auto mode figures in (c).

Tools and files named: `CLAUDE.md`, `REVIEW.md`, `.claude/commands/`, `.claude/agents`,
`.claude/settings.json`, `.mcp.json`, `/permissions`, `/sandbox`, `/statusline`, `/loop`, `/schedule`,
`/goal`, `/batch`, `/simplify`, `/btw`, `/branch`, `/teleport`, `/remote-control`, `/voice`, `/focus`,
`/effort`, `/checkup`, `/code-review`, `/fewer-permission-prompts`, `--worktree`, `--bare`, `--add-dir`,
`--agent`, `--safe-mode`, `claude agents`, ralph-wiggum plugin, Claude in Chrome, Ghostty, iTerm2, tmux.

Caveats: He says repeatedly there is no one right setup and his differs from the team's. He acknowledges
the model over-complicates, leaves dead code and avoids refactoring [2015979257038831967], that worktrees
pile up, and that Opus 5 was verbose (workaround: `outputStyle=concise`) [2091591570982371454, 2026-08-23].
Several numbers are his own or the company's. He works on a codebase with heavy internal automation that a
solo developer does not have.

Relevance: high. The most concrete, dated, first-hand description of a working setup, and it shows which
parts were dropped as models changed.

### Thariq Shihipar (@trq212, Claude Code team until 2026-10-24; 93 posts, 2025-07-14 to 2026-11-03)

Main long articles: prompt caching [2024574133011673516, 2026-02-19]; Seeing like an Agent
[2027463795355095314, 2026-02-27]; How We Use Skills [2033949937936085378, 2026-03-17]; Session Management
and 1M Context [2044548257058328723, 2026-04-15]; The Unreasonable Effectiveness of HTML
[2052809885763747935, 2026-05-08]; dynamic workflows [2061907337154367865, 2026-06-02]; Finding Your
Unknowns [2073100352921215386, 2026-07-03]; new rules of context engineering [2080710971228918066,
2026-07-24]; Spending your effort [2103576349499855160, 2026-09-25].

Thesis: Design for what the current model can do, and keep revisiting it. Context is the scarce resource:
load detail progressively, manage sessions deliberately, and give the model files, bash and references
instead of rules. His own working style is spec by interview, rich artifacts, low effort to build and high
effort to verify.

Practices
- Spec workflow: start from a minimal spec, have Claude interview you with the AskUserQuestion tool, "then
  make a new session to execute the spec" [2005315275026260309, 2025-12-28]. While implementing, keep a
  running `implementation-notes` file with design decisions, deviations, tradeoffs and open questions
  [2056418157305454805, 2026-05-18].
- Finding unknowns before, during and after: ask for a "blindspot pass"; prototype in a single HTML file
  with fake data; "Interview me one question at a time"; point at reference source code rather than
  describing; ask for a plan that leads with the decisions you are likely to change; after the work, have
  Claude quiz you, "I only merge after I pass the quiz perfectly." [2073100352921215386, 2026-07-03].
- Session management: "when you start a new task, you should also start a new session"; rewind (Esc Esc)
  to before the failed attempt and re-prompt with what you learned instead of piling on corrections;
  `/compact` with a focus instruction before autocompact fires; `/clear` with a hand-written brief;
  subagents when you will need only the conclusion [2044548257058328723, 2026-04-15]. Context rot on the 1M
  model starts around 300 to 400k tokens; `CLAUDE_CODE_AUTO_COMPACT_WINDOW=400000` is offered as a
  compromise [2044653085415604473, 2026-04-16]. Bad compacts happen when the summary cannot predict your
  next request.
- Skills: nine categories seen at Anthropic (library reference, product verification, data fetching,
  business process, scaffolding, code quality and review, CI/CD, runbooks, infrastructure operations).
  Writing tips: do not state the obvious; "The highest-signal content in any skill is the Gotchas
  section."; a skill is a folder with scripts, references and assets; avoid railroading; keep setup in a
  `config.json`; the description is a trigger for the model; store logs for memory in
  `${CLAUDE_PLUGIN_DATA}`; on-demand hooks such as `/careful` and `/freeze`; measure usage with a
  PreToolUse hook. Verification skills are worth an engineer-week [2033949937936085378, 2026-03-17].
- Context engineering for Claude 5 models: rules to judgement, examples to interface design, everything
  upfront to progressive disclosure, repetition to simple tool descriptions, memory in CLAUDE.md to
  auto-memory, simple specs to rich references (HTML mockups, test suites, code in another repo, rubrics).
  Claude Code's own prompt shrank "with no measurable loss on our coding evaluations". CLAUDE.md: describe
  the repo briefly, then gotchas; point to a verification skill instead of inlining it. `claude doctor` /
  `/doctor` right-sizes skills and CLAUDE.md [2080710971228918066, 2026-07-24]. Short form: "thin prompts",
  thick artifacts and context, thin skills [2077539537992229076, 2026-07-15].
- Effort: effort mainly changes how much verification and edge-case testing happens and how many
  assumptions Claude makes for you. His loop: spec and interview, implement on low, review and iterate on
  low, then "Verify and test on high effort". Rule of thumb: low for brainstorming and easy changes, medium
  for most feature work, high for bugs in brownfield code, max for fully autonomous hard problems
  [2103576349499855160, 2026-09-25].
- HTML instead of markdown for plans, specs, PR explainers, reports and throwaway editors, always with a
  copy-as-prompt export; "I attach a HTML code explainer to every PR I make now." Downsides he lists: 2 to
  4x slower to generate and noisy diffs [2052809885763747935, 2026-05-08]. Playground plugin for
  interactive HTML [2017024445244924382, 2026-01-29].
- Dynamic workflows: patterns (classify-and-act, fan-out-and-synthesize, adversarial verification,
  generate-and-filter, tournament, loop until done); failure modes they counter (agentic laziness,
  self-preferential bias, goal drift); quarantine agents that read untrusted content from privileged
  actions; set token budgets; one verifier per rule for rules Claude keeps missing; mine past sessions for
  repeated corrections and distil them into CLAUDE.md [2061907337154367865, 2026-06-02].
- Harness design lessons: static content first and dynamic last for caching; send updates as
  `<system-reminder>` messages; never add or remove tools mid-session; plan mode is a tool call, not a tool
  swap; defer tool loading; compaction reuses the parent prefix [2024574133011673516, 2026-02-19]. "The bar
  to add a new tool is high"; a docs-search subagent instead of stuffing the system prompt
  [2027463795355095314, 2026-02-27].
- Agents should use files and bash: write results to files and grep them, keep plans and scratch pads on
  disk [1970243260292702286, 2025-09-22], [1982869399901200638, 2025-10-27]. Personal setup in his home
  directory with a CLAUDE.md, folders for memory, journals and todos, and `/journal` and `/todos` commands
  [1944877531028725840, 2025-07-14].
- Tasks replace todos; `CLAUDE_CODE_TASK_LIST_ID` shares a task list across sessions, stored in
  `~/.claude/tasks` [2014480496013803643, 2026-01-22].

Evidence and numbers: prompt cache misses are treated as incidents; about 20 tools in Claude Code (February
2026); Terminal-Bench 3.0 examples where a task went from 1/5 at low to 5/5 at xhigh, 2 minutes versus 33
minutes [2103576349499855160]; the Bun rewrite used workflows [2061907337154367865].

Tools and files named: AskUserQuestion, `implementation-notes.md`/`.html`, `SKILL.md`, `config.json`,
`${CLAUDE_PLUGIN_DATA}`, `/rewind`, `/compact`, `/clear`, `/effort`, `/ultraplan`, `/btw`, `/doctor`,
`/deep-research`, `~/.claude/workflows`, trigger word `ultracode`, EnterPlanMode/ExitPlanMode, ToolSearch,
`defer_loading`.

Caveats: He calls his HTML habit maximalist and his effort findings toy examples. He wrote that workflow best
practices are "still developing" [2061907337154367865]. After leaving he questioned plan mode and adversarial review and warned about
agent mania [2115937378674372783]; his November forecast that models will not need to verify is not yet
practice.

Relevance: high. The most detailed written guidance on skills, context, sessions and effort, with a clear
record of which older rules were retired.

### Cat Wu (@_catwu, Claude Code product lead until late October 2026, then OpenAI; 39 posts, 2025-06-05 to 2026-11-05)

Thesis: Treat the model as someone you delegate to, and rebuild the product and your habits at every model
release.

Practices
- Opus 4.7 workflow shifts: "treat it like an engineer you're delegating to, not a pair programmer you're
  guiding line by line"; auto mode; full context in the first turn (goal, constraints, acceptance
  criteria); tell the model how to verify, in the claude.md or a `/verify-app` skill [2044808533905178822]
  to [2044808538351100377] (2026-04-16).
- Product lessons that apply to a setup: short sprints, demos and evals over docs, re-test old ideas at
  each model release and "remove the extra scaffolding that is no longer needed" [2035104388541473275,
  2026-03-20]; "Find the simplest thing that works." [2035104389808222383, 2026-03-20]; the first two are
  in [2035104385391632879] and [2035104387165786331].
- Shortcuts: `!` runs bash inline, `ctrl+s` stashes a draft, `ctrl+g` opens the prompt or plan in `$EDITOR`
  [2032499411230785661, 2026-03-13]. `claude agents` from the root code directory as a control plane
  [2053999857799672111, 2026-05-12]. Opus for planning and Sonnet for execution as a model setting
  [1955694117264261609, 2025-08-13].
- Delegated research: kick off a dynamic workflow, ask for an artifact by email, review later
  [2073806626965049686, 2026-07-05].

Evidence and numbers: internal team examples [1930703535282491903 onward, 2025-06-05]; customer figures such
as Wiz migrating 50,000 lines in a day [2028603862693941692, 2026-03-02] (vendor-reported).

Caveats: Mostly announcements; little about her own daily setup. Now at a competitor.

Relevance: medium. The delegation framing and the rule to remove scaffolding at each release are the useful
parts.

### Other Claude Code team members

Lydia Hallie (@lydiahallie; 17 posts). Skills can run in an isolated subagent with `context: fork`, and
embed shell output with a `!` command placeholder [2033603164398883042, 2026-03-16], [2034337963820327017,
2026-03-18]. Auto mode rules are written in plain English, keep built-ins with `$defaults`, and `claude
auto-mode critique` checks them [2090134982161502394], [2090134983625285845] (2026-08-19). "it's the first
model where medium is my default in Claude Code" [2096024729496994303, 2026-09-04]; effort is saved per
model in `modelSettings` [2096026520422945202]. Idle compaction summarises long idle sessions before the
cache expires; `idleCompaction: false` turns it off [2110484841926152622, 2026-10-14]. Learning output style
for staying hands-on [2056420694087594283, 2026-05-18]; custom styles in `~/.claude/output-styles`
[2080378470111256907, 2026-07-23]. She wrote the model-versus-effort article: check context first, then
ask "did it not know enough, or did it not try hard enough?"; "Effort changes how much work Claude does. The
model changes what Claude knows." [2074900291062034618, 2026-07-08]. Relevance: high for settings.

Noah Zweben (@noahzweben; 20 posts). Scheduling and remote work: `/schedule` for cloud jobs used internally
to fix CI failures and push doc updates [2036129220959805859, 2026-03-23]; routines triggered by schedule,
GitHub event or API [2044093913376706655, 2026-04-14]; `/loop` without an interval lets Claude pick the
cadence [2042670949003153647, 2026-04-10]; the Monitor tool replaces polling with background scripts that
wake the agent [2042332268450963774, 2026-04-09]; `/autofix-pr` sends a session to the cloud to keep a PR
green [2041654973491245509, 2026-04-07]. Relevance: medium.

Sid Bidasaria (@sidbid; 10 posts). Dynamic workflows: say "workflow" or set `/effort ultracode`; use for
tasks too big for one session or needing higher confidence; they are scripts, so save and commit them; they
are expensive [2060047510564163675] to [2060047521993662699] (2026-05-28). Adversarial review defined: for
each reported bug, ask two or more Claudes in isolated contexts to refute it [2060120459916750995].
Relevance: medium.

Delba de Oliveira (@delba_oliveira; 8 posts). Feedback loops article: write down the manual checks you run
(dev server, console errors, clicking through), encode them as a skill using the skill-creator plugin and an
interview, add measurable criteria (performance budget, accessibility checklist), then a second agent
reviews before merge; the team's bundled feature skill runs `/simplify`, a custom `/verify`, a design check,
opens a PR and watches CI [2062203743387459836, 2026-06-03]. Auto mode in four terms: classifier, filtering
(it sees your messages and tool calls, not Claude's reasoning or tool outputs), tier check, probe
[2065106020347613598, 2026-06-11]. Sound hooks for Stop and Notification events [2020515023412744477,
2026-02-08]. Relevance: high for verification design.

Adam Wolff (@dmwlff; 10 posts). "Most of the fancy stuff you can do with bespoke tools, custom agents, and
elaborate skills can also be achieved with a prompt." [2006035614806802820, 2025-12-30]. On dropping small
preparatory PRs: "the incremental thinking was load-bearing" [2025310199519801399, 2026-02-21]. Fable for
longer projects, Opus at medium for a quick PR [2080705598585438369, 2026-07-24]. Relevance: medium, as a
simplicity counterweight from inside the team.

Dickson Tsai (@dickson_tsai; 6 posts). HTTP hooks post events to a URL and are described as easier and more
secure than command hooks [2029235808235078095, 2026-03-04]; `/debug` reads session debug logs, for example
to learn why a hook did not fire [2019314348632555651, 2026-02-05]; rename sessions with `/rename` or a
UserPromptSubmit hook [2054008483402694807, 2026-05-12]. Relevance: medium.

Ado Kukic (@adocomplete; 46 posts). Feature catalogue as of December 2025 [2006802341228655083, 2026-01-01]:
`!` prefix, Esc Esc rewind, `--continue`/`--resume`, `/context`, `-p` headless mode, `/rename`, `/init`,
`/export`, `/sandbox`, hooks, plugins, LSP. "I default to plan mode 90% of the time." [2006803763156402395].
Settings: `defaultMode: "acceptEdits"`, `attribution`, `cleanupPeriodDays`, `alwaysThinkingEnabled`,
`additionalDirectories` [2008586048641867841] to [2008586053809271240] (2026-01-06). By October: medium for
80% of tasks, high for about 15% [2109671905733341559, 2026-10-12]. Named sessions can message each other
[2087728817012162973, 2026-08-13]. Relevance: medium; several items are dated (thinking keywords, `#`).

Alex Albert (@alexalbert__; 32 posts). Launch explainers: hooks as deterministic shell commands
[1940480979141021781, 2025-07-02]; skills and progressive disclosure, build them iteratively from real
failures [1978877546969354519], [1978877575767478633] (2025-10-16); tool search with `defer_loading`
[1993038651916533768, 2025-11-24]; Opus 4.5 prompting guide: soften emphatic tool instructions
[1993365987773890941, 2025-11-25]; against over-engineering add "Only make changes that are directly
requested. Keep solutions simple and focused." [1993366001103388929, 2025-11-25]; require reading files
before proposing edits [1993366013308813390, 2025-11-25].
Relevance: medium; the Opus 4.5 advice may be superseded.

### Official accounts (@ClaudeDevs 54, @claudeai 21, @AnthropicAI 5)

Thesis: Official guidance in 2026 centres on loops with explicit stop conditions, self-verification, auto
mode, and matching model and effort to the task.

Practices
- Loops article (written by Delba): four loop types by trigger and stop condition (turn-based, `/goal`,
  `/loop` and `/schedule`, proactive routines); deterministic criteria work best for `/goal`, where an
  evaluator model checks the condition each time Claude tries to stop; keep quality by keeping the codebase
  clean, encoding verification as skills, making docs reachable and using a second agent for review; manage
  cost by piloting on a slice, using scripts for deterministic work, and `/usage` [2074208949205881033,
  2026-07-06].
- Fable 5 start-up thread: pick a hard backlog item, let the model interview you for the spec, turn on auto
  mode; high effort as default [2064394924292997187], [2064394925358366821]; "Existing prompts or skills
  developed for prior models are often too prescriptive for Fable." [2064394926469840957]; give the model
  success criteria to check against [2064394927535185920] (all 2026-06-09).
- Model routing: an expensive model as advisor to a cheaper executor (about 92% of the score at about 63%
  of the price on SWE-bench Pro) or as orchestrator of cheaper workers (96% at 46% on BrowseComp)
  [2074606059864625355], [2074606063509528855] (2026-07-07). Guide on choosing a model and putting subagents
  on smaller models [2119898687803621427, 2026-11-09].
- Migrations: build a judge first and validate it on deliberately broken code; rulebook, dependency map and
  gap inventory; stress-test rules on a few files and throw the output away; mechanical work queue rebuilt
  from disk; two adversarial reviewers with a third on disagreement; smaller models implement, larger ones
  review; "You fix the process (loop) that produced the code." [2079654423828304282, 2026-07-21].
- Security-guidance plugin runs on hooks at three levels (file edit, end of turn, commit), with org rules in
  `claude-security-guidance.md` [2059385241115181528], [2059385243476586715] (2026-05-26).
- Auto mode mechanics and caveat [2036503583667933400, 2026-03-24]; agent view via `claude agents`
  [2053940935906439444, 2026-05-11]; Concise output style [2090245922685063634, 2026-08-20]; mods (TypeScript
  middleware shipped in plugins; they run with full machine access, install only from trusted sources)
  [2105721440490361312, 2026-10-01]; Projects [2100632677904744716, 2026-09-17].

Evidence and numbers: see (d); Bun migration cost about $165,000 at API prices, 19 regressions after merge
[2079654423828304282]; security plugin cut security-related PR comments 30 to 40% internally
[2059385242319012188].

Caveats: Vendor accounts; numbers are self-reported. Many posts only link to blog pages that are not saved
in this collection.

Relevance: high for loops, effort and model routing; medium otherwise.

### Andrej Karpathy (@karpathy; 40 posts, 2025-02-02 to 2026-11-01)

Thesis: Coding flipped for him within weeks around December 2025 from mostly manual to mostly agents. The
leverage comes from giving agents goals and tests to loop against while staying the overseer; the models
still make junior-style conceptual mistakes and ignore style instructions.

Practices
- Timeline of his own workflow: vibe coding for throwaway projects [1886192184808149383, 2025-02-02]; in
  August 2025 about 75% tab completion, agents for larger chunks, no YOLO mode, one instance at a time
  [1959703967694545296, 2025-08-24]; nanochat written by hand because agents were net unhelpful
  [1977758204139331904, 2025-10-13]; by December 80% agent coding [2015883857489522876, 2026-01-26]; in
  November 2026 Claude Code desktop with "Opus 5.5 on Medium effort as my default" [2116957135661945283,
  2026-11-01].
- Layout in January 2026: a few Claude Code sessions in Ghostty on the left, an IDE on the right to watch
  the code [2015883857489522876].
- Leverage: "Don't tell it what to do, give it success criteria and watch it go." Write tests first, put a
  browser MCP in the loop, write the naive correct version then ask for optimisation that preserves
  correctness [2015883857489522876].
- Failure modes to guard against: wrong assumptions run with unchecked, no clarifying questions, no
  pushback, bloated abstractions, dead code left behind, unrelated comments and code changed
  [2015883857489522876]; misreported experiment results and ignored CLAUDE.md style rules
  [2019851952033771710, 2026-02-06]; "The agents do not listen to my instructions in the AGENTS.md files."
  [2035173492447224237, 2026-03-21].
- Naming: "agentic engineering" for professional agent use with oversight [2019137879310836075,
  2026-02-04]; context engineering over prompt engineering [1937902205765607626, 2025-06-25].
- Build for agents: CLIs, markdown docs, skills, MCP [2026360908398862478, 2026-02-24]; DeepWiki MCP plus
  the GitHub CLI to extract one feature from a library instead of depending on it [2021633574089416993,
  2026-02-11].
- autoresearch: the human edits a prompt file, the agent edits the training code in a loop on a git branch
  with fixed 5-minute runs and a single metric [2030371219518931079, 2026-03-07]; any metric that is cheap
  to evaluate can be optimised this way [2031135152349524125, 2026-03-09]. Multi-agent research orgs with
  worktrees, tmux grids and files for communication did not work yet because the agents' ideas were poor
  [2027521323275325622, 2026-02-27].
- LLM knowledge base: `raw/` sources compiled by the LLM into a markdown wiki with index files and
  summaries, queried by an agent, outputs filed back, periodic lint passes, Obsidian as viewer; no RAG
  needed at about 100 articles [2039805659525644595, 2026-04-02]. Shared as an "idea file" for other
  people's agents to build from [2040470801506541998, 2026-04-04]. Properties he values: explicit, local,
  plain files, any model [2040572272944324650]. He still reads what is filed [2041162213160091996,
  2026-04-06].

Evidence and numbers: autoresearch ran about 700 changes over two days and cut the leaderboard time from
2.02 to 1.80 hours [2031135152349524125]; a home server setup done in about 30 minutes unattended
[2026731645169185220]; HackerTube in about 2 hours [2116957135661945283].

Tools and files named: Claude Code, Codex, Cursor, Ghostty, tmux, git worktrees, `raw/`, Obsidian, Marp,
DeepWiki MCP, GitHub CLI, `CLAUDE.md`, `AGENTS.md`.

Caveats: He reports failures openly: open-ended improvement of nanochat failed twice
[2019851952033771710]; Codex did not hold the autoresearch loop [2031083551387701698]; he gave up fighting
code-quality drift. His work is research code and personal projects.

Relevance: high. An independent heavy user whose advice (success criteria, tests first, watch for wrong
assumptions) matches the team's, and whose complaints show where instruction files fail.

### Addy Osmani (@addyosmani; Google until mid-2026, Anthropic Claude Code from 2026-09-08; 21 posts, 2025-07-19 to 2026-11-08)

Long articles: Agent Harness Engineering [2053231239721885918, 2026-05-09]; The Orchestration Tax
[2059844244907696186, 2026-05-28]; Loop Engineering [2064127981161959567, 2026-06-08]; Agentic Code Review
[2066595308629594363, 2026-06-15]; Own the Outer Loop [2074927530482835916, 2026-07-08]; Your coding agents
made you a manager [2119332146485891501, 2026-11-08].

Thesis: Quality now lives in the constraints around the agent. Engineer the harness from observed failures,
build loops with a separate checker, and keep a human accountable for the merge, with review depth set by
blast radius.

Practices
- Instruction files: auto-generated ones hurt because they duplicate what the agent can discover; keep only
  non-discoverable information (tooling gotchas, non-obvious conventions, landmines), "Every other line is
  noise."; prefer a hierarchy of files by directory [2026172457233829922, 2026-02-24].
- The ratchet: each observed failure becomes a rule, hook or reviewer check, and constraints are removed
  when a better model makes them redundant; "Every line in a good system prompt should trace back to a
  specific, historical failure." Hooks should be silent on success and verbose on failure; ten focused
  tools beat fifty overlapping ones; unverified MCP servers can inject text through tool descriptions
  [2053231239721885918].
- Attention: scale the number of agents to your review rate; sort work into delegable and judgement-heavy
  piles and do not parallelise the second; batch reviews; make agents prove the boring 80% with tests or
  screenshots [2059844244907696186].
- Loop building blocks shared by Claude Code and Codex: automations, worktrees, skills, connectors,
  sub-agents, plus a state file on disk; split maker from checker [2064127981161959567]. Secondhand: this
  article attributes to Boris the line "I don't prompt Claude anymore. I have loops running that prompt
  Claude" [2064127981161959567]; I did not find that wording in a saved Boris post.
- Review: tier by risk; require evidence before review (purpose, test output, proof it ran); keep PRs
  small; "Read the test changes more carefully than the code."; keep CI strict because agents weaken it to
  pass; "Treat every AI review as a sensor, not a verdict". For a solo developer with no users: tiering,
  test-change discipline and CI are most of what is needed [2066595308629594363].
- Short forms after joining Anthropic: multi-agent first pass on every PR, human sign-off on sensitive
  paths [2097027173941141799, 2026-09-07]; agree outcome and constraints, give exact build, test and lint
  commands, turn rejected-in-review items into skills, write lessons into CLAUDE.md instead of fixing by
  hand [2098662421644853433, 2026-09-12]; keep a subagent only when work is parallel, needs fresh context,
  or tool choice demands it [2114967833708732607, 2026-10-27].
- Manager article: a check the agent can run is the highest-leverage habit and the verify command is the
  most useful CLAUDE.md line; brief only what the agent cannot read from the repo; requests (prompts,
  CLAUDE.md, skills) versus requirements (hooks, deny rules, managed settings); after two failed
  corrections restart with a better prompt; five questions before an unattended run (done condition,
  self-verification, boundaries, turn or spend limit, where output lands and who approves); pilot on three
  files first [2119332146485891501].

Evidence and numbers (as he cites them, from vendors and papers not saved here): Faros AI, 22,000
developers: churn up 861%, defect rate from 9% to 54%, zero-review merges up 31.3%; GitClear: about 4x
output for about 12% real gain; CodeRabbit: AI PRs with about 1.7x more issues [2066595308629594363]; a
Wharton result on accepting wrong AI answers and an Anthropic trial with a 17-point comprehension gap
[2074927530482835916].

Caveats: He flags that some data comes from vendors selling review tools. Later posts are written as an
Anthropic employee and lean on Claude Code features.

Relevance: high. The clearest guidance for sizing review and instructions to a small project.

### Simon Willison (@simonw; 18 posts, 2025-06-16 to 2026-11-10)

Thesis: Agents raise the discipline required; your job is to deliver code you have shown to work.
Practices: the lethal trifecta (private data, untrusted content, external communication) as the security
test for any agent setup [1934602159984984235, 2025-06-16]; red/green TDD, where the agent watches tests
fail first [2025992745299652906, 2026-02-23]; anti-pattern of sending unreviewed code to collaborators
[2029260505324412954, 2026-03-04]; tools for agents to demonstrate their work beyond tests (Showboat,
Rodney) [2021280918204228082, 2026-02-10]; stop overloading prompts with examples and don't-lists
[2079553486568800405, 2026-07-21]; a prompting-guide tip to tell the model "This codebase is yours"
[2120029347948220500, 2026-11-10]. "they make software engineering even harder" [2103288927805476900,
2026-09-25]. Caveat: his posts mostly link to his blog and guide, which are not in this collection; his
interview with Cat Wu and Thariq (simonwillison.net/2026/Jul/21/cat-and-thariq/) is an unfetched lead.
Relevance: medium here, high via the linked guide.

### Mitchell Hashimoto (@mitchellh; 17 posts, 2025-10-11 to 2026-09-16)

Thesis: Use agents heavily but keep systems understanding; do not accept results you cannot judge.
Practices: "any diff an agent generates over ~1500 lines is too big"; try the whole feature loosely first,
then decompose into atomic reviewable tasks (and do the decomposition yourself in parallel), run those as
separate agents, repeat [2066645959539556852, 2026-06-15]. The "whiteboard defense": be able to explain and
defend any customer-facing system you ship; prototypes are exempt [2100249348345057389, 2026-09-16]. Slop is
acceptable for experiments and regenerable scaffolding with transparency, not for other people's projects
[2052397933522506079, 2026-05-07]. A judge agent prompt that distrusts the author [2089111740395270615,
2026-08-16]. Nightly agents reviewed at 06:00, at least two agents running constantly [2087227139154448436,
2026-08-11]. `go doc` and `gopls` make agents productive in Go [2046319366489407803, 2026-04-20]. Evidence:
a loop optimised a renderer from 88ms to 1.5ms for about $350, while his hand-written version ran at 20
microseconds [2060088112257372610, 2026-05-28]; 16 sessions and $15.98 for one Ghostty feature
[1977016133409820684, 2025-10-11]. Caveat: Codex proposed an unauthenticated shutdown API after a lazy
prompt [2089446702285758559, 2026-08-17]. Relevance: high for review thresholds and scepticism.

### Peter Steinberger (@steipete; 22 posts, 2025-11-07 to 2026-09-24)

Thesis: Stop prompting turn by turn; design loops and give the agent a real machine to test on. Practices:
"You should be designing loops that prompt your agents." [2063697162748260627, 2026-06-07]; a maintainer
loop that wakes every 5 minutes and routes work to threads, with orchestrator, triage, autoreview and
computer-use skills [2064998499780084154, 2026-06-11]; a progress tracker markdown file for long runs
[1986799989775810955, 2025-11-07]; convert an MCP server to a compiled CLI with mcporter and one line in
the agents file: "Progressive disclosure, no context pollution." [1986968745504334300, 2025-11-08]; tell
the model there is a bug and it keeps looking [2060672154727825718, 2026-05-30]; give the agent its own
computer for end-to-end tests [2073214429655883814, 2026-07-04]; an ambitious cleanup target such as
removing 20% of the least useful tests within 2% coverage [2103148444701610233, 2026-09-24]. Evidence:
about 6,000 lint and type issues fixed overnight [1986799989775810955]; about 400k lines of tests deleted
with little coverage change [2103147927313199260]. Caveat: Codex-centred, high token budgets. Relevance:
medium.

### Geoffrey Huntley (@GeoffreyHuntley; 25 posts, 2025-04-21 to 2026-10-16)

Thesis: A simple outer loop with a prompt file, specs and a fresh context per iteration goes a long way;
the hard parts are systems engineering. Practices: run the same `PROMPT.md` in a while-true loop with a
checkpoint file [1914271203579273381], [1914271208058864039] (2025-04-21); "One cycle = one context
window" [1914271223489724588, 2025-04-21], and restart when context nears its limit; `/specs` written from a product view
[1914271213331058924]; mix deterministic workflow engines with the agent loop [2092975233556996212,
2026-08-27]; a recurring janitor task to improve names and structure because agents replicate bad patterns
[2111161924683456867, 2026-10-16]; prerequisites for factories: sandboxing, monorepo, reproducible builds,
CI/CD, secrets [2082525589416923314, 2026-07-29]. Caveat: mostly links to his blog; strong career claims.
Relevance: medium.

### Steve Yegge (@Steve_Yegge; 11 posts, 2025-03-09 to 2026-09-02)

Practices: after an agent with permissions disabled wiped a production database password, "Make sure your
agent is always following a written plan that you have reviewed!" [1946360175339974807, 2025-07-19]; "you
have to keep an iron grip on system size" because models outbuild what they can maintain
[2094947586373505122, 2026-09-02]; carefulness as the property that matters for production work
[2079346280988348865, 2026-07-20]. With 20+ concurrent agents his job reduced to asking, credentials, taste
choices and communication [2077475727327604932, 2026-07-15]. Caveat: two saved posts are image-only.
Relevance: medium, mainly as a failure report.

### OpenAI Codex people

Tibo Sottiaux (@thsottiaux; 3 posts): file deletions happened mostly in full-access mode without sandbox or
auto review [2077630111499882637, 2026-07-16]; 300k default context chosen deliberately
[2108778939057664357, 2026-10-10]. Alexander Embiricos (@embirico; 5 posts): long-lived threads plus "using
a subagent in parallel, do X" [2046033614106931414, 2026-04-20]; scheduled check-ins
[2051521360896422264, 2026-05-05]; AGENTS.md, Agent Skills, `.agents` config and Agent Plugins as shared
standards [2085403842154512454, 2026-08-06]. Ryan Lopopolo (@_lopopolo; 13 posts, at Google Cloud by late
2026 per a post seen only in a search listing, Secondhand): "Skills are run books not programs."
[2084024338366578939, 2026-08-02]; "The harness should be constantly working to make itself obsolete."
[2090990833675939875, 2026-08-22]; "Literally everything you give the agent is prompts." after a 5-point
eval lift from renaming a docs folder [2106110500719501413, 2026-10-02]; prompts for deleting low-value
tests and finding places that fight the framework [2086269569841377295, 2026-08-09], [2099339717976478086,
2026-09-14]. Karel Doostrlnck (OpenAI researcher; 1 article): worktrees, many shells, one editor per
worktree, "Don't get baited by overly fancy tooling."; the agent commits its own notes and helpers to a
personal folder so it improves across sessions [2019477361557926281, 2026-02-05]. Others: Codex `/goal`
[2049917871799636201, 2026-04-30], subagents [2033636701848174967, 2026-03-16]. Relevance: medium; useful
for cross-harness parity (AGENTS.md, skills, `/goal`, subagents, worktrees exist in both).

### Guillermo Rauch (@rauchg; 11 posts, 2026-05-31 to 2026-11-09)

Practices: research in a plain `research/` folder with an AGENTS.md describing format and practices, synced
by git, reports rendered as HTML [2081103993917649134, 2026-07-25]; README written by hand for people,
internal docs in terse English for agents [2106848085267902815, 2026-10-04]; know when to stop hardening
and optimising: "Agents will happily drill no matter what." [2107962327169675566, 2026-10-07]; offload
parallel work to cloud sandboxes with a skill rather than a custom orchestrator [2119878364794372162,
2026-11-09]. Caveat: promotes Vercel products; no posts from other Vercel engineers were collected.
Relevance: medium.

### swyx (@swyx; 12 posts, 2025-03-30 to 2026-08-10)

Practices: log every execution step in development so the model can debug its own code [2005825608358715527,
2025-12-30]; a long-running skill to turn a prototype into a tested, maintainable repo, 103 commits in about
16 hours [2057559570177007912, 2026-05-21]; weekly automations [2078244735794413786, 2026-07-17]. Opinion:
removing human code review is "the Final Boss" and he is not there yet [2028795270306079156, 2026-03-03].
Relevance: low to medium.

### Dario Amodei (@DarioAmodei; 7 posts, 2025-10-11 to 2026-09-12)

No coding practice on X; see (d). Relevance: low for a setup, context only.

### Context posts by others (35 posts)

Saved because team members replied to or quoted them: questions that drew Boris's CLAUDE.md answers
[2007200436781232329], [2007568991364014486]; Lucas Beyer's request for agent-managed memory
[2006857780976812181, 2026-01-01]; reports of Opus 4.6 versus Codex on autoresearch [2019824445792424385],
[2031044694441148709]; a deleted-drive report [2107621483392446572]; Jarred Sumner on workflows and
adversarial review in the Bun rewrite [2060050578026189172, 2026-05-28]; Lee Robinson on minimal agent
rules [1993162978410004777, 2025-11-25]; and one long article by the CEO of a ten-person company running a
permanent agent fleet with no PRs, hourly deploys and AI judges for taste decisions, 0.9% of changes
reverted, $3.1M of tokens in a month [2115623382721126826, 2026-10-29]. Relevance: low; the last is an
extreme data point, self-reported.
