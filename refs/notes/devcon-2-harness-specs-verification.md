# AI Native DevCon London (June 2026), batch 2: harness engineering, specs, verification

Sources read: 14 of 14 assigned transcripts, each start to end. One supplementary source, already in
the corpus but not in the batch list, was also read in full because the Lopopolo talk does not contain
the repo-layout details and numbers the assignment asks about: the OpenAI article `Harness engineering:
leveraging Codex in an agent-first world` (key OAI-HE). Everything taken from it is labelled OAI-HE.

Reading conditions that limit confidence:

- All 14 are auto-captions with no speaker labels. Tool and people names are often garbled; I flag
  each spelling I am unsure of. Verbatim quotes keep the caption text, including its errors.
- `4d3-Zrmf9Wo` (Obstbaum and Willoughby, evals) is badly garbled for most of its length. Many
  sentences cannot be parsed; several numbers are attached to unreadable context. I report only what
  is legible and mark the rest.
- No file carries a publication date. The 11 full talks are from the conference in June 2026 (titles
  and recap narration say so). The 3 recap videos (`606n8YC_-fU`, `DFDyRt4cU1Q`, `fwL31sNbq8g`) open
  with `Back in June` and advertise a November event in New York, so they were published between
  June and November 2026.
- OAI-HE has no date in its file. Inference: it says the first commit landed in late August 2025 and
  describes the following five months, so it was written around early 2026.

Source keys: LOPO (Lopopolo talk), OAI-HE (OpenAI article, supplementary), SLOAN, BOCK (Böckeler),
MART (Martinelli), AZRI (Azriel), CORM (Cormack), FARL (Farley), STACK (Paul Stack), EVAL (Obstbaum
and Willoughby), KUSH (Kushwaha), WALT (May Walter), R-SDD, R-VER, R-REV (the three recap videos).

## Cross-cutting findings

### Recurring practices

1. Every agent mistake becomes a durable guardrail, not a one-off correction. Preferred order of
   durability: prompt tweak (not durable), written doc, reviewer agent that reads the doc, lint or
   structural test. LOPO [10:15], [12:21]; OAI-HE (Enforcing architecture and taste); BOCK [18:35]
   (citing Mitchell Hashimoto); STACK [08:09], [14:21].
2. Keep the root instruction file small and make it a map plus an operating loop; put detail in
   docs, skills and per-topic guardrail files loaded on demand. LOPO [15:22], [18:27]; OAI-HE
   (roughly 100 lines); MART [16:26], [22:39]; BOCK [19:36]. STACK differs in style (a terse
   constraint list) but not in size philosophy [13:20].
3. Prefer deterministic checks (lint, types, structural tests, import-boundary scanners) over
   instructions for anything that can be checked mechanically, and write the failure message as a
   remediation instruction for the agent. LOPO [16:22], [21:35]; OAI-HE; BOCK [19:36], [20:37];
   CORM [21:40].
4. Passing tests are not proof. Add other signals: a test oracle, traces and logs the agent can
   query, a running app driven through a browser, runtime production data, security review of the
   whole codebase, spec-by-spec verification. CORM [16:33], [18:37]; AZRI [06:11]; WALT [03:08];
   LOPO [22:39]; OAI-HE (Increasing application legibility); FARL [26:54].
5. Use an independent reviewer with a different context from the implementer: adversarial plan
   review, persona reviewers, a spec reviewer given the base branch instead of the diff, a second
   model judging test quality. STACK [11:16], [15:22]; LOPO [18:27], [23:41]; AZRI [14:29];
   R-VER [06:07] (Meta).
6. Make the agent prove its work the way a teammate would: logs, screenshots, a recorded video of
   the feature working. LOPO [22:39]; OAI-HE (Increasing levels of autonomy); AZRI [17:34].
7. Split planning from execution and give each verification item its own fresh-context subagent;
   long sequential checking in one context degrades. AZRI [09:19], [12:28]; STACK [20:30] (one
   worktree per issue, never needs to clear context).
8. Decide how much human review a change gets by risk, not uniformly. BOCK [33:58]-[36:01]
   (probability, impact, detectability); MART [07:11], [24:42]; AZRI [28:54] (verify the critical
   1 to 5 percent); WALT [22:43].
9. Move the human decision earlier: review the plan, spec or ADR carefully, then let agents check
   implementations against it. R-VER [08:08]-[09:12] (Batey); STACK [12:16]; MART [08:13];
   FARL [21:41].
10. Run continuous cleanup (garbage collection, drift detection) on a schedule, separate from the
    per-change pipeline. OAI-HE (Entropy and garbage collection); BOCK [21:39]; WALT [06:16];
    LOPO [24:44].
11. Standardise the codebase on one pattern per concern, because existing code acts as a prompt and
    agents copy what is there. LOPO [14:22]; OAI-HE (Entropy and garbage collection); BOCK [36:01];
    MART [19:33].
12. Do not let the agent scaffold the project from memory; use the framework's own initializer or
    CLI so dependencies are current. MART [22:39].
13. Skills carry the how; they should be backed by scripts or a CLI where possible, and evaluated.
    STACK [11:16]; MART [09:14], [15:25]; WALT [18:34]; EVAL [16:47]-[24:00]; SLOAN [26:54].
14. A human triages what enters the loop, both for product direction and because inbound issues are
    an injection surface. STACK [25:36]; WALT [22:43]; AZRI [15:32] (untrusted preview URLs run in
    an ephemeral sandbox).
15. Do not flood humans with agent-opened PRs; send a short, scored report and let the human choose
    to open a ticket or PR. WALT [21:42]-[23:44]; R-REV [01:01]-[02:03] (drive-by PRs).
16. Fix flaky tests immediately and keep the suite fast so it can run constantly. CORM [13:28],
    [14:32]. OAI-HE disagrees (see contradictions).
17. Capture session history, review comments and failures as data and mine them periodically for
    missing guardrails. LOPO [24:44]; R-REV [06:08]-[07:13] (bdougie); STACK [14:21].
18. Match model strength to task type; small or cheap models for narrow, well-specified work and
    for simple verification steps. BOCK [05:12]-[08:20]; AZRI [26:47].

### (a) What harness engineering consists of, concretely

Definition. Lopopolo (who says of the term `kind of having invented the term here` [00:00]) defines
it as making the definition of a good job legible and surfacing it just in time during the agent's
run [10:15]-[11:19]. His stated goal: "I never want to give the same review feedback twice" [10:15].
Böckeler's reading: "it's reasonable to think of harness engineering as context engineering for
coding agents" [14:32]; she notes the term gained traction around February 2026 and is still
ambiguous because some people use it for improving the coding agent product itself [14:32].
Sloan (Tessl) describes the harness as a layer wrapping the codebase containing skills,
evaluations, hooks and policies [07:19].

Three phases of context delivery (LOPO [15:22]-[18:27]):

- Start of run: a numbered operating loop in the agent file. "the most important thing that ends up
  in that agent file is a numbered set of steps" [15:22]. Steps named: ground in the docs knowledge
  base and the ticket, read through past ADRs and design docs (caption says `address`; unsure),
  read the critical user journeys so a QA plan is in mind. He accepts slowness here.
- Messy middle: lints and tests written for agents, which assume tool output gets truncated and
  whose errors are "descriptive error messages that point them to run books for remediation steps"
  [16:22]. He calls this just-in-time prompt injection of the agent by its own tools, and prefers it
  to up-front rules because it does not occupy context and because "a tool called output is going to
  be given less weight during an auto compaction" [17:25].
- After the run: many LLM judges grade the static diff against guardrail docs and talk to the
  implementing agent on the PR thread [18:27].

AGENTS.md size and role.

- LOPO: the file is a map of where context lives and when to read it, not a rule list. "We don't
  want to jam a ton of rules in here" [18:27]. It points to a curated set of review personas that
  are bulleted lists of guardrails [19:28]. The talk gives no line count.
- OAI-HE (We made repository knowledge the system of record): the one-big-file approach was tried
  and failed for four stated reasons (crowds out context, everything-important means nothing is,
  rots, cannot be mechanically verified). Replacement: "give Codex a map, not a 1,000-page
  instruction manual"; the file is "(roughly 100 lines) is injected into context and serves
  primarily as a map".
- STACK: CLAUDE.md is "It is the executable contract." [13:20], a terse list of hard constraints
  (strict TypeScript, no `any`, named exports only, licence header on every file, no fire-and-forget
  promises, every command has log and JSON output, import only from the module's public entry, never
  leak internal paths) plus a final self-update line telling the agent to "record it and propose an
  update to your MD before we continue" [14:21] when it hits a non-obvious problem.
- MART: CLAUDE.md `has not much inside` except a reference to guideline files; most knowledge is
  in skills [16:26]. He cites a Zurich university study: "the bigger the system prompt, more
  hallucinations you get probably" [23:41], and says no file may beat a big one. He does not name
  the study; I could not verify it from the transcript.
- BOCK: move rarely-triggered rules out of AGENTS.md into a lint rule with a custom message; "It's
  much more effective to have this linting rule than to like stuff it into your context every single
  time the agent runs" [19:36].
- CORM, as a caution: the agent ignored an explicit AGENTS.md rule about flaky tests. "It says so in
  the agents.md file, and you're ignoring it again." [13:28].

Repo structure and docs layout.

- OAI-HE: a structured `docs/` directory is the system of record. Named contents: design docs
  catalogued and indexed with verification status; a set of core beliefs; architecture documentation
  giving a top-level map of domains and package layering; a quality document grading each product
  domain and layer; plans as first-class artifacts (lightweight ephemeral plans for small changes,
  checked-in execution plans with progress and decision logs for complex work); active plans,
  completed plans and known technical debt versioned together. The article's directory-tree figure
  was not captured in the saved text, so exact file names are not available from this corpus.
- OAI-HE (Enforcing architecture and taste): each business domain has fixed layers with one allowed
  dependency direction (Types, Config, Repo, Service, Runtime, UI); cross-cutting concerns enter
  through one `Providers` interface.
- LOPO adds documentation of product features, critical user journeys and why the app exists
  [19:28]-[20:32], and standardising on one stack per concern because "all the code in the repository
  of itself, outside of the documentation knowledge base is also prompts" [14:22].
- STACK: a separate UAT repository holding user-level tests run against the built binary, with the
  rule that tests are the source of truth [14:21], [17:26].

Linters and structural tests.

- LOPO: tests on the AST and on file layout; "really blunt hammers around file line counts, or
  whether or not snapshot tests exist" [20:32]. Requiring a snapshot test with 100% branch coverage
  for every React component pushes the model toward small pure components [20:32]. An ESLint ban:
  "statically disallow any function that has a type of any or unknown" except when parsing input in
  a route handler or from the database [21:35]. A custom guardrail asserting retries and timeouts
  on every network call, generated cheaply with exhaustive table-driven tests [16:22]-[17:25].
- OAI-HE: custom lints for structured logging, schema and type naming, file size limits and
  platform reliability rules; "we write the error messages to inject remediation instructions into
  agent context". Also linters and CI jobs that check the docs are current, cross-linked and
  well-structured.
- BOCK: an import-scanning tool to enforce which modules may call which [19:36]-[20:37]; codemod
  tools such as OpenRewrite as computational guides [17:35].
- CORM: encode an invariant in types so no test is needed, for example an authorised-request type
  that every protected function must take [21:40].
- STACK: unit, integration, contract, property and architectural tests, then out-of-repo UAT, then
  adversarial tests (injection, killing the process mid-run, deleting data) [14:21]-[15:22].

How humans review.

- LOPO: the agent "needs to convince me to merge its code" [22:39] with logs, screenshots or a
  recorded reproduction video. He reviews like a tech lead: benefit of the doubt, biased to merge,
  asking only for P2-and-above issues [23:41], caring about invariants and interfaces, not
  keystrokes [25:45]. Reviewer agents are "really just a matrix CI job that points out a bunch of
  markdown files to judge this thing" [23:41]. Recurring review findings are a signal to shift a
  guardrail earlier.
- OAI-HE: humans may review PRs but are not required to; most review is agent-to-agent; merge gates
  are minimal and PRs short-lived.
- STACK: humans approve the plan and choose what to build; then five automated merge gates (code
  review, adversarial review, CLI user-experience review, CI security review, skill checks) and
  auto-merge [15:22]-[17:26]. Plan and adversarial reviewer loop at most five times before a human
  arbitrates [12:16].
- MART: no pull requests; trunk-based development with ongoing paired review, depth set by risk
  [24:42].
- R-VER (Batey): stop trying to review a 7,000-line PR line by line; review an ADR in a separate
  PR first, with diagrams, then have agents check every later PR against the ADRs [07:07]-[09:12].
- R-REV (Kerr, McKinsey): review still matters because "it's not about quality control. It's about
  engaging with the mental model" [05:07].

Entropy and garbage collection.

- OAI-HE: agents replicate existing patterns, including poor ones. The team first spent Fridays on
  manual cleanup ("Our team used to spend every Friday (20% of the week) cleaning up"), then encoded
  `golden principles` in the repo and scheduled background agent tasks that scan for deviations,
  update quality grades and open small refactoring PRs; "Most of these can be reviewed in under a
  minute and automerged." A recurring doc-gardening agent opens fix-up PRs for stale docs.
- BOCK: calls this continuous drift detection and puts inferential (LLM) checks here, not in the
  per-commit pipeline. Her own set: a modularity review, a dependency freshness review and a
  security review triggered about weekly [21:39]. She warns it needs a team process, as with
  vulnerability backlogs [22:40].
- LOPO: collect every review comment, interruption, failed build and production exception and
  "slurp all this data up and dream over it every night" [24:44] with subagents that propose prompt
  improvements and missing guardrails.
- CORM: periodic refactoring weeks are part of the loop [24:44]-[25:47].

Numbers reported for the OpenAI work.

- LOPO talk: about three concurrent local sessions is his personal maximum [05:08]; "I can let a
  task go for six, 12, 36 hours and still get good results" [06:09]; 100% code coverage and 100%
  typed code are required [21:35]; guardrail docs can be compacted away on tasks spanning 15
  context windows [27:47]. The talk gives no repository size, PR count or team size.
- OAI-HE: zero manually written lines; about one tenth of the hand-written time (their estimate);
  on the order of a million lines in five months; "roughly 1,500 pull requests have been opened and
  merged with a small team of just three engineers"; 3.5 PRs per engineer per day; team grew to
  seven; hundreds of internal users; single runs of six hours or more; AGENTS.md roughly 100 lines;
  20% of the week formerly spent on cleanup.

Beyond code (SLOAN). A harness can pass every check and still be wrong when the missing context
lives outside the repo: the agent used a generic button instead of the design-system export button
that encodes accessibility rules, and "as far as the harness was concerned, everything went
smoothly" [05:13]. Product and design context lives in Figma, Linear, Notion and the CRM, drifts in
both directions, and a live MCP connection adds rate limits, cost, availability risk and
non-reproducible evals [10:26]-[11:28]. His options: vendors open up, a maintenance agent sits
between the tools and the harness, or the repo absorbs the context [17:34]-[19:38].

### (b) State of spec-driven development

What worked.

- MART: system use cases (actor, preconditions, main scenario, alternative flows, postconditions)
  plus an entity model, kept as files in the repo, with stack-specific skills doing the generation.
  He skips the separate plan and task phases used by Kiro and Spec Kit [06:10]. Postconditions act
  as acceptance criteria checked in tests [15:25]. In these projects "in those projects we don't
  prompt" [15:25]: the developer runs an implement skill against one use case. Demo: about 1.5
  minutes for a list screen [22:39]. For legacy work he extracts use cases and entity model from old
  code, tests and docs, has business people review them, then generates new code [10:17].
- MART preconditions: scaffold with the framework's own tool ("never let AI create the project"
  [22:39]), small instruction file, architecture docs (arc42), skills, MCP vector search over large
  in-house docs. With these he claims a near-deterministic rerun [23:41]-[24:42].
- STACK: structured plan generated from a triaged issue, attacked by an adversarial reviewer for up
  to five rounds, then human approval before implementation [11:16]-[12:16].
- R-VER (Batey): ADR-first. A system-level decision "always comes as a completely separate pull
  request in something called an architectural decision record" [08:08], reviewed hard by a human.
- FARL: BDD-style executable specifications written in a problem-specific DSL, used both as the
  prompt and as the acceptance test [24:51]-[25:53].
- AZRI side effect: once teams knew an agent would verify features against the ticket, "it
  encouraged them to write better specs" [24:44].

What failed.

- AZRI: agents ignore parts of detailed specs. His example ticket included a recording of a bug not
  to repeat; the delivered feature repeated it [04:07]-[05:07]. "coding agents that we are using are
  not focused on verifying features" [06:11].
- AZRI: a verifier given only the spec invents requirements (a new command, backward compatibility
  nobody asked for) [12:28]-[13:28]; "without to be grounded with the code, it's just not connected
  to reality" [13:28].
- R-VER (Batey): agents wrote more and longer ADRs until "not a single human understood them"
  [08:08]. Fix: the human starts the ADR and demands diagrams.
- MART: his first vibe-coded system (Windsurf, autumn 2024) could not be adapted to a second
  customer because he did not know what he had built [01:01]-[02:05]. Direct language-to-language
  translation of legacy code `never worked` and is only lift and shift [10:17]-[11:19].
- MART: "So you need the harness." [24:42]; specs alone are not enough. He also stopped writing
  generic skills for more stacks because the combinations are too many [16:26].
- MART: the work moves to requirements. "Now you have two weeks and then five minutes and two weeks,
  something like that." [26:47]. Two requirements engineers have more work than the one developer.
- SLOAN frames the industry arc as spec-driven development, then context engineering, then harness
  engineering [01:02]. BOCK's intro notes her earlier widely-read article comparing spec tools
  [00:00]; her talk itself does not assess spec-driven development.

How specs are kept in sync with code.

- MART: change the use case or entity model, then run the same implement skill again against the
  existing code. He does not regenerate from scratch because "my git history wouldn't look nice and
  it would be harder to review the changes" [30:00]. Work goes use case by use case, tracked Kanban
  style [21:37], [28:57].
- FARL: version-control the specifications because they are the program; run them in the deployment
  pipeline on every change [26:54].
- R-VER (Batey): "have the ADRs constantly reviewed against all of the pull requests" [09:12].
- STACK: UAT tests in a separate repo are the fixed reference; the agent is told not to change them
  and to assume a regression in the binary [17:26]-[18:26].
- OAI-HE: linters and CI check docs for freshness and cross-links; a doc-gardening agent fixes stale
  docs; plans and decision logs are checked in.
- SLOAN: for context that lives outside the repo, sync is unsolved and at enterprises it is a
  dedicated team's job; sometimes full sync is not even desirable [15:30].
- Note: the R-SDD narrator says code becomes something you can throw away and generate again
  [00:00]. Martinelli's own answer at [30:00] is that today he does not do that.

What an executable spec is.

- FARL: a specification in the form of tests that "both specify what we want and also verify that we
  got it" (R-SDD [03:10]; same passage in FARL [21:41]). The programmer invents a DSL for the
  problem, writes desired behaviours as BDD-style examples, the AI builds the test infrastructure
  that makes them executable, then generates code to satisfy them [24:51]-[25:53]. It must cover
  performance and security targets too, since those are contextual and cannot be inferred [22:45].
- AZRI uses the same phrase for a different thing: the existing ticket and design are executed by a
  spec-reviewer agent that extracts each requirement and checks it in the deployed preview
  environment through a browser [07:16]-[08:17], [17:34]. No test code is written.
- STACK calls his constraint files `executable constraints` rather than documentation [08:09].
- Inference: three meanings are in circulation: tests-as-spec (Farley), spec-as-checklist for a
  verifying agent (Azriel), and constraints enforced by gates (Stack). Only Farley's is
  deterministic.

### (c) Verification

Why tests alone mislead.

- FARL: a test generated from the code can only confirm "the working code does what the working code
  does" [05:09]; "We can't infer the goals from the solution because the solution can always be
  wrong." [05:09]. Agents will also game visible tests [26:54].
- CORM: asking for 100% coverage produced trivial tests and absurd error-injection cases; "It kind
  of wrote trivial tests" [05:08]. "You can't find security issues with tests." [16:33]; nor can
  tests judge architecture, and anything you cannot measure you cannot test [16:33]. Agents treat
  flaky tests as normal, and when chasing an eventually-consistent oracle will flip the code back
  and forth instead of fixing the test [13:28].
- CORM: a test oracle written by the same agent can share the code's logic and test nothing; he
  would build a model implementation outside the repo [29:55]-[30:55].
- R-VER (Ian Thomas, Meta): "AI was great at hallucinating awful tests" [06:07] that only raised CI
  cost.
- AZRI: unit tests cover imagined scenarios and comparing code to code is not the answer; the
  feature has to be exercised in a deployed environment [06:11], [23:43]-[24:44].
- WALT: an agent builds, another approves, tests pass, and "code still finds creative ways to fail
  in production" [03:08]. Agents propose plausible but unverified optimisations and the lazy fix of
  catching the exception [13:27].
- SLOAN: all harness checks green while the wrong component shipped [05:13].
- R-REV (bdougie): an unattended agent "was just politely hallucinating progress" [06:08].
- Dissent: LOPO requires 100% coverage, but as a steering device that forces decomposition and
  typed code, not as proof of correctness [20:32]-[21:35].

Additional signals and how to wire them into a loop.

- Remediation-bearing lint and structural-test failures during the run. LOPO [16:22]; OAI-HE.
  Böckeler's placement rule: run every cheap, fast sensor inside the coding session before commit
  [20:37].
- Agent-produced evidence at PR time: staging logs, screenshots, a recorded video. LOPO suggests a
  headless display in a container recorded with ffmpeg if no computer-use tool is available
  [22:39]. OAI-HE: app bootable per git worktree, Chrome DevTools Protocol wired in, skills for DOM
  snapshots and screenshots.
- Local observability the agent can query. OAI-HE: an ephemeral per-worktree stack with logs
  queried by LogQL and metrics by PromQL, making prompts such as a startup-time budget checkable.
  CORM: even an agent-built tracing framework is enough: "anything that can give it traces that it
  can look at to debug is amazingly useful" [18:37]. His loop: overnight repeated test runs, then
  hand the agent the trace of the failure so it reproduces rather than guesses [19:37].
- Test oracle. CORM: 1,500 tests run against real S3 pin behaviour; trust the oracle over docs
  ("never trust anyone's documentation at all" [09:16]). For new systems, write a trivial reference
  version first and test the real one against it [07:11].
- More kinds of tests: fuzzing and property-based tests found real issues; after each bug ask what
  kind of test would have caught it. CORM [15:32]. STACK lists contract, property and architectural
  tests [14:21].
- Types instead of tests for invariants. CORM [21:40]; LOPO [21:35].
- Whole-codebase security review, separate from PR review. CORM checks the findings into the repo,
  has the agent triage them ("Three quarters of them are valid." [22:40]) and then asks what tests
  would have prevented them. He names Codex Security.
- Spec verification by fresh subagents. AZRI's final design: a planner (large model) extracts
  requirements and failure scenarios; one small-model subagent per requirement runs in parallel in
  its own ephemeral sandbox with a browser session against the preview URL; an orchestrator
  collects verdicts [09:19]-[12:28], [16:33]-[17:34], [26:47]. Two tuning findings: give the
  reviewer the base branch, not the diff ("if we give the agent the base branch and the base code
  and not the diff, we're getting better results" [14:29]), and scope it to the area under review.
  Add a short list of critical flows (his example: subscription) checked on every PR [22:42].
- Adversarial reviewers and gates. STACK: reviewer told to "Assume everything is broken. Try and
  prove that it's broken." [15:22]; black-box UAT of the built binary in another repo; the product
  itself reproduces errors against the matching source version and files a well-formed issue
  [19:28].
- Held-back tests and pipeline execution. FARL: "We run the test cells in a deployment pipeline.
  Otherwise the AI is going to cheat." [26:54]; keep some tests hidden from the agent.
- A second model judging tests. R-VER (Meta): an `anti test slop` check on CI using a different AI
  tool, now run on most diffs with many AI-generated tests [06:07].
- Production runtime data. WALT: a sensor mapping production behaviour to function level (call
  frequency, duration, failures, which endpoints and business flows a function serves), exposed
  through an MCP server and a query layer (ClickHouse), with skills on top ("we have the skills of
  how to approach an HTTP 500, how to approach a memory leak, how to approach a performance
  degradation" [18:34]). It also answers the inverse question of what a planned change will affect
  [17:34]. Run as a scheduled workflow (GitHub Agentic Workflows on GitHub Actions, weekly, report
  to Slack) [09:23]-[11:25]. BOCK lists production sensors for latency and scalability as the last
  stage of her sensor placement [22:40].
- Evals for the context itself. EVAL: measure a skill on three things: discovery (does its
  description trigger), trajectory (did the agent follow the intended steps) and outcome
  [23:00]-[24:00]. SLOAN: evals to confirm context helps and does not overwhelm [26:54].
- Session logs as a signal. R-REV (bdougie): dump all agent sessions to a database and have the
  agent write end-of-session observation notes in markdown [07:13]. LOPO: nightly mining [24:44].
- Human as a sensor. CORM deliberately keeps himself in the loop and does not automate everything
  first, so he learns what goes wrong [23:41]. WALT: "If something works 90% of the time. It's not
  an automation, it's streamlining humans." [16:30].

### (d) Böckeler's map of the landscape and her cautions

The map, in three rings (BOCK [02:08]-[23:44]):

1. Model. Four things to know: models are not magic; they are stateless, so the harness resends the
   history each turn [04:10]; a bigger context window trades against attention; and model choice
   should follow task type (autocomplete, a few known files, large change needing code research,
   planning or debugging). She ran a local model in OpenCode on an M3 with 48 GB (caption `when
   3.6`, probably Qwen; unsure) and a small model the caption renders `GEMA for` (probably Gemma;
   unsure): speed acceptable, tool calling still weak, fine for a one-paragraph utility script
   [07:17]-[08:20].
2. Coding harness (the agent product): system prompts, built-in tools, code search, orchestration
   including subagents (caption `subjects`), caching, UI, extensibility and observability
   [09:22]-[10:24]. Named: Claude Code, Cursor, OpenAI Codex, OpenCode, the pi coding agent (cited
   for malleability). She warns against confusing interface with quality (terminal is not why
   Claude Code was good) and notes bloat: "With Claude Code, it hasn't even taken a year, and we
   feel like it's maybe a bit much." [11:26].
3. User harness, or context engineering for coding agents: rule files (AGENTS.md, CLAUDE.md),
   skills, MCP servers, subagents, extensions, plugins, hooks. She calls the current feature spread
   overwhelming, a storming phase, and says how to use these features was about half the conference
   [13:31].

Her mental model for the third ring [15:32]-[18:35]:

- Markdown content is of three kinds: normative (conventions), informative (product context,
  reference docs) and instructions (workflows such as failing test first).
- Guides are feed-forward: "So we're trying to anticipate what the agent might do wrong." [16:34].
  Sensors are feedback that triggers self-correction before a human looks.
- Each can be inferential (an LLM; "a review agent is an LLM judging the work of another LLM"
  [17:35]) or computational (deterministic, CPU: static analysis, codemods such as OpenRewrite,
  import scanners).
- The human steers the set of guides and sensors; every agent mistake is a prompt to engineer one
  [18:35].

Sensor placement along the path to production [20:37]-[22:40]: in the coding session before commit
when cheap and fast; at PR or integration time for extra inferential sensors; in CI only
computational ones ("you don't want the green or red state of your pipeline to depend on semantic
interpretation of an LLM" [21:39]); scheduled drift detection for inferential reviews; production
sensors via observability.

Timeline she gives [25:46]-[27:49]: autocomplete, IDE context, agentic modes about 18 months before
the talk, vibe coding, background agents, Claude Code generally available about a year, context
engineering term about a year, Opus 4.5 moment, skills, swarms (Gastown, around January 2026;
Cursor and Anthropic large experiments; a tool the caption renders `Cloud flow`, unsure), harness
engineering as the newest buzzword. She places swarms at an experimental stage [24:46].

Cautions [28:51]-[41:10]:

- Security: secrets leaking and a supply chain under attack; think harder about dependencies and
  sandboxing. She lists "Sandboxing is too tedious. Surely nothing will go wrong" [39:05] as a form
  of surrender.
- Stability: the DORA report found stability getting worse.
- Changeability: in a young, fully AI-built codebase "I made a change that touched 41 files, but it
  shouldn't have" [29:54].
- Token cost: from a 2024 keynote claim of 12 cents per 100 lines to newsletter reports of
  developers spending 500 dollars a day (caption has `not spending`, likely `now`; unsure).
- Cognitive load and burnout: people report about three hours of this before needing a break.
- Review crisis: "the state is no we cannot review faster" [31:57]. A flow crisis may follow: she
  cites James Lewis's prediction of congestion collapse as silos overproduce [32:58].
- Autonomy is real but unevenly distributed; choose supervision by "risk assessment out of
  probability impact and detectability" [33:58]. You earn less supervision through feedback loops,
  better context and a well-factored codebase: "AI can also deal with a well factored code base
  much better than with a messy code base" [36:01].
- Cognitive debt, cognitive deferral and cognitive surrender (the last from a paper she saw via a
  writer the caption renders `Adios Mani`, probably Addy Osmani; unsure). Examples of surrender:
  not reasoning about a big change, always using the biggest model, waiting for models to fix
  everything, being unable to work on the codebase without AI [38:02]-[39:05].
- For leaders this is still horizon two; ROI is unknown and people need time to build a good setup
  [41:10].

### (e) Farley's critique and the discipline he says still applies

Critique (FARL [02:05]-[19:37]):

- Vibe coding and programming in natural language have a place but are bad ideas as the method.
  "Vibe coding alone is simply not good enough." [11:19]. Natural language fails the three things a
  programming language gives: consistent grammar, unambiguous intent, repeatable execution. His
  verdict on prompts as source: "Not repeatable. Not deterministic, not version controllable."
  [13:22] (version-controlling the prompt does not reproduce the result).
- AI-generated tests derived from existing code are mostly a cop-out by people who will not state
  their goals; useful only for behaviour-preserving refactoring. "Automating testing from a solution
  is a bit of a joke." [28:57].
- Agents make big-bang changes, which removes incremental learning; most public success stories are
  small systems [16:31]-[17:33].
- The bottleneck did not move much: "We sped up the coding bit. That was the easy part of software
  development" [15:27]. Someone producing 12,000 lines a day cannot have it reviewed or manually
  tested: "No human being can review 12,000 lines of code per day." [18:37].

Discipline that still applies [19:37]-[30:01]:

- Tests are measurement against stated goals: "They are a form of measurement." [03:05]. Goals must
  be specified by people, including performance and security levels.
- Work in small steps, treat each change as an experiment, gather feedback from a deployment
  pipeline after every change. Continuous delivery practice is unchanged: "It's table stakes."
  [19:37].
- Specify with executable, BDD-style acceptance tests in a domain language; version-control them;
  run them in the pipeline; hold some back so the agent cannot game them [26:54].
- The core skill is analysing and decomposing problems [28:57].
- He does not write code by hand any more and uses a precise, prescriptive form of natural language
  [11:19] (also R-REV [10:18]).
- His forward claim: the AI is like a compiler and "as long as we get the results, who cares about
  the implementation?" [30:01]. He names an open-source project demonstrating the approach; the
  caption renders it `NYSE`, which I cannot resolve [31:03].

### (f) Every measured result or number given

Most are self-reported by speakers about their own projects; only EVAL describes a study, and that
transcript is badly garbled.

LOPO and OAI-HE: listed under (a).

STACK (self-reported, five-person company):
- Started from a blank board on 25 January 2026; about four months of work at the talk [03:02]-[04:03].
- Last 30 days: 295 issues opened, 217 shipped, 81 closed as duplicate or won't-do [18:26]. These
  do not sum (217 + 81 = 298); the transcript does not explain it.
- Median time to triage 4.6 elapsed hours; triage to shipped 1.6 (caption `Ayers`, presumably
  hours; unsure) [18:26].
- Cost: a 200-dollar Claude Code Max plan each plus 1,500 to 2,000 dollars a month for CI review;
  he rounds to 3,000 dollars a month [18:26].
- Plan and adversarial review loop capped at five rounds [12:16]; five merge gates [15:22]; five
  agents running on his laptop during the talk [28:40]; a lost session costs about ten minutes
  [26:36]; no context clear needed for about two months because each issue gets a new worktree
  [20:30]. He cites a supply-chain incident affecting 364 npm packages [10:12].

CORM (self-reported, solo):
- 350,000 lines of Rust [02:04]; comparable systems take two years to a decade [01:02].
- Per-file coverage between 75% and 100% (caption wording is muddled) [06:09]; 1,500 tests against
  S3 [06:09]; "I currently have 5000 tests that run in two minutes" [14:32].
- Two repeatable HTTP 500 errors found in S3 itself [10:21]-[11:23].
- About three quarters of security-review findings valid [22:40].
- One refactoring week of plus 120,000 and minus 75,000 lines; one 43,000-line file had to be split
  [24:44]. Others told him agents fail past 100,000 lines; his project contradicts that [02:04].

AZRI: managers report three to five times more PRs waiting [02:04]; tickets with 10 to 12, sometimes
20 requirements, some consistently skipped by a single verifier [10:22]; 12 to 15 parallel
subagents [12:28]; about six months to a working spec reviewer [17:34]; runs dozens of times per PR
[18:37]; aim the agent at "the 1 or 5% in the product that matters most" [28:54].

MART: 500 microservices at one insurer [17:27]; team per self-contained system reduced from 5 to 7
people to 1 or 2 [21:37]; 1.5 minutes for the demo use case [22:39]; two weeks of spec to five
minutes of generation [26:47]; six customers on the process [09:14]; two requirements engineers to
one developer on a proof of concept [26:47].

BOCK: 80% of her commits in 15 years went straight to main [20:37]; drift reviews about weekly
[21:39]; Amazon's reported 400 to 500 developer-years saved on Java upgrades, mostly codemods given
to AI [18:35]; about 250 messages a week (median) in an internal chat during spikes [27:49]; 41
files touched by one change [29:54]; 12 cents per 100 lines (2024 claim) versus 500 dollars a day
and over 100,000 dollars a year [30:56]; about half the conference talks were on harness features
[13:31].

EVAL (study, garbled):
- "we currently have roughly 150,000 engineers" in the Stanford study, companies committing to one
  year [04:08].
- Method: an expert panel estimates implementation time and rates maintainability per change;
  panels agree highly; a model replicates the panel at scale [05:09]-[06:09].
- 46 teams compared over time; a gap between AI-using and other teams growing from about 5% to up
  to 60% (the years in the caption are corrupted) [07:10]-[08:14]. The teams he calls laggards
  show no meaningful change in output [09:16] (sentence partly garbled).
- Rank stability of individual performance: "The pivoted was 0.70." then "it dropped to 0.45"
  [10:22]; meaning, who the top performers are has reshuffled.
- Adoption levels L1 to L4: repositories that adopt agents with no harness, tooling or instruction
  files show volume changes without quality gains; at L2 and L3 all analysed metrics improve
  [13:37]-[14:40] (details unreadable).
- Skill evals: "we've got 500 skills. We have 1000 tasks." and 19 model and harness permutations
  [16:47].
- "we see 55% following the instructions of skill. Even when the skill is not present" [17:47]:
  much skill content is already in the model, so it costs tokens for nothing. A with-skill figure
  is given but unreadable (`1,993%`).
- Skills help most where conventions are local or newer than training data (style conventions,
  security and compliance, infrastructure); less for generic data processing and testing
  [21:58]-[23:00]. Example: a registry's newer token-less publishing method that models do not know
  [19:52]-[20:55] (names garbled).
- Changing the harness around a fixed model moves scores a lot (caption says 200%; garbled) [24:00].
- A figure of 1.2% of budget for skill descriptions is mentioned [24:00]; context unreadable.

WALT: example findings of 30 to 40% improvement from a small change [23:44]; an endpoint with P90
near 100 ms that occasionally took 45 seconds [23:44]; an N+1 query present for six years in a
15-year-old codebase [19:38]-[20:42]; a batch of about 80 auto-opened PRs nobody reviewed [21:42]; target
state of 80% of fixes merged unchanged before trusting full automation [28:51].

KUSH: chat contexts of 1K to 4K tokens versus tens to hundreds of thousands for agents [02:02];
"one user message can lead to 20 to 40 tool calls" [04:05]; speculative decoding roughly 3x
generation speed [10:15]; with one second of tool time per one second of model time a GPU supports
about twice the users [19:34].

FARL: 12,000 lines of code a day from one multi-agent user [18:37].

Recaps: a 7,000-line PR as the unit nobody can review (R-VER [07:07]); 30 seconds to generate a
drive-by fix versus maintainer review time, ten subagents producing ten PRs in a minute (R-REV
[01:01]-[02:03]); ten agents of 1,000 turns each with little achieved (R-REV [07:13]).

### Contradictions and open questions

- 100% coverage. LOPO requires it and uses it to shape code [20:32]-[21:35]. CORM tried it and
  dropped it as a poor use of time that yields trivial tests [05:08]. Inference: they agree it is
  not a correctness proof; they differ on whether the structural pressure is worth the noise.
- LLM judges as merge gates. LOPO, OAI-HE and STACK gate or auto-merge on reviewer agents. BOCK
  says keep inferential sensors out of the CI red/green state [21:39].
- Shift left or right. LOPO starts with interventions "as far right in the process as I can"
  [11:19] to save his own time and moves them left only when a pattern recurs. BOCK says run
  sensors as early as cost allows [20:37]. A questioner challenged Lopopolo on this [26:46].
- Flaky tests. CORM: "never have flaky tests with AI is my hard rule" [13:28]. OAI-HE: "Test flakes
  are often addressed with follow-up runs rather than blocking progress indefinitely." (Throughput
  changes the merge philosophy).
- Does the code matter. FARL [30:01] and STACK [01:01] say stop caring about the code if behaviour
  is verified. Kerr (R-REV [05:07]), BOCK [29:54], [37:02] and an audience member at AZRI [29:56]
  say understanding and changeability still matter. CORM does not read the code but inspects
  interface types between modules and refactors heavily [22:40].
- AI-written tests. FARL calls them mostly a dumb idea when derived from code. CORM leans on
  agent-written tests anchored to an external oracle. AZRI distrusts unit tests in general. Meta
  adds a judge for test quality.
- Plan and task phases. MART skips them and goes spec to code through skills. STACK and AZRI rely
  on an explicit planning stage with separate review.
- Pull requests. MART and BOCK commit to trunk; STACK automates PR gates; WALT found automated PRs
  ignored; STACK refuses all external PRs and all hand-written code on supply-chain grounds
  [06:07], [09:11].
- Instruction file style. Map plus operating steps (LOPO, OAI-HE), terse hard constraints (STACK),
  near-empty pointer file (MART). No one advocates a long file. CORM shows rules in the file being
  ignored.
- Regenerate or patch. The R-SDD narration and FARL's compiler analogy imply disposable code; MART
  patches existing code so diffs stay reviewable.
- Open: how architectural coherence holds over years in agent-built code (OAI-HE, What we are still
  learning); how to keep external product and design context in sync (SLOAN); whether review
  throughput can ever match generation (BOCK, FARL); STACK admits a honeymoon period [29:44].
- Scale caveat for a solo developer. Inference: LOPO, OAI-HE and STACK describe team-funded
  pipelines (matrix reviewer jobs, nightly mining, thousands of dollars of CI review). CORM is the
  only solo large-project account, and he chose to stay in the loop rather than automate review.

## Per source

### Harness Engineering: How to Build Software When Humans Steer and Agents Execute (Ryan Lopopolo, OpenAI, June 2026)
File: refs/videos/c8bE0cj7vHY/transcript.md   URL: https://www.youtube.com/watch?v=c8bE0cj7vHY
Thesis: Code production is no longer the constraint; human time, human and model attention, and the
context window are. The engineer's job is to write down what good means and arrange for it to reach
the agent at the right moment, converting every piece of feedback into a static guardrail.
Practices:
- Re-evaluate the whole workflow with each model release: "completely retooling your stack and the
  way you work with every point release of the model" [03:07].
- Three scarce resources: human time, attention, context window [05:08]-[06:09]. Remove your
  synchronous attention to go parallel; accept more and smaller PRs.
- Plan for compaction: context is repeatedly emptied and refilled, so resurface key context through
  tools instead of relying on the opening prompt [07:09], [17:25].
- Agent file holds a numbered operating loop and a map, not rules [15:22], [18:27].
- Per-area guardrail files written as review personas (backend, design system and so on); the agent
  file says which apply to which kind of change, and agents page them in themselves [19:28],
  [26:46]-[27:47].
- Lints and tests designed for agents: assume truncated output, give descriptive errors pointing to
  runbooks [16:22].
- Coarse structural rules: file line counts, snapshot test per React component with 100% branch
  coverage, ban on `any` and `unknown` outside input parsing [20:32]-[21:35].
- Vibe-code throwaway guardrail tooling freely; its code quality does not matter [17:25], [25:45].
- Classify the change (prototype or production feature needing staged rollout and flags) and give
  the agent runbooks per class [13:21].
- Turn a Slack thread about a fix into a guardrail by asking the agent in-thread to open a PR adding
  it [19:28].
- Require proof of work; record reproduction videos [22:39].
- Reviewer agents run as a CI matrix over markdown persona files; implementer and reviewers iterate
  on the PR until satisfied; human asks only for P2 and above [23:41].
- Watch which review comments recur and move those checks earlier [23:41].
- Mine all feedback nightly with subagents [24:44].
Evidence and numbers: about three concurrent sessions; tasks of 6, 12, 36 hours; tasks spanning 15
context windows lose guardrail context. No repo-scale numbers in the talk (see OAI-HE).
Tools and files named: Codex CLI, Codex app (automations), ESLint, React Suspense, ffmpeg, a
headless X display in Docker (caption `X corks`; unsure), GPT-5.2 and Opus 4.5 as the December
inflection, his open-source crate `artichoke-rand-mt` as the place he is starting to apply this.
Caveats: his approach depends on agents reliably discovering the right guardrail files; he says so
[27:47]. He has not yet put reviewer agents on his open-source work [28:50]. The OpenAI setup is
not shown; no public end-to-end example exists beyond that crate.
Relevance: high. The clearest statement of the guardrail ladder and of what goes in the root file.

### Harness engineering: leveraging Codex in an agent-first world (OpenAI, undated; about early 2026 by inference) [supplementary, not in the batch]
File: refs/articles/openai.com/index-harness-engineering/article.md   URL: https://openai.com/index/harness-engineering/
Thesis: A team shipped an internal product with no hand-written code by investing in repository
legibility, mechanical enforcement of architecture, and feedback loops. The root file is a table of
contents; the `docs/` tree is the system of record.
Practices (section headings as locators):
- Root file as map, about 100 lines; structured `docs/` with design docs, architecture map, quality
  grades, checked-in execution plans and tech-debt list (We made repository knowledge the system of
  record).
- Linters and CI validate the docs; a doc-gardening agent repairs stale docs (same section).
- Anything not in the repo does not exist for the agent; move Slack decisions into the repo (Agent
  legibility is the goal).
- Fixed layer order per domain enforced by custom lints and structural tests; lint messages carry
  remediation text (Enforcing architecture and taste).
- Enforce invariants, not implementations; parse data at boundaries (same section).
- App bootable per worktree; browser automation and an ephemeral observability stack per worktree
  (Increasing application legibility).
- Agent reviews its own change, requests agent reviews, loops until reviewers are satisfied; the
  article calls this a Ralph Wiggum loop (Redefining the role of the engineer).
- Golden principles plus scheduled cleanup agents (Entropy and garbage collection).
Evidence and numbers: listed under (a).
Tools and files named: Codex CLI, GPT-5, AGENTS.md, `docs/`, Chrome DevTools Protocol, LogQL,
PromQL, OpenTelemetry, Zod, gh.
Caveats: the article says the end-to-end autonomy depends on this repository's investment and
should not be assumed to generalise. Minimal merge gates and rerunning flaky tests are described as
right only at very high throughput. Long-term coherence is unknown. The directory-tree figure is
missing from the saved text.
Relevance: high. Supplies the layout and numbers the talk omits.

### Harness engineering beyond code: product and design constraints for agents (Marc Sloan, Tessl, June 2026)
File: refs/videos/tf6VNGH3tRk/transcript.md   URL: https://www.youtube.com/watch?v=tf6VNGH3tRk
Thesis: Agents can pass every harness check and still build the wrong thing because product and
design context lives in external tools and drifts from the code. The harness has to account for
that context, and nobody has a settled answer.
Practices:
- Recognise the failure: the agent treated a Figma design as a picture ("It used the Figma design as
  a visual treatment" [06:17]) and missed the design-system component.
- Bring design-system components into the repo with documentation (his example uses Storybook) so
  the agent picks the right one [08:22]; expect it to go stale again.
- Treat live MCP connections to external tools as a cost: rate limits, spend, availability, and
  evals that depend on changing data [10:26]-[11:28].
- Skills written by non-developers outside the repo are unversioned and invisible to the harness;
  bring them in [20:38]-[21:41].
- Context must also flow the other way: a PM driving agents alone shipped an export feature that an
  old architectural decision had deliberately hidden for cost reasons [21:41]-[22:41].
- For how much context to add: shrink to signal, store as skills, and "we need a set of evals to
  make sure that our agent is actually being boosted by that context and isn't being overwhelmed"
  [26:54].
Evidence and numbers: none measured. Draws on his time on Figma Dev Mode, the Figma MCP server and
Code Connect.
Tools and files named: Tessl, Figma (Dev Mode, MCP server, Code Connect), Linear, Notion, Storybook,
Granola, Claude Cowork.
Caveats: vendor talk; the three or four future directions are speculation. Vendors protect their
data and rate-limit access [16:34].
Relevance: medium. A solo developer is their own PM and designer, so the lesson is to keep design
tokens, component docs and decisions in the repo.

### State of Play: AI Coding Assistants (Birgitta Böckeler, Thoughtworks, June 2026)
File: refs/videos/tFffUnSq7VA/transcript.md   URL: https://www.youtube.com/watch?v=tFffUnSq7VA
Thesis: The useful way to see the field is model, coding harness, and the user's own context
engineering on top, organised as guides and sensors that are either inferential or computational.
Capability has grown, and so have real costs; supervision should follow a risk assessment, and
developers should choose deliberately what they surrender.
Practices: see (d). Additional points:
- Reflect on task type and blast radius before choosing model power [06:15].
- Visualise which files a session reads and writes to gauge blast radius [10:24].
- Replace a rarely-needed AGENTS.md rule (her example: use the custom structured logger, not
  console.log) with a lint rule whose message points to the logger [19:36].
- Enforce module layering with an import-scanning tool and agent-written rules [19:36]-[20:37].
- Do not launch a long unattended run when you do not yet know what you want [36:01].
Evidence and numbers: listed under (f).
Tools and files named: AGENTS.md, CLAUDE.md, Claude Code, Cursor, OpenAI Codex, OpenCode, pi,
OpenRewrite, Gastown, OpenClaw, DORA report, Pragmatic Engineer newsletter; people: Mitchell
Hashimoto, James Lewis, Gene Kim, Andrej Karpathy.
Caveats: she finds the term harness engineering clunky and ambiguous [14:32]. She expects autonomy
never to cover every task and situation [33:58]. Swarms are experimental.
Relevance: high. Gives the vocabulary (guides, sensors, inferential, computational) and the
placement rules for checks.

### Lessons from Spec-driven Development (Simon Martinelli, June 2026)
File: refs/videos/odbNXv9xXjc/transcript.md   URL: https://www.youtube.com/watch?v=odbNXv9xXjc
Thesis: For business applications, use cases plus an entity model are a spec both stakeholders and
agents understand; with stack-specific skills, code can be generated directly from them without a
plan and task phase. Specs need a harness around them, and the effort moves to requirements work.
Practices:
- Spec format: use case with actor, preconditions, main and alternative flows, postconditions;
  entity model derived from the data model; a use case diagram to find module boundaries
  [12:20]-[15:25], [27:54].
- "the skill must match the outcome" [09:14]: skills encode how code and tests are generated for a
  given stack; iterate on them and share them.
- Two skill levels: specification skills and stack skills [16:26].
- Test order: test-first for APIs; for UI work, build the UI first because the tests depend on its
  shape [07:11].
- Never let the agent scaffold the project; use the framework initializer [22:39].
- Small instruction file with pointers to architecture guidelines; MCP vector search for large
  in-house framework docs because skills should stay small [23:41].
- Architecture for agents: self-contained systems (vertical slices with UI, logic and database in
  one repo), not hundreds of microservices and not one huge monolith; one language stack halves the
  skill maintenance [18:28]-[20:37].
- Review by risk; trunk-based with paired review: "we do trunk based development and we do kind of
  an ongoing review process" [24:42].
- Change flow: edit the use case, rerun implement on existing code [30:00].
Evidence and numbers: listed under (f). All anecdotal from consulting engagements.
Tools and files named: Windsurf, Claude Code, CLAUDE.md, AGENTS.md, AI Unified Process (his method
and site), Amazon Kiro, GitHub Spec Kit, a method the caption renders `BMT method` (probably BMAD;
unsure), Spring Initializr, Spring PetClinic, a Java web framework the caption renders `voting`
(probably Vaadin; unsure), Quarkus (caption `quarks`), arc42, Figma MCP.
Caveats: skill distribution across different agents in one organisation is an open problem
[15:25]. Developer-centric spec tools do not cover the whole lifecycle in his view [03:05]. The
gain is only in the coding phase; requirements still take weeks.
Relevance: high. A working spec format, the rerun-on-change sync rule, and the scaffold rule apply
directly to solo full-stack work.

### Executable Specs: Building a Verification Layer for Agentic Coding (Shachar Azriel, Baz, June 2026)
File: refs/videos/aWrGSM5vVyc/transcript.md   URL: https://www.youtube.com/watch?v=aWrGSM5vVyc
Thesis: Coding agents generate features but do not verify them against the spec. A separate
spec-reviewer that extracts each requirement and checks it in the deployed preview closes that gap,
but only after substantial context engineering.
Practices (the build sequence and what each failure taught):
- One agent doing extraction and verification blew the context window [08:17].
- Planner plus one verifier ran but skipped requirements and gave inconsistent quality; by the
  fifth or sixth requirement accumulated context "makes the agent just dumber" [11:24].
- One subagent per requirement in parallel, with an orchestrator collecting verdicts [12:28].
- Spec-only input led to invented requirements; add the code, and specifically the base branch
  rather than the diff, and scope to the affected area [13:28]-[14:29].
- Opening unknown preview URLs from the agent host is like clicking phishing links; run each check
  in an ephemeral sandbox and "prefer using a third party tool instead of developing yourself"
  [16:33] for security-sensitive parts.
- Large model for extraction (specs are inconsistent), small models for click-and-check
  verification [26:47].
- Maintain a list of critical flows verified on every PR [22:42]; do not try to cover the whole
  product [28:54].
Evidence and numbers: listed under (f). Vendor's own account; no accuracy figures given.
Tools and files named: Baz Spec Reviewer, AWS Agent Core (sandbox with browser session), Jira,
Linear, Monday, Notion, GitHub; an audience member mentions Playwright MCP.
Caveats: product pitch. His dismissal of tests ("The problem that I have with tests is that they
test things that nobody really like." [23:43]) is opinion and conflicts with FARL and CORM. An
audience question on spaghetti code went unanswered for lack of time [29:56].
Relevance: high. The planner plus per-criterion subagent pattern and the base-branch finding are
directly reusable for an acceptance-criteria reviewer.

### When Tests Lie: Using Observability to Keep AI Honest (Justin Cormack, June 2026)
File: refs/videos/xHxfeWtkXrM/transcript.md   URL: https://www.youtube.com/watch?v=xHxfeWtkXrM
Thesis: On a large agent-written system, tests are discovery tools, not proof. Quality comes from
an external oracle, many kinds of fast tests, traces the agent can read, types that make errors
impossible, whole-codebase security review, regular refactoring, and a human who stays in the loop.
Practices:
- Do not chase 100% coverage [05:08].
- Use an existing system or a trivial reference implementation as oracle; keep it outside the repo
  so it cannot mirror the code [07:11], [30:55].
- Trust observed behaviour over documentation [09:16]. The agent was poor at finding edge cases
  from docs; the human did that better [11:23].
- Zero tolerance for flaky tests; fix the test before touching code [13:28].
- Keep the suite fast and run it often, including overnight repeated runs to surface rare failures
  [14:32].
- After fixing bugs, ask what kind of test would have caught them; fuzz and property tests paid off
  [15:32].
- Build more testable interfaces; he regrets not building management and reporting interfaces
  earlier [17:35].
- Have the agent build a simple tracing framework and hand it traces for debugging [18:37].
- Performance work is trial and error: "just say no, throw that one away and try something else"
  [20:37].
- Fix classes of bugs in the type system [21:40].
- Commit security findings to the repo, have the agent triage, then derive tests [22:40].
- Schedule refactoring weeks [24:44].
- "Tests are really discovery tools." [25:47]: add tests where you are suspicious.
Evidence and numbers: listed under (f).
Tools and files named: Rust, Amazon S3, MinIO (caption `Mineo`), Codex Security, agents.md.
Caveats: single-author project, not yet released at the time; distributed parts unfinished; formal
verification not yet tried [27:53]. The oracle needed retries and interpretation because S3 is
eventually consistent [07:11].
Relevance: high. The only solo large-codebase account in the batch, with concrete test practices.

### Vibe Coding: Is this really the best we can do? (Dave Farley, June 2026)
File: refs/videos/libNzUdL9eM/transcript.md   URL: https://www.youtube.com/watch?v=libNzUdL9eM
Thesis: Natural-language prompting lacks the precision, determinism and reproducibility that make
programming an engineering discipline. The durable answer is executable specifications in a domain
language, verified in a pipeline, built incrementally.
Practices: see (e).
Evidence and numbers: one anecdote (12,000 lines a day). No measurements.
Tools and files named: BDD, continuous delivery, deployment pipeline, an open-source project the
caption renders `NYSE` (unresolved).
Caveats: argument from experience, no data. His who-cares-about-the-code conclusion is contested by
other speakers. He says earlier assistants were less repeatable than current ones [12:20].
Relevance: high for principles (specify goals yourself, hold back tests, small steps); medium for
tooling detail, since no concrete DSL or file layout is shown in the transcript.

### The Humans Architect the System, the AI Writes the Code (Paul Stack, June 2026)
File: refs/videos/wuGJNWhUOoE/transcript.md   URL: https://www.youtube.com/watch?v=wuGJNWhUOoE
Thesis: A five-person company bans hand-written code and runs every change through a
skill-plus-CLI state machine: triage, plan with adversarial review, human approval, implement,
multi-gate review, auto-merge, then black-box UAT before release. Humans own architecture and
constraints.
Practices:
- Workflow as "a state machine inside a skill and a CLI" [12:16]: triage, classify, plan and
  adversarial review loop (max five), human approval, implement, reproduce or verify, PR, reviews,
  release, notify requester. "Our skill is backed by a CLI." [11:16].
- CLAUDE.md as short hard constraints plus a self-update instruction [13:20]-[14:21].
- Five merge gates including a skill-content check, because the product is agent-driven [15:22].
- UAT in a separate repo against the shipped binary; never edit tests to pass [14:21]-[18:26].
- Adversarial tests modelled on real user misbehaviour; bugs feed back into them [15:22].
- One worktree per issue; fresh context each time [20:30].
- Human decides what gets triaged: "I don't run autonomous agents that sit and triage every issue
  coming in." [25:36], citing injection risk.
- When agents deadlock, query the structured plan and review records to see the disagreement; if
  unclear, kill and restart [26:36].
- Starting advice: write down the constraints an agent cannot learn from the source, run one loop
  end to end, add the next constraint where it breaks [20:30]-[21:33].
- No external PRs accepted, to protect the supply chain [09:11].
Evidence and numbers: listed under (f). Self-reported.
Tools and files named: Claude Code, CLAUDE.md (caption `our MD`), Claude worktrees, a product the
caption calls `swamp` and a company it renders `Elder Swamp Club` (spellings unsure), AGPL v3. He
mentions a Mitchell Hashimoto tool the caption renders `voyage` (unsure), and incidents involving
Trivy and an npm worm.
Caveats: he calls this a honeymoon period and expects to redesign several times [29:44]-[30:44]. Four
months of history on a greenfield CLI product. Quality claims are his own.
Relevance: high. A concrete pipeline a very small team runs on Claude Code, with costs.

### Why evals are hard and how we're solving it (Simon Obstbaum, Stanford; Rob Willoughby, Tessl; June 2026)
File: refs/videos/4d3-Zrmf9Wo/transcript.md   URL: https://www.youtube.com/watch?v=4d3-Zrmf9Wo
Thesis (as far as legible): Large-scale repository data shows a widening gap between teams and
individuals who structure their agent use and those who do not; at the level of one skill, evals
should measure activation, trajectory and outcome, and skills pay off mainly where conventions are
local or absent from training data.
Practices:
- Agent adoption without instructions, skills or tooling does not improve quality metrics;
  structure does [13:37]-[14:40].
- Do not spend skill tokens on what the model already does: "investing in structure where the
  conventions are local importance for business, that's where the value is" [23:00].
- Evaluate model and harness together; results change with the harness [24:00].
Evidence and numbers: listed under (f).
Tools and files named: Stanford software engineering productivity study, Tessl registry; a paper
submitted to the IEEE Automated Software Engineering conference [12:33].
Caveats: transcript quality is too poor to rely on any figure beyond those quoted. The study's
control group disappeared as everyone adopted AI and the method had to change [07:10]-[08:14].
Correlational.
Relevance: medium. Supports two design rules (structure matters; skills should hold local
knowledge), but treat the numbers as unverified.

### Benchmarking the Agent Era: Measuring Performance Beyond the LLM (Amit Kushwaha, NVIDIA, June 2026)
File: refs/videos/guhTp2Q8VX0/transcript.md   URL: https://www.youtube.com/watch?v=guhTp2Q8VX0
Thesis: Inference benchmarks built for single-turn chat misrepresent agent workloads, which are
long multi-turn trajectories dominated by cached input, tool time on CPU and tail latency.
Practices: prefix caching is essential ("caching becomes kind of a must have" [06:10]); route turns
to the replica holding the cache; judge by percentile distributions after warm-up, not means.
Evidence and numbers: listed under (f).
Relevance: low. Serving-infrastructure topic. One takeaway for a setup: keep the prompt prefix
stable so provider caching works (Inference from [05:06]-[06:10]).

### From Blind Spots to Merged PRs: Runtime Intelligence for Continuous Agentic Performance (May Walter, Hud, June 2026)
File: refs/videos/-6SNbcE3C9o/transcript.md   URL: https://www.youtube.com/watch?v=-6SNbcE3C9o
Thesis: Agents lack runtime and business context, so their fixes are plausible but unverified.
Give them function-level production data and investigation skills, run the investigation on a
schedule, and hand humans a short scored list instead of a pile of PRs.
Practices:
- Automate the investigation, not the fix, so prioritisation becomes cheap [06:16].
- Requirements for a scheduled agent workflow: vendor-neutral compute, harness and model; scoped
  permissions and tools; webhook and schedule triggers; easy to edit, since workflows are code that
  keeps changing [08:22]-[09:23].
- Bridge the vocabulary gap between endpoint-level telemetry and function-level code with a
  production-to-code mapping [16:30]-[17:34].
- Layering: query language, then skills for known investigation methods, then automations
  [18:34]-[19:38]. Tools alone are not enough; give the method.
- Tell the agent what a real fix looks like, to stop the lazy fix [13:27]-[14:27].
- Score by hot path, business impact and risk; seek high-impact, low-risk changes [22:43].
- Output a human-readable finding with options (dig deeper, ticket, PR), labelled for measurement
  [23:44]. "we actually need to convince the human that it's worth the attention" [22:43].
- "It is better to do less but the right things." [26:46]: one wrong suggestion costs trust.
Evidence and numbers: listed under (f). Customer anecdotes, no aggregate results.
Tools and files named: Hud (sensor and MCP server), GitHub Agentic Workflows, GitHub Actions,
Claude Code, Slack, ClickHouse, Datadog, Sentry.
Caveats: vendor talk. Full auto-merge is a stated aspiration, not achieved.
Relevance: medium. The scheduled, report-first pattern and the layering of skills over data are
reusable; the sensor itself is a commercial product.

### Spec-Driven Development: Specs Are the Program Now (AI Native Dev recap, after June 2026)
File: refs/videos/606n8YC_-fU/transcript.md   URL: https://www.youtube.com/watch?v=606n8YC_-fU
Thesis: A narrated compilation of clips from Martinelli, Farley and Azriel, framed as specs being
the maintained artifact and code a regenerable output. No new material beyond the full talks.
Caveats: the framing overstates Martinelli, who patches existing code (MART [30:00]).
Relevance: low. Duplicate content; useful only for cleaner captions of the three clips.

### Baz, Docker and Meta on Verifying Agent Code (AI Native Dev recap, after June 2026)
File: refs/videos/DFDyRt4cU1Q/transcript.md   URL: https://www.youtube.com/watch?v=DFDyRt4cU1Q
Thesis: Clips arguing that proving code does what was asked is the hard part. Azriel and Cormack
clips repeat their talks; two clips are from talks outside this batch.
Practices (new material only):
- Ian Thomas, Meta: teams' top worry was whether the code can be trusted; a second AI tool on CI
  judges AI-written tests for value, started in one org and rolled out company-wide [05:06]-[06:07].
- Christopher Batey: system-level decisions go in a separate ADR pull request that a human reviews
  in depth with diagrams; agents then check implementations and all later PRs against the ADRs
  [07:07]-[09:12].
Evidence and numbers: a 7,000-line PR example; no measurements.
Caveats: agents left alone bloat ADRs until unreadable [08:08]. Clips are short excerpts.
Relevance: medium. The ADR-first rule and continuous ADR conformance review fit a solo setup.

### Google, McKinsey and Dave Farley on AI Code Review (AI Native Dev recap, after June 2026)
File: refs/videos/fwL31sNbq8g/transcript.md   URL: https://www.youtube.com/watch?v=fwL31sNbq8g
Thesis: Clips on what happens to review and trust when generating a change is far cheaper than
reading it. The Farley clip repeats his talk; three clips are from talks outside this batch.
Practices (new material only):
- Jack Wotherspoon, Google: drive-by agent PRs ("that takes like 30 seconds on your end" [01:01])
  shift cost to maintainers; at Google agents review first and a human still reviews every PR;
  authors often cannot explain design choices [01:01]-[03:04].
- Dave Kerr, McKinsey: fast generation makes the author's mental model, the system and colleagues'
  models diverge; review exists to resynchronise them. Also compress agent output before passing
  it to people [04:06]-[05:07].
- Brian Douglas: long unattended runs can report progress while achieving little; log every
  session to a database (his tool, Tapes; SQLite then Postgres) and have the agent write
  observation notes in a memory folder, an idea he credits to a Mastra post [06:08]-[07:13].
Evidence and numbers: ten agents at 1,000 turns each; no measurements.
Relevance: medium. Supports keeping a human-readable summary and session observations; the
open-source maintainer issues matter less for private solo work.
