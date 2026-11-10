# AI Native DevCon London (June 2026), batch 3: teams, organisations, brownfield, repository automation, cost

Sources read: 15 of 15, each from first line to last (11 full talks, 4 short compilation clips).
None failed to open. Two passages are too garbled by captions to use: the first four minutes of
the panel (PANEL [01:01]-[04:06], speaker introductions and Pini Reznik's opening answer) and the
Stanford segment of CLIP-SCALE ([03:01]-[04:02]). Nothing in them is relied on below except where
flagged.

All sources are YouTube caption transcripts with no speaker labels. Talk dates: AI Native DevCon,
London, June 2026 (exact day not in the files). The four clips were published after the event
(they open with `Back in June`) and before the November 2026 New York event they advertise.
Quotes are copied verbatim including caption errors; where a caption error changes a word, the
likely intended word is given after the quote and marked as my reading.

Source keys:

| Key | Speaker / content | File |
| --- | --- | --- |
| THOMAS | Ian Thomas, Meta (Horizon / Reality Labs) | refs/videos/NVzKtCSeoRA/transcript.md |
| ROBERTS | Katie Roberts, Nearform | refs/videos/5SKh-FmjX7U/transcript.md |
| SYME | Don Syme, GitHub Next | refs/videos/kbvqRWY-bUs/transcript.md |
| FOXWELL | Hannah Foxwell, independent | refs/videos/pyYKOLEnsZk/transcript.md |
| BATEY | Christopher Batey, CTO of a platform-engineering consultancy (caption: `Core Engineering Consulting Group`, spelling unsure) | refs/videos/tJUAef_dBtU/transcript.md |
| ODEVO | Daniel Jones (re:cinq) and Tomasz Maj (Odevo) | refs/videos/mB74LGAmmV0/transcript.md |
| DUBNOV | Tammuz Dubnov, AutonomyAI (vendor) | refs/videos/KzhjnILSP0Y/transcript.md |
| PANEL | Stephane Jourdan, Simon Rohrer, Pini Reznik (panel) | refs/videos/1grkxo4cyKY/transcript.md |
| LAWSON | Dana Lawson, CTO Netlify | refs/videos/ItTJpQz35CY/transcript.md |
| WOTHERSPOON | Jack Wotherspoon, Google (Gemini CLI) | refs/videos/HgA0spItnZI/transcript.md |
| DOUGLAS | Brian Douglas, Paper Compute (tapes.dev) | refs/videos/o-IunU6b1t8/transcript.md |
| CLIP-SCALE | Clip: Thomas, Stanford researchers, Odevo, Foxwell | refs/videos/jfTltMo0TMg/transcript.md |
| CLIP-BROWNFIELD | Clip: Roberts, Simon Martinelli, Batey, Thomas | refs/videos/UVOkQyeY16M/transcript.md |
| CLIP-PRODUCT | Clip: Marc Sloan (Tessl), Dubnov, Lawson, Emma Burrows | refs/videos/G5mAl_QBr4w/transcript.md |
| CLIP-COST | Clip: Amit Kushwaha (Nvidia), Dubnov, Luke Marsden (Helix ML), John Groetzinger (Cisco) | refs/videos/nnja7kk4EPM/transcript.md |

## Cross-cutting findings

### Recurring practices

1. Agents amplify whatever engineering baseline a repo already has, so fix tests, CI, linting and
   written standards before adding autonomy. ODEVO [10:26], [11:26]-[13:28] (citing the 2025 DORA
   report); BATEY [08:18]; PANEL [17:24]-[19:26]; ROBERTS [18:30]; DUBNOV [23:52] (agents copy a
   repo's habits, including not writing tests).
2. Deterministic checks are the first guardrail, ahead of any model-based review: linters, custom
   linters, static analysis (SonarQube), code-health tools, a fast test suite. PANEL [09:13];
   ROBERTS [18:30]; BATEY [28:47] (15 minutes maximum for the full suite); ODEVO [12:27].
3. Every observed agent mistake becomes a permanent, preferably deterministic, check in the
   harness. PANEL [17:24] and DUBNOV [12:25] both appear to credit Mitchell Hashimoto for this
   definition (name garbled in both captions, my reading); SYME [31:06] says the same in factory
   terms (add a quality gate
   rather than fix items by hand).
4. Keep instruction files short. ODEVO [19:41] teaches that stuffing every scenario into AGENTS.md
   has measured negative effects. WOTHERSPOON [15:24] keeps the content to a few lines (run the
   tests, follow the PR template) and [30:47] enables a skill by default only if it would be used
   more than half the time.
5. Check context files and skills into the repo, next to the code, and write for more than one
   harness (AGENTS.md as well as the Claude file, or a symlink). WOTHERSPOON [15:24], [23:37];
   ROBERTS [19:31]; LAWSON [19:33]; DOUGLAS [28:49]-[29:52] (skills are the portable unit across
   harnesses and models).
6. Encode repeatable workflows as skills: PR creation, docs writing, code review, ticket writing,
   planning, a multi-agent developer flow. WOTHERSPOON [15:24]-[16:26]; ROBERTS [20:35],
   [22:38]-[24:43]; THOMAS [21:48] (rules and runbooks that work like skills).
7. Put human attention on the plan, spec or architecture decision, not on every diff. BATEY
   [14:27]-[15:27] (ADR first, as its own PR); FOXWELL [27:47]-[28:47], [32:54]; ROBERTS
   [22:38]-[23:41], [25:43]; ODEVO [26:53]-[27:53]; CLIP-COST [05:09] (Marsden reviews specs);
   PANEL [12:20] (humans decide trade-offs).
8. Small slices, small PRs, one area at a time. ROBERTS [17:30], [25:43]; DUBNOV [24:54] (agent
   tuned to emit few lines and reuse components); BATEY [13:26] (a 7000-change PR is unreviewable
   for systems thinking); WOTHERSPOON [06:09] (a 30,000-line PR `is not going to pass`).
9. Scheduled or event-triggered agents maintain repos, with read-only execution, a narrow output
   channel and a human-reviewed PR or issue as the only exit. SYME [13:28]-[19:38]; THOMAS
   [21:48]-[22:50]; LAWSON [13:24]-[14:25], [20:34]; CLIP-COST [08:14]-[09:15].
10. Use a second, different model as judge of agent output in CI where deterministic checks
    cannot decide (test quality, risk). THOMAS [15:33], [25:55]; DUBNOV [24:54] (PR risk and size
    labels); BATEY [15:27] (agents check every PR against ADRs).
11. Counting activity (tokens, lines, commits, PRs, weekly users) proves nothing; measure merged
    work, untouched-merge rate, and whether the feature is used. THOMAS [27:57]-[28:57]; BATEY
    [08:18], [29:48]; DUBNOV [17:38]-[19:43].
12. Run parallel agents for mechanical work, but only one cognitively hard task at a time per
    person. BATEY [23:36]; PANEL [29:51]-[31:58]; ODEVO [33:01]-[34:03] (compulsion and overtime);
    THOMAS [19:46] (parallel agents for a repeated refactor, human as reviewer).
13. Give agents the missing domain context through a tool (MCP server, structured logs, production
    data) rather than more prose. THOMAS [20:47]-[21:48]; LAWSON [14:25]-[15:25]; PANEL [07:10],
    [15:22].
14. Stay able to switch harness and model provider. BATEY [16:27]-[17:30]; DOUGLAS [29:52];
    CLIP-COST [07:11] (Marsden); PANEL [08:11] (Rohrer's team uses OpenCode).
15. Route routine work to cheaper or local models and keep the frontier model for hard problems.
    DOUGLAS [13:21]; CLIP-COST [06:10]-[07:11]; ODEVO [24:48].
16. In brownfield code, build an evidence map and a prioritised findings backlog before changing
    anything. ROBERTS [15:26]-[18:30], [25:43]; CLIP-BROWNFIELD [02:04]-[04:07] (Martinelli).
17. Mine your own session logs for skills and recurring failures; harness session stores expire.
    DOUGLAS [09:13]-[10:16], [15:24], [21:33]; PANEL [18:25] (reflector agents that write memory
    after an incident).
18. Feature flags and progressive delivery make it safe to merge fast and polish in follow-up PRs.
    FOXWELL [22:39], [26:47]; DUBNOV [21:49]-[22:51]; ROBERTS [10:20]-[11:21].
19. Screenshots or video attached to a PR raise reviewer trust and speed. WOTHERSPOON [17:28]
    (personal Playwright skill); CLIP-COST [06:10] (Marsden).

### (a) Rolling one standard setup out across many repositories and keeping it current

What the sources actually describe (none is a multi-repo solo setup; the closest are SYME, who
personally maintains about seven open-source repos, and WOTHERSPOON, one large public repo):

- Ownership. A small named group owns the shared practice and tooling: Meta's engineering
  excellence group (THOMAS [07:16]-[08:18]); Odevo's dedicated developer-experience team that
  builds `tracking and telemetry and observational tools` (ODEVO [30:59]) plus internal trainers
  (ODEVO [30:59]-[32:00]); at Nearform, skills are split at epic level per feature team with an
  explicit warning that someone must keep them from diverging (ROBERTS [27:46]).
  Inference: for one person this collapses to one canonical source that the developer owns; the
  transferable part is ROBERTS's warning that skills diverge between teams unless someone
  reconciles them (for one person: between repos).
- Distribution.
  - In-repo, checked in: context files plus skills live in each repository (WOTHERSPOON [15:24],
    [16:26], [23:37]; ROBERTS [19:31]). For harness coverage Wotherspoon says to add the generic
    file too: "you should actually add an agent as well" [15:24] (my reading: AGENTS.md) "or
    through a symlink" [15:24].
  - One file per automation, installed per repo: a GitHub Agentic Workflow is one markdown file
    plus its hardened YAML, added with an `add` wizard from a CLI extension (SYME [13:28],
    [16:31]). Other maintainers copy the Repo Assist workflow and customise the task list for
    their repo (SYME [24:51]). Workflows can also run across repositories or a whole organisation
    `with the right permissions` (SYME [15:30]).
  - Central platform: Meta ships shared tools through existing platforms so they reach every
    engineer (THOMAS [23:50]-[24:54]); a tool built in one org (the test-slop judge) was adopted by
    the infrastructure group and rolled out company-wide (THOMAS [15:33]). Meta is a single
    monorepo [06:14], so this does not show how to sync across separate repos.
  - Netlify keeps a `system of record` it calls blueprints: "Think of it as the CLAUDE.md files,
    AGENTS.md, the architecture decision records" (LAWSON [19:33]).
- Keeping it current.
  - Error-driven: each failure is fed back into the harness as a check (PANEL [17:24]; DUBNOV
    [12:25]).
  - Source-of-truth-driven regeneration with evals as the release gate (Cisco, CLIP-COST
    [08:14]-[09:15]): a knowledge-base article change triggers a pipeline; a model classifies the
    change as minor, moderate or major, rewrites the matching skill and runs the evals. Minor
    changes that pass release automatically; major changes or new topics go to a human and need a
    new eval. "If your engineers are reviewing text diffs on a skill, you are wasting a lot of
    time." [09:15]
  - Usage-driven: generate skills from recorded sessions, then use the same session records to see
    how often each skill is invoked and whether it works (DOUGLAS [21:33]).
  - Periodic self-assessment: Meta teams rerun a six-dimension, five-level maturity workshop every
    three to four weeks and post the result (THOMAS [10:22]-[14:33]).
  - Brownfield-specific: add rules stating which existing patterns to copy and which not to, so
    skills do not replicate legacy mistakes (ROBERTS [18:30]-[19:31]).
- Versioning. Only Cisco's pipeline mentions versions (`That new version, just let it
  automatically release`, CLIP-COST [09:15]) and SYME's checked-in workflow files are versioned by
  git. No source describes semantic versions, changelogs, a plugin or a template-sync mechanism for
  pushing one setup to many separate repositories. This is a gap in this batch, not a finding.
- Measuring adoption. Meta: weekly active use (under half to over 80%, later mid to high 90s) and
  community size, then explicitly downgraded to vanity metrics (THOMAS [03:05]-[04:06],
  [27:57]-[28:57]). Odevo: share of a developer's last ten pull requests (caption says `last ten
  years`) that used AI, shown on dashboards visible to all developers (ODEVO [22:44]-[23:47]), plus
  interviews with the 6% non-users. AutonomyAI: PR count per author, merge rate, share merged with
  no developer commits (DUBNOV [17:38]-[19:43]). DOUGLAS: skill invocation counts per session
  [15:24], [20:31].
  Does not transfer: adoption rates, communities, workshops, training programmes and trainers are
  about persuading other people. Inference: the solo analogue is per-repo drift and skill-usage
  telemetry (is the standard file present and current, are skills being invoked), which DOUGLAS and
  the Cisco pipeline support but no source demonstrates across repos.

### (b) Brownfield and legacy code

- What to do first: ask the people who work in the code where it hurts, then point the agent at
  those specific problems instead of the whole repo (ROBERTS [14:26]-[15:26]). For a solo developer
  the `eyewitness` is yourself; the step still means writing the known pain points down first.
- What to document first: what the code does now. "maps of what the code is doing now, not what
  our documentation said the code was doing" (ROBERTS [16:28]), plus dependency graphs. Targeted
  investigations: dead code paths, duplication, pattern inconsistencies, complexity hotspots and a
  light OWASP-style scan that does not replace real security scanning (ROBERTS [15:26]). Output is
  human-readable docs and a version-controlled, prioritised findings backlog (ROBERTS
  [17:30]-[18:30]). All of it needs human review because the model `will confidently hallucinate
  about your code` (ROBERTS [12:23], [16:28]).
- Reverse-engineer the spec: extract use cases and an entity model from code, tests and scattered
  documentation, have the business review them, then generate new code from the reviewed spec
  (Martinelli, CLIP-BROWNFIELD [02:04]-[04:07]). Nearform did the same for product requirements and
  codebase context (ROBERTS [19:31]-[20:35]).
- Record the tribal knowledge: architecture and workflows that live in heads, old chat threads or
  undocumented modules are invisible to agents (LAWSON [16:26], [19:33]). BATEY keeps short,
  human-reviewed ADRs and has agents check every later PR against them [14:27]-[15:27].
- Safety nets before any implementation: tests you trust, logs, static analysis actually running
  and reporting (ROBERTS [18:30]); tests the agent can run (ODEVO [12:27]); linting `turned up to
  11` (PANEL [09:13]); written coding standards (ODEVO [13:28]); a full test run of 15 minutes or
  less per component (BATEY [28:47]).
- Make the repo agent-ready: rules that say which patterns are good and which are legacy (ROBERTS
  [19:31]); structured, machine-readable error output and non-interactive CLIs (LAWSON [15:25],
  [18:31]); a tool that supplies domain data so the agent can work outside the one special machine
  (THOMAS [20:47]-[21:48]).
- Known failure mode without guardrails: agents over-optimise and produce code that passes tests
  while breaking implicit architecture (ROBERTS [13:26]); agents imitate whatever the repo already
  does, good or bad (ROBERTS [18:30]; DUBNOV [22:51]-[23:52]); Meta found agents `hallucinating
  awful tests` that added CI load without value (THOMAS [15:33]).
- Change strategy: pick one of pseudo-greenfield branch, strangler fig, or branch by abstraction
  (interface plus feature flag inside the codebase), each with stated costs; all three fail when
  left half-finished (ROBERTS [06:12]-[12:23]). Work one area at a time (ROBERTS [18:30]).
- Low-risk first targets: test coverage on uncovered files that change often, repeated refactors,
  automated code-quality fixes, internal tooling (THOMAS [05:10], [17:37]-[22:50], [29:59]);
  lint-debt sweeps (DOUGLAS [14:22]).
- Repetition pays: Nearform's AG Grid migration was slow for the first few of about 80 units and
  then sped up as the skill hardened (ROBERTS [24:43]).

### (c) Repository automation (scheduled or event-driven agents)

What runs:

- GitHub Agentic Workflows (SYME; the caption mostly renders the name as `GitHub workflows`):
  markdown with front matter (triggers such as weekly schedule or issue opened/reopened, tools,
  safe outputs) hardened into a GitHub Actions YAML; the engine can be Claude Code, Copilot CLI,
  Gemini CLI or Codex [11:28]-[13:28], [15:30]. Named uses: issue triage, weekly report, continuous
  documentation, code simplification and refactoring (splitting large files), test improvement,
  performance engineering, accessibility walkthroughs of the running app, fault analysis from
  production probes, CI-time reduction, N+1 query clean-up [07:21]-[09:25], [20:43]-[21:46],
  [30:05]-[32:09].
- Repo Assist (SYME [22:48]-[23:50]): one workflow, run about once a day, that reads its memory,
  picks a couple of tasks from a maintainer-editable list (triage, comment on issues, propose
  improvements, manage labels) and opens issues or PRs. Syme contrasts this single multi-task
  workflow, which he prefers, with a colleague's `agent zoo` of hundreds of single-purpose workflows
  [19:38]-[21:46].
- Meta (THOMAS): an automated code-fix loop driven by rules and runbooks ("find a thing, fix it,
  promote a diff, get someone to review it" [22:50]); a CI judge for AI-written tests using a
  different AI tool [15:33]; maintenance-mode agents that review diffs against known criteria and
  look for approval signals [25:55]; a risk score on every diff (tool name garbled as `doctors`)
  [25:55].
- Netlify (LAWSON [13:24]-[14:25]): agents read restructured build logs, diagnose failures and
  submit fixes; every agent change gets a preview URL for a human to look at.
- Google Gemini CLI repo (WOTHERSPOON): automated code-review agent before human review [10:14];
  non-AI GitHub Actions that close items with no reply after 60 days [14:23]; issue-before-PR
  enforcement [12:20]; a cap on open PRs per external contributor (now a GitHub repository setting)
  [13:21]; `open source vacation` auto-closing during set periods [17:28]-[18:28]; vouch lists
  scanned by Actions [19:28]-[20:30].
- AutonomyAI (DUBNOV [24:54]): an agent labels every opened PR with risk level and size.
- Cisco (CLIP-COST [08:14]-[09:15]): doc change triggers skill rewrite plus evals.
- Production side (PANEL [18:25], [20:30]): an agent attached to PagerDuty alerts that starts the
  investigation and hands over a markdown file; reflector agents that add what they learned to
  memory.
- DOUGLAS [11:18], [14:22]: `sweeper` runs ten parallel agents, each in its own VM, to clear lint
  errors or write docs across an old repo.

Guardrails (mostly SYME [14:29]-[19:38]):

- The agent step runs read-only, in a container, with no direct access to secrets.
- A deterministic preload step gathers inputs (CI logs and so on) before the agent runs.
- Writes go through declared safe outputs with a tiny blast radius (for example: create one
  issue), applied in a separate stage after threat detection, not by the agent through MCP.
- Outbound network is firewalled; shared package caches are disabled to prevent cache poisoning.
- "They don't ever merge pull requests." [15:30] The PR or issue is the guaranteed human gate.
- "You must always have a security architecture" [18:36]; he tells the audience not to run a coding
  agent directly in Actions or any CI without one [17:35]-[18:36].
- In automation, unlike interactive use, safety raises throughput: "The better the quality of the
  rails that you're on, the faster your train can go" [17:35].
- When an automation produces poor output, add a quality gate to the pipeline instead of patching
  results by hand (SYME [31:06]).
- LAWSON's three principles: sandboxed execution, human in the loop by default, every action logged
  with rollback [20:34].
- THOMAS: keep human oversight first and choose which workflows are fit for unsupervised running
  [22:50], [28:57].

Review: Syme reads the overnight PRs in the morning [08:24]; a factory `gated on human
requirements` is acceptable and can be deliberately slowed [26:54]-[27:57]. Meta's fix loop ends in
human diff review [22:50]. Google still has a human review every PR after the automated reviewer
[10:14]. Cisco gates on evals and uses humans only for major changes [09:15].

Transfer to a solo developer: high. SYME's setup is explicitly one maintainer over several repos,
with a per-repo checked-in workflow file. WOTHERSPOON's contributor controls matter only for public
repos that receive outside PRs.

### (d) How work is specified, split and tracked

- Specification artefacts.
  - ADR first, as its own PR, short and visual, reviewed hard by a human; agents then review
    implementation PRs and all later PRs against the ADR set (BATEY [14:27]-[15:27]).
  - PRD from two weeks of transcribed spoken discussion, then entity relationships and business
    logic, then an agent-made task plan (ODEVO [26:53]-[27:53]).
  - Plan skill capturing technical and product considerations; a ticket-writing skill; a master
    plan the developer skill updates after each unit (ROBERTS [22:38]-[24:43]). "Let your spec be
    the contract" (ROBERTS [25:43]).
  - Reverse-engineered PRDs and use-case/entity models for existing systems (ROBERTS [19:31];
    CLIP-BROWNFIELD [02:04]).
  - Spec review by inline comment: Marsden finds "the two lines in the spec where the agent got it
    wrong" and comments there; PRs link back to the spec (CLIP-COST [05:09]-[06:10]).
  - superpowers (brainstorm, write plan, execute plan) as the spec-driven flow at Batey's company,
    with the warning that brainstorming must not replace the engineer's own design decision (BATEY
    [22:36]).
  - Counterpoint: for simple apps the input is intent, not a long requirements document; specs
    still matter for large platforms (LAWSON [10:18]-[11:20]).
- Splitting.
  - Epics, not stories: Nearform slices at epic level and gives each to a one- or two-person team
    (ROBERTS [27:46]); an Odevo team's developers pick up `a couple of epics a day` (ODEVO [27:53]).
  - PRD to story map to Jira tickets automatically; good tickets are what make parallel work
    possible (ROBERTS [20:35]).
  - Slices over rewrites (ROBERTS [25:43]); one complex task at a time plus labelled issues that are
    safe to run alongside (BATEY [23:36]).
  - Merge behind a feature flag, then polish in three or four follow-up PRs (a method he
    names, captioned `plan, Merge Polish`; DUBNOV [11:22], [21:49]-[22:51]).
  - Issue before PR, with maintainer sign-off on design for anything large (WOTHERSPOON
    [12:20]-[13:21]).
  - Labels or issue titles carve part of a repo's work into an automated sub-flow (SYME [26:54]).
- Tracking and metrics.
  - Merge rate of agent PRs: 112 merged of 142 for one GitHub Next workflow (SYME [20:43]); 74%
    merge rate and 84% merged without developer commits for non-technical authors (DUBNOV [18:40]).
    Dubnov reads a rate below 100% as healthy boundary-finding, not failure [15:33]-[17:38].
  - Open-issue count over time per repo (SYME [23:50]-[25:51]).
  - Flow state per repo: flowing, blocked (waiting on a human) or idle (SYME [26:54]-[27:57]).
  - PR throughput, time to merge, PR size on shared dashboards (ODEVO [07:20], [23:47]).
  - Feature adoption as the gate before starting the next feature (BATEY [20:34]-[21:35],
    [26:45]).
  - A findings backlog for technical debt (ROBERTS [17:30]).
  - Risk and size labels on each PR to budget review effort (DUBNOV [24:54]).
- Review policy varies and is contested; see contradictions.
- Does not transfer: PM-to-developer ratios, forward-deployed engineers, mission teams of two to
  four, on-call rota size, sprint ceremonies (FOXWELL, BATEY). Inference: what transfers is the
  shared observation that deciding what to build becomes the bottleneck (FOXWELL [06:07]; BATEY
  [19:34]; ODEVO [33:01]), which for one person argues for a written, prioritised backlog and
  cheap prototypes before committing.

### (e) Cost control

- The Uber story as told here is third-hand and inconsistent. DUBNOV: "Uber has increased the area
  spend since 2024 by six x." [05:11] (my reading: AI spend), the increase `was completely used
  within four months`, and "They are out of AI budget for the rest of the year." [06:12] A panel
  audience member cites Bloomberg saying Uber and Microsoft cancelled Claude Code licences (PANEL
  [26:47]); Rohrer replies he does not think Uber cancelled, they ended up "spending all of their AI
  budget in four months rather than 12" [28:50], and that Microsoft is steering engineers to its own
  Copilot. The clip title compresses this to `Burned 6x Its AI Budget`. No primary source is in the
  corpus; treat the figures as hearsay.
- What drove spend, according to Dubnov (a vendor arguing for his product category): raising
  limits for the same developers on the same tasks; uninterested developers who hand a task over and
  "let the agent loop endlessly, because they don't really feel the tokens" [09:16]; giving Claude
  Code to non-technical staff [09:16]-[10:18]; rework and AI-generated bugs. He cites an unnamed
  study of over 2,400 companies: "from any $100 that you spend on AI, only $18 actually goes to
  meaningful code that actually gets shipped to users" [07:13].
- Flat-rate plans hide cost. WOTHERSPOON [04:07]-[05:08]: subscriptions are heavily subsidised, so
  users feel they have unlimited resources; GitHub Copilot counted requests, not tokens, and one
  long-running prompt consumed over 60 million tokens (about $200 at API prices), which is why
  Copilot moved to token billing around the talk date. DOUGLAS [16:24]: five-hour windows and
  weekly allowances; he was also temporarily banned by Anthropic for running ten parallel sweeper
  agents [14:22]-[15:24].
- Model routing. DOUGLAS [13:21]: agents `don't always need` the top model; he ran the parallel
  sweep on Haiku and accepts slower runs overnight or at weekends; he uses a year-old cheap model
  as his daily driver and a small model for first-pass skill generation [21:33]. Marsden (CLIP-COST
  [06:10]-[07:11]): open-weight models such as GLM 5.1 on owned hardware "can now do pretty much
  80% of the work that you need to do"; spend the next three months of token budget on a machine
  (caption: `eight RTX six K pros`), keep a switchable setup, and burst to Claude Opus 4.8 for hard
  problems. ODEVO [24:48]: trained developers stop "pumping everything onto Opus 4.7".
- Caching. Kushwaha (CLIP-COST [00:00]-[03:07]): in a long agent session most input tokens are
  repeats of earlier turns, so prompt caching decides cost and time to first token; when
  a model is served from several replicas, each turn must reach the replica that holds the cache.
- Caps. The only explicit cap mechanisms in this batch are on contributions, not tokens: a limit
  on open PRs per external contributor (WOTHERSPOON [13:21]) and narrow safe outputs per workflow
  run (SYME [14:29]). No source describes a per-repo or per-task token budget.
- Review cost is part of the bill: generating is cheap, reviewing is not (WOTHERSPOON [07:09],
  [11:17]); small PRs and risk/size labels reduce it (DUBNOV [24:54]); Cisco removes humans from
  minor skill diffs (CLIP-COST [09:15]).
- Token usage is not a value metric (THOMAS [28:57]; BATEY [29:48]).
- Transfer: the routing, caching and loop-supervision points apply directly to one person on
  subscriptions plus API routes. Marsden's hardware purchase is sized for `a meaningfully sized
  organization` [07:11]; Inference: it does not obviously pay for one developer.

### (f) Every measured result or number given

Self-reported unless noted; none comes with a method description.

Meta (THOMAS):
- Leadership estimate of toil: about 50% of engineer time, target under 5% [02:05].
- Community over 40 times bigger, well over 500 people by January 2026; weekly tool use from under
  half to well over 80%, now mid to high 90s [03:05]-[04:06].
- Half a billion lines of Hack in one repo when he joined; Haskell slice half a million lines
  [05:10]-[06:14].
- Maturity model: six dimensions, five levels, rerun every 3 to 4 weeks; discussion 20 to 30
  minutes, often 45+ [10:22]-[14:33].
- Test-coverage targeting: about three hours versus about half a week; nearly 60 diffs merged
  [18:40].
- Refactoring pattern: roughly half the time [19:46].
- Automated code fix: 30 diffs generated autonomously at the start; he believes it is now several
  orders of magnitude higher (unquantified) [22:50].

Nearform (ROBERTS):
- Greenfield: 80% faster kickoff, 50% faster to MVP, four times development velocity (caption:
  `philosophy`) [02:06].
- Mature codebases estimated at 60 to 70% of enterprise software [03:07].
- Pseudo-greenfield project: about six months of scope in eight weeks, four times faster than a
  competitor's estimate; requirement reverse-engineering from months to a week; codebase mapping
  from two weeks to hours [19:31]-[20:35].
- Branch-by-abstraction project: 500,000 lines; the first AG Grid upgrade took about a month (she
  says she lacks exact metrics); about 80 units to migrate [20:35]-[24:43].
- Feature teams of 1 to 2 people instead of 4 to 5 [27:46].

GitHub Next (SYME):
- Semantic function refactoring workflow: 112 merged PRs out of 142 (79%, my arithmetic) [20:43].
- A colleague built hundreds of workflows [19:38].
- Syme maintains about seven open-source repos; example backlogs of 200 to 400 open issues [21:46].
- FSharp.Data: three major releases after enabling Repo Assist in March (year not stated); issue
  counts shown
  on a slide, not spoken [23:50]-[24:51].

FOXWELL: two-person team; first day's plan done by lunchtime, second day's by 11 a.m.; MVP in two
weeks [13:22]-[14:22]. Minimum sustainable on-call rota: four people [29:51]. One consultancy CTO:
only 2 or 3 (of the teams it works with; caption unclear) intentionally reduced team size [12:20].

BATEY: 90 to 100% of his company's code is AI-written [08:18]; a hypothetical feature PR of about
7,000 changes [13:26]; teams cut from 6-8 to 2-4 [26:45]; 15-minute maximum for a full test suite
[28:47]; `50 over 50` (my reading: 50/50) odds that generated code compiled when they started
[06:13]. Audience show of hands only, no counts.

Odevo (ODEVO):
- Company: 50,000 to 2.5 million homes and 1,000 to 14,000 employees in seven years [04:10]-[05:12].
- Before: around 30% AI use, mostly Copilot [07:20]. After training (finished mid-February, 2026
  by context):
  about 94% used AI in at least three of their last ten PRs, 50 to 60% in ten of ten, 6% not at all
  [22:44].
- 80 vendor responses to the RFP, ten shortlisted, three finalists [09:24]-[10:26]; main training
  cohort of 80 people [17:38].
- Eight-year platform rewritten to feature parity in three weeks with an external expert; team
  from 20 developers to 4 [25:50]. A mobile app in three days was attempted and failed [25:50].
- One developer `haven't written any code at work for 4 or 5 months` [29:58]; one claimed
  productivity figure is garbled (`2000 30s`) [30:59].
- One team: two weeks on requirements; 7 or 8 self-review passes before a self-merged PR [27:53].
- 15 to 30 minutes of training lost because people could not install Docker [21:42].

AutonomyAI (DUBNOV), vendor data across `hundreds of orgs and thousands of PRs`:
- Average non-technical contributor opens about 50 PRs a quarter; 74% merged; 84% of merged PRs
  have no developer commits [18:40].
- Example rejected PR: a little over 1,000 lines [16:35].
- Shopify (as reported by Dubnov): 50% of non-engineers' shipped work accepted as is [08:15].
- $18 of every $100 reaches shipped code, from a study of over 2,400 companies (unnamed) [07:13].
- Uber: AI spend up six times since 2024, increase used in four months [05:11]-[06:12].

PANEL: an agent diagnoses a production issue in 30 seconds that took developers hours or days
(Rohrer, anecdote) [07:10]; one customer sends a person home for a week every few weeks to
decompress [31:58]; harness engineering should take about as much time as prompting [28:50].

LAWSON: IDC prediction of more than 500 million new applications by 2028 [01:00]; she builds about
one app a day [01:00]; cycle time `from weeks to hours` (unquantified) [13:24].

Google / open source (WOTHERSPOON):
- Gemini CLI: 100,000 GitHub stars, over 700 external contributors [12:20].
- Issue-before-PR removes about 90% of drive-by PRs (his estimate) [12:20]-[13:21].
- Stale items closed after 60 days [14:23]; a slop PR of over 30,000 lines [06:09]; ten junk PRs
  from ten sub-agents in 30 to 45 seconds (demo) [07:09].
- GitHub: over 45 million PRs merged per month in 2025; he heard over 200 million `last month`
  (unsourced) [08:12].
- Copilot: one prompt, over 60 million tokens, about $200 at API price; a $30 plan could yield over
  $30,000 of inference [05:08]. Plans of $20 or $200 can yield thousands of dollars of inference
  [04:07].
- Skill default-on threshold: used over 50% of the time [30:47]. Review turnaround target: two days
  [25:38].
- Ghostty with vouch: PR quality `way up` (no number) [20:30].

Paper Compute (DOUGLAS):
- 1,000 turns per session, screenshot every ten turns, ten simultaneous agents [02:01]-[06:07];
  seven-second door cooldown the agent had to learn [07:07].
- Claude Code and Codex keep sessions on disk for 30 days [10:16].
- 77,000 recorded sessions since January 2026, about four gigabytes, about one gigabyte a week
  [22:33]-[23:34].
- An old repo with about 100 users had all lint errors fixed in under an hour [14:22]; account
  unblocked about 12 hours after the ban [15:24].
- Anomaly thresholds given as examples: ten tool-call failures; 26 skill invocations across ten
  sessions [15:24].
- Fine-tuning: a fine-tune (captioned `specialized fine tuning`) of a 4B Qwen model ran on a 24 GB
  card; DPO needed 32 GB, gave `middling` results on 4B and could cost about $1,000 a week in
  compute [26:42]-[27:47].

Clips:
- Stanford study across 150,000 engineers: widest performance spread they have measured; a
  rank-stability figure falling from 0.70 to 0.45 (garbled, low confidence) (CLIP-SCALE
  [02:00]-[04:02]).
- Marsden: open-weight models do about 80% of the work; hardware suggestion of eight GPUs for
  three months of token budget (CLIP-COST [06:10]-[07:11]).
- Kushwaha: by the 40th turn most input tokens are cacheable (no percentage) (CLIP-COST [01:02]).

### Contradictions and open questions

- Mandatory human code review. Remove or relax it: FOXWELL [27:47], [32:54]; one Odevo team
  self-merges after 7 or 8 agent review passes (ODEVO [27:53]); PANEL [10:15] says humans cannot
  review everything. Keep it: Google has a human review every PR (WOTHERSPOON [10:14]); SYME makes
  the PR the fixed human gate [15:30]; BATEY wants humans to keep understanding the system and
  calls the complaint that reviews are the bottleneck `crazy` [25:40]; THOMAS keeps human review
  after
  autonomous diffs [22:50]. Middle positions: review the ADR or spec instead (BATEY, FOXWELL,
  Marsden); triage by risk label (DUBNOV); evals gate minor changes (Cisco). Unresolved; for a solo
  developer there is no second human, which makes the spec-level and automated-gate positions the
  only ones available. Inference.
- Full autonomy. THOMAS [28:57], FOXWELL [04:05], PANEL [28:50] (`co-driver`), LAWSON [20:34] all
  decline it; ODEVO's lighthouse team and SYME's overnight factories go furthest, both still with a
  PR.
- Many agents at once. Syme's colleague runs hundreds of workflows and Meta and Douglas run
  parallel agents; BATEY and PANEL report that juggling several hard tasks wrecks quality and
  people ("But it will just destroy people's minds very, very quickly." PANEL [31:58]). Resolution
  offered by BATEY: parallel only for non-complex tasks.
- One workflow doing many things versus many single-purpose workflows: both exist inside the same
  GitHub Next team (SYME [19:38]-[21:46]); no comparison data.
- Skills in the repo versus context size. WOTHERSPOON checks many in but gates default-on by the
  50% rule; ODEVO says long instruction files hurt. An audience question to Wotherspoon about skill
  selection degrading as context grows got only the 50% heuristic [30:47].
- Adoption metrics. Odevo and Meta report adoption percentages as success; THOMAS and BATEY call
  the same class of number vanity. Odevo's own preferred measure is `boldness` (number of ambitious
  experiments) [24:48]-[25:50], which is not measurable as stated.
- Will hallucination go away. Rohrer says it is inherent to current models and plans around it;
  Jourdan expects models to make today's caution look dated (PANEL [22:40]-[25:47]).
- Greenfield rewrite versus incremental brownfield. Odevo rewrote an eight-year platform in three
  weeks; ROBERTS warns pseudo-greenfield duplicates shared concerns and hits a re-integration wall;
  Martinelli says translation alone is not modernisation. The Odevo result has no quality or
  post-launch data.
- Uber and Microsoft cost stories conflict between DUBNOV and PANEL (see e).
- Open: none of these sources shows a mechanism for syncing one instruction/skill/hook set across
  a dozen separate repositories, per-task token budgets, or hooks. Hooks are not mentioned in any
  of the 15 transcripts.

## Per source

### Ian Thomas - AI Native Engineering (Ian Thomas, Meta, June 2026)
File: refs/videos/NVzKtCSeoRA/transcript.md   URL: https://www.youtube.com/watch?v=NVzKtCSeoRA

Thesis: Meta's Horizon organisation moved from patchy to near-universal agent use by starting in a
small volunteer engineering-excellence group, aiming agents at toil (tests, refactors, code-quality
fixes) rather than features, and tracking progress with a team self-assessment. Human oversight
stays; full autonomy was set aside.

Practices:
- Start where the work is well understood and low risk: code modernisation, admin tasks, bugs,
  operational overhead, internal tooling and tests, not feature development [05:10]-[06:14],
  [29:59].
- Target test writing with data: teach the agent to query coverage tables and change-frequency
  data, then build a priority list of uncovered hot files [17:37].
- For a repeated refactor, teach the agent how you would do one instance, have it find the same
  shape elsewhere, run agents in parallel and act as architectural reviewer [19:46].
- Remove an environment bottleneck with context: an MCP server exposing the data behind Horizon
  Worlds let agents work in ordinary on-demand environments instead of one GPU Windows PC, and
  output quality rose [20:47]-[21:48].
- Continuous automated code fixing: detectors plus "rules and run books to the AI that look
  basically like skills or context files" [21:48], looping "find a thing, fix it, promote a diff,
  get someone to review it" [22:50].
- Counter bad AI tests in CI with a second model as judge: validation "using a different AI tool
  to judge the quality of the output" [15:33]; it now runs on diffs with a significant volume of
  AI-generated tests.
- Build narrow custom agents on a shared platform: maintenance-mode agents review diffs against
  known criteria and approval signals [25:55]; a risk score on every diff decides caution versus
  fast-tracking [25:55].
- What made wins repeatable: a clear problem definition, shared tools, human oversight first,
  iteration and sharing [22:50]-[23:50].
- Team self-assessment: six largely independent dimensions (workflow integration, prompting and
  sharing, individual and team gains, use cases, others not all named), five levels, voted
  anonymously, discussed, rerun every 3 to 4 weeks, results posted internally [10:22]-[14:33].
- Stop treating weekly users, diff counts, lines written by agents and token usage as value:
  "at the end of the day, their vanity metrics, token usage as well" [27:57].

Evidence and numbers: see (f). Community 40x to 500+; weekly use under half to over 80% then mid to
high 90s; 3 hours versus half a week and "nearly 60 diffs got merged" [18:40]; roughly half the
time on refactors; 30 autonomous diffs initially.

Tools and files named: Hack, C++, C#, Unity; MCP server for Horizon Worlds data; code-mod
infrastructure; `Confucius` (internal agent-building platform, spelling unsure); `doctors`
(per-diff risk score, caption-garbled name); Workplace; Miro; DORA research.

Caveats: single monorepo with heavy platform investment that he says took real effort to build
[24:54]; open questions he lists are code-review bottlenecks and long-term cost of rapidly
generated code nobody fully understands [26:56]-[27:57]; "we didn't really want to move to full
autonomy" [28:57]. The maturity-model slide content is not in the transcript.

Relevance: medium. The four toil patterns, the judge-in-CI for AI tests and the vanity-metric
warning transfer to one person; the community building, workshops and maturity model do not.

### Katie Roberts - Stop Maintaining, Start Evolving: Applying AI-Native Practices to Brownfield Codebases (Katie Roberts, Nearform, June 2026)
File: refs/videos/5SKh-FmjX7U/transcript.md   URL: https://www.youtube.com/watch?v=5SKh-FmjX7U

Thesis: The headline productivity numbers come from greenfield work; most software is brownfield,
where unguarded agents add hidden debt. Treat the codebase like a city: map it, build a findings
backlog, put guardrails in place, then evolve it one slice at a time through a plan skill and a
multi-agent developer skill.

Practices:
- Choose the change strategy deliberately [06:12]-[12:23]:
  - Pseudo-greenfield branch: fast at first; costs are duplicated shared concerns (auth, logging,
    error handling), divergence, late integration testing, risk of a permanent fork.
  - Strangler fig: facade at the edge, legacy frozen, routing layer gives feature flags, canary and
    rollback; costs are two systems to run and a need to finish.
  - Branch by abstraction: interface inside the codebase plus feature flag, trunk always
    releasable, both implementations comparable in production; cost is abstractions left behind.
    She notes AI helps find leftover abstractions [12:23].
- Do not let an agent refactor freely: it ends up "generating dart code, which passes all your
  tests and undermines the implicit architectural constraints" [13:26] (my reading: dead code).
- Start from the developers' known pain points (value versus complexity chart), then aim agent
  investigations at them: dead code, duplication, pattern inconsistencies, complexity hotspots,
  OWASP-style scan as a rough signal only [14:26]-[15:26].
- Generate dependency graphs and current-behaviour maps, human-reviewed [16:28]. Side effect: the
  team argued less and contributed more because the evidence was not one senior person's opinion
  [16:28]-[17:30].
- Principles list [17:30]-[18:30]: do not trust AI output blindly; small scopes; version-control
  everything; "Creates findings backlog and then prioritize your findings backlog." [17:30];
  human-readable docs reviewed by the whole team; guardrails of tests, logs and static analysis.
- Verify the guardrails work before implementing: SonarQube running and reporting, confidence in
  the test suites [18:30].
- Write pattern rules: "we have rules that make sure that our our skills don't repeat bad patterns"
  [18:30], stating "we want to see more like this, a pattern, less like that pattern" [19:31];
  keep skills alongside the code.
- Invest in a ticket-writing skill so anyone (or any agent) can pick a ticket up; this is what
  enables parallel work [20:35].
- Spend more time on planning in brownfield than habit suggests; capture it in a plan skill
  [22:38]-[23:41].
- Developer skill as a multi-agent flow: orchestrator analyses requirements; separate agents build
  test scaffolding, implement, run static analysis and quality gates, and review; then human
  review and sign-off; then it "then goes back and updates the master plan" [24:43].
- Expect the first few runs of a new skill to be slow; reuse it across the remaining units and keep
  the resulting skills as examples of what good looks like [24:43]-[25:43].
- Takeaways: "start with a math, not a migration" [25:43] (my reading: map); spec as contract;
  "thinking slices and not rewrites" [25:43].
- Slice work at epic level; watch for skills diverging between teams [27:46].

Evidence and numbers: see (f). Greenfield 80% / 50% / 4x; six months in eight weeks; months to a
week; two weeks to hours; 500,000-line codebase; about a month for the first AG Grid upgrade; 80
units.

Tools and files named: SonarQube, Cypress, AG Grid, Jira, Miro, Cursor; Adam Tornhill's `Your Code
as a Crime Scene`; Martin Fowler's strangler fig; skills named plan, developer, and a ticket skill
(caption: `great component skill`, unsure).

Caveats: consultancy figures with no method; she admits lacking exact metrics for the AG Grid
case; says pseudo-greenfield `isn't right for every project`; all AI analysis still needs human
review.

Relevance: high. The most concrete brownfield procedure in the batch, and almost all of it
(findings backlog, pattern rules, plan/ticket/developer skills, master plan) fits one person.

### Don Syme - The Agentic Repository Automation Revolution (Don Syme, GitHub Next, June 2026)
File: refs/videos/kbvqRWY-bUs/transcript.md   URL: https://www.youtube.com/watch?v=kbvqRWY-bUs

Thesis: Beside CI and CD there is a third pillar, continuous AI: scheduled and event-triggered
agents that do subjective repo work (triage, docs, refactoring, tests, performance, fault reports)
and deliver issues and PRs. Unlike interactive coding, automation gets faster the stricter its
security architecture. The repo owner becomes a flow designer who adds quality gates.

Practices:
- Define an automation as one checked-in file: "Dead simple front matter plus markdown." [13:28]
  Front matter holds triggers (schedule, issue opened/reopened), tools and safe outputs; a CLI
  extension hardens it into an Actions YAML; an `add` wizard installs samples [13:28]-[16:31].
- Run the agent sandboxed: "They run read only with no access to secret, no direct access to
  secrets." [14:29] in a container, with a pre-computed bundle of inputs [18:36].
- Constrain output to declared safe outputs (for example one issue or one PR), applied in a
  second stage after threat detection [14:29], [18:36].
- Firewall outbound network and "we turn off things like shared package coaches" [18:36] (my
  reading: caches) against cache poisoning.
- Never auto-merge: "They don't ever merge pull requests." [15:30]
- Repo Assist pattern: "It reads it's memory. And then it chooses a couple of a smorgasbord of
  tasks." [22:48] once a day; the maintainer edits the task list; it can run in a reduced mode
  while the maintainer is away [23:50].
- Use it to mine old backlogs: the agent comments on issues from as far back as 2018 with an
  assessment, turning a dormant backlog into releases [24:51].
- Weekly report fed by production probes, so a performance or quality sprint happens weekly
  instead of every few months [30:05]-[31:06].
- When output quality is poor, do not fix items by hand: "let's add a quality gate to the factory
  so we can get the whole factory flowing" [31:06].
- Scope an automation to part of a repo with labels or issue titles [26:54]; cross-repo and
  org-wide runs are possible with permissions [15:30].
- It is fine to gate or slow automation on human availability [27:57].

Evidence and numbers: "the workflow had 112 merged PRS out of 142" [20:43]; "I maintain about
seven open source repositories" [21:46]; FSharp.Data went from dormant to three major releases;
a written report, `Impact of Automated Repository Maintenance Assistance`, is cited but not in the
corpus [25:51].

Tools and files named: GitHub Agentic Workflows (caption: `GitHub workflows`), GitHub Actions,
Claude Code, Copilot CLI, Gemini CLI, Codex, MCP, Repo Assist, FSharp.Data, Deedle; blog series
`Meet the Workflow`; the `agent factory` write-up (colleague's name captioned `Pelli`, unsure); Hud
(startup, speaker captioned `May`).

Caveats: product in technical preview at the time [33:11]; his own N+1 factory was `not flowing`
for lack of a quality gate [31:06]; outcome graphs across repos varied (`Not all of them, but
most`) [25:51]; token cost of daily runs is not discussed.

Relevance: high. One maintainer, several repos, one file per repo, explicit guardrails: the closest
match to the target setup in this batch.

### Hannah Foxwell - The Reinvention of the Dev Team (Hannah Foxwell, independent advisor, June 2026)
File: refs/videos/pyYKOLEnsZk/transcript.md   URL: https://www.youtube.com/watch?v=pyYKOLEnsZk

Thesis: Coding speed is no longer the constraint; deciding what to build, the path to production
and sustainable human work are. Her three anchors: build something worth building, speed requires
safety, people matter.

Practices:
- Validate ideas with cheap working prototypes before committing to production work [07:07],
  [15:23]-[16:23].
- Automate every step between merge and production: "I am trashing anything manual on my path to
  production." [26:47] Manual testing may exist but not on the critical path.
- Use feature flags, blue-green and progressive delivery so it is safe to ship something buggy
  [22:39], [26:47].
- Use SLIs, SLOs and error budgets to decide when to slow the rate of change [23:42].
- Use agents for test coverage, migrations and refactors [26:47].
- Move review earlier: "shifting left on peer review using spec driven development" [32:54].
- Drop heavy planning cadence: "Two week sprints are absolutely too long right now" [32:54].

Evidence and numbers: two-person team (one developer, one product person) finished each day's plan
by late morning and had an MVP in two weeks; afterwards the work "looks a hell of a lot like
platform engineering" [24:45] (scalability, security). Minimum on-call team of four [29:51].

Tools and files named: none specific; references to Steve Yegge's eight levels (caption garbled),
Gas Town, a Cursor blog post on a `third era`, incident.io on product engineers, AWS and JPMorgan
case studies (not in corpus).

Caveats: explicitly offers experiments, not answers [11:17], [28:47]; says she knows nobody who
runs an agent orchestrator safely [04:05].

Relevance: medium. Team ratios and on-call do not transfer; the after-MVP observation, no manual
steps on the release path, feature flags and spec-level review do.

### Christopher Batey - Building Product Teams in the Age of AI: What We Had to Relearn Every Quarter (Christopher Batey, consultancy CTO, June 2026)
File: refs/videos/tJUAef_dBtU/transcript.md   URL: https://www.youtube.com/watch?v=tJUAef_dBtU

Thesis: For systems that hold sensitive data or run customers' production, nearly all code can be
agent-written but system-level thinking must stay human. Capture it in short ADRs, limit dependence
on any one harness or provider, and judge work by feature adoption.

Practices:
- "let's not delegate systems thinking to agents" [11:22]. Questions he wants a human to answer for
  a cross-boundary feature: what connects to what, how it authenticates, what is exposed to the
  internet, what data crosses, how each side deploys [13:26].
- ADR first: a system-level decision "always comes as a completely separate pull request" [14:27]
  with diagrams; the human spends real effort there.
- Then let agents review the implementation, and every later PR, against the ADR set to catch
  quiet architecture changes such as a newly exposed API [15:27].
- Failure they hit: agents saw ADRs existed and wrote long ones nobody read, "which completely
  defeated the point of having them" [14:27].
- Treat harness, model host and model as three separate dependencies; use an open-source harness so
  that "when Anthropic goes down, I just switch to OpenAI with a single command and I carry on"
  [16:27]. Make lock-in a conscious choice [17:30].
- Use a brainstorm / write-plan / execute-plan flow (he names superpowers) but make the design
  decision yourself [22:36].
- Parallelism rule: "work in parallel. Absolutely. But only work on one complex task at a time."
  [23:36] Label issues that are safe to run while another agent works.
- Do not start the next feature until everything possible has been done to get the last one used
  [20:34]-[21:35].
- Keep feedback fast: "It's 15 minutes for me, is absolute maximum for running a full suite of
  tests" [28:47]; design for small blast radius per deployable component.
- "Do not get sucked in by vanity metrics that measure one little bit in the middle, like token
  usage or commits or PR merged." [29:48]

Evidence and numbers: 90 to 100% AI-written code; teams of 2 to 4; no outcome metrics given.

Tools and files named: architectural decision records (ADRs), Claude Code, Codex, OpenCode (named
in the CLIP-BROWNFIELD caption of the same passage), superpowers, GitHub issues with labels,
Kubernetes.

Caveats: his velocity graph is `completely made up` by his own account [27:47]; adoption got
harder because too many features shipped [20:34]; he ran out of time before showing his test
types.

Relevance: high. ADR-first with agent conformance checks, the one-complex-task rule, provider
switchability and the 15-minute test budget all apply directly to one developer.

### Daniel Jones and Tomasz Maj - More software, faster: Odevo's AI Native transformation (re:cinq and Odevo, June 2026)
File: refs/videos/mB74LGAmmV0/transcript.md   URL: https://www.youtube.com/watch?v=mB74LGAmmV0

Thesis: A property-management group with many acquired tech stacks trained every developer the
same way after first checking delivery fundamentals. Adoption reached about 94% and one team
rebuilt its delivery process around PRDs, epics and self-merged PRs.

Practices:
- Check fundamentals before agents: CI/CD and a deployment platform, tests, agreed coding
  standards [12:27]-[13:28]. "If agents can't run tests to find out they've broken your software,
  don't be surprised when they break your software." [12:27]
- Teach context management first, including that over-full instruction files hurt: "you're better
  off having no instructions in your agents MD than lots of them" [19:41] (he cites `a couple of
  academic studies`, unnamed).
- Teach failure modes, not the happy path (exercises with old models that hallucinate easily)
  [20:41].
- Syllabus order: context, failure modes, the IDE-to-terminal jump, MCP, spec-driven development,
  multi-agent workflows [19:41]-[21:42].
- Space the learning: weekly half-day modules, each followed by trying it on real code [21:42].
- Make delivery data visible: dashboards of who works on what, PR throughput, time to merge
  [23:47].
- One team's process [26:53]-[27:53]: two weeks of spoken requirements, auto-transcribed; agents
  draft a PRD; the team hardens it and defines entities and business logic; agents split it into a
  task plan; developers take a couple of epics a day with any method (BMAD and Spec Kit are named,
  captions garbled); "they will do like 7 or 8 passes of a code review before then raising a PR,
  which they will then self merge".
- Watch for compulsive overwork and feature pressure [33:01]-[34:03].

Evidence and numbers: see (f). 30% to about 94%; "Feature parity 1 to 1 in three weeks." [25:50];
"So that was 20 devs building it for eight years. Now we have four devs building it" [25:50]; a
three-day mobile app attempt failed.

Tools and files named: Claude Code, GitHub Copilot, VS Code, AGENTS.md, MCP, Docker, Spec Kit,
BMAD, Gas Town / Gas City, Ralph Wiggum loops, Opus 4.5 and 4.7, Lovable, Liberating Structures,
TRIZ (caption: `trees`), DORA 2025 report.

Caveats: no quality, defect or cost data for the rewrite or the self-merge team; their summary
line "with AI, bad things get worse and good things can get better" [10:26] cuts both ways; the
non-engineer rollout was still future.

Relevance: medium. The fundamentals checklist, the short-instruction-file point and the PRD-to-epic
flow transfer; the training programme mechanics do not.

### Tammuz Dubnov - When Our PM Started Writing Code: What Merge Rate Taught Us About AI Adoption (Tammuz Dubnov, AutonomyAI, June 2026)
File: refs/videos/KzhjnILSP0Y/transcript.md   URL: https://www.youtube.com/watch?v=KzhjnILSP0Y

Thesis: AI-native means the person who cares about and decides a change can also execute it,
removing hand-offs. Spending more tokens on the same developers does not do that. Measure it by PR
count, merge rate and merged-without-developer-touch rate. This is a vendor talk.

Practices:
- Harness definition: after seeing a mistake, "you make it unfeasible for the agent to make the
  same mistake again" [12:25], with automatic feedback, and the harness must keep adapting.
- Harness requirements for large codebases: agent onboards itself to the code, maps product
  language to code, keeps context fresh in long sessions, checks its own work, knows what good
  looks like, learns across users [12:25]-[13:26].
- Three metrics: PRs opened per author; merge rate; share of merged PRs with no extra developer
  commits [17:38]-[19:43]. Computed from commit history before merge, ignoring merges and rebases
  [20:45].
- Expect and accept a non-100% merge rate; a rejected PR that exposes an undecided architecture
  question speeds the decision [15:33]-[17:38].
- Keep engineering guardrails; organisations that dropped them found off-product features in front
  of clients [10:18]-[11:22].
- Ship behind feature flags and refine in follow-up PRs [21:49]-[22:51].
- Agents mirror the repo: they use feature flags if the repo does, and "organizations that don't
  have a lot of tests, we see the agents don't really add test" [23:52].
- Reduce review load: tune the agent toward few lines and reuse of existing components; have an
  agent label each PR, "It labels the risk level and the size." [24:54]

Evidence and numbers: about 50 PRs per quarter per non-technical contributor, 74% merged, and "84%
of the PR merge generated by non-technical individuals simply get merged" [18:40]; Uber, Microsoft,
Shopify and the $18-per-$100 claims are relayed, unsourced.

Tools and files named: Claude Code, Cursor, Figma, AutonomyAI's agent (a product name captioned
`Tanya`, unsure); method name captioned `plan, Merge Polish` (not explained).

Caveats: sales context; numbers are from his own platform; the Uber and Microsoft accounts are
disputed in PANEL.

Relevance: medium. Non-technical contributors do not exist in a solo setup; the three merge
metrics, risk/size labels and the mirror effect do transfer to agent-authored PRs.

### Stephane Jourdan, Simon Rohrer and Pini Reznik - From Pipelines to Prompts: Surviving the Shift to AI (panel, June 2026)
File: refs/videos/1grkxo4cyKY/transcript.md   URL: https://www.youtube.com/watch?v=1grkxo4cyKY

Thesis: Three platform and operations veterans agree that agent output is only good with harness
engineering and deterministic checks, that humans cannot review every line and should decide
trade-offs, and that agents are as useful for diagnosing production as for writing code. Speaker
attribution below is inferred from context.

Practices:
- First guardrail is linting (Rohrer, regulated industry, uses OpenCode): "get your linting turned
  up to 11" [09:13]; add custom linters and code-health tools.
- Harness feedback rule: "anything that goes wrong, feed it back into the harness and then never
  let that class of error happen again" [17:24], deterministically where possible.
- Budget time for it: "If you spend about as much time engineering your harness as you do on
  prompting the actual functional output" [28:50] the quality is good; without it, terrible.
- Point agents at production evidence (logs, incident reports, code): "they will solve an issue in
  30s that could have taken developers hours" [07:10].
- Watch for agents creating services or picking tools nobody chose [10:15]-[11:19].
- Do not rely on a model to explain a system: "You need something deterministic to tell you what
  your code is doing" [14:21]; they say tooling for this at scale does not exist yet.
- Production agents that write lessons to memory after each incident; agents that start alert
  investigation and triage routing [18:25]-[21:33].
- Protect attention: constant think-wait-think cycles and multi-agent juggling cause burnout
  [29:51]-[32:58].

Evidence and numbers: anecdotes only (30 seconds versus hours; one customer's week-off practice).

Tools and files named: OpenCode, Elastic, ServiceNow, PagerDuty, Sentry, Datadog, CodeHealth (Adam
Tornhill), Glamorous Toolkit, GitHub Copilot.

Caveats: late-notice panel; opening minutes unintelligible in captions; panellists disagree on
whether hallucination will persist [22:40]-[25:47].

Relevance: medium. The lint-first rule, the feed-failures-into-the-harness rule and the time budget
are directly usable; the rest is operations at company scale.

### Dana Lawson - Built for Humans. Now Agents Are Here. (Dana Lawson, CTO Netlify, June 2026)
File: refs/videos/ItTJpQz35CY/transcript.md   URL: https://www.youtube.com/watch?v=ItTJpQz35CY

Thesis: Redesigning a platform so agents can operate it (structured errors, intent-level
operations, events, legible architecture) also made it better for human developers. Trust needs
sandboxing, a human approval point and an audit trail.

Practices:
- Make failure output parseable: "We restructured them into a structured format with
  machine-readable error codes." [15:25] alongside the human text.
- Give agents clear pass/fail signals, such as a preview deploy per change [08:17], [14:25].
- Make CLIs usable without interactive yes/no prompts [18:31].
- Expose intent-level operations rather than a 200-endpoint surface the agent must sequence
  [17:26].
- Write down tribal knowledge: "Critical workflows live in tribal knowledge and in someone's
  head." [16:26] Their system of record (blueprints): "Think of it as the CLAUDE.md files,
  AGENTS.md, the architecture decision records" [19:33]. "The goal isn't better documentation, it's
  ensuring agents can operate safely in complex systems." [19:33]
- Three trust principles: sandboxed execution, human in the loop by default ("The agent builds,
  the human approves" [20:34]), every action logged with rollback.

Evidence and numbers: IDC forecast of 500 million new applications by 2028; no internal metrics.

Tools and files named: Netlify Agent Runners, deploy previews, blueprints, CLAUDE.md, AGENTS.md,
ADRs; Claude Code, Cursor, Windsurf, v0, Bolt, Lovable, GitHub Copilot.

Caveats: partly a product pitch; she says she still does not fully trust agents [15:25], [20:34];
admits much generated software will be short-lived slop [26:42].

Relevance: medium. Structured errors, non-interactive commands and a written system of record are
cheap repo-level changes for a solo developer; the platform-design material is not.

### Jack Wotherspoon - Humans vs. Slop: Rewriting the Rules of Open-Source (Jack Wotherspoon, Google, June 2026)
File: refs/videos/HgA0spItnZI/transcript.md   URL: https://www.youtube.com/watch?v=HgA0spItnZI

Thesis: Generated code is nearly free to produce and expensive to review, which breaks the
open-source social contract. Maintainers respond with process gates, limits, checked-in context and
skills, and trust lists.

Practices:
- Issue first: "we require you to put up a issue first before you can put up a pull request"
  [12:20]; PRs without one are closed. "So this kind of eliminates 90% of those drive by" [12:20].
- Cap open PRs per external contributor (GitHub Actions, or the newer repository setting) [13:21].
- Non-AI automation: close items with no response after 60 days [14:23].
- Check in context files for more than your own tool (AGENTS.md or a symlink) with a few plain
  lines: "run the tests, follow the PR template" [15:24].
- Check in skills that codify maintainer steps: a PR-creator skill (reads the template, inspects
  the diff, runs tests, formats), a docs-writer skill enforcing the style guide, a code-review
  skill [16:26].
- Decide which skills are on by default with a usage test: "what would you use over 50% of the
  time?" [30:47]; the rest become slash commands or rules.
- Attach Playwright screenshots or video to PRs via a personal skill [17:28].
- Add a section for agents to CONTRIBUTING, and state expected review turnaround [23:37],
  [25:38].
- Other maintainers' tactics: `open source vacation` (auto-close during set periods, used by the
  Pi coding agent's maintainer), vouch (allow and deny lists of GitHub handles in a checked-in
  file, from Mitchell Hashimoto, used in Ghostty), and accepting prompts instead of code
  [17:28]-[21:32].

Evidence and numbers: see (f). "Generating code is free like we talked about, but maintaining it
is not." [07:09]

Tools and files named: Gemini CLI, Google ADK, GitHub Actions, PR templates, CONTRIBUTING,
AGENTS.md, skills (PR creator, docs writer, code review), Playwright, vouch (file extension
captioned `TD`, unsure), Ghostty, Pi coding agent, curl (flooded with fake security reports),
`/go` (a long-running mode, caption unsure).

Caveats: agents do not reliably follow context files (`that's a different ball game` [14:23]); the
90% and 200 million figures are estimates or hearsay; he has not adopted prompts-as-PRs.

Relevance: medium to high. Contributor controls matter only for public repos, but the multi-harness
context file, checked-in skills, the 50% rule and visual PR evidence apply to every repo.

### Brian Douglas - The beginners guide to training AI on your own code (Brian Douglas, Paper Compute, June 2026)
File: refs/videos/o-IunU6b1t8/transcript.md   URL: https://www.youtube.com/watch?v=o-IunU6b1t8

Thesis: Agent sessions are discarded every few hours although they hold what was learned. Record
them, turn recurring patterns into observations and skills, and only then consider fine-tuning a
small model for narrow tasks. Vendor of the recording tool, which is open source.

Practices:
- Give a long-running agent periodic checkpoints it can look back at (a screenshot every ten
  turns) [04:04].
- Do not trust an agent's own progress report: "it was just politely hallucinating progress"
  [05:06]; the missing piece was one instruction (talk to characters in the game).
- Keep a memory folder of agent-written, human-readable observations per session plus a small
  state file of learned rules, then discuss blockers with the agent [06:07]-[08:11].
- Stop losing sessions: "But we never learned from the last five hours of sessions." [09:13]
  Harness session files are deleted after 30 days [10:16].
- Mine sessions for anomalies in both directions: clusters of tool-call failures, and unusually
  frequent skill use [15:24].
- Generate a first-draft skill from searched sessions with a small model, then "go read it as a
  human with your human eyes" [21:33], then track how often it is invoked.
- A `check the tapes` skill answers why a past decision was made and can rebuild prompts and
  intent into GitHub issues [17:25]-[18:27].
- Use cheap models for rote, parallel sweeps, run overnight or at weekends [13:21].
- Treat skills as the way to move between harnesses: "you can just transfer the skills of the
  Codex or Pi coder or anything else" [29:52].

Evidence and numbers: see (f). "I fixed all lint errors that I was avoiding for years." [14:22]
in under an hour; 77,000 sessions; DPO on a 4B model: "Not good. Not even worth it." [27:47]

Tools and files named: tapes.dev, tapes deck, Stereo (agent runtime with VMs), sweeper agent,
PyBoy (caption: `PyGameBoy`), Kafka, SQLite then Postgres, Claude Code, Codex, Haiku, Qwen, QLoRA,
Unsloth, PyTorch, Karpathy's autoresearch repo; observational-memory idea credited to a blog post
(caption: `master`, probably Mastra, unsure).

Caveats: ten parallel agents got his Anthropic account suspended [14:22]; raw session capture
includes any secrets typed into prompts [19:30]-[20:31]; the tool did not support Codex at the time
[30:53]; fine-tuning is a side project and not a replacement for a frontier model [25:40].

Relevance: medium. Session mining to create and audit skills suits a solo developer across many
repos; the fine-tuning half does not.

### Meta, Stanford and Odevo on Agentic Coding at Scale (compilation clip, published after June 2026)
File: refs/videos/jfTltMo0TMg/transcript.md   URL: https://www.youtube.com/watch?v=jfTltMo0TMg

Thesis: Excerpts from THOMAS, ODEVO and FOXWELL already covered above, plus a Stanford segment
(speaker names garbled): a study across 150,000 engineers sees the widest performance spread yet,
and "people that know how to create agents, people that know how to work, they they achieve
significantly better outcomes" [03:01].
Evidence: a rank-stability number said to fall from 0.70 to 0.45 [04:02], too garbled to rely on.
Relevance: low. Nothing new and actionable beyond the full talks.

### Meta's VR Codebase Nobody Wanted to Touch - Until This (compilation clip, published after June 2026)
File: refs/videos/UVOkQyeY16M/transcript.md   URL: https://www.youtube.com/watch?v=UVOkQyeY16M

Thesis: Excerpts from ROBERTS, BATEY and THOMAS, plus Simon Martinelli on modernisation: "I extract
use case and entity model from code and tests and documentation" [02:04], business people review
it, and new code is generated from that spec; direct translation is lift and shift, whereas
"Modernization is rethinking how people are working with the software" [03:04].
Practice: with a reviewed spec in hand, new features can be added during modernisation, which older
same-system-new-technology rules forbade [04:07].
Relevance: medium for the Martinelli segment (spec extraction before rewriting); the rest
duplicates the full talks.

### Netlify's Dana Lawson: 'We Ain't Precious No More' (compilation clip, published after June 2026)
File: refs/videos/G5mAl_QBr4w/transcript.md   URL: https://www.youtube.com/watch?v=G5mAl_QBr4w

Thesis: Excerpts from DUBNOV and LAWSON, plus two new segments. Marc Sloan (Tessl): an agent given a
ticket, a Figma design and engineering skills shipped an export button using a generic component
instead of the dedicated one that carried accessibility and async behaviour; every check passed, yet
"the product and design context was missing from the agent" [03:06]. Emma Burrows (Rezonant):
product managers should become agent orchestrators, which needs a defined human-agent control
plane [07:13]-[09:18].
Practice (Inference from Sloan): component-choice and design-system rules belong in agent context,
because tests and CI will not catch a wrong-but-working component.
Relevance: medium for the Sloan failure case; low otherwise.

### Uber Burned 6x Its AI Budget in Four Months (compilation clip, published after June 2026)
File: refs/videos/nnja7kk4EPM/transcript.md   URL: https://www.youtube.com/watch?v=nnja7kk4EPM

Thesis: Four cost-related excerpts: prompt caching and cache-aware routing (Kushwaha, Nvidia), the
Uber and $18-per-$100 claims (DUBNOV, repeated), local open-weight models for most work (Marsden,
Helix ML), and eval-gated automatic skill updates (Groetzinger, Cisco).

Practices:
- Keep the conversation prefix cacheable; on multi-replica serving, route each turn to the replica
  that holds the cache: "caching becomes kind of a must have in most of these agentic developments"
  [01:02].
- Marsden's review loop: read the spec, "I find the two lines in the spec where the agent got it
  wrong" [05:09], comment on those lines, let the agent carry the change to a near-mergeable PR that
  includes screenshots and a link to the spec [06:10].
- Marsden's cost position: open-weight models "can now do pretty much 80% of the work that you
  need to do" [06:10]; build for easy switching between agents and models and burst to a frontier
  model for hard tasks [07:11].
- Cisco's pipeline: source doc change, model classifies size of change, rewrites the skill, runs
  evals. "If it's a minor change, just changing a typo or wording and the evils pass, I don't
  really need to have my human gate." [09:15] (my reading: evals). Major change or new topic: human
  review and a new eval that states what success looks like.
- Cisco's warning: agent-built memories drift from the source documents and destroy trust when an
  answer contradicts the article it cites [08:14].

Evidence and numbers: 80% (Marsden's estimate); eight GPUs; Uber and $18 figures as in DUBNOV.

Tools and files named: GLM 5.1, Claude Opus 4.8, RTX 6000-class GPUs (caption: `RTX six K pros`),
GitHub Actions (as analogy), skills, evals.

Caveats: short excerpts without the surrounding talks; Marsden sells a product in this space; the
hardware advice is aimed at organisations.

Relevance: medium to high. The eval-gated skill-update pipeline and memory-drift warning bear
directly on keeping a shared skill set current; caching and routing bear on cost.
