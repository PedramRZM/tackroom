# Claude Code docs: mechanisms that carry instructions and extend the agent (reference digest)

Scope: project-level configuration for a template synced into many repos. No user-level config.
Sources: saved doc pages under `refs/articles/code.claude.com/docs-en-<slug>-md/article.md`, all
fetched 2026-11-10 (per each `meta.json`). Installed Claude Code: 2.1.322. Only the saved text is
treated as truth; nothing here comes from memory.

Citation format: `[slug > Section heading]`, where `slug` is the folder name without the
`docs-en-` prefix and `-md` suffix (so `[memory > Import additional files]` is
[`refs/articles/code.claude.com/docs-en-memory-md/article.md`](https://code.claude.com/docs/en/memory.md), section "Import additional files").
Quotes are verbatim and under 25 words. "Inference:" marks anything not stated by the docs.

Sources read: 34 pages in full, 1 page in part (settings-reference, plugin keys only). The list,
and the pages not read, are at the end under "Sources read". Sections: 1 instruction files,
2 skills, 3 subagents, 4 orchestration and loops, 5 plugins, 6 styles/worktrees/checkpoints/
sessions, 7 context window and caching, then (a) decisions, (b) user-level-only, (c) changed
recently, (d) ambiguities.

---

## 1. Instruction files: CLAUDE.md, CLAUDE.local.md, AGENTS.md, imports, rules, auto memory

### 1.1 What they are for

- CLAUDE.md: "instructions you write to give Claude persistent context" [memory > intro]. Both
  CLAUDE.md and auto memory "are loaded at the start of every conversation. Claude treats them as
  context, not enforced configuration." [memory > CLAUDE.md vs auto memory]
- Delivery: "CLAUDE.md content is delivered as a user message after the system prompt, not as part
  of the system prompt itself." [memory > Claude isn't following my CLAUDE.md]
- To enforce rather than advise: "To block an action regardless of what Claude decides, use a
  PreToolUse hook instead." [memory > CLAUDE.md vs auto memory]
- What belongs: "facts Claude should hold in every session: build commands, conventions, project
  layout, \"always do X\" rules." Multi-step procedures or part-of-codebase items go to a skill or
  a path-scoped rule. [memory > When to add to CLAUDE.md]
- When to add an entry: Claude repeats a mistake, review catches something it should have known,
  you retype the same correction, or a new teammate would need it. [memory > When to add to CLAUDE.md]

### 1.2 Locations and load order (CLAUDE.md)

Listed "in load order, from broadest scope to most specific" [memory > Choose where to put CLAUDE.md files]:

| Scope | Location | Project-level? |
| - | - | - |
| Managed policy | macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`; Linux/WSL `/etc/claude-code/CLAUDE.md`; Windows `C:\Program Files\ClaudeCode\CLAUDE.md` (or the `claudeMd` key in `managed-settings.json`, honoured in managed/policy settings only) | No |
| User | `~/.claude/CLAUDE.md` | No |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Yes (commit) |
| Local | `./CLAUDE.local.md` (create manually, gitignore) | Yes, but personal and uncommitted |

- Ancestors load at launch: Claude Code loads `CLAUDE.md` and `CLAUDE.local.md` "from your current
  working directory and every directory above it." [memory > How CLAUDE.md files load]
- Concatenated, not overriding: "All discovered files are concatenated into context rather than
  overriding each other." Order is filesystem root down to the working directory; within a
  directory `CLAUDE.local.md` is appended after `CLAUDE.md`. [memory > How CLAUDE.md files load]
- Nested/child directory files load lazily: a subdirectory `CLAUDE.md`/`CLAUDE.local.md` loads
  "once Claude reads, writes, or edits another file in that subdirectory", including a Bash
  command that counts as a read "such as `cat` or `head` on a single file".
  [memory > How CLAUDE.md files load]
- A nested file does not show under Memory files in `/context all`; "a `Loaded` line with its path
  appears in the terminal" when it loads. To test, create it from the shell, not via Claude.
  [memory > Claude isn't following my CLAUDE.md]
- `--add-dir` directories: their CLAUDE.md files "are not loaded" by default; set
  `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` to load their `CLAUDE.md`, `.claude/CLAUDE.md`,
  `CLAUDE.local.md` and `.claude/rules/*.md` (except rules with `paths`).
  [memory > Load from additional directories]
- HTML comments: block-level `<!-- ... -->` comments "are stripped before the content is injected
  into Claude's context"; comments inside code blocks are kept; the Read tool still shows them.
  [memory > How CLAUDE.md files load]
- Monorepo opt-out: `claudeMdExcludes` (array of globs matched "against absolute file paths"),
  settable at user, project, local or managed layer, arrays merge; cannot exclude the managed
  file. [memory > Exclude specific CLAUDE.md files]
- Verify loading with `/context all` (Memory files list) and `/memory`; the `InstructionsLoaded`
  hook logs which files load, when and why. [memory > Set up a project CLAUDE.md; Claude isn't following my CLAUDE.md]

### 1.3 Size limits and compaction (CLAUDE.md and rules)

- Target: "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce
  adherence." [memory > Write effective instructions]
- Hard limit at launch: Claude gets the whole of each launch-loaded CLAUDE.md "as long as the file
  is 4 MiB or smaller. Claude Code skips a file over 4 MiB and loads none of it."
  [memory > How it works (note)]
- Warnings: an instruction file over the recommended length triggers a warning at startup and in
  `/status`; there is also a warning when files "add up past a combined limit at session start.
  Each CLAUDE.md, rules file, and `@path` import counts as a separate file." The combined limit's
  number is not stated. [memory > My CLAUDE.md is too large]
- On-demand files are truncated: a subdirectory CLAUDE.md/CLAUDE.local.md (and its imports), a
  subdirectory's `.claude/rules/` files, and path-scoped rules (project or user) over the per-file
  limit deliver only their start plus a note to Read the rest. Limits: 200K window = 40,000
  characters; 1M window = 200,000 characters on Opus 4.6 / Sonnet 4.6 and 150,000 on later models.
  "Before v2.1.309, Claude Code didn't apply this limit to files that load on demand."
  [memory > Claude ignores the end of my subdirectory CLAUDE.md]
- Compaction: "Project-root CLAUDE.md survives compaction: after `/compact`, Claude re-reads it
  from disk and re-injects it into the session." Nested CLAUDE.md files and `paths:` rules "load
  again on demand". [memory > Instructions seem lost after /compact]
- Writing style: concrete and verifiable ("Use 2-space indentation" not "Format code properly"),
  markdown headers and bullets, no contradictions: "if two instructions contradict each other,
  Claude may pick one arbitrarily." [memory > Write effective instructions]
- Audit: `/doctor prompt-audit` (v2.1.283+) checks CLAUDE.md, CLAUDE.local.md, AGENTS.md, rules,
  skills, commands, subagents and output styles under `.claude/` and `~/.claude/` for outdated or
  conflicting content; it runs through the bundled `/claude-api` skill. `/doctor` proposes trims
  that cut "content Claude can derive from the codebase". [memory > Audit your instruction files; My CLAUDE.md is too large]
- Built-in guidance can compete: if CLAUDE.md sets commit/PR rules, "turn off the built-in ones
  with `includeGitInstructions`" and set `attribution`. [memory > Claude isn't following my CLAUDE.md]

### 1.4 `@` imports

- Syntax `@path/to/import` anywhere in CLAUDE.md; "Imported files are expanded and loaded into
  context alongside the CLAUDE.md that references them." [memory > Import additional files]
- Paths: relative and absolute allowed; relative paths "resolve relative to the file containing
  the import, not the working directory." [memory > Import additional files]
- Depth: recursive imports "with a maximum depth of four hops". [memory > Import additional files]
- Spaces: backslash-escape each space; "A path wrapped in quotes isn't imported at all".
  [memory > Import additional files]
- Not parsed inside code: "Import parsing skips Markdown code spans and fenced code blocks." Wrap a
  mention in backticks (`` `@README` ``) to keep it literal. [memory > Import additional files]
- No context saving: imports "help you organize a long file but don't reduce its context cost".
  [memory > Write effective instructions]
- External imports (path resolves outside the working directory) in a project-level file trigger a
  one-time approval dialog: "If you decline, the imports stay disabled and the dialog doesn't
  appear again." [memory > Import additional files (warning)]
  Inference: a template must not rely on imports of files outside the repo (for example
  `@~/.claude/...`), both because of the dialog and because the user wants no user-level state.

### 1.5 AGENTS.md and how it interacts with CLAUDE.md

- Direct reading requires v2.1.277+ ("Reading `AGENTS.md` directly requires Claude Code v2.1.277 or
  later"). [memory > AGENTS.md (note)]
- Default behaviour (`claude-md-or-agents-md`) [memory > AGENTS.md; When Claude Code reads AGENTS.md]:
  - AGENTS.md only, no CLAUDE.md/CLAUDE.local.md at or above cwd: Claude reads AGENTS.md.
  - Both present: "Your `CLAUDE.md` files only".
  - CLAUDE.md that imports AGENTS.md: CLAUDE.md with AGENTS.md included through the import.
- Files that suppress AGENTS.md: "a `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in your
  working directory or any directory above it". Files that do not suppress it and keep loading
  alongside: `~/.claude/CLAUDE.md`, managed CLAUDE.md, `.claude/rules/` files.
  [memory > When Claude Code reads AGENTS.md]
- Gotcha: a personal `CLAUDE.local.md` "stops Claude from reading `AGENTS.md` for you" under the
  default. [memory > When Claude Code reads AGENTS.md (note)]
- What is read when AGENTS.md is active: every `AGENTS.md` and `.claude/AGENTS.md` at cwd and
  above at session start; a subdirectory's `AGENTS.md` when Claude opens a file there with the
  Read tool and that subdirectory has none of the three CLAUDE.md files; `@path` imports inside it
  are expanded; `claudeMdExcludes` applies. Listed as not read: `AGENTS.local.md`,
  `AGENTS.override.md`, "or anything under a `.agents/` directory".
  [memory > When Claude Code reads AGENTS.md]
- Setting "Project instructions" (in `/config`), values: `claude-md-or-agents-md` (default),
  `claude-md-and-agents-md` (each directory's CLAUDE.md first, AGENTS.md after; an AGENTS.md
  already imported or symlinked is not read twice), `claude-md`, `managed-only`.
  [memory > Choose which instruction files load]
- USER-LEVEL ONLY: the settings-file form is `pluginConfigs` > `cc-plugin-agents-md@builtin` >
  `options.instructionFiles`, and Claude Code "ignores it in project and local settings files"
  (read from `~/.claude/settings.json`, a `--settings` file, or managed settings). Before v2.1.285
  the plugin ID was `agents-md@builtin`. [memory > Choose which instruction files load]
- Differences from CLAUDE.md when read through the setting: `InstructionsLoaded` hooks do not
  fire; `--add-dir` directories' AGENTS.md does not load; an external `@path` import loads only if
  already approved, with no prompt. [memory > Where AGENTS.md differs from CLAUDE.md]
- Unavailable when: version before v2.1.277; the built-in plugin was disabled with `/plugin`; in
  some cases the first session after upgrading from v2.1.276 or earlier. Before v2.1.281 Bedrock
  or telemetry-disabled sessions read CLAUDE.md only. [memory > When AGENTS.md support is unavailable]
- The portable, project-level way to share one file: a `CLAUDE.md` next to `AGENTS.md` containing
  `@AGENTS.md`, with Claude-specific instructions below the import ("Claude reads the imported file
  first, then the rest"). "Keeping the import never makes Claude read `AGENTS.md` twice".
  [memory > Share one file with other coding tools; Remove an earlier AGENTS.md workaround]
- Symlink alternative (`ln -s AGENTS.md CLAUDE.md`) has two costs: Edit/Write "refuse to write
  through a symlink", and on Windows Git may check the symlink out as a one-line text file; the
  docs say "use the `@AGENTS.md` import instead" there. [memory > Share one file with other coding tools]
- Anti-patterns named: a CLAUDE.md that tells Claude in words to read AGENTS.md ("Claude sees
  `AGENTS.md` only if it decides to open the file"), and a `SessionStart` hook that prints
  AGENTS.md (adds a second copy). [memory > Remove an earlier AGENTS.md workaround]
- `/init` reads `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`; with
  `CLAUDE_CODE_NEW_INIT=1` also `AGENTS.md`, `.devin/rules/`, `.windsurf/rules/`, `.windsurfrules`,
  `.clinerules`. `/import` copies another agent's config once. [memory > Migrate instructions from other tools]

### 1.6 `.claude/rules/*.md`

- Purpose: modular topic files; path-scoped rules "only load into context when Claude works with
  matching files, reducing noise and saving context space." [memory > Organize rules with .claude/rules/]
- Discovery: "All `.md` files are discovered recursively", so subdirectories work. One topic per
  file, descriptive filename. [memory > Set up rules]
- Locations: project `.claude/rules/` (project-level), user `~/.claude/rules/`. User rules load
  before project rules; "Neither set overrides the other". [memory > User-level rules]
- Loading without `paths`: "loaded at launch with the same priority as `.claude/CLAUDE.md`."
  [memory > Set up rules]
- Loading with `paths`: "loads when Claude uses the Read, Write, or Edit tool on a matching file",
  and on a Bash command that counts as a read (`cat`/`head` on a single file).
  [memory > Path-specific rules]
- Frontmatter: `paths` is the only field. "`paths` is the only field Claude Code reads from a rule;
  any other field is ignored without an error." Type: YAML list or comma-separated string; not
  required. Frontmatter is removed before the rule enters context. Unparseable YAML: the rule
  loads as if it had no `paths` (so it becomes always-on); `claude --debug` shows the error.
  [memory > Rule frontmatter reference]
- Pattern base: project rules are relative to "the directory that contains the rule's `.claude`
  folder"; user rules relative to the primary working directory. [memory > Path-specific rules]
- Glob semantics: `**/*.ts` anywhere; `*.md` matches `.md` files anywhere under the base;
  `/*.md` only directly in the base; brace expansion `{ts,tsx}` supported; a rule's `paths` list
  shares "one budget of 1,000 expanded patterns and 4 MiB"; an invalid `[` pattern matches
  nothing; escape a literal `[` as `\[`. [memory > Path-specific rules]
- Symlinks: `.claude/rules/` supports symlinks, but a target outside the working directory is
  treated like an external import: approval needed once per project, "and after that only the
  ones without a `paths` field load." Network-path targets never load.
  [memory > Share rules across projects with symlinks]
  Inference: symlinked shared rules are a poor distribution mechanism for a template (approval
  dialog, loss of `paths`); copied files avoid both.
- `--setting-sources` without `project` skips project rules (since v2.1.211 this includes
  on-demand rules). [memory > Set up rules]
- Rules vs skills: "Rules load into context every session or when matching files are opened."
  For task-specific instructions "that don't need to be in context all the time, use skills
  instead".
  [memory > Organize rules with .claude/rules/ (note)]
- Per-file truncation for path-scoped rules: see 1.3.

### 1.7 Auto memory

- What: "notes Claude writes itself based on your corrections and preferences" [memory > intro].
  Four `type` values in memory-file frontmatter: `user`, `feedback`, `project`, `reference`.
  Claude skips what it can derive from the codebase and what CLAUDE.md already says.
  [memory > Auto memory]
- Storage: `~/.claude/projects/<project>/memory/` with a `MEMORY.md` index plus one topic file per
  memory; `<project>` "is derived from the git repository, so all worktrees and subdirectories
  within the same repo share one auto memory directory." "Auto memory is machine-local."
  [memory > Storage location]
- Listed as "Global only", not committed. [claude-directory > File reference]
- Loaded: "The first 200 lines of `MEMORY.md`, or the first 25KB, whichever comes first, are loaded
  at the start of every conversation." Topic files are read on demand. Over-limit writes succeed
  but return an error telling Claude to rewrite the index. [memory > How it works]
- Default: "Auto memory is on by default in local sessions." Off by default in self-hosted
  environment sessions (outside Claude Tag). [memory > Enable or disable auto memory]
- Disable per project (project-level, committable): `"autoMemoryEnabled": false` in "that
  project's settings". Also `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` (environment variable; the page
  does not say whether a project settings `env` block is honoured for it). The `/memory` toggle
  writes `autoMemoryEnabled` to user settings. [memory > Enable or disable auto memory]
- Relocate: `autoMemoryDirectory`, "read from any settings scope: user, project, local, policy, or
  `--settings`"; "The value must be an absolute path or start with `~/`." In project/local
  settings it is honoured "under the same workspace trust rule as hooks in settings files", and
  with `permissions.blockReadsOutsideWorkingDirectories` on, no auto memory is loaded from or
  saved to a directory a repository-supplied settings file chooses. [memory > Storage location]
  Inference: because a relative path is not accepted, a committed setting cannot portably point
  auto memory into the repo itself; for the no-global-state goal the checkable option is
  `autoMemoryEnabled: false` in `.claude/settings.json`.
- Retention: memory files are excluded from the `cleanupPeriodDays` sweep. `claude purge` deletes
  "Transcripts and auto memory under `projects/`". [memory > Storage location; claude-directory > Clear local data]
- Subagents: main-conversation auto memory "isn't loaded into subagents" except a fork; a
  subagent's own memory (`memory` field) is separate. [memory > How it works]
- Requests to remember something go to auto memory; to put it in CLAUDE.md instead, ask Claude
  directly, like "add this to CLAUDE.md,".
  [memory > View and edit with /memory]

### 1.8 The `.claude` directory map (what is project-level)

From [claude-directory > File reference] (Scope / Commit columns):

| File | Scope | Commit |
| - | - | - |
| `CLAUDE.md` | Project and global | yes |
| `rules/*.md` | Project and global | yes |
| `settings.json` | Project and global | yes |
| `settings.local.json` | Project only | no (gitignored when Claude Code saves a setting to it) |
| `.mcp.json` | Project only | yes |
| `.worktreeinclude` | Project only | yes |
| `skills/<name>/SKILL.md` | Project and global | yes |
| `commands/*.md` | Project and global | yes ("Single-file prompts; same mechanism as skills") |
| `output-styles/*.md` | Project and global | yes |
| `agents/*.md` | Project and global | yes |
| `workflows/*.js` | Project and global | yes |
| `agent-memory/<name>/` | Project and global | yes |
| `~/.claude.json` | Global only | no |
| `projects/<project>/memory/` | Global only | no |
| `keybindings.json` | Global only | no |
| `themes/*.json` | Global only | no |

- Project-scope files live "under `.claude/` (or at the root for `CLAUDE.md`, `.mcp.json`, and
  `.worktreeinclude`)". [claude-directory > File reference]
- `AGENTS.md` may sit at "Project root, `.claude/`, or any directory". [claude-directory > What's not shown]
- Frontmatter field names per file type (full field detail in sections 2, 3, 6)
  [claude-directory > Frontmatter fields by file]:
  - `skills/<name>/SKILL.md`: `name`, `description`, `when_to_use`, `argument-hint`, `arguments`,
    `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`,
    `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`,
    `compatibility`
  - `commands/*.md`: "The skill fields except `name` and `paths`"
  - `agents/*.md`: `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`,
    `maxTurns`, `autoCompactWindow`, `skills`, `mcpServers`, `hooks`, `memory`, `background`,
    `effort`, `isolation`, `color`, `initialPrompt`, `omitClaudeMd`, `experimental`
  - `output-styles/*.md`: `name`, `description`, `keep-coding-instructions`, `force-for-plugin`
  - `rules/*.md`: `paths`
- Overrides to anything in project files: managed settings, CLI flags such as `--permission-mode`
  or `--settings`, and some env vars. [claude-directory > File reference (note)]
- Transcripts hold the system prompt, tool definitions and "The instruction files it loaded, such
  as CLAUDE.md", in plaintext under `~/.claude/projects/`. [claude-directory > Application data]
- Session scratchpad (temp files without permission prompts) lives under the temp dir
  (`/tmp/claude-<uid>/<project>/<session-id>/scratchpad/` on Linux), only when signed in with a
  claude.ai account on the Anthropic API and `enableArtifact` is not `false`.
  [claude-directory > Session scratchpad directory]

### 1.9 Which mechanism for what (features-overview tables)

- "When to use it" column [features-overview > Match features to your goal]:
  - CLAUDE.md: "Project conventions, \"always do X\" rules"
  - Output style: a voice, length or format wanted in every response, or a non-engineering role
  - Skill: "Reusable content, reference docs, repeatable tasks"
  - Subagent: "Context isolation, parallel tasks, specialized workers"
  - Dynamic workflow: "Work that outgrows a handful of subagents, or findings you want cross-checked"
  - MCP: "External data or actions"
  - Hook: "Automation that must run on every matching event"
  - Plugin: "Use plugins when you want to reuse the same setup across multiple repositories" or
    to distribute through a marketplace.
- Triggers, in the order "most teams add them" [features-overview > Build your setup over time]:
  convention wrong twice -> CLAUDE.md; keep asking for shorter/same format -> output style; same
  prompt typed to start a task -> user-invocable skill; same playbook pasted a third time -> skill;
  copying data from a tab Claude cannot see -> MCP server; many file reads to find a symbol ->
  code intelligence plugin; side task floods the conversation -> subagent; "You want something to
  happen every time without asking" -> hook; "A second repository needs the same setup" ->
  "Package it as a plugin".
- CLAUDE.md vs rules vs skills [features-overview > Compare similar features]:

  | Aspect | CLAUDE.md | `.claude/rules/` | Skill |
  | - | - | - | - |
  | Loads | Every session | Every session, or when matching files are opened | On demand, when invoked or relevant |
  | Scope | Whole project | Can be scoped to file paths | Task-specific |
  | Best for | Core conventions and build commands | Language-specific or directory-specific guidelines | Reference material, repeatable workflows |

- Rule of thumb: "Keep CLAUDE.md under 200 lines. If it's growing, move reference content to
  skills or split into `.claude/rules/` files." [features-overview > Compare similar features, CLAUDE.md vs Skill]
- Hook vs skill: hook "Fires on its event without Claude deciding"; skill "Claude interprets the
  instructions; outcome can vary". Context cost: hook "Zero unless the hook returns output"; skill
  "Description loads each session; full content loads when used".
  [features-overview > Compare similar features, Hook vs Skill]
- Guardrails: "An instruction like \"never edit `.env`\" in CLAUDE.md or a skill is a request, not
  a guarantee." "If a rule must hold every time, make it a hook rather than a prompt instruction."
  [features-overview > Compare similar features, Hook vs Skill]
- Skill vs subagent: skill "Adds to your main window"; subagent "Uses a separate window with its
  own input and output tokens". They combine: a subagent preloads skills (`skills:`), a skill runs
  isolated with `context: fork`. [features-overview > Compare similar features, Skill vs Subagent]
- Subagent vs dynamic workflow: "With subagents, Claude decides turn by turn what runs next. In a
  workflow, the script decides". [features-overview > Compare similar features, Subagent vs Dynamic workflow]
- Layering when a feature exists at several levels [features-overview > Understand how features layer]:
  - CLAUDE.md: additive; "When instructions conflict, Claude uses judgment to reconcile them."
  - Skills and subagents override by name: "managed > user > project for skills; managed > CLI
    flag > project > user > plugin for subagents". Plugin skills are namespaced.
  - MCP servers override by name: "local > project > user".
  - Hooks merge: "all registered hooks fire for their matching events regardless of source."
  Note for a project-only template: a user-level skill with the same name as a template skill
  wins over the project one (see 2.2), whereas a project subagent wins over a user one.
- Context cost by feature [features-overview > Context cost by feature]:

  | Feature | When it loads | What loads | Context cost |
  | - | - | - | - |
  | CLAUDE.md | Session start | Full content of each file that loads at session start | Every request |
  | Output styles | Session start, and again on switch | The active style's full instructions; nothing for Default | Every request |
  | Skills | Session start + when used | Descriptions at start, full content when used | Low (descriptions every request) |
  | MCP servers | Session start | Tool names; full schemas on demand | Low until a tool is used |
  | Code intelligence | After file edits and on demand | Diagnostics after edits; symbol locations on lookup | Low |
  | Subagents | When spawned | Fresh context with specified skills, or parent conversation for a fork | Isolated from main session |
  | Hooks | On trigger | Nothing (runs externally) | Zero, unless hook returns additional context |

- Too much context is also a quality problem: it "can also add noise that makes Claude less
  effective; skills may not trigger correctly, or Claude may lose track of your conventions."
  [features-overview > Understand context costs]
- Skill selection failure mode: "If descriptions are vague or overlap, Claude may load the wrong
  skill or miss one that would help." [features-overview > Understand how features load, Skills]
- Tip: "Use `disable-model-invocation: true` for skills with side effects. This saves context and
  ensures they run only when you name them." [features-overview > Understand how features load, Skills]
- What a subagent's fresh context contains: its own system prompt ("not the Claude Code system
  prompt"), full content of `skills:` entries, CLAUDE.md and git status (Explore and Plan start
  with neither; `omitClaudeMd` drops user, project and local CLAUDE.md), and whatever the lead
  passes in the prompt. [features-overview > Understand how features load, Subagents]
- MCP: tool names and server instructions load at start; "Full JSON schemas stay deferred until
  Claude needs a specific tool." Tool search is on by default.
  [features-overview > Understand how features load, MCP servers]

### 1.10 Best-practices page: what to write down, what to enforce

- Two kinds of instruction: non-deterministic (prompt, `CLAUDE.md`, skill; "there's no
  *guarantee* that it'll follow your instructions") and deterministic (hook, deny rule, managed
  setting; "Claude Code applies this every time, no matter what the model decided to do").
  [best-practices > Deterministic and non-deterministic instructions]
- The docs' matrix [best-practices > Deterministic and non-deterministic instructions]:

  | | Non-deterministic (Claude decides) | Deterministic (Claude Code enforces) |
  | - | - | - |
  | What to do | Your prompt, `CLAUDE.md`, skills Claude picks up itself | Hooks, and which skills only you can start |
  | What it can touch | Auto mode's classifier | Deny rules, the sandbox in strict mode, managed settings |
  | When it's done | A request for evidence, `/goal`, `/code-review` | Tests, typecheck, a `Stop` hook, CI |
  | How much it spends | Effort level, Claude's own pace | `--max-turns` or `--max-budget-usd` with `-p`, a spend limit |
  | Who has the last word | Claude's summary of what it did | Branch protection, a person who approves the merge |

- Default to letting Claude decide: "Most of the time, you want Claude to decide."
  [best-practices > Deterministic and non-deterministic instructions]
- Signal to move a line to a hook: "If you keep adding emphasis to a `CLAUDE.md` line and Claude
  still misses it, that's a sign the line belongs in a hook." And the reverse: hooks for mere
  preferences should be deleted. [best-practices > Deterministic and non-deterministic instructions (tip)]
- What to write down: "Only write down what Claude can't find by reading the repo, or what it
  would otherwise spend time rediscovering every session." Two-question test: "Could it find this
  by reading the code?" and "Would it actually go and look?" If both yes, leave it out.
  [best-practices > Tell Claude what it can't see]
- CLAUDE.md content list: exact test/typecheck/lint commands and how to run a single test file;
  places where the code is misleading; decisions not in the repo; "Anything you've had to correct
  twice already". Reason: "every line in it takes a little of Claude's attention on *every* task,
  whether it's relevant or not." [best-practices > Keep CLAUDE.md short]
- "the single most useful line in your `CLAUDE.md` is the command that runs" the check.
  [best-practices > Give Claude a check to run]
- CLAUDE.md gives the command; enforcement is a `Stop` hook: "A line like `Always typecheck before
  you finish` in this file works most of the time, not every time." [best-practices > Keep CLAUDE.md short]
- Emphasis is an anti-pattern: "adding IMPORTANT probably won't fix it." Either "the file has
  grown long enough that the line gets lost, or the line is a rule that can't have exceptions".
  [best-practices > Keep CLAUDE.md short (note)]
- Path rule guidance: "If a rule only matters in one part of the codebase, put it in
  `.claude/rules/` with a `paths:` filter". [best-practices > Scope rules to one part of the codebase]
- Skills: team procedures go in `.claude/skills/<name>/SKILL.md`; "The `CLAUDE.md` rule applies to
  skills too: only write down what Claude can't find on its own." Side-effect workflows get
  `disable-model-invocation: true`. [best-practices > Put team procedures in skills]
- CLI before MCP: "If that system has a CLI, that's usually the easiest way in." Connected MCP
  servers "add their tool names and instructions to the context even when you're not using them".
  [best-practices > Connect the tools Claude needs]
- Verification ladder, weakest to strongest: prompt ("keep going until they pass"), `/goal`
  condition, `Stop` hook (exit code 2 blocks; stderr goes back to Claude), independent
  `/code-review` in a fresh subagent. Always "ask Claude for *evidence*: the command it ran and its
  output, or the screenshot." [best-practices > Give Claude a check to run]
- Stop hook cap: "If the hook blocks eight stops in a row with no tool call between them, Claude
  Code overrides the next block and ends the turn." Raise with `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.
  [best-practices > Enforce the check with a Stop hook]
- Reviewer prompts should say "skip style": "A reviewer that's asked to find problems will always
  find *something*." [best-practices > Review against your spec (note)]
- Real enforcement uses `command` or `http` hooks: "A `prompt` or `agent` hook asks *another
  model* to decide, so it isn't deterministic either." Add `onFailure: "block"` if the action
  must be stopped when the hook itself crashes or times out. [best-practices > Enforce steps with hooks]
- Hook restraint: "a hook is for a rule with *zero* exceptions". "If you ever find yourself at
  forty of them, most are probably preferences". [best-practices > Enforce steps with hooks; Choose who a rule applies to]
- Deny rules: "`deny` rules hold in every permission mode, including auto and
  `bypassPermissions`". A `Read` deny catches `cat .env` but "won't catch a script that opens the
  file"; a `WebFetch` deny does nothing about `curl` unless the sandbox is on.
  [best-practices > Limit access with permission rules and the sandbox]
- Project settings and trust: for committed `.claude/settings.json`, "Its deny rules apply right
  away. Its `allow` rules wait until each person accepts the trust dialog", and workspace trust
  decides when its hooks start running. [best-practices > Choose who a rule applies to]
- USER-LEVEL ONLY: "The `autoMode` block also has to live in `~/.claude/settings.json` rather than
  the project, because the classifier ignores `autoMode` in project settings."
  [best-practices > Change the permission mode (warning)]
- Defaults named: interactive terminal and VS Code sessions start in auto mode; "Claude Opus 5.5
  at medium effort" on most plans; subagents delegated automatically; automatic compaction.
  [best-practices > Change a default]
- Effort replaces prompt wording: `think step by step` / `be thorough` are "ordinary prompt text
  rather than keywords"; `ultrathink` still works for one turn; `be ambitious` still helps for
  scope. [best-practices > Write a specific prompt; Change the model and effort]
- Subagent cost: "every subagent sends its own requests and they count against the same usage";
  "You get parallelism or a fresh pair of eyes out of it, but not a smarter answer." Savings:
  `model: haiku` for simple jobs, short summaries, `tools: Read, Grep, Glob` for a reviewer
  ("enforced by Claude Code rather than requested in a prompt"). [best-practices > Know what subagents cost]
- Sessions: `/clear` between unrelated tasks; `/compact <focus>`; after two failed corrections
  "run `/clear` and write a better prompt instead of a third". Prompt cache "lasts about an hour
  on a subscription and five minutes on an API key, cloud provider, or usage credits."
  [best-practices > Keep cost and context down; Steer the session]
- Unattended-run checklist (five questions): what done looks like; can it check its own work;
  what may it touch; what stops it (`--max-turns`, `--max-budget-usd`, spend limit); where the
  result goes and who signs off. [best-practices > Let Claude run without you]
- `--bare` "skips hooks, skills, plugins, MCP servers, and `CLAUDE.md` files, the repo's as well as
  the machine's". [best-practices > Run Claude from a script]
  Note for the template: a `--bare` run ignores everything the template ships.
- `/loop`: "Each run is another turn in the same session, so don't leave one going in a long
  conversation." [best-practices > Start runs on a schedule or an event]
- Obsolete advice table ("What you can stop doing"): aggressive context management; IMPORTANT/ALL
  CAPS ("piling on emphasis mostly makes Claude over-apply the rule"); subagents to protect
  context; delegating for a better answer; `think hard`; telling Claude to keep going or not be lazy ("more likely
  to cause over-work than fix a stall"); and "Describe your architecture and file layout in
  `CLAUDE.md`" ("Claude reads the repo itself. Only write down what isn't in there.").
  [best-practices > What you can stop doing]

### 1.11 Monorepos and large codebases (how the same mechanisms layer by directory)

- Where you launch decides what loads: from the repository root, "Root only; subdirectory files
  load on demand"; from a subdirectory, "That directory's plus every ancestor's".
  [large-codebases > Choose where to start Claude]
- Settings are not inherited: "Project settings in `.claude/settings.json` aren't inherited from
  parent directories the way CLAUDE.md files are." "Each subdirectory's `.claude/settings.json`
  must be self-contained rather than layered on a root file."
  [large-codebases > Choose where to start Claude; Put it together]
  Consequence for a template: hooks and deny rules in the root `.claude/settings.json` do not
  apply to a session started in a package that has its own `.claude/settings.json`; that file
  needs its own copy. (The docs send readers to the settings page for which file a session
  reads; that page is outside this assignment.)
- Inside a worktree the working directory is the worktree root, so "Put any other settings you
  need inside worktrees, such as permission rules or hooks, in the repository root's
  `.claude/settings.json`." [large-codebases > Check out only the directories you need (note)]
- Two-level split: root CLAUDE.md for "instructions that apply everywhere, such as coding
  standards and commit conventions"; per-subdirectory CLAUDE.md for that area's stack.
  [large-codebases > Layer CLAUDE.md files by directory]
- Per-directory CLAUDE.md vs path-scoped rule [large-codebases > Choose between per-directory CLAUDE.md and path-scoped rules]:

  | Approach | File location | Loads when | Use when |
  | - | - | - | - |
  | Per-directory `CLAUDE.md` | Inside the directory, alongside its code | At launch when started from that directory, or on demand | Directory owners maintain their own conventions |
  | Path-scoped rule in `.claude/rules/` | Central `.claude/` at the repo root | When Claude works with a file matching the `paths:` glob | You want all conventions in one place, or the same rule applies to many scattered paths |

- Keeping instruction files current: review CLAUDE.md edits in pull requests; "Revisit after major
  model releases" because workaround instructions "may become overhead"; a `Stop` hook can review
  the transcript and propose CLAUDE.md updates. [large-codebases > Layer CLAUDE.md files by directory]
- `claudeMdExcludes` is "static, not a per-task switch"; patterns match absolute paths, so start
  them with `**/`. [large-codebases > Exclude irrelevant CLAUDE.md files]
- Read deny rules for checked-in generated or vendored code: `Read(./**/dist/**/*)` etc., ending
  in `/**/*` "so that each rule covers everything inside the directory but not the directory
  itself". Searches already respect `.gitignore`. Deny rules "don't cover subprocesses that open
  files themselves", and `grep -r` over a directory still includes denied files.
  [large-codebases > Block reads of generated and vendored code]
- Worktree settings: `worktree.sparsePaths` (directories relative to the repo root; root-level
  files always checked out; "include `.claude` in the list") and `worktree.symlinkDirectories`
  (for example `node_modules`). Lists merge across scopes. [large-codebases > Check out only the directories you need]
- Additional directories [large-codebases > Grant access across packages or repositories]:

  | Added with | Loads CLAUDE.md and rules | Loads skills |
  | - | - | - |
  | `additionalDirectories` setting | Never | Never |
  | `--add-dir` flag or `/add-dir` command | Only with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | Yes |

- Per-directory skills live under `<dir>/.claude/skills/`; from the repo root, skills from every
  touched subdirectory accumulate and "can accumulate into the hundreds". "Keep descriptions short
  and lead with words a request would contain". Shared skills go in the root `.claude/skills/`;
  "When shared skills need their own version history or must work across repositories, package
  them as a plugin instead." [large-codebases > Keep skills discoverable]
- A skill at the root can be scoped with `paths` (for example `**/migrations/**`).
  [large-codebases > Add per-directory skills]
- When layering stops scaling: "Move conventions and reference content out of always-loaded
  CLAUDE.md and into mechanisms that load on demand" (skills, plugins, MCP servers).
  [large-codebases > Centralize conventions when layering stops scaling]
- A `SessionStart` hook's stdout is added "to Claude's context before the first prompt".
  [large-codebases > Recommend the right plugin at session start]
- Long cross-package changes: plan first; "Claude Code re-injects the plan file after each
  compaction, so the plan survives where conversation history may not".
  [large-codebases > Scope and plan changes that span packages]
- `.claude/settings.local.json`: "Claude Code adds that file to your global gitignore when it
  saves a setting there"; when creating it by hand, gitignore it yourself.
  [large-codebases > Exclude irrelevant CLAUDE.md files]
  Inference: a template should list `.claude/settings.local.json`, `CLAUDE.local.md` and
  `.claude/worktrees/` in the repo's own `.gitignore` rather than rely on a global gitignore.


---

## 2. Skills (and custom commands)

### 2.1 What they are for

- "Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit." "Claude uses
  skills when relevant, or you can invoke one directly with `/skill-name`." [skills > intro]
- When to create one: "when you keep pasting the same instructions, checklist, or multi-step
  procedure into chat", or "when a section of CLAUDE.md has grown into a procedure rather than a
  fact." [skills > intro]
- Cost model: "a skill's body loads only when it's used, so long reference material costs almost
  nothing until you need it." [skills > intro]
- Standard: skills "follow the Agent Skills open standard"; Claude Code adds invocation control,
  subagent execution and dynamic context injection. [skills > intro]
- Two content types: reference content (knowledge applied inline) and task content (step-by-step
  action, usually `disable-model-invocation: true`). [skills > Types of skill content]

### 2.2 Locations and precedence

[skills > Choose where skills load]

| Location | Path | Loads in | Project-level? |
| - | - | - | - |
| Enterprise | `.claude/skills/<skill-name>/SKILL.md` in the managed settings directory | All users on managed machines | No |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects on this machine, not Cowork or cloud sessions | No |
| Project | `.claude/skills/<skill-name>/SKILL.md` | Sessions in this repository, "but not cloud threads in a project" | Yes |
| Nested | `<subdir>/.claude/skills/<skill-name>/SKILL.md` | Sessions started in or below `<subdir>`; from above, once Claude works on files there | Yes |
| Additional directory | `.claude/skills/<skill-name>/SKILL.md` in an `--add-dir` directory | That session | Depends on the directory |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Wherever the plugin is enabled, as `/plugin-name:skill-name` | Via plugin |
| claude.ai account | Skills enabled for the account | Cowork, cloud, and signed-in terminal sessions | No |

- Name clash precedence: "Enterprise over personal, and personal over project." Example given:
  with `deploy` in both `~/.claude/skills/` and the project, "`/deploy` runs the personal one".
  [skills > Resolve skills that share a name]
  Consequence for a project-only template: a user's personal skill of the same name shadows the
  template's skill.
- Project skill vs bundled skill or built-in command: "Your skill replaces the bundled command,
  but not its aliases." A project `code-review` skill replaces `/code-review`; `/review` still runs
  the bundled one. Same for built-ins in a local terminal session (`usage` replaces `/usage`, not
  `/cost`). [skills > Resolve skills that share a name]
- Skill vs `.claude/commands/` file with the same name: "The skill". [skills > Resolve skills that share a name]
- Plugin skill vs any other: "Both load, because plugin skills are namespaced".
  [skills > Resolve skills that share a name]
- Discovery: project skills load from `.claude/skills/` in the start directory "and in every
  parent directory up to the repository root". Nested skills below the start directory "load the
  first time Claude reads or edits a file in that subdirectory"; `/add-dir` loads them sooner
  (v2.1.257+). [skills > Load skills in monorepos and subdirectories]
- Nested name clash: `/deploy` runs the root skill, `/apps/web:deploy` the nested one; both stay
  available. [skills > Load skills in monorepos and subdirectories]
- Worktrees: in a linked worktree parents are searched only up to the worktree root; on v2.1.277+
  "when the worktree checkout has no `.claude/skills` directory at its root, Claude Code loads the
  main checkout's project skills instead." [skills > Load skills in monorepos and subdirectories]
- Symlinked skill folders are allowed in enterprise, personal and project locations; loaded once
  even if several locations point at the same target. [skills > Choose where skills load]
- Reserved names: a folder named `synced` (any capitalisation) is skipped; outside a plugin, a
  name that is `anthropic-skills` or starts with `anthropic-skills:` does not load.
  [skills > Choose where skills load; Names reserved for synced skills]
- Name characters refused: zero-width/control characters, private-use characters, direction
  changers, non-plain blanks, `<` or `>`. Debug with `claude --debug`, search for `[names]`.
  [skills > Characters a skill name can't hold]
- Cloud limits: "In a project's cloud thread, skills committed to a repository's `.claude/skills/`
  aren't available." For cloud sessions other than project threads, committing the skill works.
  "Plugins declared in the repository's `.claude/settings.json` and plugins enabled only in your
  user settings don't load in cloud sessions". [skills > Use skills in Cowork and cloud sessions]
- Skill folder as a plugin: adding `.claude-plugin/plugin.json` to a personal or project skill
  folder lets Claude Code load it "as a plugin named `<name>@skills-dir` with its own agents,
  hooks, and MCP servers"; in a project it requires the workspace trust dialog and can be blocked
  by managed settings. [skills > Choose where skills load]
- Synced skills (claude.ai account) arrive without setup in signed-in terminal sessions
  (v2.1.273+), downloaded to `~/.claude/skills/synced/`; includes Anthropic built-ins such as `pdf`
  and `xlsx` which "always sync". Stop with `syncClaudeAiSkills: false` "in your user settings"
  (or managed). Synced skills are invoked as `/<name>` or `/anthropic-skills:<name>`; a local skill
  wins the short name. [skills > Skills synced from claude.ai]
  Note: this is user-account state a project cannot switch off (see end section b).

### 2.3 SKILL.md frontmatter (complete, as documented)

General rules [skills > Frontmatter reference]:
- "All fields are optional. Only `description` is recommended".
- "Claude Code ignores a field it doesn't recognize without reporting an error."
- Field names are lowercase-hyphenated "except `when_to_use`".
- Booleans accept `yes`, `no`, `on`, `off`, `1`, `0` in any case, plus `true`/`false`.
- Frontmatter is read "only when the opening `---` is the file's first line."
- Unparseable YAML: "the skill still loads with no fields set" (so `/name` works but the
  description cannot be matched). Find with `claude plugin validate .claude/skills` (v2.1.233+).
  [skills > Frontmatter reference; Skill not triggering]

| Field | Type / allowed values | Default | Notes |
| - | - | - | - |
| `name` | string | directory name | Command name in the `/` menu |
| `description` | string | first non-empty line of the body | "Recommended". Combined with `when_to_use`, truncated at 1,536 characters in the listing. Put the key use case first. `<`/`>` display as `&lt;`/`&gt;` |
| `when_to_use` | string | none | Trigger phrases or example requests; appended to `description`; counts toward the 1,536 cap |
| `argument-hint` | string | none | Autocomplete hint, e.g. `[issue-number]` |
| `arguments` | space-separated string or YAML list | none | Named positional arguments for `$name` substitution |
| `disable-model-invocation` | boolean | `false` | `true` stops Claude loading it automatically; also stops preloading into subagents and running from a session-scoped scheduled task |
| `user-invocable` | boolean | `true` | `false` hides it from the `/` menu and typing `/name` does not run it |
| `allowed-tools` | space- or comma-separated string, or YAML list | none | Pre-approval "during the turn that invokes this skill"; clears on the next user message |
| `disallowed-tools` | space- or comma-separated string, or YAML list | none | Removes tools from the pool while the skill is active; clears on the next user message; cannot remove `EndConversation` while another tool remains |
| `model` | same values as `/model`, or `inherit` | session model | Applies "for the rest of the current turn"; with `context: fork` sets the forked subagent's model |
| `effort` | `low`, `medium`, `high`, `xhigh`, `max` | effort resolution order | Rest of the current turn; does not override `CLAUDE_CODE_EFFORT_LEVEL`; with `context: fork` sets the fork's effort |
| `context` | `fork` | inline | Runs in a forked subagent context |
| `agent` | subagent type name | `general-purpose` | Only with `context: fork`; built-ins (`Explore`, `Plan`, `general-purpose`) or any custom subagent from `.claude/agents/` |
| `background` | boolean | `true` | Only with `context: fork`; `false` waits for the result in the invoking turn |
| `hooks` | hooks config | none | Registered when the skill is invoked and kept "for the rest of the session" |
| `paths` | comma-separated string or YAML list of globs | none | Auto-loads only when working with matching files; relative to the current working directory |
| `shell` | `bash` or `powershell` | `bash` | Shell for `` !`command` `` and ` ```! ` blocks |
| `metadata` | YAML map | none | Free-form; Claude Code does not act on it; non-map value is dropped |
| `license` | string | none | Agent Skills spec; accepted, not acted on |
| `compatibility` | string up to 500 characters | none | Agent Skills spec; accepted, not acted on |

- Portable subset (claude.ai uploads, Skills API, `package_skill.py`): `name`, `description`,
  `license`, `compatibility`, `metadata`, `allowed-tools`. Any other field makes upload fail with
  "Unexpected key(s) in SKILL.md frontmatter". [skills > Using skill frontmatter outside Claude Code]
- Command name sources: `.claude/skills/deploy-staging/SKILL.md` -> `/deploy-staging` (or the
  frontmatter `name`; "The directory name also invokes the skill");
  `.claude/commands/frontend/component.md` -> `/frontend:component`;
  `my-plugin/skills/review/SKILL.md` -> `/my-plugin:review`.
  [skills > How a skill gets its command name]

### 2.4 Invocation control

[skills > Control who invokes a skill]

| Frontmatter | You can invoke | Claude can invoke | When loaded into context |
| - | - | - | - |
| (default) | Yes | Yes | Description always in context, full skill loads when invoked |
| `disable-model-invocation: true` | Yes | Not on its own | Description not in context, full skill loads when invoked |
| `user-invocable: false` | No | Yes | Description always in context, full skill loads when invoked |

- `disable-model-invocation: true` is for "workflows with side effects or that you want to control
  timing, like `/commit`, `/deploy`, or `/send-slack-message`." If Claude tries anyway, "Claude Code
  blocks the call". [skills > Control who invokes a skill]
- `user-invocable: false` is for "background knowledge that isn't actionable as a command."
  [skills > Control who invokes a skill]
- Position matters: `/deploy staging` at the start of a message runs the skill directly; after
  plain text (`go ahead and /deploy to staging`) "Nothing runs directly", it only counts as
  permission for Claude to run it. [skills > Where you write the skill's name]
- Stacking: at the terminal prompt, "the first skill plus up to five more stacked after it" are
  expanded; via SDK or `claude -p` only the first loads. Expansion stops at a forked skill (such
  as `/code-review`) or `/loop`. [skills > Stack several skills in one message]
- Permission rules: `Skill` in deny rules disables all skills; `Skill(name)` exact,
  `Skill(name *)` prefix match. [skills > Restrict Claude's skill access]
- Settings-side control, `skillOverrides` (key = skill name; a missing key is `"on"`)
  [skills > Override skill visibility from settings]:

  | Value | Listed to Claude | In `/` menu |
  | - | - | - |
  | `"on"` | Name and description | Yes |
  | `"name-only"` | Name only | Yes |
  | `"user-invocable-only"` | Hidden | Yes |
  | `"off"` | Hidden | Hidden |

  "Plugin skills are not affected by `skillOverrides`." The `/skills` menu saves to
  `.claude/settings.local.json`. In user, project and local settings entries match skill names
  only (not aliases).
- Bundled skills: turned off as a group with `disableBundledSkills`; one at a time with
  `skillOverrides` `"off"`. [skills > Bundled skills; Remove a skill]

### 2.5 Arguments and substitutions

[skills > Available string substitutions; Pass arguments to skills]

| Variable | Meaning |
| - | - |
| `$ARGUMENTS` | All arguments as typed. If no placeholder receives an argument, Claude Code appends `ARGUMENTS: <value>` |
| `$ARGUMENTS[N]` | 0-based index |
| `$N` | Shorthand for `$ARGUMENTS[N]` |
| `$name` | Named argument from `arguments` frontmatter, mapped by position |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_EFFORT}` | `low`, `medium`, `high`, `xhigh` or `max` |
| `${CLAUDE_SKILL_DIR}` | Directory containing the skill's `SKILL.md` |
| `${CLAUDE_PROJECT_DIR}` | Project root (same value hooks and MCP servers receive) |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin installation directory; plugin skills only |
| `${CLAUDE_PLUGIN_DATA}` | Plugin persistent data directory; plugin skills only |

- Indexed arguments use shell-style quoting; a missing indexed argument "stays in the content
  unchanged"; a missing named argument "expands to an empty string".
- Escape a literal `$1` as `\$1.00`; `${CLAUDE_*}` variables cannot be escaped this way.
- `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PROJECT_DIR}` are substituted in the body and in Bash rules
  in `allowed-tools`, which "lets a skill run a bundled script without a permission prompt":
  `allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)`.

### 2.6 Supporting files

- Layout: `SKILL.md` (required) plus e.g. `reference.md`, `examples.md`, `scripts/helper.py`
  ("executed, not loaded"). Reference them from `SKILL.md` "so Claude knows what each file contains
  and when to load it". [skills > Add supporting files]
- Size: "Keep `SKILL.md` under 500 lines. Move detailed reference material to separate files."
  [skills > Add supporting files (tip)]
- Body style: "State what to do rather than narrating how or why"; "every line is a recurring
  token cost" once loaded. [skills > Types of skill content]

### 2.7 Dynamic context injection

[skills > Inject dynamic context and subsections]
- Inline `` !`<command>` `` and fenced ` ```! ` blocks run "before the skill content is sent to
  Claude"; output replaces the placeholder. One pass only; output is not re-scanned.
- Inline form is recognised only when `!` is at the start of a line or right after whitespace.
- Runs in the session shell's current working directory (which moves when Claude runs `cd`); use
  `${CLAUDE_SKILL_DIR}` or `${CLAUDE_PROJECT_DIR}` for stable paths.
- Timeout: "the Bash tool's default 2-minute timeout". stderr is merged into stdout with `bash`.
- Failure: "A failed command aborts the entire skill invocation, not just its own placeholder."
  Any non-zero exit fails, except exit code 1 from search and comparison commands; append
  `|| true` to commands expected to exit non-zero.
- Permissions: "Injected commands never prompt for permission while the skill renders." Outside
  auto mode, anything other than allow aborts the invocation; "pre-approve it with
  `allowed-tools`". Deny and ask rules still override `allowed-tools`. In auto mode the skill
  loads with an instruction telling Claude to run the command first.
- Disable: `"disableSkillShellExecution": true` replaces each command with
  `[shell command execution disabled by policy]` for user, project, plugin and additional-directory
  skills; bundled and managed skills are unaffected.
- Never run for claude.ai-synced skills on your machine (v2.1.228+).
- `ultrathink` anywhere in skill content requests deeper reasoning. [skills > Inject dynamic context (tip)]

### 2.8 `context: fork` and `agent`

[skills > Run skills in a subagent]
- "Claude Code starts a new subagent of the type set in the `agent` field and gives it the skill
  content as its prompt." "The subagent doesn't see your conversation history".
- Naming trap: "a skill with `context: fork` doesn't run in a fork of the current conversation".
- Runs in the background by default; `background: false` waits. Claude Code also waits in `-p`/SDK
  mode, with `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`, when an earlier invocation of the same
  skill is still running, when a session-scoped scheduled task fires it, and when a dynamic
  workflow agent invokes it (v2.1.295+).
- A backgrounded fork gets "the narrower tool set that applies to background subagents"; set
  `background: false` to keep the full tool set.
- Checkpoints: a background forked skill "applies its edits outside your session's checkpoints".
- Anti-pattern: "`context: fork` only makes sense for skills with explicit instructions." A
  guidelines-only skill "returns without meaningful output."
- `agent: Explore` (or Plan) starts with the skill content and the agent's own system prompt,
  "and none of your CLAUDE.md files." Put everything the task needs in SKILL.md.
- The two directions:

  | Approach | System prompt | Task | Also loads |
  | - | - | - | - |
  | Skill with `context: fork` | From agent type | SKILL.md content | CLAUDE.md, per the agent's startup context |
  | Subagent with `skills` field | Subagent's markdown body | Claude's delegation message | Preloaded skills + CLAUDE.md, per the subagent's startup context |

### 2.9 Allowed tools and hooks in skills

- `allowed-tools` "does not restrict which tools are available: every tool remains callable".
  The grant lasts one turn; re-invoking re-applies it. Session-wide pre-approval belongs in
  permission settings. [skills > Pre-approve tools for a skill]
- Trust gap to know about: "Workspace trust doesn't gate this field. Claude Code applies a project
  skill's `allowed-tools` even in a `-p` run in a folder you've never trusted."
  [skills > Pre-approve tools for a skill]
- Managed overrides: `allowManagedPermissionRulesOnly` makes Claude Code ignore `allowed-tools` in
  project and personal skills (v2.1.282+); `strictPluginOnlyCustomization` listing `hooks` means a
  project skill declaring `hooks` loses its `allowed-tools` pre-approval and its hooks do not run.
  [skills > When only managed permission rules apply; When managed settings lock hooks to plugins]
- Skill `hooks`: registered on invocation, apply "from the time the skill is invoked until the
  session ends." Format, `once` option and limits are on the hooks page (not in this
  assignment's sources). [skills > Frontmatter reference; Claude stops following a skill]

### 2.10 Loading, lifecycle, budget

- Listing: names always listed; descriptions are dropped to fit a character budget that "scales
  at 1% of the model's context window", dropping "starting with the skills you invoke least".
  Raise with `skillListingBudgetFraction` (e.g. `0.02`) or `SLASH_COMMAND_TOOL_CHAR_BUDGET`; per
  entry cap 1,536 characters, configurable with `skillListingMaxDescChars`.
  [skills > Skill descriptions are cut short]
- "Every skill in the skill listing adds to your context on every turn, whether or not Claude ever
  uses it." `/skill-doctor` (v2.1.252+) reports cost and usage; `/doctor` estimates the listing's
  cost. [skills > Find unused skills; Skill descriptions are cut short]
- Lifecycle: the rendered SKILL.md "enters the conversation as a single message and stays there
  across later turns." Claude Code "does not re-read the skill file on later turns, so write
  guidance that should apply throughout a task as standing instructions rather than one-time
  steps." [skills > Skill content lifecycle]
- Re-invocation with identical rendered content adds only a short "already loaded" note.
  [skills > Skill content lifecycle]
- Compaction: most recent invocation of each skill re-attached, "keeping the first 5,000 tokens of
  each", combined budget 25,000 tokens, filled from the most recently invoked.
  [skills > Skill content lifecycle]
- Mid-session edits: Claude Code watches `~/.claude/skills/`, project `.claude/skills/` and
  `--add-dir` skills; changes apply "within the current session, without a restart." A top-level
  skills directory created after session start needs `/reload-skills`. "Live change detection
  covers `SKILL.md` text only." Not in bare mode. [skills > Edit a skill during a session]
- Commit-time hook-up: if a skill named `verify` or `simplify` exists at enterprise, personal,
  project or additional-directory level (or as a `.claude/commands/` file) and Claude can invoke
  it, "Claude Code's commit instructions tell Claude to run it right before each commit, except
  for changes to docs or tests" (v2.1.286+; removed if `includeGitInstructions` is off).
  [skills > Run your checks before each commit]
- `/run-skill-generator` commits a per-project recipe to `.claude/skills/run-<name>/`; `/verify`
  may write `.claude/skills/verify/SKILL.md`, which "replaces the bundled `/verify`" at the repo
  root. [skills > Run and verify your app]

### 2.11 Relationship to custom commands

- "Custom commands have been merged into skills." "A file at `.claude/commands/deploy.md` and a
  skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way."
  [skills > intro (note)]
- A command file "is the older format and still works. It supports the same frontmatter except
  `name` and `paths`." "Prefer a skill for new work, since skills also support supporting files."
  [skills > Choose where skills load]
- `--add-dir` loads that directory's `.claude/skills/`, `.claude/commands/` and `.claude/agents/`,
  but only `.claude/skills/` is watched for changes. `permissions.additionalDirectories` "grants
  file access only and loads none of these." [skills > Load skills from a directory outside the project]

### 2.12 Testing and troubleshooting guidance

- "Seeing a skill trigger tells you Claude found it, not that it did what you intended."
  Baseline comparison: run realistic prompts in fresh sessions with the skill on and with it
  `"off"` in `skillOverrides`. [skills > Evaluate and iterate on a skill]
- Tools: `claude plugin eval` (plugin skills, CI gate) and the `skill-creator` plugin
  (`evals/evals.json`); "The two formats aren't interchangeable." [skills > Evaluate and iterate on a skill]
- Not triggering: put keywords users would say in the description; check `paths` files are inside
  the working directory. Triggering too often: "Make the description more specific" or add
  `disable-model-invocation: true`. [skills > Skill not triggering; Skill triggers too often]
- Stops being followed: a must-hold rule goes into a hook (possibly the skill's own `hooks`);
  judgment guidance should be worded for the whole task ("Run the tests after every edit");
  after compaction re-invoke the skill. [skills > Claude stops following a skill]

### 2.13 Built-in commands and bundled skills (name space a template shares)

- "A command is only recognized at the start of your message." "Up to six skills can be chained."
  [commands > intro]
- Three kinds of entries in the command table: built-in commands ("behavior is coded into the
  CLI"), bundled skills ("a prompt handed to Claude"), and bundled workflows. [commands > All commands]
- Bundled skills listed (marked Skill): `/artifact-capabilities`, `/artifact-diagramming`,
  `/batch`, `/claude-api`, `/claude-in-chrome`, `/code-review` (alias `/review`), `/dataviz`,
  `/debug`, `/design`, `/design-sync`, `/doctor` (alias `/checkup`),
  `/fewer-permission-prompts`, `/loop` (alias `/proactive`), `/run`, `/run-skill-generator`,
  `/simplify`, `/slides`, `/update-config`, `/verify`, `/workflow-authoring`. Bundled workflow:
  `/deep-research`. `/plugin-authoring` is a skill from a built-in plugin. [commands > All commands]
- Built-in command names a project skill could collide with include: `/plan`, `/init`, `/memory`,
  `/context`, `/compact`, `/clear` (aliases `/reset`, `/new`), `/resume` (alias `/continue`),
  `/branch`, `/fork`, `/subtask`, `/background` (`/bg`), `/goal`, `/schedule` (`/routines`),
  `/tasks`, `/agents`, `/skills`, `/hooks`, `/permissions`, `/config`, `/status`, `/usage`
  (`/cost`, `/stats`), `/export`, `/diff`, `/rewind` (`/checkpoint`, `/undo`), `/recap`,
  `/security-review`, `/import`, `/workflows`, `/stop`, `/focus`, `/copy`, `/help`.
  [commands > All commands]
- Collision rule (from 2.2): a project skill with a built-in or bundled name "replaces the
  built-in command, but not its aliases" in a local terminal session.
  [skills > Resolve skills that share a name]
  Inference: a template skill named `plan`, `verify`, `run`, `debug`, `review`, `simplify`,
  `loop`, `schedule`, `init` or `goal` would shadow or interact with a built-in. `verify` and
  `simplify` additionally trigger the pre-commit instruction (2.10). Choosing distinct names
  avoids silently removing built-in behaviour.
- Useful built-ins for the workflow the template encodes [commands > Commands across a typical workflow]:
  first session `/init`, `/memory`, `/mcp`, `/permissions`; during a task `/plan`, `/model`,
  `/effort`, `/context`, `/compact`, `/btw`; before shipping `/diff`, `/code-review` (with
  `--fix`), `/security-review`; between sessions `/clear`, `/resume`, `/branch`, `/fork`; when
  wrong `/rewind`, `/doctor`, `/debug`.
- `/code-review [low|medium|high|xhigh|max|ultra] [--fix] [--comment] [--max-findings ...]
  [pr#|branch|path]`; `/simplify` runs four review agents in parallel and "doesn't look for
  correctness bugs". [commands > All commands]
- `/fewer-permission-prompts` writes "a prioritized allowlist to project `.claude/settings.json`".
  `/update-config` edits the matching `settings.json`. [commands > All commands]
  Note: both modify committed project files a template also owns.
- Removed or replaced commands: `/pr-comments` "Removed in v2.1.91"; `/vim` "Removed in v2.1.92";
  `/ultraplan` "Removed. Use plan mode instead"; `/ultrareview` is an alias of
  `/code-review ultra`; `/usage-credits` was "Previously `/extra-usage`"; before v2.1.212 `/bug`
  and `/share` were aliases of `/feedback`. [commands > All commands]


---

## 3. Subagents

### 3.1 What they are for, and when the docs say to use them

- "Use one when a side task would flood your main conversation with search results, logs, or file
  contents you won't reference again". "Define a custom subagent when you keep spawning the same
  kind of worker with the same instructions." [sub-agents > intro]
- Each "runs in its own context window with a custom system prompt, specific tool access, and
  independent permissions", and its requests "count toward the same usage limits".
  [sub-agents > intro]
- Use the main conversation when: frequent back-and-forth; phases share significant context; a
  quick targeted change; "Latency matters". Use subagents when: verbose output not needed in main
  context; you want to "enforce specific tool restrictions or permissions"; "The work is
  self-contained and can return a summary". [sub-agents > Choose between subagents and main conversation]
- For a question about something already in the conversation use `/btw`, not a subagent.
  [sub-agents > Choose between subagents and main conversation]
- Warning on fan-out: "Running many subagents that each return detailed results can consume
  significant context, and each subagent spends tokens of its own". [sub-agents > Run parallel research]
- Docs' best practices: "Design focused subagents"; "Write descriptions that single out one
  subagent"; "Limit tool access"; "Check into version control". [sub-agents > Example subagents (tip)]

### 3.2 Locations and precedence

[sub-agents > Choose the subagent scope]

| Location | Scope | Priority | Project-level? |
| - | - | - | - |
| Managed settings (`.claude/agents/` in the managed settings directory) | Organization-wide | 1 (highest) | No |
| `--agents` CLI flag (JSON) | Current session | 2 | No |
| `.claude/agents/` | Current project | 3 | Yes |
| `~/.claude/agents/` | All your projects | 4 | No |
| Plugin's `agents/` directory | Where plugin is enabled | 5 (lowest) | Via plugin |

- A project subagent beats a user subagent of the same name (opposite of skills; see 2.2).
- Project discovery walks up: "every `.claude/agents/` between there and the repository root is
  scanned"; on a name clash "the definition closest to the working directory" wins.
- Recursive scan; subfolders do not affect identity ("identity comes only from the `name`
  frontmatter field"). Duplicate `name` within one `.claude/agents/` tree: one is loaded, "chosen
  by filesystem read order rather than a documented precedence."
- Plugin subfolders do affect identity: `agents/review/security.md` in `my-plugin` registers as
  `my-plugin:review:security`.
- `--add-dir` directories' `.claude/agents/` also load.
- Plugin subagents: "plugin subagents don't support the `hooks`, `mcpServers`, or
  `permissionMode` frontmatter fields. These fields are ignored when loading agents from a
  plugin." Workaround: copy the agent into `.claude/agents/`, or ship hooks in the plugin's
  `hooks/hooks.json` and MCP servers in its `.mcp.json`. `initialPrompt` is also ignored for
  plugin subagents (field table).
- Edits apply mid-session: Claude Code watches `~/.claude/agents/` and `.claude/agents/` and "the
  next delegation uses the updated definition, with no restart needed." Restart still needed
  when the `agents` directory did not exist at session start, for `--add-dir` agents, and with
  `--disable-slash-commands`. [sub-agents > Write subagent files (note)]
- `/agents` now only "prints a reminder"; the interactive wizard existed on v2.1.197 and earlier.
  [sub-agents > Quickstart (note)]

### 3.3 File format

- "Subagent files use YAML frontmatter for configuration, followed by the system prompt in
  Markdown". The body "becomes the system prompt". "Subagents receive only this system prompt plus
  basic environment details like the working directory, not the Claude Code system prompt."
  [sub-agents > Write subagent files]
- "Only `name` and `description` are required." Multi-word fields are camelCase (unlike skills,
  which are hyphenated); unrecognised fields are ignored silently. Debug: `claude --debug`, search
  `~/.claude/debug/<session-id>.txt` for `does not recognize or apply` (v2.1.296+).
  [sub-agents > Frontmatter reference]
- Files silently skipped: no `name` (treated as documentation); opening `---` not on the first
  line; `name` starting with `-`, containing `:`, or longer than 256 characters; `name` without
  `description`; YAML that does not parse. Pre-check with `claude plugin validate .claude/agents`
  (v2.1.233+). [sub-agents > Subagent files Claude Code skips]

### 3.4 Frontmatter fields (complete, as documented)

[sub-agents > Frontmatter reference]

| Field | Required | Type / allowed values | Default and notes |
| - | - | - | - |
| `name` | Yes | string, at most 256 characters, no `:` | Hooks receive it as `agent_type`; filename need not match |
| `description` | Yes | string | "When Claude should delegate to this subagent" |
| `tools` | No | comma-separated string or YAML list | Omitted: "Inherits every tool available to subagents". Zero resolvable entries usually fails to launch. Do not list `Skill` to preload skills |
| `disallowedTools` | No | same format as `tools` | Applied first, then `tools`. An entry with a specifier such as `Bash(git push *)` "still removes the whole tool" |
| `model` | No | `sonnet`, `opus`, `haiku`, `fable`, a full model ID such as `claude-opus-5-5`, or `inherit` | Omitted: subagent model order (3.5) |
| `permissionMode` | No | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`; `manual` is an alias for `default` | Omitted: inherits the main conversation's mode. Ignored for plugin subagents |
| `maxTurns` | No | integer | At the limit the output is returned "marked as partial" and can be resumed (v2.1.246+) |
| `autoCompactWindow` | No | integer token count from `100000` to `1000000` | v2.1.296+. Write a plain integer: "`200k` as 200" is out of range. No effect with `--agent`/`agent` setting |
| `skills` | No | list of skill names | Full content injected at startup, "up to the first 32 distinct names" |
| `mcpServers` | No | list of server names and/or inline definitions | Inline servers connect when the subagent starts and disconnect when it finishes. Ignored for plugin subagents |
| `hooks` | No | hooks config | Run only while the subagent is active. Ignored for plugin subagents |
| `memory` | No | `user`, `project`, `local` | Persistent memory directory (3.8) |
| `background` | No | boolean | `true` keeps it in the background "even when Claude asks to wait for it" |
| `omitClaudeMd` | No | boolean | `true` starts without user, project and local CLAUDE.md; managed policy files still load. Ignored as main session agent. v2.1.271+ |
| `effort` | No | `low`, `medium`, `high`, `xhigh`, `max` | Overrides session effort, not `CLAUDE_CODE_EFFORT_LEVEL` |
| `isolation` | No | `worktree` | Temporary git worktree, "branched by default from your default branch rather than the parent session's `HEAD`"; cleaned up if no changes |
| `color` | No | `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` | Display colour |
| `initialPrompt` | No | string | Auto-submitted first user turn when run as main session agent (`--agent` or `agent` setting). Ignored for plugin subagents |
| `experimental` | No | map; `cacheTtl`: `5m` or `1h` | Prompt cache lifetime for this subagent's requests; v2.1.248+; "reads the field only from subagent files" |

- `--agents` JSON accepts `prompt` plus `description`, `tools`, `disallowedTools`, `model`,
  `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `autoCompactWindow`, `skills`,
  `initialPrompt`, `memory`, `effort`, `background`, `omitClaudeMd`, `isolation`; `color` and
  `experimental` are ignored there. [sub-agents > Choose the subagent scope]

### 3.5 Model and effort

- Model resolution order: (1) "The per-invocation `model` parameter"; (2) the definition's
  `model` frontmatter, "where `inherit` selects the main conversation's model"; (3) the
  `CLAUDE_CODE_SUBAGENT_MODEL` environment variable; (4) "The main conversation's model". Before
  v2.1.251 the env var came first. [sub-agents > Choose a model]
- Family alias quirk: if the main conversation's model is in the same family as the alias, "the
  subagent runs on the main conversation's exact model, including any `[1m]` suffix".
  [sub-agents > Choose a model]
- Force one model everywhere (subagents, teammates, workflow agents): set
  `CLAUDE_CODE_SUBAGENT_MODEL` and `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` in a settings `env` block
  (v2.1.257+); frontmatter `model` is then ignored. [sub-agents > Run every subagent on one model]
- Thinking: "There is no per-subagent thinking setting"; subagents inherit the main
  conversation's extended thinking configuration (v2.1.198+). [sub-agents > Choose a model]
- Effort: frontmatter `effort`, overridden by a per-invocation `effort` parameter (v2.1.292+),
  both overridden by `CLAUDE_CODE_EFFORT_LEVEL`. With no field, the session's level applies only
  "On the main conversation's model". [sub-agents > Choose an effort level]
- Check with `/tasks` (model and effort shown per row, v2.1.242+). [sub-agents > Choose a model]

### 3.6 Tools and permissions

- Tools removed from every subagent even if listed: `Agent` at the depth limit,
  `AskUserQuestion`, `EndConversation`, `EnterPlanMode`, `ExitPlanMode` (unless `permissionMode`
  is `plan`), `ScheduleWakeup`, `WaitForMcpServers`, `Workflow`. [sub-agents > Available tools]
- Background subagents (the default) keep every MCP tool but only these built-ins: `Read`,
  `Grep`, `Glob`, `LSP`, `Bash`, `PowerShell`, `Edit`, `Write`, `NotebookEdit`, `WebFetch`,
  `WebSearch`, `TodoWrite`, `Skill`, `ToolSearch`, `EnterWorktree`, `ExitWorktree`, `Monitor`,
  `TaskStop`, `SendMessage`, `Artifact` (plus `SubagentHandback`). "the same definition can
  resolve to different tools in the foreground and the background." Forks skip both filters.
  [sub-agents > Available tools]
- MCP entries: `mcp__github__*` in `tools`; `mcp__github` or `mcp__github__*` in
  `disallowedTools`; `mcp__*` withholds every MCP tool. [sub-agents > Restrict which tools a subagent can use]
- To keep Bash but block commands, use a `permissions.deny` rule (applies to main conversation and
  subagents). [sub-agents > Restrict which tools a subagent can use]
- `Agent(worker, researcher)` in `tools` is an allowlist of spawnable types only for an agent
  running as the main thread with `claude --agent`; in a subagent definition "any type list inside
  the parentheses is ignored." `Task(...)` still works as an alias (renamed in 2.1.63).
  [sub-agents > Restrict which subagents can be spawned]
- Disable specific subagents: `permissions.deny` with `Agent(Explore)` or `Agent(my-custom-agent)`;
  stop forks with `Agent(fork)`. [sub-agents > Disable specific subagents; Turn fork mode off]
- `permissionMode` is conditional on the parent: under parent `bypassPermissions`, `acceptEdits`
  or auto mode "the subagent runs in that same mode and Claude Code ignores the `permissionMode`
  you set"; under parent `plan` it stays in plan; under parent `default` or `dontAsk` the set
  value applies, except `bypassPermissions` (v2.1.267+) and unavailable `auto`.
  [sub-agents > Permission modes]
- Inline `mcpServers` in a project agent file need folder trust (since v2.1.238); "a parent
  folder's trust" and the automatic trust of `-p`/SDK sessions do not count.
  [sub-agents > Trust required for inline MCP servers]
- Context tip: to keep an MCP server and its tool descriptions out of the main conversation,
  "define it inline here rather than in `.mcp.json`."
  [sub-agents > Scope MCP servers to a subagent]
- Frontmatter hooks in project subagents need the workspace trust dialog for the folder holding
  the agent file ("trusting a parent folder isn't enough, and a `-p` session doesn't count as
  trusted"). Until then the subagent runs but its hooks are skipped. `Stop` in frontmatter becomes
  `SubagentStop`. Settings-file hooks "all apply inside subagents". Settings can also hook
  `SubagentStart`/`SubagentStop` with the agent `name` as matcher.
  [sub-agents > Define hooks for subagents]

### 3.7 Built-in subagents

[sub-agents > Built-in subagents]

| Agent | Model | Tools | Notes |
| - | - | - | - |
| Explore | main conversation's model (on Fable with subscription/Console/gateway: the `opus` alias model) | read-only; Write and Edit denied | Thoroughness: quick, medium, very thorough. Starts without CLAUDE.md and git status. One-shot, cannot be resumed |
| Plan | inherits | read-only; Write and Edit denied | Used in plan mode. Starts without CLAUDE.md and git status. One-shot |
| general-purpose | `CLAUDE_CODE_SUBAGENT_MODEL` if set, else main model | every tool available to subagents | Default for `context: fork` skills |
| claude | follows the model order | every tool available to subagents | Catch-all; default agent for a dispatched background session |
| statusline-setup | Sonnet | - | `/statusline` |
| claude-code-guide | Haiku | - | Questions about Claude Code |

- Overriding: "A user or project subagent named `Explore` overrides the built-in and keeps its
  own `model` field, so define one with `model: haiku`".
- Remove Explore and Plan with `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` (v2.1.198+); remove all
  built-ins in non-interactive/SDK mode with `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1`.

### 3.8 Memory, skills preload, startup context

- `memory` scopes [sub-agents > Enable persistent memory]:

  | Scope | Location |
  | - | - |
  | `user` | `~/.claude/agent-memory/<name-of-agent>/` |
  | `project` | `.claude/agent-memory/<name-of-agent>/` |
  | `local` | `.claude/agent-memory-local/<name-of-agent>/` |

  "`project` is the recommended default scope." With memory on, the system prompt includes the
  first 200 lines or 25KB of `MEMORY.md`, and Read, Write and Edit are auto-enabled.
- Dependency on auto memory: "if you turn auto memory off, with the `autoMemoryEnabled` setting or
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY`, the `memory` field has no effect".
  [sub-agents > Enable persistent memory]
  Consequence: a template that sets `autoMemoryEnabled: false` also disables project-scoped
  subagent memory.
- Skills preload: full content, first 32 distinct names; "This field controls which skills are
  preloaded, not which skills the subagent can access". Skills with
  `disable-model-invocation: true` cannot be preloaded. Missing skills are skipped with a debug
  warning. To block skills entirely omit `Skill` from `tools` or add it to `disallowedTools`.
  [sub-agents > Preload skills into subagents]
- Startup context of a non-fork subagent: its own system prompt; the delegation message; every
  level of the CLAUDE.md hierarchy the main conversation loads (including project rules and
  AGENTS.md loaded as project instructions); git status; preloaded skills; a sibling roster.
  Not passed: output style, main auto memory, the parent's context-window size.
  [sub-agents > What loads at startup]
- Even with `omitClaudeMd`, Explore or Plan, "a subdirectory's `CLAUDE.md` and matching path-scoped
  rules still load when the subagent works with files there." [sub-agents > What loads at startup]
- Guidance: "most rules don't need to reach the subagent itself." If one must, "restate it in
  the prompt you give Claude when delegating." [sub-agents > What loads at startup]
- Description budget: combined custom-subagent descriptions over 15,000 tokens trigger a startup
  warning (all subagents still load). "move detail into each subagent's system prompt, which only
  loads when that subagent runs." [sub-agents > intro; Understand automatic delegation]
- Delegation: "include phrases like \"use proactively\" in your subagent's description field" to
  encourage it. [sub-agents > Understand automatic delegation]

### 3.9 Invocation, background, forks, nesting, limits

- Three ways to invoke: natural language (Claude decides), @-mention such as
  `@"code-reviewer (agent)"` or `@agent-<name>` ("guarantees the subagent runs for one task"),
  session-wide `claude --agent <name>` or `"agent": "code-reviewer"` in `.claude/settings.json`.
  [sub-agents > Invoke subagents explicitly]
- As main session agent the subagent's system prompt "replaces the default Claude Code system
  prompt entirely"; CLAUDE.md still loads even with `omitClaudeMd`.
  [sub-agents > Invoke subagents explicitly]
- Background is the default: "a subagent that Claude spawns from your main conversation starts in
  the background." In interactive sessions Claude can wait only if fork mode is off
  (`CLAUDE_CODE_FORK_SUBAGENT=0` in settings `env`), or with
  `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`. In `-p`/SDK Claude can wait.
  [sub-agents > Which subagents run in the background; Let Claude wait for a subagent]
- Background permission prompts surface in the main session; a lasting grant applies "to the whole
  session, including your main conversation." [sub-agents > Tools, permissions, and results of background subagents]
- Fork: "a subagent that inherits the entire conversation so far"; same system prompt, tools,
  model; shares the parent's prompt cache so "a fork costs less than a fresh subagent for tasks
  that need the same context." Start one with `/subtask <task>`. "A fork can't spawn further
  forks." Fork mode is on by default from v2.1.302 (interactive terminal from v2.1.232).
  [sub-agents > Fork the current conversation; How forks differ; Turn fork mode off]
- Nesting: "up to three layers below the main conversation"; change with
  `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` ("Set `1` to turn nesting off").
  [sub-agents > Let subagents spawn their own subagents]
- Concurrency: default 20 running subagents, then `Concurrent subagent limit reached`; change with
  `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (v2.1.217+). No limit on the total per session.
  [sub-agents > Concurrent subagent limit]
- Resume: Claude uses `SendMessage` with the agent ID or name; resumed subagents "retain their
  full conversation history". Explore and Plan cannot be resumed. Transcripts at
  `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`, unaffected by main
  compaction. [sub-agents > Resume subagents]
- Authority: "no message from any agent counts as your approval for a pending permission
  prompt", and "no agent message can change a subagent's permission settings, `CLAUDE.md`, or
  configuration." [sub-agents > Resume subagents]
- Output scanning: subagent reports are scanned; imitation tags get a backslash and a
  `[harness: subagent output matched instruction-shaped pattern(s):` marker line; "It isn't a
  substitute for restricting what a subagent can reach". [sub-agents > Subagent output scanning]
- Isolation: `isolation: worktree` runs Bash/PowerShell inside the worktree; commands that
  redirect git into the main checkout are blocked. With agent teams enabled, a named subagent
  launches as a teammate and "An `isolation` value in the subagent's frontmatter doesn't prevent
  it". [sub-agents > Write subagent files; Subagent names]
- Subagent auto-compaction exists; `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` applies to subagents.
  [sub-agents > Auto-compaction]


---

## 4. Running more than one agent, and keeping a session running

### 4.1 The docs' comparison of parallel approaches

[agents > intro table; Choose an approach]

| Approach | What it gives you | Use it when | Status |
| - | - | - | - |
| Subagents | Delegated workers inside one session returning a summary | A side task would flood the main conversation | GA |
| Agent view | One screen to dispatch and monitor background sessions (`claude agents`) | Several independent tasks to hand off and check on | "Research preview" |
| Agent teams | Coordinated sessions with shared task list and inter-agent messaging, managed by a lead | You want Claude to split a project, assign pieces, keep workers in sync | "Experimental and disabled by default" |
| Projects | One ongoing conversation at claude.ai/code or desktop; Claude starts parallel threads | Work spans many tasks over days or weeks and should run with your machine off | "Public beta on Pro, Max, and Ultra" |
| Dynamic workflows | A script that runs many subagents and cross-checks results | A job outgrows a handful of subagents, or findings need verifying against each other | Paid plans; on Pro enabled from `/config` |

- Decision questions: who coordinates (Claude in one conversation: subagents; you hand off: agent
  view; Claude supervises a group: agent teams; "A script holds the plan": workflows); do workers
  need to talk (cross-session messaging, or teammates); do tasks touch the same files (worktrees;
  "Agent teams don't isolate teammates in worktrees"). [agents > Choose an approach]
- Supporting tools: worktrees, cross-session messaging, and `/batch` ("a skill that has Claude
  split one large change into 5 to 30 worktree-isolated subagents"). [agents > intro]
- Cost note: "Running several sessions or subagents at once multiplies token usage."
  [agents > intro (note)]
- Checking on work: `claude agents` (background sessions), `/tasks` (anything in the background
  of this session), `/workflows` (workflow runs). "`/agents` is separate from `claude agents`."
  [agents > Check on running work]

### 4.2 Dynamic workflows

- What: "a JavaScript script that orchestrates many subagents at once." "Claude writes the
  script for the task you describe, and a runtime executes it in the background".
  [workflows > intro]
- When: "when a task needs more agents than one conversation can coordinate", or "when you want
  the orchestration codified as a script you can read and rerun." [workflows > intro]
- Who holds the plan [workflows > When to use a workflow]:

  | | Subagents | Skills | Agent teams | Workflows |
  | - | - | - | - | - |
  | Who decides what runs next | Claude, turn by turn | Claude, following the prompt | The lead agent, turn by turn | The script |
  | Where intermediate results live | Claude's context window | Claude's context window | A shared task list | Script variables |
  | What's repeatable | The worker definition | The instructions | The team definition | The orchestration itself |
  | Scale | A few delegated tasks per turn | Same as subagents | A handful of long-running peers | Dozens to hundreds of agents per run |
  | Interruption | Restarts the turn | Restarts the turn | Teammates keep running | Resumable in the same session |

- Availability: "all paid plans, with Anthropic API access, and on Amazon Bedrock, Google
  Cloud's Agent Platform, and Microsoft Foundry." "On Pro, turn them on from the Dynamic workflows
  row in `/config`." [workflows > intro (note)]
- File locations [workflows > Save the workflow for reuse; Distribute a workflow in a plugin]:
  - `.claude/workflows/` in the project (project-level; "shared with everyone who clones the repo")
  - `~/.claude/workflows/` (personal)
  - a plugin's `workflows/` directory (or the `workflows` manifest field), namespaced:
    `/acme-tools:release-audit`
  - Precedence: "If a project workflow and a personal workflow share a name, the project one
    runs." In a monorepo, workflows load from every `.claude/workflows/` between cwd and the repo
    root; closest wins.
  - Saving refuses to write if `.claude`, `.claude/workflows` or the target file is a symlink.
    Inference: a template that symlinks `.claude` into repos would break saving project workflows.
  - Each file becomes a `/<name>` command. [claude-directory > File reference]
- How they are started: ask in the prompt ("use a workflow") or include the keyword `ultracode`;
  `/effort ultracode` makes Claude plan a workflow "for each substantive task"; or run a bundled
  (`/deep-research`), saved or plugin workflow by name. The keyword only works in a prompt a human
  typed, not with `-p`, a scheduled task prompt, or relayed webhook/PR-comment text.
  [workflows > Have Claude write a workflow; Where the keyword works]
- Script API as documented [workflows > What the saved script looks like; Edit a saved script]:
  - `export const meta = { name, description }` must be the first statement and a plain object
    literal; optional `phases` list whose entries match `phase()` titles exactly. Non-literal
    values drop `/<name>` from autocomplete.
  - Body: "plain JavaScript with top-level `await`".
  - `agent(prompt, options)` spawns one subagent; documented options: `schema` (JSON schema; the
    subagent returns JSON matching it), `label`, `stallMs`. Resolves to `null` if stopped or on an
    unrecoverable API error.
  - `pipeline(items, fn)` runs one per item; keeps `null` slots (hence `.filter(Boolean)`).
  - `parallel()` "runs a set of agent tasks at the same time and waits for all of them".
  - `phase()` groups following agents under a title; `log()` shows a message above the phases.
  - `args` global: structured input from the invocation; `undefined` if omitted.
  - `return` value is the run's result.
  - Determinism: "`Date.now()`, `Math.random()`, and a no-argument `new Date()` throw inside the
    script". Pass a timestamp through `args`.
  - Schema validation retries: five attempts, then the call fails; `MAX_STRUCTURED_OUTPUT_RETRIES`.
  - Authoring reference: the `/workflow-authoring` bundled skill (v2.1.248+); reload edited
    scripts with `/reload-skills`.
  - The page defers the Workflow tool's inputs to the Agent SDK reference (not in this
    assignment's sources).
- Limits [workflows > Behavior and limits]:
  - "No mid-run user input"; for sign-off between stages "run each stage as its own workflow".
  - No direct filesystem or shell access from the script; no module loading (`import()` fails).
  - "Up to 16 concurrent agents by default", fewer with fewer CPUs;
    `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` from 1 to 256 (v2.1.269+).
  - "Up to 4,096 items in a single `parallel()` or `pipeline()` call".
  - "1,000 agents total per run".
  - Stalled agent restarts at most five times (sixth stall fails the call).
- Permissions: per-run approval prompt in Manual/accept-edits; in Auto "First launch only. Any
  **Yes** records consent in your user settings"; none in bypass, `-p` or SDK, where a `Workflow`
  or `Workflow(<name>)` allow rule, auto mode, or a `PreToolUse` hook returning `"allow"` lets it
  start. Workflow subagents use the session's permission rules; "add the tools the agents need to
  your allow rules before starting." [workflows > Approve the plan before it runs]
- Resume: completed agents return saved results; the first agent whose prompt differs, and every
  agent after it, runs again; a failed agent and everything started after it reruns. A run does
  not continue on its own after you background or exit the session. [workflows > Resume after a pause]
- Cost guidance: "a single run can use meaningfully more tokens than working through the same task
  in conversation." "run the workflow on a small slice first". `Large workflow` warning at more
  than 25 agents or a projected 1.5 million tokens (advisory only). Model per agent follows the
  subagent order; ask for a smaller model for cheap stages. [workflows > Cost]
- Size guideline `workflowSizeGuideline` (any settings file): `unrestricted`; `small` "Fewer than
  5 agents"; `medium` "Fewer than 10 agents"; `large` "Fewer than 50 agents". Default `medium`, or
  `small` on Pro. Advice, not a cap. [workflows > Set a size guideline]
- Ultracode cost: "each request uses more tokens and takes longer"; with it on the Large workflow
  warning, the concurrent subagent limit and the first-launch approval in auto mode are skipped.
  The `ultracode` setting makes every session start with it. [workflows > Let Claude decide with ultracode]
- Cache: workflow agents' cache holds five minutes by default "including on a Claude
  subscription"; `subagentPromptCacheTtl: "1h"` extends it. Fan-out start is staggered up to
  `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS` (5000). [workflows > Prompt caching in a fan-out]
- Off switches: `/config` toggle, `"disableWorkflows": true` (the docs name
  `~/.claude/settings.json` and managed settings), or `CLAUDE_CODE_DISABLE_WORKFLOWS=1`.
  [workflows > Turn workflows off]

### 4.3 `/goal`

- What: "sets a completion condition and Claude keeps working toward it without you prompting each
  step. After each turn, a model checks whether the condition holds." [goal > intro]
- Use for "substantial work with a verifiable end state". [goal > intro]
- Mechanism: "`/goal` is a wrapper around a session-scoped prompt-based Stop hook." The evaluator
  is the configured small fast model; "It does not call tools, so it can only judge what Claude
  has already surfaced in the conversation." [goal > How evaluation works; Evaluation model and cost]
- Configured in a repo? No: it is typed per session ("active for the current session only").
  The repo-level equivalent is a Stop hook, which "lives in your settings file, applies to every
  session in its scope". [goal > Compare ways to keep a session running]
- Stop conditions: verdict Met, verdict Impossible, an error you have to fix (auth failure,
  exhausted credit, context overflow compaction could not clear, unavailable model),
  `/goal clear` (aliases `stop`, `off`, `reset`, `none`, `cancel`), or `/clear`. No tool use for
  several turns stops the loop with the goal still set. [goal > How evaluation works; When a turn fails; Clear a goal]
- Limits: one goal per session; condition "up to 4,000 characters"; bound it with a clause such as
  `or stop after 20 turns`. [goal > Use /goal; Write an effective condition]
- Writing conditions: "One measurable end state", "A stated check", "Constraints that matter".
  [goal > Write an effective condition]
- Does not change permission mode; pair with auto mode for unattended turns. [goal > Set a goal]
- Non-interactive: `claude -p "/goal ..."` runs the loop to completion. [goal > Run non-interactive]
- Background work defers evaluation; check-ins after 30 minutes
  (`CLAUDE_CODE_GOAL_CHECKIN_MINUTES`, `0` disables check-ins and retries); at most three idle
  check-ins per goal between prompts. [goal > Background work defers evaluation]
- Requirements: same workspace trust rule as settings hooks; unavailable when `disableAllHooks` is
  `true` or `allowManagedHooksOnly` is set. [goal > Requirements]
  Note for the template: a project that sets `disableAllHooks` also disables `/goal`.
- Three ways to keep a session running [goal > Compare ways to keep a session running]:

  | Approach | Next turn starts when | Stops when |
  | - | - | - |
  | `/goal` | The previous turn finishes (or an idle check-in or automatic retry comes due) | A model confirms the condition is met or judges it impossible, an error you must fix, or `/goal clear` |
  | `/loop` | A time interval elapses | You stop it, or Claude decides the work is done |
  | Stop hook | The previous turn finishes | Your own script or prompt decides |

### 4.4 `/loop` and session-scoped scheduled tasks

- What: "Session-scoped scheduled tasks let Claude re-run a prompt automatically on an interval
  within a Claude Code session." `/loop` is a bundled skill. [scheduled-tasks > intro; Run a prompt repeatedly with /loop]
- Forms: `/loop 5m check the deploy` (fixed, converted to cron); `/loop check the deploy` (Claude
  picks a delay "between one minute and one hour" each iteration); bare `/loop` (built-in
  maintenance prompt or `loop.md`). Units `s`, `m`, `h`, `d`; seconds round up to a minute.
  [scheduled-tasks > Run a prompt repeatedly with /loop]
- Repo configuration: `.claude/loop.md` (project-level, "Takes precedence when both files exist")
  or `~/.claude/loop.md`. Plain Markdown; replaces the built-in maintenance prompt for bare
  `/loop` only; "content beyond 25,000 bytes is truncated"; edits "take effect on the next
  iteration". [scheduled-tasks > Customize the default prompt with loop.md]
- Built-in maintenance prompt order: continue unfinished work; tend the current branch's PR;
  cleanup passes. "Claude does not start new initiatives outside that scope".
  [scheduled-tasks > Run the built-in maintenance prompt]
- Skills as loop prompts: `/loop 20m /review-pr 1234`; a scheduled fire "only runs skills that
  Claude is allowed to invoke on its own", so skills with `disable-model-invocation: true` reach
  Claude as plain text. [scheduled-tasks > Run a prompt repeatedly with /loop]
- Stop conditions: self-paced loop: `Esc` (or Claude calls `ScheduleWakeup` with `stop: true`);
  fixed-interval loop: ask Claude to cancel it (`Esc`/`Ctrl+C` do not); otherwise "Recurring tasks
  automatically expire 7 days after creation." [scheduled-tasks > Stop a loop; Seven-day expiry]
- Limits: "A session can hold up to 50 scheduled tasks at once"; minimum interval 1 minute; tasks
  fire only while Claude Code is running and idle; "No catch-up for missed fires"; a self-paced
  `/loop` is not restored on resume. Jitter: recurring tasks run late by up to half the gap,
  at most 30 minutes; `*/5 * * * *` runs 4 minutes 45 seconds after the previous run to stay
  inside a five-minute cache. [scheduled-tasks > Manage session-scoped scheduled tasks; Jitter; Limitations]
- Tools: `CronCreate`, `CronList`, `CronDelete` (5-field cron, local timezone, no `L`/`W`/`?`/name
  aliases). [scheduled-tasks > Manage session-scoped scheduled tasks; Cron expression reference]
- Disable: `CLAUDE_CODE_DISABLE_CRON=1`. [scheduled-tasks > Disable session-scoped scheduled tasks]
- With feature-flag fetching off, a task kept across sessions is stored in the project's
  `.claude/scheduled_tasks.json`; a copied file lists tasks but does not run them elsewhere.
  [scheduled-tasks > Limitations]
  Note: a template should not ship `.claude/scheduled_tasks.json` (tasks run only in the folder
  where they were created).
- Alternative to polling: the Monitor tool "avoids polling altogether and is often more
  token-efficient"; event push uses Channels. [scheduled-tasks > Let Claude choose the interval; intro (note)]
- Scheduling options compared [scheduled-tasks > Compare scheduling options]:

  | | Cloud | Desktop | `/loop` |
  | - | - | - | - |
  | Runs on | Cloud | Your machine | Your machine |
  | Requires machine on | No | Yes | Yes |
  | Requires open session | No | No | Yes |
  | Persistent across restarts | Yes | Yes | Restored on `--resume`, with exceptions |
  | Access to local files | No (fresh clone) | Yes | Yes |
  | Permission prompts | Auto mode by default | Configurable per task | Inherits from session |
  | Minimum interval | 1 hour | 1 minute when Claude sets it, 1 hour in the forms | 1 minute |

  The page's tip: cloud tasks "for work that should run reliably without your machine", Desktop
  tasks "when you need access to local files and tools", and `/loop` "for quick polling during a
  session".

### 4.5 Agent teams

- Status: "Agent teams are experimental and disabled by default." [agent-teams > intro (warning)]
- What: "One session acts as the team lead, coordinating work, assigning tasks, and synthesizing
  results." "Teammates work independently, each in its own context window, and communicate
  directly with each other." [agent-teams > intro]
- Check lighter options first: "Before you set up a team, check whether a lighter option does the
  job." [agent-teams > intro]
- When: research and review, new modules, debugging with competing hypotheses, cross-layer
  coordination. Not for "sequential tasks, same-file edits, or work with many dependencies".
  "Agent teams add coordination overhead and use significantly more tokens than a single
  session." [agent-teams > When to use agent teams]
- Repo configuration: only the enabling env var, e.g. in a settings `env` block:
  `"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"`. Project settings apply after user settings, so a
  project `env` entry of `1` wins over a user `0`. [agent-teams > Enable agent teams; Claude spawns teammates instead of subagents]
- No project team file: "There is no project-level equivalent of the team config. A file like
  `.claude/teams/teams.json` in your project directory is not recognized as configuration".
  Reusable roles come from subagent definitions instead. [agent-teams > Architecture]
- Side effect of enabling: "while agent teams are enabled, a subagent that Claude names launches
  as a teammate, so teams can form even when you didn't ask for one." Claude Code "doesn't ask you
  to confirm the launch." [agent-teams > Enable agent teams; How Claude starts agent teams]
  Inference: a template that enables agent teams in committed settings changes ordinary subagent
  delegation for everyone; the docs give no way to enable teams without this side effect.
- Requires an interactive session; with `-p`/SDK Claude does not spawn teammates.
  [agent-teams > Enable agent teams]
- State lives in user space: mailboxes at `~/.claude/teams/{team-name}/inboxes/{agent-name}.json`,
  team config at `~/.claude/teams/{team-name}/config.json` (removed at session end), task list at
  `~/.claude/tasks/{team-name}/` (stays on disk). [agent-teams > Architecture]
- Display mode: `teammateMode` (`"in-process"` default, `"auto"`, `"tmux"`, `"iterm2"`); the docs
  say to set it "in `~/.claude/settings.json`" or pass `--teammate-mode`.
  [agent-teams > Choose a display mode]
- Subagent definitions as teammates: applied parts are `tools`, `model`; for in-process
  teammates also `disallowedTools`, `effort`, `autoCompactWindow`, and the body appended to the
  default system prompt (split-pane: body replaces it). `skills` is not applied in either mode;
  `mcpServers` only for split-pane. [agent-teams > Use subagent definitions for teammates]
- Teammate model order: spawn prompt, definition `model`, `CLAUDE_CODE_SUBAGENT_MODEL`, lead's
  model. `teammateDefaultModel` "was removed in v2.1.234". [agent-teams > Specify teammates and models]
- Teammates load "the same project context as a regular session: CLAUDE.md, MCP servers, and
  skills"; the lead's conversation history does not carry over. [agent-teams > Context and communication]
- Permissions: "You can't set per-teammate permission modes at spawn time. A new teammate starts
  with the lead's mode". Prompts appear in the lead session. No agent message counts as user
  consent. [agent-teams > Permissions; Messages between agents]
- Quality gates via hooks: `TeammateIdle`, `TaskCreated`, `TaskCompleted` (exit code 2 blocks and
  sends feedback). [agent-teams > Enforce quality gates with hooks]
- Stop conditions: ask the lead to shut a teammate down (teammate may reject); `x` on a selected
  teammate; the team ends with the session. [agent-teams > Shut down teammates; Talk to teammates directly]
- Limits and sizing: no hard limit on teammates; "Start with 3-5 teammates for most workflows";
  "Having 5-6 tasks per teammate keeps everyone productive"; one team per session; no nested
  teams; no resumption of in-process teammates; lead is fixed; split panes need tmux or iTerm2
  and are not supported in VS Code's integrated terminal, Windows Terminal or Ghostty.
  [agent-teams > Choose an appropriate team size; Size tasks appropriately; Limitations]
- Best practices: give teammates context in the spawn prompt; "Two teammates editing the same file
  leads to overwrites"; start with research and review; "Letting a team run unattended for too
  long increases the risk of wasted effort." [agent-teams > Best practices]

### 4.6 Cloud scheduled tasks (formerly routines)

- Status and naming: "Scheduled tasks are in research preview." A cloud scheduled task, "formerly
  a routine, is a saved Claude Code configuration: a prompt, one or more repositories, and a set
  of connectors". [routines > intro]
- The old name survives in the web address `claude.ai/code/routines`, the `/routines` alias for
  `/schedule`, the `/fire` API path, its beta header, and the `<routine-fire-payload>` tag.
  [routines > Where the name routines still appears]
- Triggers: Schedule (recurring or one-off), API (HTTP POST with a bearer token), GitHub (pull
  request, release, issue events with filters). One task can combine triggers. [routines > intro; Supported events]
- Where it is configured: NOT in the repo. "Scheduled tasks belong to your individual claude.ai
  account. They are not shared with teammates". Created at claude.ai/code/routines, the Desktop
  app, or `/schedule` in the CLI. [routines > Create a scheduled task]
- What a repo contributes to a run: the cloned repository, so skills "committed to the cloned
  repository" (outside a project's threads) and, for a task with one repository, a committed
  `.mcp.json` server. Locally added MCP servers (`claude mcp add`) do not appear.
  [routines > Create a scheduled task; Connectors]
- Requirements: Pro, Max, Ultra, Team or Enterprise; `/schedule` "requires a claude.ai
  subscription login" (hidden with a Console API key or cloud provider login).
  [routines > intro; /schedule returns "Unknown command"]
- Prompt guidance: "the prompt must be self-contained and explicit about what to do and what
  success looks like." [routines > Create from the web]
- Trust model: the fired prompt "is therefore not live user input and can't act as approval or
  consent for actions during the run." API `text` arrives wrapped in `<routine-fire-payload>` as
  untrusted data; "a routine's saved prompt must opt in to acting on fire text".
  [routines > Create from the web; Trigger a scheduled task]
- Schedule limits: "Expressions that run more often than once per hour are rejected." Five-field
  cron is in UTC (unlike `/loop`, which is local time). Runs on the hour may start minutes late.
  [routines > Add a schedule trigger]
- Hourly limits [routines > Usage and limits]: scheduled runs 100 per hour per account; Run now +
  API fires + re-running a one-off 30 per hour per task; Run now 100 per hour per account; API
  fires 100 per hour per account. "None of these hourly limits has overage." Runs draw down
  subscription usage like interactive sessions.
- Permissions: a run on Anthropic's cloud "begins in auto mode unless auto mode is unavailable";
  it still stops for ask rules and repeated-block thresholds. [routines > Permission prompts during a run]
- Git: each repository "is cloned at the start of a run"; Claude pushes to `claude/`-prefixed
  branches unless told otherwise; control with branch protection rules. GitHub connection missing
  for 72 hours turns the task off. [routines > Repositories and branch permissions]
- Stop conditions: the session ends; on/off switch pauses the schedule; a one-off turns itself
  off after running; run outcomes are Succeeded, Failed, Cancelled and "say how the session ended,
  not whether Claude completed the work". [routines > View and interact with runs; Edit and control scheduled tasks]
- Docs' safety advice from best-practices: protect `main` with a branch rule the task cannot
  bypass and "watch the first few runs of anything new before trusting it unattended."
  [best-practices > Start runs on a schedule or an event (warning)]

### 4.7 Agent view and background sessions

- Status: "Agent view is in research preview." Introduced in v2.1.139. [agent-view > intro (note); Version history]
- What: "Agent view, opened with `claude agents`, is one screen for all your background sessions:
  what's running, what needs your input, and what's done." Each background session "is a full
  Claude Code conversation that keeps running without a terminal attached". [agent-view > intro]
- When: "several independent tasks Claude can work on without you watching every step."
  [agent-view > intro]
- Ways to create a background session: type a prompt in agent view; `/background` (`/bg`) or `←`
  on an empty prompt inside a session; `/fork` (copy the conversation into a new background
  session); `claude --bg "<prompt>"` from the shell (`--bg` cannot be combined with `-p`);
  `claude --bg --exec '<command>'` for a shell job. [agent-view > Dispatch new agents]
- What a repo can configure:
  - Project settings are read: "A background session reads its settings from the directory it
    runs in", including project `env` values. [agent-view > Settings and provider]
  - `worktree.bgIsolation: "none"` in the project's `.claude/settings.json` turns off worktree
    isolation for background sessions. [agent-view > How file edits are isolated]
  - The `agent` setting is the default subagent for dispatched sessions (overridden by
    `claude agents --agent` or naming one in the prompt). [agent-view > Dispatch defaults]
  - `disableAgentView: true` (setting) or `CLAUDE_CODE_DISABLE_AGENT_VIEW` turns the feature off;
    then `/fork` starts a forked subagent and `/subtask` is unavailable.
    [agent-view > Turn off agent view; sub-agents > Fork the current conversation (note)]
  - Custom subagents and skills are dispatch targets: `<agent-name> <prompt>` or `@<agent-name>`
    runs that subagent as the session's main agent; `/<command>` dispatches a skill as the first
    prompt. "Packaging a recurring task as a skill lets you start the same workflow from agent
    view repeatedly without retyping the prompt." [agent-view > Dispatch an agent from agent view]
  - Naming hazard: "a prompt that happens to begin with one of your subagent names dispatches
    that subagent rather than treating the word as plain text." [agent-view > Dispatch an agent from agent view]
    Inference: template subagent names should not be ordinary first words of a task prompt
    (for example `review`, `fix`, `plan`); hyphenated role names avoid accidental matches.
- What a repo cannot set permissively: for a session dispatched from an agent view opened with
  `←`, `permissions.defaultMode` values "`auto` and `bypassPermissions` take effect only from
  managed settings, a `--settings` file, or `~/.claude/settings.json`", and Claude Code refuses a
  project `defaultMode` "that selects a more permissive mode than the session you came from was
  in." [agent-view > Permission mode]
- File isolation: "Before editing files, Claude moves the session into an isolated git worktree
  under `.claude/worktrees/`". Skipped for a session you backgrounded yourself, a session already
  in a linked worktree, non-git directories without a `WorktreeCreate` hook, and writes outside
  the working directory. [agent-view > How file edits are isolated]
- Git behaviour of background sessions in their own worktree: "Claude commits without asking, and
  pushes the branch when the repository has a remote"; opens a draft PR when the task calls for
  it; never pushes to `main`/`master`, force-pushes or merges. Override: "if the task, `CLAUDE.md`,
  or memory says you handle committing or pushing yourself, Claude leaves git to you."
  [agent-view > How file edits are isolated]
  Note for the template: a CLAUDE.md line about who commits and pushes changes this default.
- Stop conditions: `Ctrl+X` (stop; again within two seconds deletes), `/stop` inside the session
  or as a peek reply, `claude stop <id>`; an idle unattached session's process is stopped after
  about an hour (conversation kept; pin with `Ctrl+T`); machine shutdown stops sessions (sleep
  does not). [agent-view > Organize the list; The supervisor process; Sessions show as failed or stopped after shutdown]
- Deleting from agent view removes a Claude-created worktree "including uncommitted changes";
  `claude rm` keeps it when it has uncommitted changes; unpushed commits block the first delete.
  [agent-view > What deleting a session removes]
- Limits: "running ten agents in parallel uses quota roughly ten times as fast as running one";
  sessions are local; dispatch prompts shorter than four characters are rejected.
  [agent-view > Limitations; Prompt rejected as too short]
- State is user-level: `~/.claude/daemon.log`, `~/.claude/daemon/roster.json`,
  `~/.claude/jobs/<id>/state.json`, `~/.claude/jobs/<id>/tmp/` (`CLAUDE_JOB_DIR`). Read state with
  `claude agents --json` (`state`: `working`, `blocked`, `done`, `failed`, `stopped`), not the
  files. [agent-view > Where state is stored; Read session state from a script]
- Shell commands: `claude attach`, `claude logs`, `claude stop`, `claude respawn`, `claude rm`,
  `claude daemon status|logs|stop --any`. [agent-view > Manage sessions from the shell]
- What carries over when backgrounding: background shell commands, backgrounded subagents,
  `/loop` tasks; a dynamic workflow "Continues only when Claude relaunches it"; a running monitor
  stops. Launch flags (`--settings`, `--setting-sources`, `--add-dir`, `--plugin-dir`,
  `--mcp-config`, ...) carry through. [agent-view > What carries over when you background]
- Row summaries cost one short Haiku-class request per turn end and per mid-turn rewrite.
  [agent-view > Cost of row summaries]
- Notifications fire the `Notification` hook with `agent_needs_input` or `agent_completed`.
  [agent-view > Read session state]

### 4.8 Projects (cloud threads coordinated from one conversation)

- Status: "Projects are in public beta on Pro, Max, and Ultra plans and rolling out gradually."
  Not on Team or Enterprise yet; not in the terminal CLI, VS Code or JetBrains.
  [claude-projects > intro (note); Limitations]
- What: "A project is one ongoing conversation where Claude coordinates a stream of related work
  for you." "You tell it what needs doing and it starts a thread for each task." Threads are usually
  cloud sessions. [claude-projects > intro]
- When: "the work has a goal that outlasts one session and keeps producing tasks." Not for one
  task that fits in a session, work where every task needs your machine, or one repeating
  scheduled task. [claude-projects > When to use a project; When something else fits better]
- Configuration is not in the repo: "You change project settings at claude.ai/code or in the
  desktop app, not in `settings.json`." [claude-projects > Project settings reference]
- THE KEY TABLE FOR A REPO TEMPLATE: what a cloud thread picks up from a repository
  [claude-projects > What threads pick up from your repositories]:

  | In each repository | In a cloud thread |
  | - | - |
  | `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/` at the repository root | Loaded from every repository when the thread starts. Subdirectory `CLAUDE.md` files and path-specific rules "aren't loaded" |
  | Skills under `.claude/skills/` | Not loaded (enable the skill for the claude.ai account instead) |
  | Agents and commands under `.claude/` | Not loaded |
  | MCP servers in `.mcp.json` | Not loaded (use claude.ai connectors) |
  | Plugins enabled in `.claude/settings.json` | Not loaded (add in Project settings > Plugins) |
  | Permission rules in `.claude/settings.json` | Not applied |
  | Hooks in `.claude/settings.json` | Not run |
  | `env` in `.claude/settings.json` | Not applied (use the cloud environment) |

  Consequence: in project cloud threads only the root CLAUDE.md and unscoped root rules carry the
  template's guidance; hooks and deny rules (the enforcement layer) do not exist there.
  A thread run on the user's own computer through Remote Control does use "the files, tools, MCP
  servers, and Claude Code settings on that machine, including its hooks and permission rules".
  [claude-projects > Run a thread on your own computer]
- Standing context: project instructions "up to 16,000 characters" sent to each new thread;
  project memory (a `MEMORY.md` index plus files, separate from local auto memory). Guidance:
  "put instructions about a repository in its `CLAUDE.md` and notes about the project in project
  memory." [claude-projects > Give a project standing context]
- Project-instruction brief should cover: purpose; where work happens (repos, branch, PR naming);
  "How a thread checks its own work before calling it done"; what to do when something is
  missing; what needs go-ahead first. [claude-projects > Write project instructions]
- Defaults and limits: a new project "runs every thread on Opus at high effort"; threads run in
  auto mode; "The enforced limit is 500 new threads per day across your projects"; a thread limit
  you ask for "is a preference rather than a cap"; uploads up to 1,000 files and 2 GB at a time,
  single file up to 480 MB; up to 10 folders. [claude-projects > Your first batch; What draws on your plan; Add files and folders]
- Stop conditions: Stop/Esc in a thread; Pause, Archive, Delete in Project settings; threads are
  auto-resolved "after a week with no activity"; a thread at the plan limit waits and by default
  continues at reset. [claude-projects > Open a thread when you need control; Pause, archive, or delete a project; See what needs you in Overview]
- Risk: "If the sandbox can't be resumed, the thread continues from a fresh clone, so uncommitted
  changes can be lost." "On long tasks, ask Claude to commit and push work in progress."
  [claude-projects > Limitations]

### 4.9 Choosing between them (the docs' own guidance, collected)

- Keep the current session going: toward a verifiable condition use `/goal`; on a time interval
  use `/loop`; for deterministic or per-scope checks use a Stop hook.
  [goal > Compare ways to keep a session running]
- Schedule independent of a session: cloud scheduled tasks (no machine needed, fresh clone,
  minimum 1 hour), Desktop scheduled tasks (local files), GitHub Actions; `/loop` only "for quick
  polling during a session". [scheduled-tasks > Compare scheduling options; Limitations]
- Parallel work: subagents for side tasks inside one session; agent view for independent tasks
  you hand off; agent teams when workers must coordinate among themselves (experimental);
  workflows when "A script holds the plan" and scale or cross-checking matters; projects for work
  that outlasts sessions and runs in the cloud. [agents > Choose an approach]
- Verification strength ladder: prompt request, `/goal`, Stop hook, independent review.
  [best-practices > Give Claude a check to run]
- Only these can be shipped in a repo as files: subagent definitions (`.claude/agents/`), saved
  workflows (`.claude/workflows/*.js`), `.claude/loop.md`, Stop and other hooks in
  `.claude/settings.json`, skills that package a recurring task, and env/settings switches
  (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`, `workflowSizeGuideline`, `worktree.bgIsolation`,
  `agent`). Goals, loops, teams, cloud scheduled tasks and projects are started or stored outside
  the repo (session, `~/.claude`, or the claude.ai account). This list is a synthesis of 4.2 to
  4.8, not a statement from one page.


---

## 5. Plugins and marketplaces

### 5.1 What a plugin is, and when the docs say to use one

- "A Claude Code plugin is a directory of skills, agents, hooks, MCP servers, or other components
  that Claude Code installs and loads as one unit." [plugins-overview > intro]
- "A plugin is a directory of components, usually with a manifest. The manifest, a JSON file at
  `.claude-plugin/plugin.json`, gives the plugin its name". [plugins-overview > Understand what a plugin is]
- Standalone first: "Skills, subagents, hooks, and MCP servers all work on their own, without a
  plugin." "Use a plugin when you want several skills, subagents, hooks, or MCP servers packaged
  as one unit." Make one "to give your own setup to teammates, install it in many projects, or
  publish versioned releases." [plugins-overview > Decide whether you need a plugin]
- Always-on cost: "An enabled plugin is part of every session, not only the sessions where you use
  it." Names and descriptions of model-invocable skills, agents and commands are in context every
  turn; its MCP servers run alongside each session; "what the plugin runs, it runs as you."
  [plugins-overview > What an enabled plugin adds to your sessions]
- Marketplace: "a repository or directory with a `.claude-plugin/marketplace.json` file that lists
  plugins and where to fetch each one. It's a catalog, not a hosted store."
  [plugins-overview > Get plugins from a marketplace]
- Install scopes: user ("enabled for you in every project on this computer"), project ("enabled
  for everyone who works in this repository, through the committed `.claude/settings.json`. Each
  collaborator still installs it on their own machine"), local.
  [plugins-overview > Understand install scopes]
- Cloud: a cloud session "doesn't load the plugins in your local settings."
  [plugins-overview > Understand install scopes]

### 5.2 How a plugin gets from settings to a session (loading reference)

- Three stages: declared in settings (`enabledPlugins`, `extraKnownMarketplaces`); fetched to
  disk under `~/.claude/plugins/` (`known_marketplaces.json`, `installed_plugins.json`, `cache/`);
  loaded in the running session (startup or `/reload-plugins`).
  [plugins-loading > Check which stage a plugin reached]
- The disk stage is user-level state: "There is one `known_marketplaces.json` per user, so a
  marketplace you add in one project is available in every project". Root is `~/.claude/plugins`
  unless `CLAUDE_CODE_PLUGIN_CACHE_DIR` is set. [plugins-loading > Check which stage a plugin reached; Find plugins on disk]
- Plugin ids and origins [plugins-loading > Find where a plugin came from]:

  | ID ends in | How it got there | On/off |
  | - | - | - |
  | `@<marketplace>` | Installed from a marketplace you added | `enabledPlugins` `true`/`false` |
  | `@inline` | `--plugin-dir`, `--plugin-url`, `CLAUDE_CODE_PLUGIN_DIRS`, or SDK `plugins` option; session only | On unless manifest `defaultEnabled: false` or settings say `false` |
  | `@skills-dir` | A plugin directory with `.claude-plugin/plugin.json` under `~/.claude/skills/` or the project's `.claude/skills/` | Manifest `defaultEnabled`, unless settings set `"<name>@skills-dir"` |
  | `@synced` | Turned on for the claude.ai account and downloaded | On unless disabled; org-required ones always load |

  `inline`, `skills-dir` and `synced` are reserved marketplace names.
- The two repository routes, in the docs' words: "To share a plugin through a repository, list it
  under `enabledPlugins` in `.claude/settings.json` or place it under `.claude/skills/`." "Claude
  Code doesn't scan a project's `.claude/plugins/` directory."
  [plugins-loading > Plugins shared through a repository]
- Route A, `enabledPlugins` in project settings, needs a per-machine install: "By default, a
  plugin enabled only in your project's `.claude/settings.json` doesn't load at session start
  until you install it on your machine." Install with
  `claude plugin install <name>@<marketplace> --scope project`, repeated "in each of your clones".
  [plugins-loading > Enabled in project settings but not installed]
- Exceptions that load without an install [plugins-loading > Enabled in project settings but not installed]:
  - a seed directory;
  - a plugin listed by a relative path "in a marketplace you added from a local path": "you have
    nothing to run, because the plugin loads at session start";
  - listed by a relative path in the `marketplace.json` of a git marketplace you have added: run
    `/reload-plugins` (current session only), or `CLAUDE_CODE_SYNC_PLUGIN_INSTALL=1` for a `-p` run.
- External-source fetch is not triggered by committed project settings: "Claude Code fetches a
  plugin with an external source only when one of these sources sets the plugin to `true`": user
  settings, an untracked `.claude/settings.local.json`, `--settings`, managed settings.
  [plugins-loading > Enabled in project settings but not installed]
- Route B, a plugin folder under the project's `.claude/skills/` (`<name>@skills-dir`):
  - loads in place, never copied [plugins-loading > In-place and copied plugins];
  - "loads only after the same trust check that applies to project allow rules in
    `.claude/settings.json`. Trusting a parent folder or running with `-p` isn't enough."
  - its MCP servers "go through the same per-server approval as a project `.mcp.json`"; MCP
    bundles or servers from files outside the plugin directory are skipped; "Background monitors
    do not load". [plugins-loading > Trust check and component limits for repository plugins]
  - no parent search: Claude Code "reads the `.claude/skills/` of the session's primary working
    directory and, unlike plain skills and commands, doesn't search parent directories for
    plugins." Launch from the repo root. [plugins-loading > Check why a repository plugin didn't load]
  - blocked silently by managed `strictPluginOnlyCustomization`, a `strictKnownMarketplaces`
    allowlist without `{ "source": "skills-dir" }`, or `blockedMarketplaces`.
    [plugins-loading > Skills-directory plugins blocked by managed settings]
  - shadowing: between two skills-directory plugins of the same name "the copy under
    `~/.claude/skills/` loads and the project's `.claude/skills/` copy is dropped".
    [plugins-loading > Name conflicts]
- `enabledPlugins` precedence, lowest to highest: `--add-dir`, user, project, local, flag
  (`--settings`), managed; merged key by key. To opt out of a project-enabled plugin locally, set
  it `false` in `.claude/settings.local.json`. [plugins-loading > Find where a plugin is enabled]
- Name-conflict order (highest first): managed-settings plugin; `--plugin-dir`/`--plugin-url`/
  `CLAUDE_CODE_PLUGIN_DIRS`; installed marketplace plugin; skills-directory plugin; synced
  plugin. [plugins-loading > Name conflicts]
- In place vs copied: `--plugin-dir` and skills-directory plugins load in place; relative-path
  plugins "in a marketplace you added from a local path" load in place ("Your edits to the source
  directory take effect at the next session start or `/reload-plugins`, and you don't need to
  increase the version"); every other marketplace plugin is copied into
  `cache/<marketplace>/<plugin>/<version>/`, and "Files outside the plugin directory aren't
  copied". [plugins-loading > In-place and copied plugins]
- Paths cannot escape the plugin root (`../shared-utils`, outward symlinks, and on macOS/Linux any
  backslash path are rejected). [plugins-loading > Paths that escape the plugin directory]
- Versions: manifest `version` first, then the marketplace entry's `version`, else derived from
  the source (commit SHA for git sources; `unknown` for a non-git local directory or `npm`).
  "a manifest that pins `\"version\": \"1.0.0\"` keeps every user on the cached copy until its
  author changes the string". [plugins-loading > How Claude Code computes the version]
- Auto-update default: on for Anthropic's official marketplaces, "off for every other
  marketplace"; controlled by `autoUpdate` on the `extraKnownMarketplaces` entry.
  [plugins-loading > Which marketplaces and plugins auto-update]
- Node dependencies of a copied plugin are installed automatically only with `package.json` plus
  `bun.lock`, `npm-shrinkwrap.json` or `package-lock.json`; `yarn.lock` and `pnpm-lock.yaml` are
  skipped; no lifecycle scripts; 60-second timeout; not run for in-place plugins.
  [plugins-loading > Node.js package dependencies]
- Cloud: "A cloud session doesn't add the marketplaces a repository lists under
  `extraKnownMarketplaces`". [plugins-loading > Plugins shared through a repository]
- Synced plugins (claude.ai account) load as `<name>@synced` in signed-in terminal sessions
  (v2.1.273+); turn all off with `syncClaudeAiPlugins: false` "in your user settings"; "To keep
  the plugin out of a project in every environment, set the same key in the project's committed
  `.claude/settings.json`" (`"<name>@synced": false`). [plugins-loading > Control which synced plugins load]

### 5.3 Structure and what a plugin can contain

Layout [plugins-create > Plugin layout; plugins-components > Add each kind of component]:

| Location (plugin root) | Component | Manifest key | Name the user sees |
| - | - | - | - |
| `.claude-plugin/plugin.json` | Manifest (only this file goes in `.claude-plugin/`) | - | plugin `name` |
| `skills/<name>/SKILL.md` | Skills | `skills` (adds to the default scan) | `/<plugin>:<directory>` |
| `SKILL.md` at the root | Single skill (only with no `skills/` and no `skills` key) | - | set `name` in frontmatter |
| `commands/<file>.md` | Commands (older format) | `commands` (replaces the scan; path, array, or object with `source`/`content`) | `/<plugin>:<file>`, subfolders add `:` segments |
| `agents/*.md` | Subagents | `agents` (replaces the scan) | `<plugin>:<name>`; subfolders add segments |
| `hooks/hooks.json` | Hooks, top-level `"hooks"` key, same shape as settings | `hooks` (both load) | - |
| `.mcp.json` | MCP servers | `mcpServers` (manifest wins on same name) | `plugin:<plugin>:<server>`; tools `mcp__plugin_<plugin>_<server>__<tool>` |
| `.lsp.json` | LSP servers | `lspServers` | - |
| `bin/` | Executables on the Bash tool's `PATH` (after the user's own entries) | - | bare command |
| `settings.json` | Default settings; "Only two keys take effect from a plugin, `agent` and `subagentStatusLine`; every other key is dropped" | `settings` | - |
| `output-styles/<name>.md` | Output styles | `outputStyles` | `<plugin>:<name>` in `/output-style` |
| `themes/<slug>.json` | Themes | `experimental.themes` | in `/theme` |
| `workflows/*.js` | Dynamic workflows | `workflows` | `/<plugin>:<meta.name>` |
| `monitors/monitors.json` | Background monitors | `experimental.monitors` | - |
| (manifest only) | Channels bound to an MCP server | `channels` | - |
| (manifest only) | `userConfig` prompts | `userConfig` | `${user_config.*}`, `CLAUDE_PLUGIN_OPTION_<KEY>` |

- What a plugin cannot carry:
  - Project instructions: "To include instructions in a plugin, write them as a skill. Claude Code
    doesn't load a `CLAUDE.md` at the plugin root". [plugins-components > Skills]
  - Permissions, env, or any setting beyond `agent` and `subagentStatusLine`.
    [plugins-components > Default settings]
  - Inference: `.claude/rules/` files and deny rules have no plugin equivalent in these pages, so
    a plugin can deliver the template's skills, agents, hooks, MCP servers, workflows and output
    styles, but not its CLAUDE.md, rules, or permission rules.
- Plugin agents: supported frontmatter is `name`, `description`, `model`, `effort`, `maxTurns`,
  `autoCompactWindow`, `tools`, `disallowedTools`, `skills`, `memory`, `background`,
  `omitClaudeMd`, `isolation`, `color`, and `experimental.cacheTtl`; ignored: `permissionMode`,
  `hooks`, `mcpServers`, `initialPrompt`. [plugins-components > Frontmatter fields in plugin agents]
- Plugin hooks fire for the whole session: "A plugin's hooks don't wait for one of the plugin's
  skills or commands to be used." Hook processes get `CLAUDE_PLUGIN_ROOT`, `CLAUDE_PLUGIN_DATA`;
  quote `"${CLAUDE_PLUGIN_ROOT}/..."` in shell-form commands. [plugins-components > When plugin hooks fire; Environment, quoting, and matching MCP tools]
- Must-hold rules in a plugin go in a hook, not a skill. [plugins-components > Skills]
- Path variables: `${CLAUDE_PLUGIN_ROOT}` (changes per version; "Don't write state there"),
  `${CLAUDE_PLUGIN_DATA}` (resolves to `~/.claude/plugins/data/<id>/`, user-level state),
  `${CLAUDE_PROJECT_DIR}`. [plugins-components > Reference plugin paths and store data]
- Monitors: run "with your full user permissions and outside the sandbox"; not in `-p` mode; do
  not load from repository (skills-dir/project-scope) plugins (5.2).
  [plugins-components > Monitors]
- Renaming effect of moving a standalone setup into a plugin: skills and agents gain the
  `<plugin>:` prefix; "hooks have no prefix, so a hook that is in both your settings file and
  `hooks/hooks.json` runs twice". [plugins-create > Convert an existing .claude/ setup]
- Session-only loading for development: `claude --plugin-dir ./my-plugin` (directory, `.zip`, or
  since v2.1.265 a folder of plugins), `--plugin-url`, or `CLAUDE_CODE_PLUGIN_DIRS` (v2.1.280+).
  "Project and local settings can't set this variable". [plugins-create > Develop without a marketplace]
- `claude plugin init <name>` scaffolds under `~/.claude/skills/` (user level). The project
  equivalent is created by hand: "create the same layout yourself at
  `<project>/.claude/skills/<name>/`, including its `.claude-plugin/plugin.json`."
  [plugins-create > Share the plugin through a repository]
- In a skills-directory plugin the root `SKILL.md` is also a plain skill invoked as `/my-tool`;
  skills under `skills/` get the prefix (`/my-tool:example`). [plugins-create > Name the plugin's skills]
- Validation: `claude plugin validate <path>` (add `--strict` to fail on warnings); `/plugin`
  Installed and Errors tabs; `claude plugin list`. [plugins-create > Test and debug]
- Behavioural testing: `claude plugin eval` "runs your test cases with and without the plugin and
  scores the difference." [plugins-create > Check that the plugin changes Claude's behavior]

### 5.4 Manifest (`.claude-plugin/plugin.json`)

- Optional: "Without it, Claude Code loads the components it finds in the standard layout." The
  name then comes from the marketplace entry or the directory name. [plugins-manifest-reference > Manifest file]
- "`name` is the only required key." [plugins-manifest-reference > Fields]
- Fields (type; notes) [plugins-manifest-reference > Fields]:

  | Field | Type | Notes |
  | - | - | - |
  | `$schema` | String | Ignored at load |
  | `name` | String | Required. Kebab-case; no spaces, `@`, `:`, path separators. Namespaces every component |
  | `displayName` | String | UI name; not used for namespacing |
  | `version` | String | Not checked against semver. "Setting it keeps users on that version until you change it" |
  | `description` | String | Shown in `/plugin` |
  | `author` | Object | `name` required; optional `email`, `url` |
  | `homepage` | String | Must parse as a URL or the plugin fails to load |
  | `repository` | String | Not validated |
  | `license` | String | SPDX identifier |
  | `keywords` | Array of strings | Discovery tags |
  | `metadata` | Object | Free-form; not read |
  | `icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl` | String | Anthropic directory listing only; not read by Claude Code |
  | `defaultEnabled` | Boolean | Default `true`. Whether the plugin starts enabled when the user has not set it |
  | `dependencies` | Array of strings or objects | `"name"`, `"name@marketplace"`, or `{ name, marketplace, version }` |
  | `settings` | Object | "Only `agent` and `subagentStatusLine` take effect" |
  | `userConfig` | Object | Values prompted for on enable |
  | `types` | Path | `.d.ts` for a mod |
  | `channels` | Array of objects | Each bound to one of the plugin's MCP servers |
  | `skills` | Path or array of paths | Directories; `"."` is the plugin root. Adds to the default scan |
  | `commands` | Path, array of paths, or object | Replaces the default scan. Object values set exactly one of `source` or `content`, plus optional `description`, `argumentHint`, `model`, `allowedTools` |
  | `agents` | Path or array of paths | `.md` files only (no directories). Replaces the default scan |
  | `hooks` | Path, object, or array of either | Merged with `hooks/hooks.json`. A hooks file needs the top-level `"hooks"` wrapper; an inline object is the event map itself |
  | `mcpServers` | Path, object, or array of either | `.json` files, `.mcpb`/`.dxt` bundles (path or `https://` URL), or inline map. Later names replace earlier |
  | `lspServers` | Path, object, or array of either | Strict objects; `command` and `extensionToLanguage` required |
  | `outputStyles` | Path or array of paths | Replaces the default scan |
  | `workflows` | Path or array of paths | Replaces the default scan |
  | `experimental` | Object | Holds `themes`, `monitors`, `evals` |
  | `experimental.themes` | Path or array of paths | Replaces `themes/` |
  | `experimental.monitors` | Path or inline array | Defaults to `monitors/monitors.json`; entries need `name`, `command`, `description`; optional `when` (`"always"` default, or `"on-skill-invoke:<skill>"`) |
  | `experimental.evals` | Path or array of paths | Eval case directory if not `evals/` |

- Reserved names: `claude plugin validate` errors on names starting with `claude-`, `anthropic-`,
  `anthropics-` or `cc-plugin-`, on `claude`, `anthropic`, `anthropics`, `claude-code`,
  `claude-mods`, and on `official` beside `claude`/`anthropic`; warns when `claude` or `anthropic`
  appears as a whole word elsewhere. [plugins-manifest-reference > name]
  Note: a plugin made from this repository must not take a `claude-` name; `tackroom` is clear.
- Unknown top-level keys are stripped with a validate warning; unknown keys inside `userConfig`
  options, `channels` entries, `lspServers` configs and `monitors` entries are errors.
  [plugins-manifest-reference > Unrecognized fields]
- Path rules: every component path is relative to the plugin root and "must start with `./`";
  must resolve inside the root and exist. [plugins-manifest-reference > Path rules]
- Combination with defaults: replaces (`commands`, `agents`, `outputStyles`, `workflows`,
  `experimental.themes`, `experimental.monitors`); adds (`skills`); merges (`hooks`, `mcpServers`,
  `lspServers`). [plugins-manifest-reference > How each key combines with its default location]
- `userConfig` option fields: `type` (`string`, `number`, `boolean`, `directory`, `file`),
  `title`, `description` required; optional `required`, `default`, `options` (v2.1.271+),
  `multiple`, `sensitive`, `min`/`max`. Non-sensitive values are saved under `pluginConfigs` "in
  the user's `settings.json`"; sensitive ones in the platform's secure store.
  [plugins-manifest-reference > User configuration; Where values are stored]
- Environment variables: `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, `${CLAUDE_PROJECT_DIR}`.
  "The variables aren't present in the environment of commands Claude runs through the Bash
  tool"; in skill, command and agent content write the `${...}` reference in the Markdown body.
  [plugins-manifest-reference > Where each variable resolves]
- "A `CLAUDE.md` at the plugin root isn't loaded as context". [plugins-manifest-reference > Standard layout]
- Marketplace entry vs manifest: with no `plugin.json` the entry is the manifest; with one and
  `strict` unset or `true` the entry's `commands`, `agents`, `skills`, `outputStyles`, `themes`
  are appended; with `strict: false` any such declaration is a conflict. The manifest's `version`
  overrides the entry's; the entry's `defaultEnabled` and display fields override the manifest's.
  [plugins-manifest-reference > Marketplace entries and the manifest]

### 5.5 Plugin dependencies

- `dependencies` in `plugin.json`: strings (`"audit-logger"`, `"name@marketplace"`) or objects
  with `name` (required), `version` (semver range such as `~2.1.0`, `^2.0`, `>=1.4`, `=2.1.0`),
  `marketplace`. Bare names resolve in the declaring plugin's own marketplace.
  [plugins-dependencies > Declare a dependency with a version constraint]
- Without a constraint "a dependency moves to each new release its marketplace publishes the next
  time users update." [plugins-dependencies > Declare dependencies]
- Bundle pattern: a plugin with only `name` and `dependencies` installs a curated set with one
  command. [plugins-dependencies > Bundle plugins for a team]
- Cross-marketplace dependencies are not installed unless the root marketplace lists the target
  in `allowCrossMarketplaceDependenciesOn` (or the user already has it enabled at the same scope).
  [plugins-dependencies > Depend on a plugin from another marketplace]
- Version constraints resolve against git tags named `<plugin-name>--v<version>`; create with
  `claude plugin tag --push`. For a relative-path plugin the marketplace repository is tagged. "A
  local folder that isn't a git repository has no tags, so Claude Code installs the dependency
  from the folder's current contents". [plugins-dependencies > Create a release tag; How a constraint resolves against tags]
- Non-git sources (`npm`, `archive`, `command`): the constraint is only checked at load, against
  the `version` in the dependency's `plugin.json`. [plugins-dependencies > Constrain a dependency that has a non-git source]
- Conflicting ranges (`~2.1` vs `~3.0`) fail the second install with `has conflicting version
  requirements`. [plugins-dependencies > Combine constraints from several plugins]
- Local testing: `claude --plugin-dir ./my-dependency --plugin-dir ./my-plugin`.
  [plugins-dependencies > Test a plugin and its dependency locally]

### 5.6 Plugin security and trust

- "A Claude Code plugin you install can execute arbitrary code on your machine with your user
  privileges." [plugins-security > intro]
- What runs outside permission rules and the sandbox: "command hooks and monitors are shell
  commands that run with your full user permissions." Hooks, monitors, MCP servers, LSP servers
  and mod processes run "outside the sandbox." Claude's own tool
  calls (the plugin's MCP tools, Bash running `bin/` executables) do go through permission rules.
  [plugins-security > Understand what a plugin can do]
- Skills, commands and agents "enter Claude's context as instructions". [plugins-security > Understand what a plugin can do]
- Auto-update means "the files you reviewed can change on disk." [plugins-security > Understand what a plugin can do]
- "Installing a plugin also enables it, unless its manifest or marketplace entry sets
  `defaultEnabled: false`". [plugins-security > Understand what a plugin can do]
- Review steps: `claude plugin marketplace list` (source), `/plugin` details pane ("Will
  install"), read `hooks/hooks.json`, `.mcp.json`, `bin/`, and
  `claude --plugin-dir <dir> plugin details <name>` for a component inventory.
  [plugins-security > Review a plugin before you install]
- Marketplace tiers by name: official names (for example `claude-plugins-official`,
  `claude-code-plugins`, `agent-skills`, `anthropic-agent-skills`), community
  (`claude-community`, `claude-plugins-community`, `healthcare`), third-party (everything else,
  including "A marketplace that a coworker or your organization publishes"). Official and
  community names are accepted only from `github.com/anthropics/` sources.
  [plugins-security > Identify Anthropic's marketplaces by name]
- Managed settings can allowlist/blocklist marketplaces, force-enable plugins, turn off
  `--plugin-dir`/`--plugin-url`/`CLAUDE_CODE_PLUGIN_DIRS`, and limit hooks to managed ones.
  [plugins-security > Enforce plugin controls for your organization]
- Uninstall leaves cached files under `~/.claude/plugins/cache/` for 14 days.
  [plugins-security > Remove a plugin you no longer trust]

### 5.7 Marketplaces: file format and sources

- A marketplace is "a directory or repository with a `.claude-plugin/marketplace.json` file that
  lists your plugins and where to fetch each one." [plugins-create-marketplace > intro]
- `marketplace.json` required keys: `name`, `owner` (`name` required), `plugins`. Optional:
  `$schema`, `description`, `version`, `metadata.description`, `metadata.version`,
  `metadata.pluginRoot` (v2.1.239+), `forceRemoveDeletedPlugins`,
  `allowCrossMarketplaceDependenciesOn`, `renames`. Unknown keys are ignored (validate warns).
  [plugins-marketplace-reference > Top-level fields; Marketplace file]
- Plugin entry: `name` and `source` required; optional `description`, `version`, `category`,
  `tags`, `strict` (default `true`), `relevance`, `dependencies`, `defaultEnabled` (default
  `true`), `displayName`, `metadata`, `headers`, `headersHelper`, plus every `plugin.json` field
  except the directory listing fields. [plugins-marketplace-reference > Plugin entries]
- Plugin source types: relative path string (must start with `./`; `"."` is the marketplace
  root), `github` (`repo`, `ref`, `sha`), `url` (`url`, `ref`, `sha`), `git-subdir` (`url`,
  `path`, `ref`, `sha`), `npm` (`package`, `version`, `registry`), `archive` (`url`, `sha256`),
  `command` (`command`, `timeout`, `mode`; v2.1.229+). [plugins-marketplace-reference > Plugin sources]
- A relative-path plugin source resolves only when Claude Code has the marketplace's files:
  marketplace sources "`github`, `git`, `file`, and `directory`" yes; `url` no; for `settings`,
  "relative paths are rejected outright." [plugins-marketplace-reference > Relative path plugin source]
- Marketplace source types usable in `extraKnownMarketplaces`: `url`, `github`, `git`, `file`
  (`path` to the `marketplace.json`), `directory` (`path` = the marketplace root), `settings`
  (inline catalog: `name`, `plugins`, `owner`; plugin sources must be object types). `npm`,
  `skills-dir`, `hostPattern`, `pathPattern` fail to load there.
  [plugins-marketplace-reference > Marketplace sources; Fields by type]
- Naming rules: the entry name should equal the plugin's manifest name ("Keep the two names the
  same"); a user "can't have two marketplaces with the same name registered at once"; a long list
  of reserved names (official and community names, `inline`, `builtin`, `skills-dir`, `synced`,
  `npm`, `pip`, `uv`, `cargo`, `github`, `gh`, names starting with `claudeai-`, names that
  impersonate official ones such as `claude-plugins-v2`).
  [plugins-create-marketplace > Keep the entry name and the manifest name the same; plugins-marketplace-reference > Reserved names]
- Adding a marketplace: `claude plugin marketplace add <source>` or `/plugin marketplace add`
  with `owner/repo`, a git URL, a local directory or file ("Start a relative path with `./` or
  `../`"), or a hosted `marketplace.json` URL. The CLI reports "(declared in user settings)".
  [plugins-install > Add a marketplace; plugins-create-marketplace > Create a marketplace step 4]
- One-step form: `claude plugin install <plugin> --marketplace <source>` (v2.1.292+); a new
  marketplace "is declared in your user settings even when you pass `--scope project`".
  [plugins-install > Add and install from your shell]
- Local-path marketplace behaviour: "Claude Code reads the plugin's files directly from
  `my-marketplace/plugins/`." Edits "take effect at the next session start or when you run
  `/reload-plugins` in a session, with no change to the plugin's `version`."
  [plugins-create-marketplace > Test an edit to a plugin]
- Removing a marketplace uninstalls every plugin installed from it. [plugins-install > Manage marketplaces]
- Validation: `claude plugin validate ./my-marketplace`; a missing relative source directory
  passes validation and fails at install. [plugins-create-marketplace > Validate and test]

### 5.8 How a project enables a plugin or marketplace from its own `.claude/settings.json`

- Keys: `enabledPlugins` (object mapping `plugin-name@marketplace-name` to a Boolean; scope "Any
  file") and `extraKnownMarketplaces` (object mapping a marketplace name to `{ source, autoUpdate? }`;
  scope "Any file"). [settings-reference > enabledPlugins; extraKnownMarketplaces] (section-only
  read of `docs-en-settings-reference-md`, the two key entries; that page is not one of the
  assigned full reads.)
- Trust gate: project `extraKnownMarketplaces` entries are honoured "only after you accept the
  workspace trust dialog for that folder"; in an untrusted folder, "including a `-p` run there,
  it ignores them without a message." [settings-reference > extraKnownMarketplaces]
- Enabling is not installing: project settings turn a plugin on "for everyone in the repository.
  This doesn't install them, so each user installs them". Each collaborator "also runs `claude
  plugin install <name>@<marketplace> --scope project` once per clone".
  [settings-reference > enabledPlugins; plugins-install > Choose an install scope]
- Project settings beat user settings for `enabledPlugins`; a user opts out with `false` in
  `.claude/settings.local.json`. [settings-reference > enabledPlugins]
- Uninstalling a project-enabled plugin offers "Disable for me" (writes `false` to
  `.claude/settings.local.json`) or "Uninstall for everyone" (edits the shared file).
  [plugins-install > Uninstall a plugin the project enables]
- `directory` marketplace source: "a local filesystem path, with `path`. Use it for development,
  or for a marketplace your organization deploys to each machine." The only example path is
  absolute (`/opt/acme/claude-plugins`, in a managed-settings example).
  [settings-reference > Marketplace source types; prependPlugins example]
- `pluginConfigs` (plugin `userConfig` answers) is "User or managed" only: "Claude Code ignores
  project and local entries". [settings-reference > pluginConfigs]
- Not loaded in cloud sessions or project cloud threads (see 4.8 and 5.2).

### 5.9 Can a directory inside the repo act as the plugin or marketplace? Assessment against file copying

What the docs establish:

1. Skills-directory plugin (documented, project-level, no install step). A folder
   `<project>/.claude/skills/<name>/` containing `.claude-plugin/plugin.json` loads as
   `<name>@skills-dir`, in place, after the workspace trust dialog.
   [plugins-create > Share the plugin through a repository; plugins-loading > Plugins shared through a repository]
   Costs stated by the docs: launch must be from the directory whose `.claude/skills/` holds it
   (no parent search); MCP servers need per-server approval; monitors do not load; a same-named
   plugin under the user's `~/.claude/skills/` shadows it; managed settings can silently block
   it; skills under its `skills/` become `/<name>:<skill>` and agents `<name>:<agent>`; plugin
   agents lose `hooks`, `mcpServers`, `permissionMode`, `initialPrompt`.
2. Local `directory`/`file` marketplace with relative-path plugins (documented for development and
   for org-deployed machines). Such plugins load in place at session start with "nothing to run".
   [plugins-loading > Enabled in project settings but not installed; In-place and copied plugins]
   What the docs do not state: whether a `path` in a project `.claude/settings.json`
   `extraKnownMarketplaces` entry may be relative to the repository. Every documented example is
   an absolute path or a CLI argument. An absolute path cannot be committed portably.
   Registering a marketplace also writes user-level state (`known_marketplaces.json` "per user";
   `marketplace add` "declared in user settings"), which conflicts with a no-global-state goal.
3. `--plugin-dir <repo-dir>` loads a repo folder as a plugin for one session, but it is a launch
   flag; `CLAUDE_CODE_PLUGIN_DIRS` cannot be set from project or local settings.
   [plugins-create > Load plugins from an environment variable]
4. `.claude/plugins/` is not scanned. [plugins-loading > Plugins shared through a repository]

What no plugin route can carry (so files must be copied anyway): `CLAUDE.md`/`AGENTS.md`,
`.claude/rules/`, `permissions` and other settings keys, `.claude/loop.md`, `.mcp.json` at
project scope, `.worktreeinclude`. A plugin's `settings.json` honours only `agent` and
`subagentStatusLine`, and a plugin-root `CLAUDE.md` is not loaded. [plugins-components > Default settings; Skills]

Inference (assessment, not a docs statement):
- For a template synced into many repos with no user-level config, plain file copying into
  `.claude/` is the only route that covers every mechanism, works without an install step, keeps
  unprefixed names (`/plan`, `reviewer`), keeps full subagent frontmatter, and leaves no state in
  `~/.claude/plugins`.
- A skills-directory plugin inside the repo is the closest plugin-shaped alternative that stays
  project-level, but it still has to be copied into each repo (so it does not remove the sync
  step); what it buys is one namespaced unit with bundled hooks/MCP/`bin/`, at the cost of the
  restrictions in item 1.
- A hosted marketplace plus `extraKnownMarketplaces` + `enabledPlugins` in each repo gives
  versioned updates without re-copying, but needs a per-machine, per-clone install, writes
  user-level state, does not load in cloud sessions, and still cannot deliver instructions,
  rules or permissions. The features-overview trigger ("A second repository needs the same
  setup" -> "Package it as a plugin") points this way for skills/agents/hooks, so a hybrid
  (copied instruction layer, plugin for the tool layer) is consistent with the docs; whether it
  is worth the install step is a judgment call the docs do not settle.


---

## 6. Output styles, worktrees, checkpointing, sessions

### 6.1 Output styles

- What: "a set of instructions that sets Claude's role, tone, and response format for every
  response in a session." Not enforcement: "It doesn't guarantee that something always happens
  or never happens." [output-styles > intro (note)]
- Built-ins besides Default: Proactive, Concise (v2.1.237+), Explanatory, Learning. Default means
  "no output style is selected". [output-styles > Built-in output styles]
- Locations: user `~/.claude/output-styles`; project `.claude/output-styles` (project-level);
  managed `.claude/output-styles` in the managed settings directory; plugins' `output-styles/`.
  Project styles load from every `.claude/output-styles/` between cwd and the repo root; closest
  wins on a name clash. [output-styles > Create a custom output style]
- Frontmatter (all optional; hyphenated; misspelled fields ignored silently; unparseable YAML
  loads the style under its file name with no fields) [output-styles > Frontmatter reference]:

  | Field | Default | Description |
  | - | - | - |
  | `name` | the file name | Shown in the `/config` picker |
  | `description` | none | Shown in the `/config` picker |
  | `keep-coding-instructions` | `false` | `true` keeps Claude Code's built-in software engineering instructions alongside the style |
  | `force-for-plugin` | `false` | Plugin styles only; applies the style whenever the plugin is enabled, overriding the user's `outputStyle` |

- Selecting: `/output-style <style>`, `/config`, or the `outputStyle` settings key. The command
  and menus "save your choice to `.claude/settings.local.json`". The settings value is
  case-sensitive (`Explanatory`; `explanatory` gives Default). Project settings take precedence
  over `~/.claude/settings.json`. [output-styles > Change your output style]
  Inference: a template can set `outputStyle` in committed `.claude/settings.json`, which then
  overrides each user's global default for that repo.
- Loading and cost: "Claude Code sends the active style's instructions with every request."
  A custom style without `keep-coding-instructions: true` drops the built-in engineering section
  ("how to scope changes, write comments, and verify work") on the full system prompt.
  [output-styles > How output styles work]
- Mid-session: a switch applies from the next message (since v2.1.251); but style files are read
  at startup, "so if you create or edit one during a running session, restart Claude Code".
  [output-styles > Change your output style; Create a custom output style]
- Scope: main conversation and forks; "Other subagents run their own system prompt, so styles
  don't change how they respond." Survives compaction (section 7). [output-styles > How output styles work]
- Choosing [output-styles > Choose between an output style and other features]: voice/length/
  format/role for every response -> output style; project conventions -> CLAUDE.md; one kind of
  task -> skill; must happen every time -> hook; focused helper -> subagent; launch-time addition
  -> `--append-system-prompt`.

### 6.2 Checkpointing and rewind

- "checkpointing automatically captures the state of your code before each prompt you send that
  starts a turn." Snapshots for "the 100 most recent checkpoints in a session"; saved with the
  conversation so `/rewind` works after resume; removed by the retention sweep (about 30 days,
  `cleanupPeriodDays`). [checkpointing > Automatic tracking]
- `/rewind` (or `Esc` twice on an empty prompt) options: Restore code and conversation; Restore
  conversation; Restore code; Summarize from here; Summarize up to here; Never mind.
  [checkpointing > Rewind and summarize]
- Summaries can be guided by typing instructions on the Summarize row; originals stay in the
  transcript. For a separate attempt use `/branch` or `claude --continue --fork-session`.
  [checkpointing > Guide a summary]
- Limits [checkpointing > Limitations]:
  - "A file that only Bash commands changed isn't tracked and stays as it is."
  - Subagent edits are usually not captured; only a foreground forked skill's edits are restored.
  - External changes and other sessions' edits are not tracked.
  - Symlinked and hard-linked files are skipped on restore ("Config files a dotfile manager
    symlinks into your project and files pnpm hard-links into place both fall into this
    category").
  - "Checkpoints are designed for quick, session-level recovery", not a replacement for Git.
- Not configurable from the repo beyond `cleanupPeriodDays`; state lives in
  `~/.claude/file-history/<session>/`. [claude-directory > Cleaned up automatically]

### 6.3 Worktrees

- What: "Running each Claude Code session in its own worktree gives it a separate copy of the
  files to edit". They "isolate file edits". [worktrees > intro]
- Start: `claude --worktree <name>` (`-w`) creates `.claude/worktrees/<name>/` on branch
  `worktree-<name>`; no name generates one such as `bright-running-fox`; `"#1234"` or a PR/MR URL
  creates `.claude/worktrees/pr-<number>`. Interactive runs need workspace trust; `-p` skips the
  check. Claude can also enter one via the `EnterWorktree` tool. [worktrees > Start Claude in a worktree; Branch from a pull request]
- Repo-level configuration (all project-level):
  - `.gitignore`: "Add `.claude/worktrees/` to your `.gitignore`". [worktrees > Start Claude in a worktree (tip)]
  - `.worktreeinclude` at the project root, `.gitignore` syntax: "Only files that match a pattern
    and are also gitignored are copied". Applies to `--worktree`, subagent worktrees and desktop
    parallel sessions; not processed under a `WorktreeCreate` hook. Keep it to small files: "it
    copies rather than links". [worktrees > Copy gitignored files into worktrees; best-practices > Run sessions in parallel]
  - `worktree.baseRef`: `"fresh"` (default; branch from the remote default branch) or `"head"`
    (current local `HEAD`). "You can't set `worktree.baseRef` to a branch name."
    [worktrees > Choose the base branch]
  - `worktree.bgIsolation: "none"` (4.7) and `worktree.symlinkDirectories` (named in
    best-practices for large directories such as `node_modules`).
  - `WorktreeCreate`/`WorktreeRemove` hooks replace the git logic (non-git VCS, other locations).
    [worktrees > Replace worktree creation with a hook; Non-git version control]
  - Subagent frontmatter `isolation: worktree`. [worktrees > Isolate subagents with worktrees]
- Symlink constraint: "Claude Code refuses to create a worktree when `.claude`,
  `.claude/worktrees`, or the worktree directory itself is a symlink".
  [worktrees > Worktree creation fails on a symlinked path]
  Consequence: a template must be copied into `.claude/`, not provided by symlinking `.claude`.
- Hooks in worktrees: "`${CLAUDE_PROJECT_DIR}` stays put"; "it still points at the project root
  where the session started", so `${CLAUDE_PROJECT_DIR}/.claude/hooks/check-style.sh` runs the
  main checkout's script; the hook input's `cwd` is the worktree root.
  [worktrees > Ask Claude to create a worktree (note)]
  Consequence: template hook scripts that act on files must read `cwd` from the hook input, not
  assume `${CLAUDE_PROJECT_DIR}`.
- What worktrees share with the main checkout: the `.git` directory; project-scope plugins;
  "don't ask again" approvals (saved to the main checkout's `.claude/settings.local.json`); and,
  when the worktree has no `.claude/skills` at its root (for example because it is gitignored),
  the main checkout's skills, agents and commands. [worktrees > What worktrees share with the main checkout]
- Instruction files for worktree subagents: a subagent in its own worktree "takes the instruction
  files it starts with from your main conversation, not from its worktree", and under
  `.claude/worktrees/` it does not load the worktree root's `CLAUDE.md` or `.claude/rules/`.
  [worktrees > Isolate subagents with worktrees]
- Desktop-app worktree sessions read settings, hooks, skills, agents, commands and `.mcp.json`
  from the main checkout's root; "`CLAUDE.md` files and `.claude/rules/` still load from the
  worktree." [worktrees > What worktrees share with the main checkout]
- Isolation enforcement (four checks): file edits targeting the main checkout; command working
  directory; git redirects (`git -C`, `--git-dir`, `GIT_DIR`, `GIT_WORK_TREE`, `cd` then git);
  command shape. Not covered: "a command that writes into the main checkout without running git
  there, such as `cp` or a shell redirect". [worktrees > How Claude Code enforces isolation]
- Cleanup: clean unnamed worktree is removed on exit; named or dirty ones prompt; `-p` runs leave
  worktree and lock in place (`git worktree remove`, `git worktree unlock`). A periodic sweep
  removes subagent and background-session worktrees older than `cleanupPeriodDays` unless they
  hold work. [worktrees > Clean up worktrees; Clean up subagent and background-session worktrees]
- Gotchas: repo-local git filter drivers (for example `git lfs install --local`) are skipped, so
  LFS files are pointers (`git lfs pull`); `git replace` objects are ignored; `includeIf` in the
  repository `.git/config` blocks creation. [worktrees > Troubleshooting]
- "A worktree is a fresh checkout, so initialize your development environment there"; keep the
  install command in CLAUDE.md so Claude runs it in a new checkout.
  [worktrees > Set up the worktree environment; best-practices > Run sessions in parallel]

### 6.4 Sessions (resume, name, branch) and long tasks

- "A session is a saved conversation tied to a project directory. Claude Code stores it locally as
  you work". [sessions > intro]
- Storage is user-level: `~/.claude/projects/<project>/<session-id>.jsonl`; the format "is
  internal to Claude Code and changes between versions". Retention `cleanupPeriodDays` (30-day
  default, settable in `settings.json`). Move with `CLAUDE_CONFIG_DIR` (environment variable).
  `CLAUDE_CODE_PROJECT_DIR_NAME` must be set in the shell environment: "an `env` block in a
  settings file can't set it." [sessions > Where transcripts are stored; Name the project directory yourself]
- Resume entry points: `claude --continue`, `claude --resume [name|id|transcript-path]`,
  `claude --from-pr <number>`, `/resume`. [sessions > Resume a session]
- What a resume restores: conversation history (from the last compaction summary onward), model,
  agent (`--agent` or `agent` setting), permission mode (with exceptions; `bypassPermissions` is
  not restored), an active `/goal`, unexpired session-scoped scheduled tasks. Not restored:
  interrupted tool calls, background Bash and monitor tasks, and launch flags such as
  `--mcp-config`, `--settings`, `--plugin-dir`, `--add-dir`. The standard settings files "are
  re-read at launch, so configuration that lives in them doesn't need to be passed again."
  [sessions > What a resumed session restores]
  Consequence: configuration kept in committed project files survives resume; configuration
  passed by flag does not.
- Naming for multi-day work: `claude -n auth-refactor`, `/rename auth-refactor`, then
  `claude --resume auth-refactor`; `/clear oauth-migration` names the session being left.
  [sessions > Name your sessions; Manage context within a session; best-practices > Steer the session]
- Branching: `/branch [name]` or `claude --continue --fork-session` copies the conversation and
  leaves the original intact. Resuming the same session in two terminals without forking
  interleaves messages into one transcript. [sessions > Branch a session]
- Context controls inside a session: `/clear`, `/compact [instructions]`, `/context`.
  [sessions > Manage context within a session]
- Hidden from the picker and `--continue`: sessions whose first prompt was `/loop`, and `-p`/SDK
  sessions (resumable by ID). [sessions > /loop, -p, Agent SDK, and background sessions]
- Script access: `claude -p --output-format json`, `claude -p --resume <id> ... | jq -r '.result'`,
  the `transcript_path` hook input (a `SessionEnd` hook can archive the transcript), `/export`.
  [sessions > Access conversations from scripts]
- Cost of resuming a long conversation after a break: the "Resume this conversation?" dialog
  estimates the share of the 5-hour limit the saved conversation alone would use.
  [sessions > The "Resume this conversation?" dialog]
- Handoff: the saved pages document no dedicated "handoff" command or file. The documented
  building blocks for continuing long work in a fresh context are a spec file written first
  ("start a fresh session to build from it"), `/compact <focus>`, `/rewind` summaries, named
  sessions, project-root CLAUDE.md (re-injected after compaction), and for cloud work project
  memory. [best-practices > Brainstorm with Claude first; context-window > When your context fills up]
  Inference: a template-level handoff skill (writing state to a file in the repo) is a custom
  convention, not a Claude Code feature.


---

## 7. Context window: what loads, what it costs, what survives

Caveat: the saved `context-window` page is the written companion of an interactive simulation. The
saved markdown says the timeline uses "representative token counts" but contains none of the
per-item token figures from the simulation; the only numbers in the saved text are the compaction
caps below. [context-window > What the timeline shows]

- Loads before the first prompt: "CLAUDE.md, auto memory, MCP tool names, and skill descriptions
  all load into context." AGENTS.md can load in place of CLAUDE.md; an output style or
  `--append-system-prompt` text adds more. [context-window > What the timeline shows]
- During work: each file read adds to context, path-scoped rules "load automatically alongside
  matching files", a PostToolUse hook fires after each edit. [context-window > What the timeline shows]
- Subagent: "Only the summary and a small metadata trailer come back."
  [context-window > What the timeline shows]
- What survives compaction [context-window > What survives compaction]:

  | Mechanism | After compaction |
  | - | - |
  | System prompt and output style | Both still apply |
  | Project-root CLAUDE.md and unscoped rules | Re-injected from disk |
  | Auto memory | Re-injected from disk |
  | Skill descriptions | Rebuilt from current skills and re-injected (v2.1.304+) |
  | Git status snapshot | If the session started with one, a fresh one is read |
  | Plan written in plan mode | Re-injected from disk |
  | Rules with `paths:` frontmatter | Reloaded on demand |
  | Nested CLAUDE.md in subdirectories | Reloaded on demand |
  | Files Claude read or edited | Up to five re-read, most recently modified first |
  | Invoked skill bodies | Re-injected, capped at 5,000 tokens per skill and 25,000 tokens total; oldest dropped first |
  | Background commands and background subagents | Keep running; Claude is reminded which |
  | Context that hooks added earlier | Summarized with the rest |
  | SessionStart hooks matching the `compact` source | Run again; output added to the compacted context |

- Re-read files: "A file over 5,000 tokens comes back as a path reference without its content".
  [context-window > What survives compaction]
- Design consequence stated by the docs: "If a rule must persist across compaction, drop the
  `paths:` frontmatter or move it to the project-root CLAUDE.md." [context-window > What survives compaction]
- Skill truncation: "Truncation keeps the start of the file, so put the most important
  instructions near the top of `SKILL.md`." [context-window > What survives compaction]
- Compaction summarisation inherits the session's extended-thinking configuration "As of
  v2.1.198". [context-window > What survives compaction]
- Before the automatic pass: `/compact <focus>`, `/rewind` then "Summarize from here" or
  "Summarize up to here", `/autocompact 500k` (set the threshold), `/clear` between unrelated
  tasks, delegate large reads to a subagent. [context-window > When your context fills up]
- 1M window: "Fable models, Sonnet 5 and later, Haiku 5.5, Opus 4.6 and later, and Sonnet 4.6
  support a 1 million token context window." [context-window > When your context fills up]
- Inspect a real session: `/context` gives "a live breakdown by category with optimization
  suggestions". [context-window > Check your own session]

### 7.1 Related facts from how-claude-code-works and common-workflows

- The loop has three phases: gather context, take action, verify results. Claude Code "is the layer around
  the model that provides the tools and manages the context the model sees"; that layer is the
  "agentic harness". [how-claude-code-works > The agentic loop]
- Persistence rule: "Put persistent rules in CLAUDE.md rather than relying on conversation
  history." [how-claude-code-works > When context fills up]
- Compaction steering from the repo: "add a \"Compact Instructions\" section to CLAUDE.md or run
  `/compact` with a focus". [how-claude-code-works > When context fills up]
- The compaction summary "keeps your requests and key code snippets, but detailed instructions
  from early in the conversation may be lost." [how-claude-code-works > When context fills up]
- Context Claude Code adds on its own (system reminders): CLAUDE.md files, output-style
  instructions, a note when a previously read file changes on disk, and "The commit and pull
  request attribution lines". Controls: `attribution`, and `includeGitInstructions: false` to
  remove the built-in commit and PR instructions. [how-claude-code-works > Context Claude Code adds on its own]
- Auto mode is the built-in starting permission mode for interactive terminal and VS Code
  sessions "With Claude Code v2.1.283 or later". [how-claude-code-works > Control what Claude can do]
- "`/init` generates a starter CLAUDE.md"; "`/doctor` runs a setup checkup".
  [how-claude-code-works > Ask Claude Code for help]
- `@file` mentions: content is included when it fits the Read tool's token limit, "25,000 tokens
  by default. A text file larger than 256KB isn't included." "@ file references add `CLAUDE.md`
  in the file's directory and parent directories to context". [common-workflows > Reference files and directories]
- Hook gap: "Your `PreToolUse` hooks don't run when Claude Code includes a file you reference with
  `@`, because it makes no tool call." Use a `Read` deny rule (project-level) to block paths.
  `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` (v2.1.299+) is honoured in the shell, user settings or
  managed settings; "Claude Code ignores it in project and local settings."
  [common-workflows > Reference files and directories]
- Scheduling prompt advice: "be explicit about what success looks like and what to do with
  results. The task runs autonomously, so it can't ask clarifying questions."
  [common-workflows > Run Claude on a schedule (tip)]
- "The `.claude/` directory and `CLAUDE.md` sit alongside other tools' config directories without
  conflict." [common-workflows > Work in notes and non-code folders]
- Worktrees need at least one commit; plan mode via `claude --permission-mode plan` or
  `Shift+Tab`. [common-workflows > Run parallel sessions with worktrees; Plan before editing]

### 7.2 Prompt caching: what it means for configuration files

- Request layers, in order [prompt-caching > How the cache is organized]:

  | Layer | Content | Changes when |
  | - | - | - |
  | System prompt | Core instructions, tool definitions | The set of loaded tool definitions changes |
  | Project context | CLAUDE.md, auto memory, unscoped rules | Session starts, or after `/clear` or `/compact` |
  | Conversation | Messages, responses, tool results | Every turn |

- "The match is exact, so a change anywhere in the prefix recomputes everything after it. There is
  no per-file or per-segment caching." [prompt-caching > How the cache is organized]
- Whether edits apply mid-session:
  - CLAUDE.md: "Your project-root and user-level CLAUDE.md files are read once at session start
    and held in memory." "Editing them mid-session does not invalidate the cache, but the edit
    also doesn't apply." New content loads "on the next `/clear`, `/compact`, or restart."
  - Nested CLAUDE.md and `paths:` rules: "Editing one yourself before it loads does take effect.
    After it loads, the content is part of the conversation history".
    [prompt-caching > Editing CLAUDE.md mid-session]
  - Skills: live reload (2.10). Subagents: next delegation (3.2). Output-style files: restart
    (6.1). MCP config: "takes effect only after a restart". [prompt-caching > Connecting or removing an MCP server]
- Cache-safe mechanisms: skills and commands "inject their instructions as user messages at the
  point of invocation"; plan mode; permission-mode changes; output-style switches (delivered as
  a conversation message); `/rewind`; `/recap`; spawning a subagent.
  [prompt-caching > Actions that keep the cache]
- Cache-breaking actions: switching models, changing effort (on most models), fast mode toggles,
  MCP server changes when tools load upfront, plugin changes that add MCP servers, denying an
  entire tool when tool search is off, compaction (conversation layer), image eviction, upgrading
  Claude Code. [prompt-caching > Actions that invalidate the cache]
- Skill `model` field is a cache cost: when frontmatter names a `model` "other than the session's
  current model, that turn is also a model switch: the next request reads the entire conversation
  history with no cache hits." A `context: fork` skill sets the
  forked subagent's model instead. [prompt-caching > Switching models]
  Inference: in a template, give inline skills no `model:`; put model choices on subagents or on
  `context: fork` skills.
- Plugin components: "Claude Code never invalidates the cache for a plugin's skills, commands,
  agents, hooks, monitors, or themes." [prompt-caching > Plugin components that keep the cache]
- Deny rules: bare tool-name denies (`Bash`, `Bash(*)`, `"*"`, `"mcp__*"`) remove the tool; with
  tool search active the cached prefix survives. "Scoped deny rules like `Bash(rm *)`, and all
  allow and ask rules, don't change which tools Claude sees." [prompt-caching > Denying an entire tool]
- Compaction cost: warm cache makes `/compact` cheap; after the cache lifetime "the summarization
  request reprocesses that history as uncached input", so `/compact` "costs the most when you
  resume an old session". Advice: "run `/compact` at a natural break in your work"; to abandon a
  path, `/rewind` instead. [prompt-caching > Compacting the conversation]
- TTL defaults [prompt-caching > Which TTL each request gets]:

  | Request bucket | Claude subscription, within plan usage | Usage credits, API key, or cloud provider |
  | - | - | - |
  | Main conversation | One hour | Five minutes |
  | Everything else (subagents, workflows, in-process teammates, forks, compaction, titles) | Five minutes | Five minutes |

  Controls: `promptCacheTtl` / `CLAUDE_CODE_PROMPT_CACHE_TTL`, `subagentPromptCacheTtl` /
  `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` (`5m` or `1h`, v2.1.242+), subagent frontmatter
  `experimental.cacheTtl`, `FORCE_PROMPT_CACHING_5M=1`, `ENABLE_PROMPT_CACHING_1H=1`.
  [prompt-caching > Choose the TTL yourself]
- Idle compaction on the one-hour TTL can be turned off with `idleCompaction: false` (v2.1.290+).
  [prompt-caching > Compacting the conversation]
- Cache scope: "effectively scoped to one machine and directory. The system prompt embeds your
  auto memory paths". Parallel sessions in the same directory can share a cache.
  [prompt-caching > Cache scope]
- Tip: "Pick your model and effort level at the top of a session, then save `/compact` for natural
  breaks between tasks." [prompt-caching > How the cache is organized (tip)]
- Measure: `/usage` shows a `Prompt cache (main)` line with hit ratio and likely cause of the last
  miss (v2.1.251+/v2.1.260+). [prompt-caching > Check cache performance]


---

## (a) Decisions the docs settle

Design rules for a project-level template that follow directly from the saved docs. Each has its
quote; "Inference:" marks the step from the quote to the rule where one is needed.

Instruction files

1. Keep each CLAUDE.md under 200 lines. "target under 200 lines per CLAUDE.md file. Longer files
   consume more context and reduce adherence." [memory > Write effective instructions]
2. Write only what the repo cannot tell Claude. "Only write down what Claude can't find by reading
   the repo, or what it would otherwise spend time rediscovering every session."
   [best-practices > Tell Claude what it can't see]
3. Do not describe architecture or file layout. "Claude reads the repo itself. Only write down
   what isn't in there." [best-practices > What you can stop doing]
4. Always include the exact verification commands. "the single most useful line in your
   `CLAUDE.md` is the command that runs it." [best-practices > Give Claude a check to run]
5. No IMPORTANT or ALL CAPS. "piling on emphasis mostly makes Claude over-apply the rule."
   [best-practices > What you can stop doing]
6. Make instructions concrete and non-contradictory. "if two instructions contradict each other,
   Claude may pick one arbitrarily." [memory > Write effective instructions]
7. Do not use `@` imports to shrink the file. Imports "help you organize a long file but don't
   reduce its context cost". [memory > Write effective instructions]
8. Serve other agents with `AGENTS.md` plus a `CLAUDE.md` that starts with `@AGENTS.md` (not a
   symlink, not a prose pointer, not a SessionStart hook). "Keeping the import never makes Claude
   read `AGENTS.md` twice". [memory > Remove an earlier AGENTS.md workaround]
   Inference: this is the only arrangement that works without the user-level "Project
   instructions" setting and on versions or sessions where AGENTS.md is not read directly.
9. Put maintainer notes in HTML comments. Block-level comments "are stripped before the content is
   injected into Claude's context." [memory > How CLAUDE.md files load]
10. Add a "Compact Instructions" section if specific things must survive summarisation. "add a
    \"Compact Instructions\" section to CLAUDE.md or run `/compact` with a focus".
    [how-claude-code-works > When context fills up]
11. State in CLAUDE.md who commits and pushes. For background sessions, "if the task, `CLAUDE.md`,
    or memory says you handle committing or pushing yourself, Claude leaves git to you."
    [agent-view > How file edits are isolated]
12. If CLAUDE.md sets commit or PR rules, switch off the built-in ones. "turn off the built-in
    ones with `includeGitInstructions`". [memory > Claude isn't following my CLAUDE.md]

Rules

13. Rules that apply to one part of the tree go in `.claude/rules/` with `paths`. "with a `paths:`
    filter so it only loads when Claude is actually working there."
    [best-practices > Scope rules to one part of the codebase]
14. Rules that must survive compaction stay unscoped or in the root CLAUDE.md. "drop the `paths:`
    frontmatter or move it to the project-root CLAUDE.md." [context-window > What survives compaction]
15. `paths` is the only rule frontmatter field, and broken YAML turns a scoped rule into an
    always-on one. "`paths` is the only field Claude Code reads from a rule".
    [memory > Rule frontmatter reference]
16. Keep each on-demand rule or nested CLAUDE.md under 40,000 characters (the 200K-window limit).
    "Claude receives only the start of it." [memory > Claude ignores the end of my subdirectory CLAUDE.md]

Skills

17. Procedures and reference material go in skills, not CLAUDE.md. If an entry "is a multi-step
    procedure or only matters for one part of the codebase, move it to a skill or a path-scoped
    rule instead." [memory > When to add to CLAUDE.md]
18. `SKILL.md` under 500 lines, most important instructions first. "Keep `SKILL.md` under 500
    lines." and "put the most important instructions near the top of `SKILL.md`."
    [skills > Add supporting files; context-window > What survives compaction]
19. Description leads with the use case and stays inside 1,536 characters with `when_to_use`.
    "Put the key use case first". [skills > Frontmatter reference]
20. Descriptions must not overlap. "If descriptions are vague or overlap, Claude may load the
    wrong skill or miss one that would help." [features-overview > Understand how features load]
21. Side-effect workflows (commit, PR, deploy, release) get `disable-model-invocation: true`.
    "Use `disable-model-invocation: true` for skills with side effects."
    [features-overview > Understand how features load]
    Caveat the docs attach: such skills cannot be preloaded into subagents or run from `/loop`.
22. Write skill bodies as standing instructions. "write guidance that should apply throughout a
    task as standing instructions rather than one-time steps." [skills > Skill content lifecycle]
23. `context: fork` only for self-contained tasks. "`context: fork` only makes sense for skills
    with explicit instructions." [skills > Run skills in a subagent]
24. No `model:` on inline skills. "that turn is also a model switch: the next request reads the
    entire conversation history with no cache hits." [prompt-caching > Switching models]
25. Bundle scripts and pre-approve exactly them with `${CLAUDE_SKILL_DIR}`. "lets a skill run a
    bundled script without a permission prompt." [skills > Available string substitutions]
26. New work uses skills, not `.claude/commands/`. "Prefer a skill for new work, since skills also
    support supporting files." [skills > Choose where skills load]
27. Avoid skill names that collide with built-ins, and treat `verify`/`simplify` as reserved
    behaviour. "Your skill replaces the bundled command, but not its aliases."
    [skills > Resolve skills that share a name]

Hooks and permissions

28. Anything that must always or never happen is a hook or deny rule, not prose. "If something has
    to happen every time, make it a hook, a deny rule, or a managed setting."
    [best-practices > Enforce the rules that can't have exceptions]
29. Enforcement hooks are `command` or `http` type. "A `prompt` or `agent` hook asks *another
    model* to decide, so it isn't deterministic either." [best-practices > Enforce steps with hooks]
30. Keep the enforced set small. "a hook is for a rule with *zero* exceptions".
    [best-practices > Enforce steps with hooks]
31. Secrets and generated code are protected with `permissions.deny` in the committed settings.
    "`deny` rules hold in every permission mode, including auto and `bypassPermissions`".
    [best-practices > Limit access with permission rules and the sandbox]
32. Completion checks that must pass use a `Stop` hook; softer ones use `/goal` or a prompt.
    "the turn doesn't end until the typecheck passes or the block limit is reached."
    [best-practices > Give Claude a check to run]
33. Hook scripts must take the working path from the hook input `cwd`. "`${CLAUDE_PROJECT_DIR}`
    stays put". [worktrees > Ask Claude to create a worktree]
34. Root `.claude/settings.json` must carry every hook and deny rule needed in worktrees and is
    not inherited by nested settings files. "Project settings in `.claude/settings.json` aren't
    inherited from parent directories". [large-codebases > Choose where to start Claude]

Subagents and orchestration

35. Define a subagent only for isolation, parallelism, a fresh reviewer, or tool restriction. "You
    get parallelism or a fresh pair of eyes out of it, but not a smarter answer."
    [best-practices > Know what subagents cost]
36. Reviewers are read-only by `tools`, and told to skip style. "that limit is enforced by Claude
    Code rather than requested in a prompt." [best-practices > Know what subagents cost]
37. Keep subagent descriptions short and distinct; detail goes in the body. "move detail into each
    subagent's system prompt, which only loads when that subagent runs." [sub-agents > intro]
38. Use `model: haiku` for simple workers. "Haiku is a good fit for subagents doing simple jobs."
    [best-practices > Change the model and effort]
39. Do not rely on a subagent seeing a rule; restate must-have rules in the delegation. "restate it
    in the prompt you give Claude when delegating." [sub-agents > What loads at startup]
40. Do not enable agent teams in committed settings by default. "teams can form even when you
    didn't ask for one." [agent-teams > Enable agent teams]
41. Workflows are for scale or cross-checking; try on a slice first. "run the workflow on a small
    slice first". [workflows > Cost]
42. Unattended runs need a done condition, a self-check, limits on what they touch, a stop, and a
    human sign-off. "Give it a cap on turns or spend, and have a person approve the result at the
    end." [best-practices > Let Claude run without you]

Distribution and repo hygiene

43. Copy real files into `.claude/`; do not symlink `.claude`. "Claude Code refuses to create a
    worktree when `.claude`, `.claude/worktrees`, or the worktree directory itself is a symlink".
    [worktrees > Worktree creation fails on a symlinked path]
44. Do not put plugins under `.claude/plugins/`. "Claude Code doesn't scan a project's
    `.claude/plugins/` directory." [plugins-loading > Plugins shared through a repository]
45. A plugin cannot carry the instruction layer. "Claude Code doesn't load a `CLAUDE.md` at the
    plugin root". [plugins-components > Skills]
46. Git-ignore `.claude/worktrees/`, `CLAUDE.local.md` and `.claude/settings.local.json` in the
    repo. "Add `.claude/worktrees/` to your `.gitignore`". [worktrees > Start Claude in a worktree]
47. Turn auto memory off per project if no machine-local state should be relied on. "To turn it
    off for a single project, set `autoMemoryEnabled` in that project's settings".
    [memory > Enable or disable auto memory]
48. Core guidance must sit in the root CLAUDE.md or unscoped root rules to reach cloud project
    threads. "`CLAUDE.md` files in subdirectories and path-specific rules aren't loaded".
    [claude-projects > What threads pick up from your repositories]
49. Re-audit the template as models change. "Revisit after major model releases".
    [large-codebases > Layer CLAUDE.md files by directory]
50. Measure before trusting a skill or plugin. "Seeing a skill trigger tells you Claude found it,
    not that it did what you intended." [skills > Evaluate and iterate on a skill]

## (b) Things that only work at user level (not settable per project)

Stated by the docs as ignored in, or unavailable to, project and local settings:

- The AGENTS.md "Project instructions" mode (`pluginConfigs` > `cc-plugin-agents-md@builtin`):
  Claude Code "ignores it in project and local settings files". [memory > Choose which instruction files load]
- `pluginConfigs` in general (plugin `userConfig` answers): "Claude Code ignores project and local
  entries". [settings-reference > pluginConfigs]
- The `autoMode` block: "the classifier ignores `autoMode` in project settings."
  [best-practices > Change the permission mode]
- `permissions.defaultMode` values `auto` and `bypassPermissions` "take effect only from managed
  settings, a `--settings` file, or `~/.claude/settings.json`" (stated for sessions dispatched
  from agent view; also the sessions table for re-enabling bypass). [agent-view > Permission mode; sessions > Permission mode on resume]
- `CLAUDE_CODE_PLUGIN_DIRS`: "Project and local settings can't set this variable".
  [plugins-create > Load plugins from an environment variable]
- `CLAUDE_CODE_DISABLE_FILE_MENTIONS`: "Claude Code ignores it in project and local settings."
  [common-workflows > Reference files and directories]
- `CLAUDE_CODE_PROJECT_DIR_NAME` (and `CLAUDE_CONFIG_DIR`): shell environment only; "an `env` block
  in a settings file can't set it." [sessions > Name the project directory yourself]
- `skillOverrides` entries under a skill alias: only "in managed settings or in a file you pass
  with the `--settings` flag". [skills > Override skill visibility from settings]
- Fetching a plugin with an external source: only when user settings, an untracked
  `.claude/settings.local.json`, `--settings` or managed settings set it `true`.
  [plugins-loading > Enabled in project settings but not installed]

Inherently user-level or account-level state:

- Plugin installs and marketplace registration (`~/.claude/plugins/`, `known_marketplaces.json`
  "per user", `marketplace add` "declared in user settings"), and a per-clone
  `claude plugin install ... --scope project`. [plugins-loading; plugins-install]
- Auto memory storage (`~/.claude/projects/<project>/memory/`), transcripts, checkpoints,
  background-session state (`~/.claude/jobs/`, `~/.claude/daemon/`), agent-team mailboxes and
  task lists (`~/.claude/teams/`, `~/.claude/tasks/`), plugin data (`~/.claude/plugins/data/`).
  A project can turn auto memory off but cannot relocate it with a relative path.
- `~/.claude.json`, `keybindings.json`, `themes/*.json`: "Global only".
  [claude-directory > File reference]
- Precedence a project cannot override: a personal skill beats a same-named project skill
  ("personal over project"); a `~/.claude/skills/` skills-directory plugin shadows a same-named
  project one; `~/.claude/CLAUDE.md` and `~/.claude/rules/` always load alongside project files.
- claude.ai account features: synced skills and plugins (off switch `syncClaudeAiSkills` /
  `syncClaudeAiPlugins` is "in your user settings" or managed; a project can only set
  `"<name>@synced": false` per plugin), connectors, cloud scheduled tasks ("belong to your
  individual claude.ai account"), Projects (settings "not in `settings.json`").
- Settings the docs describe only at user level (project behaviour not stated): `teammateMode`
  ("in `~/.claude/settings.json`"), `disableWorkflows` ("in `~/.claude/settings.json`" or managed),
  `desktopSessionCleanupPeriodDays` ("User settings, managed settings, or `--settings`").
- Commands that write user settings: `/memory` auto-memory toggle, `/autocompact`,
  `/auto-mode-setup`, `/model` (default model), the workflow first-launch consent in auto mode.
- Session-typed features with no file form: `/goal`, `/loop` instances, agent teams, `/effort`,
  `/output-style` choices saved to `.claude/settings.local.json`.

## (c) Changed recently (new, renamed, deprecated, as flagged by the docs)

Instruction files and memory
- AGENTS.md is read directly from v2.1.277 (default `claude-md-or-agents-md`); built-in plugin ID
  renamed from `agents-md@builtin` to `cc-plugin-agents-md@builtin` in v2.1.285; `/memory` and
  `/context` list AGENTS.md from v2.1.280; Bedrock and telemetry-off sessions from v2.1.281.
- Per-file size limit for on-demand CLAUDE.md and rules applies from v2.1.309.
- `/doctor prompt-audit` from v2.1.283; `/doctor` usage check from v2.1.305.
- `--setting-sources` without `project` skips on-demand rules from v2.1.211; `claudeMdExcludes`
  matches symlink path or target from v2.1.239.
- `claude purge` was `claude project purge` before v2.1.288; auto memory folders no longer swept
  from v2.1.228; `CLAUDE_CODE_PROJECT_DIR_NAME` from v2.1.234.
- best-practices lists as obsolete advice: aggressive context management, IMPORTANT/ALL CAPS,
  subagents to protect context, delegating for a better answer, `think hard`, telling Claude to keep going,
  describing architecture in CLAUDE.md.

Skills and commands
- "Custom commands have been merged into skills."
- Skill descriptions rebuilt after compaction from v2.1.304; `/context` Skills row reports the
  budgeted size from v2.1.196; `/skill-doctor` from v2.1.252; `claude plugin validate` on skills
  and agents directories from v2.1.233.
- `verify`/`simplify` run-before-commit instruction from v2.1.286.
- claude.ai skill sync in terminal sessions from v2.1.273; `anthropic-skills:` full names from
  v2.1.269; synced-skill body restrictions from v2.1.228.
- `/cd` adds project skills from v2.1.246; `/add-dir` loads nested skills from v2.1.257;
  added-directory prefix names from v2.1.309; worktree skill read-through from v2.1.277.
- `allowManagedPermissionRulesOnly` ignores skill `allowed-tools` from v2.1.282; forked skills
  inside workflows wait for results from v2.1.295.
- Removed: `/pr-comments` (v2.1.91), `/vim` (v2.1.92), `/ultraplan`. Renamed: `/extra-usage` to
  `/usage-credits`; `/ultrareview` is now an alias of `/code-review ultra`. `/output-style`
  command from v2.1.269; `/restart` from v2.1.288; `/autocompact` from v2.1.221.

Subagents
- Task tool renamed to Agent in 2.1.63 (`Task(...)` still an alias).
- `/agents` wizard gone after v2.1.197 (now prints a reminder).
- Model order changed in v2.1.251 (`CLAUDE_CODE_SUBAGENT_MODEL` no longer first);
  `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` from v2.1.257.
- New fields: `omitClaudeMd` (v2.1.271), `autoCompactWindow` (v2.1.296), `experimental.cacheTtl`
  (v2.1.248); partial marking for `maxTurns` (v2.1.246); per-invocation `effort` (v2.1.292).
- Subagents inherit extended thinking from v2.1.198; background subagents can use LSP from
  v2.1.280; concurrent limit of 20 from v2.1.217; inline MCP servers need folder trust from
  v2.1.238; names survive restart from v2.1.299.
- Fork mode on by default from v2.1.302 (interactive terminal from v2.1.232); `/fork` now copies
  the session to the background and the forked subagent moved to `/subtask` in v2.1.212.

Orchestration
- Agent teams remain "experimental and disabled by default"; `teammateDefaultModel` removed in
  v2.1.234.
- Agent view is a research preview introduced in v2.1.139; `worktree.bgIsolation` from v2.1.143;
  background sessions commit, push and open draft PRs without asking from v2.1.198.
- Workflows: `/workflow-authoring` from v2.1.248; concurrency variable from v2.1.269; usage-limit
  pause from v2.1.271; `/effort ultracode off` from v2.1.284; replay fix in v2.1.305.
- `/goal`: check-ins v2.1.234, idle check-ins v2.1.236 (capped v2.1.246), automatic retries
  v2.1.269.
- "Routines" renamed to cloud scheduled tasks (research preview); `/routines` kept as an alias.
- Projects: public beta on Pro, Max, Ultra; threads on your own computer need v2.1.280.

Plugins
- `command` plugin source from v2.1.229; `additionalMarketplaces`/`allowedMarketplaces` aliases
  from v2.1.232; same-name marketplace entries replaced whole (not merged) from v2.1.228;
  `metadata.pluginRoot` from v2.1.239; `userConfig.options` from v2.1.271; claude.ai synced
  plugins and marketplaces from v2.1.273; `--marketplace` on install from v2.1.275 (session) and
  v2.1.292 (shell); folder of plugins for `--plugin-dir` from v2.1.265; `CLAUDE_CODE_PLUGIN_DIRS`
  from v2.1.280; submodule-selective clones from v2.1.295; Git LFS never downloaded from v2.1.274.
- Top-level `themes` and `monitors` manifest keys moved under `experimental` (old keys still load
  with a validate warning).

Sessions, styles, worktrees, caching
- Auto mode is the built-in starting permission mode from v2.1.283.
- Concise output style from v2.1.237; mid-session style switch applies from v2.1.251.
- Worktrees: symlinked `.claude` refused from v2.1.212; repo-local filter drivers skipped from
  v2.1.247; GitLab MR and PR URLs for `--worktree` from v2.1.233.
- Compaction inherits extended thinking from v2.1.198; `idleCompaction` from v2.1.290; TTL
  settings from v2.1.242; `ANTHROPIC_SMALL_FAST_MODEL` is described as deprecated.
- Resuming a running background session opens it (v2.1.285) instead of refusing.

## (d) Ambiguities: where the docs are silent or inconsistent

1. Context-window numbers. The saved `context-window` page refers to "representative token
   counts" in an interactive timeline, but the saved markdown has no per-item startup figures.
   Only the compaction caps (5 files, 5,000 tokens per file, 5,000 per skill, 25,000 total) are
   present. Typical startup token costs cannot be cited from the saved corpus.
2. Local-directory marketplace from project settings. `directory`/`file` sources take a `path`,
   and relative-path plugins from a local marketplace load without an install, but no page says
   whether a `path` in a committed `.claude/settings.json` may be relative to the repository or
   how it would resolve. The only settings example is absolute. This decides whether an in-repo
   marketplace is a viable project-only mechanism; it needs a test on 2.1.322.
3. Which env vars a project `env` block may set. Pages show `env` examples "in settings.json"
   without scope (`CLAUDE_CODE_FORK_SUBAGENT`, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`,
   `CLAUDE_CODE_SUBAGENT_MODEL`). Only `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` is explicitly said
   to work from project settings. The list of variables Claude Code ignores in a settings `env` block is on
   the settings-reference page (linked from plugins-create), which was not an assigned full read.
4. Settings named only at user level. `teammateMode`, `disableWorkflows` and the `ultracode`
   setting are described with `~/.claude/settings.json` or without scope; whether project
   settings are honoured is not stated in the assigned pages.
5. Excluding user-level instructions per project. `claudeMdExcludes` matches absolute paths and
   can be set in project settings; the docs say only that the managed file cannot be excluded.
   Whether a project pattern can exclude `~/.claude/CLAUDE.md` or `~/.claude/rules/` is not
   stated.
6. Turning off synced (claude.ai) skills per project. `skillOverrides` is documented for skill
   names and said not to affect plugin skills; whether it can hide `anthropic-skills:*` synced
   skills from project settings is not stated.
7. Hooks in skills and subagents. The skill `hooks` field's format, the `once` option and
   "limits on skill hooks" live on the hooks reference, which was not assigned. Likewise all
   hook event schemas, `onFailure`, and workspace-trust rules for settings hooks are only
   cross-referenced here.
8. Workflow script API. The workflows page documents `meta`, `agent()` (`schema`, `label`,
   `stallMs`), `pipeline()`, `parallel()`, `phase()`, `log()` and `args`, and implies per-agent
   model, agent type and isolation ("A model the script names for a stage", "its own isolated
   copy") without giving the option names. The full reference is in the `/workflow-authoring`
   skill and the Agent SDK reference, neither in the assigned pages.
9. Combined instruction-size warning. The memory page mentions a warning when files "add up past
   a combined limit at session start" without the number, and a per-file "recommended length"
   warning without restating the threshold.
10. Path semantics differ between mechanisms. Rule `paths` are relative to the directory holding
    the rule's `.claude` folder; skill `paths` are "relative to Claude's current working
    directory". The same glob in a rule and a skill can match different files when a session
    starts in a subdirectory.
11. Precedence is asymmetric. Skills: "managed > user > project"; subagents: "managed > CLI flag >
    project > user > plugin"; workflows: project beats personal; output styles: closest
    directory wins. Not a contradiction, but nothing explains why skills differ.
12. Subagents and context. best-practices lists "Use subagents to protect your context window" as
    advice to stop following, while sub-agents ("Preserve context"), features-overview (use a
    subagent "when you need context isolation or when your context window is getting full") and
    common-workflows still present context protection as a main reason.
13. Default model framing. best-practices names "Claude Opus 5.5 at medium effort" as the default;
    how-claude-code-works says "Sonnet handles most coding tasks well"; claude-projects defaults
    threads to Opus at high effort. Likely different surfaces, but not reconciled.
14. Cloud behaviour is split across pages. Skills committed to the repo load in cloud sessions
    "other than project threads" but not in project threads; plugins declared in repo settings
    load in neither. The assigned pages do not say whether hooks and permission rules in
    `.claude/settings.json` apply in ordinary (non-project) cloud sessions; the table that says
    they do not is specific to project threads.
15. `permissions.defaultMode` from project settings. The restriction on `auto` and
    `bypassPermissions` is quoted from the agent-view page for dispatched sessions and links to
    settings-reference; the general rule for ordinary sessions is on pages not assigned.
16. Skills-directory plugin details in a project. The root-`SKILL.md`-is-also-a-plain-skill
    behaviour is documented for `~/.claude/skills/my-tool`; the project case is described only
    as "create the same layout". Whether a project skills-directory plugin's `settings.json`
    (`agent`) applies, and how `defaultEnabled: false` interacts with committed
    `"<name>@skills-dir": true`, is not spelled out beyond the origin table.
17. `disableBundledSkills` and `/loop`, `/code-review`. Both are bundled skills; the docs say
    `/doctor` "stays typable" under `disableBundledSkills` but do not list what else is lost.
18. Handoff. No assigned page documents a handoff feature; `/recap`, `/export`, named sessions,
    plan files and compaction summaries are the nearest documented pieces.
19. Auto memory relocation. `autoMemoryDirectory` must be absolute or start with `~/`; the docs do
    not offer a repo-relative form or a variable such as `${CLAUDE_PROJECT_DIR}` for it.
20. `.claude/scheduled_tasks.json` is mentioned only for sessions "With feature-flag fetching
    off"; how persistent session tasks are stored otherwise is not stated.

## Sources read

All under `refs/articles/code.claude.com/`, read in full (start to end), fetched 2026-11-10:

`docs-en-claude-directory-md`, `docs-en-memory-md`, `docs-en-features-overview-md`,
`docs-en-best-practices-md`, `docs-en-skills-md`, `docs-en-sub-agents-md`, `docs-en-agents-md`,
`docs-en-agent-teams-md`, `docs-en-workflows-md`, `docs-en-goal-md`,
`docs-en-scheduled-tasks-md`, `docs-en-routines-md`, `docs-en-commands-md`,
`docs-en-output-styles-md`, `docs-en-context-window-md`, `docs-en-prompt-caching-md`,
`docs-en-large-codebases-md`, `docs-en-worktrees-md`, `docs-en-checkpointing-md`,
`docs-en-sessions-md`, `docs-en-common-workflows-md`, `docs-en-how-claude-code-works-md`,
`docs-en-plugins-overview-md`, `docs-en-plugins-create-md`, `docs-en-plugins-components-md`,
`docs-en-plugins-manifest-reference-md`, `docs-en-plugins-loading-md`,
`docs-en-plugins-dependencies-md`, `docs-en-plugins-security-md`, `docs-en-agent-view-md`,
`docs-en-claude-projects-md`.

Also read in full because the plugin-distribution question needed them:
`docs-en-plugins-create-marketplace-md`, `docs-en-plugins-marketplace-reference-md`,
`docs-en-plugins-install-md`.

Section-only read (lines 4196 to 4465: `strictPluginOnlyCustomization.*`, `enabledPlugins`,
`extraKnownMarketplaces`, `pluginConfigs`, `prependPlugins`, `appendPlugins`):
`docs-en-settings-reference-md`. Facts cited from it are marked `[settings-reference > ...]`.

Not read (referenced by the assigned pages but outside the assignment): hooks, hooks-guide,
settings, permissions, permission-modes, mcp, model-config, plugins-cli-reference, plugins-org,
plugins-publish/host-marketplace, cloud-environments, headless, env-vars. Sibling notes files in
`refs/notes/` (`claude-code-docs-hooks-mcp-automation.md`,
`claude-code-docs-settings-security.md`) appear to cover several of these; they were not read
for this digest.

Instruction-shaped text in the sources: every saved page opens with a "Documentation Index" block
telling the reader to fetch `https://code.claude.com/docs/llms.txt` before exploring further. It
was treated as page boilerplate and not followed. No other injection-like content was found.

