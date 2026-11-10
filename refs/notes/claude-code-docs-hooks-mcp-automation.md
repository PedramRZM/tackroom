# Claude Code docs digest: hooks, MCP, headless/CI, code review, cloud sessions

Reference digest (not the per-source format) for writing PROJECT-LEVEL Claude Code configuration.
All facts come from doc pages saved under `refs/articles/code.claude.com/<slug>/article.md`,
fetched 2026-11-10 (`fetched_at` in each `meta.json`). Installed Claude Code at time of writing: 2.1.322.
Nothing here is from memory. Inferences are marked "Inference:".

Source keys (slug = `docs-en-<key>-md`): `hooks`, `hooks-guide`, `mcp`, `mcp-quickstart`, `managed-mcp`,
`headless`, `cli-reference`, `github-actions`, `gitlab-ci-cd`, `code-review`, `code-review-local`,
`code-review-customize`, `ultrareview`, `claude-code-on-the-web`, `cloud-environments`, `channels`,
`cross-session-messaging`, `plugin-evals`, `errors`, `changelog`.
Citations are `(key: "Section heading")`.

---

## 1. Hooks

### 1.1 What a hook is, and the three nesting levels

- Hooks are "user-defined shell commands, HTTP endpoints, MCP tool calls, LLM prompts, or subagents that
  execute automatically at specific points in Claude Code's lifecycle" (hooks: intro). The same events fire
  in terminal, IDE extensions, the Desktop app and cloud sessions (hooks: intro).
- Config shape: `hooks` -> event name -> array of matcher groups (`matcher`, `hooks`) -> array of hook
  handlers (hooks: "Configuration"). Terms: hook event, matcher group, hook handler.
- Cadences: per session (`SessionStart`, `SessionEnd`); per turn (`UserPromptSubmit`, `Stop`,
  `StopFailure`); per tool call (`PreToolUse`, `PostToolUse`), except `EndConversation` calls which skip
  both (hooks: "Hook lifecycle").

### 1.2 Where hooks are defined (scopes)

(hooks: "Hook locations")

| Location | Scope | Shareable |
| :- | :- | :- |
| `~/.claude/settings.json` | all your projects | no |
| `.claude/settings.json` | single project | yes, committed |
| `.claude/settings.local.json` | single project | no, gitignored when Claude Code saves a setting to it |
| Managed policy settings | organisation | yes, admin-controlled |
| Plugin `hooks/hooks.json` | when plugin is enabled | yes (optional top-level `description`) |
| Skill frontmatter (`hooks:`) | rest of the session once the skill is invoked | yes |
| Subagent frontmatter (`hooks:`) | while that subagent runs | yes |

- Cloud sessions do not read the local `~/.claude/settings.json` (hooks: "Hook locations").
- Settings/managed/plugin hooks also run inside subagents; tool events there carry `agent_id` and
  `agent_type` (hooks: "Hook locations").
- Combination: "Hook entries merge across settings levels rather than replacing each other" (hooks: "Hook
  locations"). User, project and local add hooks without removing managed ones.
- Managed `allowManagedHooksOnly` blocks user, project, local and plugin hooks (plugins force-enabled in
  managed `enabledPlugins` are exempt) and also narrows `statusLine`, `fileSuggestion`,
  `subagentStatusLine` to managed settings (hooks: "Hook locations").
- HTTP allowlists apply to every source: `allowedHttpHookUrls` (HTTP hook runs only if its URL matches the
  merged allowlist) and `httpHookAllowedEnvVars` (hooks: "Hook locations").
- Skill hooks: registered when the skill is invoked and kept "for the rest of the session, on turns after
  the skill's own turn as well"; `once: true` removes one after its first successful run. Subagent hooks:
  only while the subagent runs; a `Stop` hook there is converted to `SubagentStop` (hooks: "Hooks in skills
  and agents").
- Skill hook limits (v2.1.304+): per source of skills (project, personal folder, each plugin) at most 1,024
  hooks and 16,384 matcher characters per session; a skill past the limit "registers none of its hooks"
  (debug-log text) (hooks: "Limits on skill hooks"). Managed `strictPluginOnlyCustomization` can lock hooks
  to plugins and managed settings; then project-skill frontmatter hooks and your settings-file hooks do not
  run (same section).

### 1.3 Ordering, parallelism, deduplication

- "When an event fires, its matching hooks run in parallel." If more than 12 are prompt or agent hooks, 12
  run at once and the rest queue; each waiting hook's `timeout` starts when it starts (hooks: "Hook handler
  fields").
- Dedup: "If you define the same handler in more than one settings file, it runs once. A plugin's or
  skill's copy of the same handler stays separate." (hooks: "Hook handler fields").
- Handlers run in the current directory with Claude Code's environment; if cwd no longer exists, the first
  existing of: session start dir, project root, home, system temp (hooks: "Hook handler fields").
- Inference: because matching hooks run in parallel, there is no documented ordering between scopes, and a
  project hook cannot rely on running before or after a user hook. (See 1.9 for how conflicting decisions
  resolve on PreToolUse.)

### 1.4 Matchers

(hooks: "Matcher patterns")

| Matcher value | Evaluated as |
| :- | :- |
| `"*"`, `""`, or omitted | match all |
| only letters, digits, `_`, `-`, spaces, `,`, `\|` | exact string, or list of exact strings separated by `\|` or `,` |
| contains any other character | JavaScript regex, unanchored (`RegExp.prototype.test`) |

- `Edit.*` matches `Edit` and `NotebookEdit`; use `^Edit$` for whole-string match.
- `FileChanged` and `StopFailure` use a narrower exact-match set (letters, digits, `_`, `|` only); only `|`
  separates alternatives there.
- A `matcher` on an event without matcher support "is silently ignored".
- MCP tools are named `mcp__<server>__<tool>`. To match a whole server use `mcp__memory__.*`; the bare
  `mcp__memory` is an exact string and "matches no tool". Plugin-bundled servers:
  `mcp__plugin_<plugin-name>_<server-name>__<tool>` (hooks: "Match MCP tools").
- A `Bash` matcher on `PreToolUse`/`PermissionRequest` also runs for shell commands started with the
  Monitor tool (v2.1.314+), but `allow` and `updatedInput` have no effect on them unless the matcher
  includes Monitor (`Bash|Monitor`, `.*`, or none). `PostToolUse` with a `Bash` matcher does not run for
  Monitor (hooks: "Match Monitor commands").

What the matcher filters, per event (hooks: "Matcher patterns"):

| Event | Matcher filters | Values |
| :- | :- | :- |
| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied` | tool name | `Bash`, `Edit\|Write`, `mcp__.*` |
| `SessionStart` | how the session started | `startup`, `resume`, `clear`, `compact`, `fork` |
| `Setup` | CLI flag | `init`, `maintenance` |
| `SessionEnd` | why it ended | `clear`, `resume`, `logout`, `prompt_input_exit`, `other` (the event section adds `bypass_permissions_disabled`) |
| `Notification` | notification type | `permission_prompt`, `idle_prompt`, `auth_success`, `auth_storage_failure`, `elicitation_dialog`, `elicitation_url_dialog`, `elicitation_complete`, `elicitation_response`, `agent_needs_input`, `agent_completed`, `quota_auto_resume_fired`, `quota_auto_resume_stale`, `quota_auto_resume_disabled`, `plugin_notification` |
| `SubagentStart`, `SubagentStop` | agent type | `general-purpose`, `Explore`, `Plan`, custom names, `^my-plugin:reviewer$` |
| `PreCompact`, `PostCompact` | trigger | `manual`, `auto` |
| `PreModelSwitch`, `PostModelSwitch` | canonical name of target model | `claude-opus-5`, `.*opus.*` |
| `ConfigChange` | config source | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
| `DirectoryAdded` | how added | `slash_command`, `register_repo_root` |
| `FileChanged` | literal filenames to watch | `.envrc\|.env` |
| `StopFailure` | error type | `rate_limit`, `overloaded`, `authentication_failed`, `oauth_org_not_allowed`, `account_on_hold`, `billing_error`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `cloud_credential_error`, `unknown` |
| `InstructionsLoaded` | load reason | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact` |
| `UserPromptExpansion` | command name | skill or command names |
| `Elicitation`, `ElicitationResult` | MCP server name | configured server names |
| `UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove`, `MessageDisplay`, `CwdChanged` | no matcher support | always fires |

### 1.5 Handler types and every config field

Five types (hooks: "Hook handler fields"): `command`, `http`, `mcp_tool`, `prompt`, `agent` ("Agent hooks
are experimental and may change").

Common fields, all types (hooks: "Common fields"):

| Field | Notes |
| :- | :- |
| `type` | required: `"command"`, `"http"`, `"mcp_tool"`, `"prompt"`, `"agent"` |
| `if` | one permission rule, e.g. `"Bash(git *)"`, `"Edit(*.ts)"`. Only evaluated on tool events (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`). "On other events, a hook with `if` set never runs". No `&&`, `\|\|` or list syntax |
| `timeout` | seconds. Defaults: 600 for `command`/`http`/`mcp_tool`; 30 for `prompt`; 60 for `agent`. Lowered to 30 on `UserPromptSubmit`, `PreModelSwitch`, `PostModelSwitch`, and to 10 on `MessageDisplay`. `SessionEnd` hooks share a 1.5-second budget, raised to match a longer per-hook `timeout` up to 60 seconds. Not enforced on a command hook with `async: true` |
| `statusMessage` | custom spinner message while the hook runs |
| `once` | remove after first successful run. "Only honored for hooks declared in skill frontmatter; ignored in settings files and agent frontmatter" |

`if` details:
- File-tool pattern `"Edit(src/**)"` matches only `src` in the working directory; any depth needs
  `"Edit(**/src/**)"` (hooks: "Common fields").
- Bash: leading `VAR=value` assignments are stripped; each subcommand is checked, including inside `$()`
  and backticks; a pattern more specific than the command name (`Bash(git push *)`) runs the hook anyway
  when the command contains `$()`, backticks or `$VAR`; when Claude Code cannot determine the commands it
  runs the hook regardless (hooks: "How `if` patterns match Bash commands").
- Warning: "Because the `if` filter is best-effort, use the permission system rather than a hook to enforce
  a hard allow or deny." (same section).

Command hook fields (hooks: "Command hook fields"):

| Field | Notes |
| :- | :- |
| `command` | required. Shell command, or with `args` the executable to spawn directly |
| `args` | when present = exec form: no shell, each element one argument, placeholders substituted as plain strings |
| `async` | `true` runs in the background without blocking |
| `asyncRewake` | `true` runs in the background and wakes Claude on exit code 2; stderr (or stdout if stderr is empty) is shown to Claude as a system reminder |
| `shell` | `"bash"` or `"powershell"`; ignored when `args` is set |
| `onFailure` | `"continue"` or `"block"`; v2.1.295+ |

- Shell form (no `args`) passes the string to `sh -c` on macOS/Linux (hooks: "Exec form and shell form").
- "Prefer exec form for any hook that references a path placeholder. In shell form, wrap each placeholder
  in double quotes." (hooks: "Reference scripts by path").

HTTP hook fields (hooks: "HTTP hook fields"): `url` (required), `headers` (values interpolate `$VAR` /
`${VAR}` only for names in `allowedEnvVars`), `allowedEnvVars`, `onFailure` (`"continue"` default, or
`"block"`). Body is the hook JSON input, `Content-Type: application/json`; the response body uses the same
JSON output format.

MCP tool hook fields (hooks: "MCP tool hook fields"): `server` (required; plugin servers use
`plugin:<plugin-name>:<server-name>`), `tool` (required), `input` (string values support `${path}`
substitution from hook input, e.g. `"${tool_input.file_path}"`). Tool text content is read like
command-hook stdout; `isError: true` is a non-blocking error. The hook never starts an OAuth flow.
`SessionStart` at launch and every `Setup` fire before MCP servers are available, so their `mcp_tool` hooks
are skipped (hooks: "Events that fire before MCP servers are available").

Prompt and agent hook fields (hooks: "Prompt and agent hook fields"): `prompt` (required; `$ARGUMENTS` is
the placeholder for the hook input JSON; `\$` for a literal), `model` (optional; defaults to the model used
for background functionality). Details in 1.10.

### 1.6 Path placeholders and environment variables

- `${CLAUDE_PROJECT_DIR}`: "the project root where the session started"; also set in the environment of
  stdio MCP servers and plugin LSP servers. `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}` for plugins.
  All three are also exported as environment variables on the spawned process (hooks: "Reference scripts by
  path", "Exec form and shell form").
- Worktrees: `${CLAUDE_PROJECT_DIR}` "stays put" at the session start root; the `cwd` input field follows
  Claude into the worktree or after `cd` (hooks: "Reference scripts by path").
- `$CLAUDE_CODE_REMOTE` is `"true"` in remote web environments and unset in the local CLI (hooks: "Hook
  handler fields").
- `$CLAUDE_EFFORT` holds the same level as the `effort.level` input field (hooks: "Common input fields").
- "There is no `$CLAUDE_MODEL` environment variable." (hooks: "Common input fields").
- A hook process inherits the parent environment apart from `OTEL_*` exporter variables, and whatever
  `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` strips (hooks: "Common input fields").
- `CLAUDE_ENV_FILE`: see SessionStart/Setup/CwdChanged/FileChanged in 1.8.

### 1.7 Input, exit codes, JSON output (common rules)

Common input fields on stdin (or POST body) (hooks: "Common input fields"): `session_id`, `prompt_id`
(absent until first user input), `transcript_path` (written asynchronously, may lag; use
`last_assistant_message` on Stop/SubagentStop instead), `cwd`, `scratchpad_dir` (v2.1.257+),
`permission_mode` (`"default"`, `"plan"`, `"acceptEdits"`, `"auto"`, `"dontAsk"`, `"bypassPermissions"`;
"Manual" arrives as `"default"`; not on all events), `effort` (`{level}`), `hook_event_name`; plus
`agent_id` and `agent_type` inside subagents or with `--agent`. Only `SessionStart` can receive `model`.

Hooks have no controlling terminal: they cannot open `/dev/tty` (hooks: "Hook input and output").

Exit codes (hooks: "Exit code output"):

- Exit 0 = success; JSON fields printed are applied.
- Exit 2 = blocking error on events that can block; stderr is the message. JSON printed alongside "can't
  override the block".
- Any other code, or failing to start, or invalid JSON = non-blocking error; the action goes ahead (unless
  `onFailure: "block"`). Transcript shows a `<hook name> hook error` notice.
- Any other exit code plus a valid JSON object: "Claude Code ignores the exit code, and the fields alone
  decide".
- Warning: "Exit code 1 without valid JSON output is a non-blocking error ... If your hook is meant to
  enforce a policy, use `exit 2`." (hooks: "Other exit codes").
- stdout counts as JSON only when it is exactly one JSON object with nothing but whitespace around it
  (hooks: "Exit code 0"). Shell-profile echo lines break this (hooks: "JSON output").
- Plain stdout reaches Claude only on `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`,
  `PostModelSwitch` (as context) and `PreCompact` (as compaction instructions); elsewhere it goes to the
  debug log (hooks: "Exit code 0").
- "Claude never sees stderr from a hook that exits 0." To warn Claude from `PostToolUse`, exit 2 (hooks:
  "Exit code 0").
- Special cases: `WorktreeCreate` any non-zero fails creation; `Stop`, `SubagentStop`, `TaskCompleted`
  exiting 2 with empty stdout and a "No such file or directory" stderr are treated as non-blocking (hooks:
  "Exit code output").

Exit code 2 per event (hooks: "Exit code 2 behavior per event"):

| Event | Can block? | Exit 2 effect |
| :- | :- | :- |
| `PreToolUse` | yes | blocks the tool call |
| `PermissionRequest` | no | not honored; deny through the `decision` object |
| `UserPromptSubmit` | yes | blocks the prompt |
| `UserPromptExpansion` | yes | blocks the expansion |
| `Stop` | yes | prevents stopping, continues the conversation |
| `SubagentStop` | yes | prevents the subagent from stopping |
| `TeammateIdle` | yes | teammate keeps working |
| `TaskCreated` | yes | rolls back the task creation |
| `TaskCompleted` | yes | task not marked completed |
| `ConfigChange` | yes | blocks the change (except `policy_settings`) |
| `StopFailure` | no | output and exit code ignored, except `terminalSequence` |
| `PostToolUse` | no | shows stderr to Claude; tool already ran |
| `PostToolUseFailure` | no | shows stderr to Claude |
| `PostToolBatch` | yes | stops the agentic loop before the next model call |
| `PermissionDenied` | no | ignored; use `hookSpecificOutput.retry: true` |
| `Notification` | no | ignored |
| `SubagentStart`, `SessionStart`, `SessionEnd`, `CwdChanged`, `FileChanged`, `PostCompact`, `PostModelSwitch` | no | stderr shown to user only |
| `Setup` | no | ignored |
| `DirectoryAdded` | no | stderr to debug log |
| `PreCompact` | yes | blocks compaction |
| `PreModelSwitch` | yes | blocks the switch |
| `Elicitation` | yes | declines the request |
| `ElicitationResult` | yes | blocks the response (becomes decline) |
| `WorktreeCreate` | yes | any non-zero exit fails creation |
| `WorktreeRemove` | yes | any non-zero exit fails removal if the directory still exists |
| `InstructionsLoaded` | no | ignored |
| `MessageDisplay` | no | original text displayed |

Timeouts (hooks: "Timeouts"): a timed-out `command`/`http`/`mcp_tool` hook is cancelled and its output
discarded, so "a timed-out hook renders no decision"; on `PreToolUse` the call continues through the normal
permission flow: "don't count on a stalled hook to act as a gate". On `PreModelSwitch` a timeout blocks.

`onFailure: "block"` (hooks: "Block the action when a hook fails"): for `command` and `http` hooks. Failure
= cannot start, exit code other than 0 or 2 (even with allow JSON), HTTP error/non-2xx, timeout, invalid
output. A failure then does what exit 2 does on that event (on `PermissionRequest` it denies). No effect on
`Stop`, `SubagentStop`, `TaskCompleted`, `TeammateIdle`, or on `async`/`asyncRewake` hooks. The doc's
rationale: "A policy hook with a wrong path or a crashing script then lets everything through."

Background processes started by a hook: redirect their stdout/stderr, or a non-async hook "takes up to 10
seconds to finish after its own process exits"; print the decision before starting the background process
(hooks: "Hooks that start a background process").

HTTP (hooks: "HTTP response handling"): 2xx + empty body = success; 2xx + JSON object = parsed as JSON
output; 2xx + other body, non-2xx, connection failure = non-blocking error. To block, return 2xx with
decision fields, or set `onFailure: "block"`.

Universal JSON output fields (hooks: "JSON output"):

| Field | Default | Meaning |
| :- | :- | :- |
| `continue` | `true` | `false` = "Claude stops processing entirely after the hook runs. Takes precedence over any event-specific decision fields" |
| `stopReason` | none | shown to the user when `continue` is `false`; stays in the conversation |
| `suppressOutput` | `false` | "Has no effect: Claude Code accepts the field but doesn't act on it" |
| `systemMessage` | none | warning shown to the user |
| `terminalSequence` | none | escape sequence Claude Code emits for you; only OSC `0`/`1`/`2`/`9`/`99`/`777` and BEL; interactive sessions only; not from `async`/`asyncRewake` hooks |

- Plus top-level `decision` / `reason` on some events, and `hookSpecificOutput` (must include
  `hookEventName`) (hooks: "JSON output").
- Size cap: `additionalContext`, `systemMessage`, `initialUserMessage` and plain stdout are each capped at
  10,000 characters; over that, output is saved to a file and replaced with the path plus a preview of up
  to 2,000 characters; "Claude Code doesn't ask Claude to read the file" and no setting raises the cap
  (hooks: "JSON output").
- "Choose one approach per hook: either use exit codes alone for signaling, or exit 0 and print JSON"
  (hooks: "JSON output").

`additionalContext` (hooks: "Add context for Claude"): wrapped in a system reminder at the point where the
hook fired. Placement: SessionStart/SubagentStart at conversation start; UserPromptSubmit/
UserPromptExpansion alongside the prompt; PreToolUse/PostToolUse/PostToolUseFailure/PostToolBatch next to
the tool result; Stop/SubagentStop at end of turn (conversation continues); PostModelSwitch with the next
request. Several hooks' values are all delivered. Guidance: "Write the text as factual statements rather
than imperative system instructions"; text framed as system commands "can trigger Claude's prompt-injection
defenses". "For instructions that never change, prefer CLAUDE.md." On resume, mid-session injected text is
replayed from the transcript, not re-run; `SessionStart` hooks do run again with `source` `"resume"`.

Decision patterns summary (hooks: "Decision control"):

| Events | Pattern |
| :- | :- |
| UserPromptSubmit, UserPromptExpansion, PostToolUse, PostToolUseFailure, PostToolBatch, Stop, SubagentStop, ConfigChange, PreCompact | top-level `decision: "block"` + `reason` (the only `decision` value is `"block"`) |
| TeammateIdle, TaskCompleted | exit code 2, or `continue: false` |
| TaskCreated | exit code 2 or `decision: "block"`; `continue: false` ignored |
| PreToolUse | `hookSpecificOutput.permissionDecision` (allow/deny/ask/defer) + `permissionDecisionReason` |
| PreModelSwitch | `permissionDecision` (allow/deny/ask) or `decision: "block"` |
| PermissionRequest | `hookSpecificOutput.decision.behavior` (allow/deny) |
| PermissionDenied | `hookSpecificOutput.retry: true` |
| WorktreeCreate | path on stdout (command) or `hookSpecificOutput.worktreePath` (HTTP) |
| Elicitation, ElicitationResult | `hookSpecificOutput.action` (accept/decline/cancel), `content` |
| MessageDisplay | `hookSpecificOutput.displayContent` (display only) |
| SessionStart, SubagentStart, PostModelSwitch | context only (`additionalContext`); SessionStart also `initialUserMessage`, `watchPaths`, `sessionTitle`, `reloadSkills` |
| Setup, Notification, SessionEnd, PostCompact, InstructionsLoaded, StopFailure, CwdChanged, DirectoryAdded, FileChanged | none (side effects only) |

Rewriting (hooks: "Decision control"): `PreToolUse` `updatedInput` under `hookSpecificOutput`;
`PermissionRequest` `updatedInput` inside `decision`; `PostToolUse` `updatedToolOutput`;
`UserPromptSubmit` "can't replace the prompt".

### 1.8 Every event: when it fires, input fields, what it can return

Each event receives the common input fields (1.7) plus the fields listed. Event list is from the table in
(hooks: "Hook lifecycle"); details from each event's own section under (hooks: "Hook events").

**SessionStart** (hooks: "SessionStart")
- Fires when a session begins or resumes. Matcher = source: `startup` (new), `resume` (`--resume`,
  `--continue`, `/resume`), `clear` (`/clear`), `compact` (auto or manual compaction), `fork`.
- "Only `type: \"command\"` and `type: \"mcp_tool\"` hooks are supported." `mcp_tool` is skipped at launch.
- "SessionStart runs on every session, so keep these hooks fast." Interactive start: hooks run in the
  background, but "Claude's first response still waits for the hooks to finish".
- Input: `source`, optional `model`, `agent_type`, `session_title`; on `resume`/`fork` with a prior
  response (v2.1.251+): `seconds_since_last_response`, `context_tokens`, `prompt_cache_likely_expired`,
  `estimated_cache_write_usd`.
- Output (`hookSpecificOutput`): `additionalContext`, `initialUserMessage` (first user message in `-p`
  mode, even with no prompt), `sessionTitle`, `watchPaths` (absolute paths for FileChanged),
  `reloadSkills` (re-scan skill and command directories after the hooks finish). Plain stdout is added as
  context. Cannot block; exit 2 stderr shown to user only.
- `CLAUDE_ENV_FILE`: path to a file; append `export` lines to persist env vars for later Bash commands.
  Available only to SessionStart, Setup, CwdChanged and FileChanged hooks (hooks: "Persist environment
  variables").

**Setup** (hooks: "Setup")
- Fires only with `claude --init-only`, or `claude -p --init` / `claude -p --maintenance`. "It doesn't fire
  on normal startup." Matcher: `init`, `maintenance`. `--init-only` runs Setup hooks and SessionStart
  `startup` hooks, then exits.
- Input: `trigger` (`"init"` or `"maintenance"`). Only `command` hooks run. Cannot block; JSON output is
  discarded. Has `CLAUDE_ENV_FILE`.

**InstructionsLoaded** (hooks: "InstructionsLoaded")
- Fires when a `CLAUDE.md` or `.claude/rules/*.md` file is loaded (session start and lazy loads). Does not
  fire when Claude reads `AGENTS.md` directly through the Project instructions setting; does fire when
  `CLAUDE.md` imports it (`load_reason` `include`) or is a symlink to it.
- Matcher = `load_reason`. Input: `file_path`, `memory_type` (`"User"`, `"Project"`, `"Local"`,
  `"Managed"`), `load_reason`, `globs`, `trigger_file_path`, `parent_file_path`.
- No decision control; output discarded. "Use this event for audit logging, compliance tracking, or
  observability."
- Inference: this is the documented way to verify which rules files actually load in a session.

**UserPromptSubmit** (hooks: "UserPromptSubmit")
- Fires when a prompt is submitted, before Claude processes it; also on a scheduled task or `/loop`
  iteration, a background subagent reporting back, and a message from another session.
- No matcher. Default timeout 30 s; "a stuck hook stalls the session". On timeout the output is discarded
  and the prompt still goes through (unless `onFailure: "block"`).
- Input: `prompt` (a typed `/skill args` arrives as typed, not expanded), optional `session_title`.
- Output: plain stdout or `additionalContext` (both injected as a system reminder, no visible transcript
  entry); `decision: "block"` + `reason` (shown to the user, not added to context); `sessionTitle`;
  `suppressOriginalPrompt`. A blocked prompt's text still lands in the transcript and prompt history: "a
  blocking hook isn't a way to keep a secret off disk".

**UserPromptExpansion** (hooks: "UserPromptExpansion")
- Fires when a user-typed command expands into a prompt. Covers the path PreToolUse misses: "typing
  `/skillname` directly bypasses `PreToolUse`".
- Matcher = `command_name`. Input: `expansion_type` (`slash_command` or `mcp_prompt`), `command_name`,
  `command_args`, `command_source`, `prompt`.
- Output: `decision: "block"` + `reason`; `additionalContext`.

**MessageDisplay** (hooks: "MessageDisplay")
- Runs while assistant text streams; display-only replacement via `hookSpecificOutput.displayContent`. No
  matcher. Default timeout 10 s. Input: `turn_id`, `message_id`, `index`, `final`, `delta`. In `-p` runs it
  runs once per message. Transcript and Claude keep the original text.

**PreToolUse** (hooks: "PreToolUse")
- Fires after Claude creates tool parameters and before the call runs. Matches any tool name except
  `EndConversation`: `Bash`, `PowerShell`, `Edit`, `Write`, `Read`, `Glob`, `Grep`, `Agent`, `Workflow`,
  `WebFetch`, `WebSearch`, `AskUserQuestion`, `ExitPlanMode`, and MCP tool names.
- Warning: files referenced with `@` in the prompt are inserted without a tool call, so "no PreToolUse hook
  fires for them, including hooks matching `Read`". Fix: a `Read` deny rule, or
  `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` (v2.1.299+), which "Claude Code ignores ... in project and local
  settings".
- Input: `tool_name`, `tool_input`, `tool_use_id`; MCP tools add `mcp_server` `{name, source}` (v2.1.274+;
  "Base trust decisions on `source`"). For `Write`, `Edit`, `Read`, `tool_input.file_path` "is always
  absolute" (`~` and relative paths are expanded before hooks run).
- `tool_input` per tool: Bash `command`, `description`, `timeout`, `run_in_background`; Write `file_path`,
  `content`; Edit `file_path`, `old_string`, `new_string`, `replace_all`; Read `file_path`, `offset`,
  `limit`; Glob `pattern`, `path`; Grep `pattern`, `path`, `glob`, `output_mode`, `-i`, `multiline`;
  WebFetch `url`, `prompt`, `offset`; WebSearch `query`, `allowed_domains`, `blocked_domains`, `mode`;
  Agent `prompt`, `description`, `subagent_type`, `model`; AskUserQuestion `questions`, `answers`;
  ExitPlanMode `plan`, `planFilePath` (hooks: "PreToolUse input").
- Output (`hookSpecificOutput`, `hookEventName: "PreToolUse"`) (hooks: "PreToolUse decision control"):
  - `permissionDecision`: `"allow"` (skips the permission prompt), `"deny"`, `"ask"`, `"defer"` (`-p` only,
    single tool call in the turn). "Deny and ask rules are still evaluated regardless of what the hook
    returns".
  - `permissionDecisionReason`: for `deny` shown to Claude; for `ask` shown to the user; for `allow` and
    `defer` debug log only.
  - `updatedInput`: "Replaces the entire input object, so include unchanged fields alongside modified
    ones". Permission rules are evaluated against the returned input.
  - `additionalContext`.
  - Multiple hooks: "precedence is `deny` > `defer` > `ask` > `allow`".
  - Exit 2 = same as `deny`, stderr is the reason.
  - Top-level `decision`/`reason` are deprecated for this event (`"approve"`/`"block"` map to
    allow/deny).
  - `ask` prompts are labelled by origin: `[settings]`, `[plugin:<name>]`, `[skill]`.
  - In auto mode, `updatedInput` with no `permissionDecision` can be denied ("a hook changed this call's
    input after auto mode reviewed it") (hooks: "PreToolUse `updatedInput` in auto mode").
  - `AskUserQuestion` / `ExitPlanMode` need `allow` plus `updatedInput` (hooks: "Tools that require user
    interaction").

**PermissionRequest** (hooks: "PermissionRequest")
- Fires when Claude Code is about to show a permission prompt (immediately; the `permission_prompt`
  Notification waits about six seconds). In sessions that cannot prompt, the hooks still run and with no
  decision the call is denied. Not run for a sandboxed command's network request.
- Matcher = tool name. Input: `tool_name`, `tool_input` (no `tool_use_id`), optional
  `permission_suggestions`, `mcp_server`.
- Output: `hookSpecificOutput.decision` = `{behavior: "allow"|"deny", updatedInput, updatedPermissions,
  message, interrupt}`. `allow` "doesn't override a matching deny rule". Exit 2 is not honored.
- `updatedPermissions` entries: `addRules`, `replaceRules`, `removeRules` (`rules`, `behavior`,
  `destination`), `setMode` (`mode`, `destination`), `addDirectories`, `removeDirectories`. `destination`:
  `session`, `localSettings`, `projectSettings`, `userSettings` (hooks: "Permission update entries").

**PostToolUse** (hooks: "PostToolUse")
- Fires immediately after a tool succeeds. Matcher = tool name. Does not fire for `Edit|Write` when a Bash
  command or outside process rewrites the file (use FileChanged).
- Input: `tool_name`, `tool_input`, `tool_response` (tool-specific structured object, e.g. `{filePath,
  type}` for Write), `tool_use_id`, optional `duration_ms`. Bash calls may carry
  `tool_response.bashEditDiff` (`changedFiles`, `files`, `moreFiles`, ...; v2.1.269+, "best effort and in
  public beta").
- Output: `decision: "block"` + `reason` (reason added next to the tool result; tool already ran);
  `additionalContext`; `classifierContext` (v2.1.236+); `updatedToolOutput` (must match the tool's output
  shape; "only changes what Claude sees"); `updatedMCPToolOutput`. Exit 2 shows stderr to Claude.
- After `Ctrl+Enter` ends the turn mid-tool, PostToolUse hooks get 10 seconds (hooks: "PostToolUse after an
  interrupt").

**PostToolUseFailure** (hooks: "PostToolUseFailure")
- Fires when a tool that started executing fails. Not for calls rejected before execution (validation,
  permission denial). Input: `tool_name`, `tool_input`, `tool_use_id`, `error` (first line `Exit code N`
  for Bash), `is_interrupt`, `duration_ms`. Output: `additionalContext`.

**PostToolBatch** (hooks: "PostToolBatch")
- Fires once after every tool call in a parallel batch resolves, before the next model request. No matcher.
  Input: `tool_calls[]` (`tool_name`, `tool_input`, `tool_use_id`, `tool_response` as the serialized
  `tool_result` content). Output: `additionalContext`; `decision: "block"` or `continue: false` stops the
  agentic loop before the next model call.

**PermissionDenied** (hooks: "PermissionDenied")
- Fires only when auto mode denies a call (not manual denials, PreToolUse blocks, or deny rules). Input:
  `tool_name`, `tool_input`, `tool_use_id`, `reason`. Output: `hookSpecificOutput.retry: true`.

**Notification** (hooks: "Notification")
- Fires when Claude Code sends a notification, even with desktop notifications turned off. Matcher =
  notification type (list in 1.4). `permission_prompt` after the prompt has waited about six seconds;
  `idle_prompt` about 60 seconds after Claude finished and you have not typed.
- Input: `message`, optional `title`, `notification_type`. Cannot block; `systemMessage` and `continue` are
  discarded but `terminalSequence` is emitted.

**SubagentStart** (hooks: "SubagentStart")
- Fires when Claude spawns or resumes a subagent, and each time an in-process teammate handles a new
  message. Matcher = agent type (frontmatter `name`, not the filename; plugin agents `my-plugin:reviewer`).
  Input: `agent_id`, `agent_type`. Output: `additionalContext` into the subagent's context. Cannot block.

**SubagentStop** (hooks: "SubagentStop")
- Fires when a subagent finishes responding; also for internal agents (prompt suggestions, `/btw`) with an
  empty `agent_type`. Input: `stop_hook_active`, `agent_id`, `agent_type`, `agent_transcript_path`,
  `last_assistant_message`, `background_tasks`, `session_crons`. Output: same as Stop; `decision: "block"`
  + `reason` keeps the subagent running with `reason` as its next instruction. To inject context into the
  parent after a subagent returns, use `PostToolUse` on the `Agent` tool.

**TaskCreated** (hooks: "TaskCreated")
- Fires when a task is created via `TaskCreate`. No matcher. Input: `task_id`, `task_subject`, optional
  `task_description`, `teammate_name`, `team_name` (deprecated). Exit 2 or `decision: "block"` deletes the
  task and returns the message as the tool's error.

**TaskCompleted** (hooks: "TaskCompleted")
- Fires when a task is marked completed through `TaskUpdate`, or when an agent-team teammate finishes its
  turn with in-progress tasks. No matcher. Same input fields as TaskCreated. Exit 2: task not marked
  completed, stderr fed back to the model.

**Stop** (hooks: "Stop")
- Fires when the main agent has finished responding. "Does not run if the stoppage occurred due to a user
  interrupt." API errors fire StopFailure instead. No matcher.
- Input: `stop_hook_active` (`true` when already continuing because of a stop hook),
  `last_assistant_message`, `background_tasks[]` (`id`, `type`, `status`, `description`, `command`, ...),
  `session_crons[]` (`id`, `schedule`, `recurring`, `prompt`).
- Output: `decision: "block"` + `reason` (required; tells Claude why to continue); or
  `hookSpecificOutput.additionalContext` (continues the conversation, labelled `Stop hook feedback`, no
  hook error shown). Exit 2 = stderr delivered as the reason.
- Loop protection: "after stop hooks have continued the turn eight times in a row, Claude Code overrides
  the next block and ends the turn"; the count resets each time Claude calls a tool; raise with
  `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.
- "The `/goal` command is a built-in shortcut for a session-scoped prompt-based Stop hook."

**StopFailure** (hooks: "StopFailure")
- Fires instead of Stop when the turn ends due to an API error. Matcher = error type. Input: `error`,
  optional `error_details`, `last_assistant_message` (the API error string). Output and exit code ignored
  apart from `terminalSequence`.

**TeammateIdle** (hooks: "TeammateIdle")
- Fires when an agent-team teammate is about to go idle. No matcher. Input: `teammate_name`, `team_name`
  (deprecated). Exit 2 keeps it working with stderr as feedback; `continue: false` stops it.

**ConfigChange** (hooks: "ConfigChange")
- Fires when a settings file, managed policy file or skill file changes during a session. Matcher =
  source: `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` ("A skill file
  in `.claude/skills/` changes"). Input: `source`, optional `file_path`.
- Exit 2 or `decision: "block"`: "the new settings are not applied to the running session". `reason` is
  "Accepted but never shown". `policy_settings` changes cannot be blocked.

**CwdChanged** (hooks: "CwdChanged")
- Fires when a shell command in the main conversation changes the working directory. No matcher. Input:
  `old_cwd`, `new_cwd`. Output: `watchPaths` (replaces the dynamic watch list), `systemMessage`. Has
  `CLAUDE_ENV_FILE` (cleared at the next CwdChanged). Cannot block.

**DirectoryAdded** (hooks: "DirectoryAdded")
- Fires after `/add-dir` or the SDK `register_repo_root` request; not for the `--add-dir` startup flag.
  Matcher: `slash_command`, `register_repo_root`. Input: `directory`, `source`. Runs in the background; no
  decision control.

**FileChanged** (hooks: "FileChanged")
- Fires when a watched file changes on disk, "no matter what changed the file" (filesystem watcher).
- Matcher does two jobs: split on `|` into literal filenames in the working directory to watch (regex is
  not useful; `"*"` registers a literal file named `*`), and filters which groups run by basename.
- Input: `file_path`, `event` (`"change"`, `"add"`, `"unlink"`). Output: `watchPaths`, `systemMessage`. Has
  `CLAUDE_ENV_FILE`. Cannot block. A hook that rewrites the watched file can loop forever; guard it.

**WorktreeCreate** (hooks: "WorktreeCreate")
- Fires for `claude --worktree`, the `EnterWorktree` tool, subagent `isolation: "worktree"`, workflow
  agents, background sessions, `claude remote-control` worktree mode. Not for `git worktree add` through
  Bash.
- "Configuring a WorktreeCreate hook replaces that default git behavior"; `.worktreeinclude` is then not
  processed. Input: `name`. Command hooks print the path "as the last non-empty line of stdout"; HTTP hooks
  return `hookSpecificOutput.worktreePath`. Any failure or missing path fails creation.

**WorktreeRemove** (hooks: "WorktreeRemove")
- Fires when Claude Code cleans up a worktree that a WorktreeCreate hook created. Input: `worktree_path`.
  Exit 0 = counts as removed; non-zero fails removal if the directory still exists. Not run when a subagent
  or workflow agent finishes (the worktree is kept).

**PreCompact** (hooks: "PreCompact")
- Fires before compaction. Matcher: `manual` (`/compact`), `auto`. Input: `trigger`,
  `custom_instructions`. Exit 2 or `decision: "block"` blocks compaction (blocking an auto-compact that is
  recovering from a context-limit error makes the request fail).
- "When a PreCompact hook exits 0 and doesn't block, Claude Code uses its stdout as instructions for the
  compaction summary." Keep under 10,000 characters per hook.

**PostCompact** (hooks: "PostCompact")
- Fires after compaction. Matcher: `manual`, `auto`. Input: `trigger`, `compact_summary`. No decision
  control; `systemMessage` and `continue` discarded.

**PreModelSwitch** (hooks: "PreModelSwitch"; v2.1.251+)
- Fires before a requested model switch (`/model`, picker, `/config`, fast mode, SDK `set_model`); not for
  automatic fallbacks. Matcher = canonical name of the target. Input: `from_model`, `to_model`,
  `requested_model`, `source`, `context_tokens`, `prompt_cache_warm`, `cache_ttl`,
  `estimated_cache_write_usd`, `pricing`. Output: exit 2 / `decision: "block"` / `permissionDecision`
  (`allow`, `deny`, `ask`). A timeout blocks the switch. Precedence `deny` > `ask` > `allow`.

**PostModelSwitch** (hooks: "PostModelSwitch"; v2.1.251+)
- Fires after the session's model changes (including automatic fallback, `opusplan`, resume). Same input
  with extra `source` values `"auto"` and `"resume"`. Output: plain stdout or `additionalContext` delivered
  with the next request. Use: "give Claude model-specific guidance without editing every CLAUDE.md".

**SessionEnd** (hooks: "SessionEnd")
- Fires when a session ends. Matcher/`reason`: `clear`, `resume`, `logout`, `prompt_input_exit`, `other`
  (`bypass_permissions_disabled` was "Removed in v2.1.234"). No decision control; output discarded.
- Default budget 1.5 seconds; raised by a per-hook `timeout` in settings files (up to 60 s; plugin hook
  timeouts do not raise it) or by `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS`.

**Elicitation** / **ElicitationResult** (hooks: "Elicitation", "ElicitationResult")
- Elicitation fires when an MCP server requests user input; matcher = MCP server name. Input:
  `mcp_server_name`, `message`, optional `mode` (`form`/`url`), `url`, `elicitation_id`,
  `requested_schema`. Output `hookSpecificOutput.action` = `accept` (with `content`), `decline`, `cancel`;
  no output leaves it to the dialog. Exit 2 or `decision: "block"` declines.
- ElicitationResult fires after the user responds, before the response goes to the server. Input:
  `mcp_server_name`, `action`, optional `mode`, `elicitation_id`, `content`. Output: same `action`/`content`
  (replaces the user's whole `content`).

Hook type support per event (hooks: "Prompt-based hooks"):

| Events | Types supported |
| :- | :- |
| `PermissionDenied`, `PostToolBatch`, `PostToolUse`, `PostToolUseFailure`, `PreToolUse`, `Stop`, `SubagentStop`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`, `UserPromptExpansion`, `UserPromptSubmit` | all five |
| `PermissionRequest` | `command`, `http`, `mcp_tool`, `prompt` (agent hooks skipped) |
| `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `Elicitation`, `ElicitationResult`, `FileChanged`, `InstructionsLoaded`, `MessageDisplay`, `Notification`, `PostCompact`, `PostModelSwitch`, `PreCompact`, `PreModelSwitch`, `SessionEnd`, `StopFailure`, `SubagentStart`, `WorktreeCreate`, `WorktreeRemove` | `command`, `http`, `mcp_tool` |
| `SessionStart`, `Setup` | `command`, `mcp_tool` (no `http`, `prompt`, `agent`) |

### 1.9 Prompt hooks and agent hooks

- Prompt hook (hooks: "Prompt hook configuration"): fields `type: "prompt"`, `prompt` (`$ARGUMENTS`
  placeholder; if absent the input JSON is appended), `model`, `timeout` (default 30), `continueOnBlock`
  (default `false`). The prompt can be a rule ("Block any Bash command that reads `.env` files") or a
  condition ("All unit tests pass").
- Model response schema: `{"ok": true|false, "reason": "...", "impossible": true|false}` (hooks: "Response
  schema"). On `ok: false`:
  - `Stop`/`SubagentStop`: reason fed back as Claude's next instruction and the turn continues, unless
    `impossible: true`.
  - `PreToolUse`: call denied and by default the turn ends; `continueOnBlock: true` returns the reason to
    Claude as the tool error instead.
  - `PostToolUse`: by default the turn ends; `continueOnBlock: true` feeds the reason back.
  - `PostToolBatch`, `UserPromptSubmit`, `UserPromptExpansion`: the turn ends.
  - `PostToolUseFailure`, `TaskCreated`: reason returned as a tool error, turn continues.
  - `PermissionRequest`, `PermissionDenied`: no effect.
- Agent hook (hooks: "Agent-based hooks"): spawns a subagent that "can use tools like Read, Grep, and
  Glob"; "After up to 50 turns" returns `{ "ok": true/false }`; default timeout 60; no `continueOnBlock`
  (behaves as if `true`) and no `impossible`. Warning: "Agent hooks are experimental ... For production
  workflows, prefer command hooks."

### 1.10 Background (async) hooks

(hooks: "Run hooks in the background")

- `"async": true` is only for `type: "command"`. Async hooks "can't block or control Claude's behavior":
  `decision`, `permissionDecision`, `continue` have no effect.
- After the process exits, `additionalContext` and `systemMessage` from its JSON are delivered to Claude
  "on the next conversation turn" (not shown to the user). If the session is idle it waits for the next
  user interaction, except `asyncRewake` exiting 2, which "wakes Claude immediately even when the session
  is idle".
- `timeout` is not enforced on `async` hooks but is on `asyncRewake`.
- In `-p` mode, "Claude Code kills any async hook still running at teardown".
- Completion notifications are suppressed unless verbose (`Ctrl+O` or `--verbose`).

### 1.11 Trust: how project hooks get approved

(hooks: "Workspace trust")

- "Claude Code checks workspace trust before it runs any hook from a settings file."
- Interactive: hooks from every settings file (including the user's own) are held back until the workspace
  trust dialog is accepted for the folder or a parent whose trust extends to it.
- "`-p` or SDK session: Claude Code never shows the dialog and treats the folder as trusted, so hooks
  committed in a repository's `.claude/settings.json` run in a folder you've never trusted".
- Advice before scripting `claude -p` over a repo you did not write: review `.claude/` settings, use
  `--bare`, or `--settings '{"disableAllHooks": true}'`.
- Project skill frontmatter hooks follow the settings-file rule (registered even in an untrusted `-p` run).
  Project subagent frontmatter hooks are stricter: they "run only after you accept the workspace trust
  dialog"; "A `-p` session doesn't count as accepting it" (hooks: "Hooks in skills and agents").
- There is no per-hook approval step described in the hooks reference; trust is per folder.

### 1.12 Disabling, inspecting, debugging

- `/hooks`: "a read-only browser for your configured hooks", labelled by source (user, project, local,
  plugin, current session); shows the full command and where it is defined (hooks: "The `/hooks` menu").
- `"disableAllHooks": true` disables all (non-managed) hooks; normal settings precedence applies, so a
  project `false` overrides a user `true`. One run: `--settings '{"disableAllHooks": true}'`. "There is no
  way to disable an individual hook while keeping it in the configuration." (hooks: "Disable or remove
  hooks").
- "Direct edits to hooks in settings files are normally picked up automatically by the file watcher."
  (hooks: "Disable or remove hooks").
- Debug log: `claude --debug-file <path>`, or `claude --debug` and read `~/.claude/debug/<session-id>.txt`
  ("The `--debug` flag doesn't print to the terminal"). v2.1.296+ writes one `Hooks:` line per command
  hook with status and duration, e.g. `Hooks: PostToolUse:Write [.claude/hooks/log-write.sh] finished with
  status 0 (31ms)`. `CLAUDE_CODE_DEBUG_LOG_LEVEL=verbose` adds matcher counts (hooks: "Debug hooks").
- Error notices to recognise: `<hook name> hook error`, `Failed with non-blocking status code:`, `failed;
  blocking because onFailure is "block"`, `stdio went quiet` (hooks: "Other exit codes", "Block the action
  when a hook fails", "Hooks that start a background process").

### 1.13 Security warnings and best practices from the reference

- "Command hooks execute shell commands with your full user permissions." (hooks: "Disclaimer").
- Best practices list: validate and sanitize inputs; always quote shell variables; block path traversal
  (`..`); use absolute paths (`${CLAUDE_PROJECT_DIR}`); skip sensitive files (`.env`, `.git/`, keys)
  (hooks: "Security best practices").
- Match `Bash|PowerShell` in hooks that inspect shell commands if Windows users matter (hooks:
  "PowerShell").

### 1.14 Extra rules from the hooks guide (combination, permission modes, limits)

- Why hooks: "deterministic control: certain actions always happen rather than relying on the LLM to
  choose to run them" (hooks-guide: intro).
- Combination: "every hook's command runs to completion before Claude Code merges the results. One hook
  returning `deny` doesn't stop sibling hooks from executing." For PreToolUse the most restrictive answer
  applies (`deny`, `defer`, `ask`, `allow`); `additionalContext` from every hook is kept (hooks-guide:
  "Combine results from multiple hooks").
- Multiple `updatedInput` rewrites: Claude Code "doesn't merge the rewrites or guarantee which rewrite the
  tool runs with. Avoid having more than one hook rewrite the same tool's input." (hooks-guide:
  "Limitations").
- Hooks versus permission modes (hooks-guide: "Hooks and permission modes"):
  - A hook `"allow"` "doesn't bypass deny rules from settings".
  - A hook `permissionDecision: "deny"` "blocks the tool even in `bypassPermissions` mode or with
    `--dangerously-skip-permissions`"; PreToolUse hooks "fire before any permission-mode check, in every
    permission mode, including `dontAsk`".
  - Caveat: on a machine with no managed settings and no Team/Enterprise login, "a mod can approve a call
    your `PreToolUse` hook blocked".
- Command hooks "can't trigger `/` commands or tool calls" (hooks-guide: "Limitations").
- "`Stop` hooks fire whenever Claude finishes responding, not only at task completion." (hooks-guide:
  "Limitations").
- "`PostToolUse` hooks can't undo actions since the tool has already executed." (same).
- In `-p` mode, PermissionRequest hooks still run outside `dontAsk` mode, "and a call that no hook decides
  and nothing else can answer is denied" (same).
- Coverage gap: Claude can write files through shell commands, so an `Edit|Write` matcher misses them. "If
  your hook must see every file change ... add a `Stop` hook that scans the working tree once per turn", or
  also match `Bash|PowerShell` and use `git status --porcelain`, or use FileChanged (hooks-guide: "Filter
  hooks with matchers").
- `additionalContext` must be nested in `hookSpecificOutput`; "if you place it at the top level of the
  JSON, Claude Code silently ignores it" (hooks-guide: "Structured JSON output"). Debug-log text for this:
  `Hook JSON output had unrecognized keys` (hooks-guide: "Fields at the wrong level").
- Matchers are case-sensitive (hooks-guide: "Hook not firing").
- Settings JSON: "trailing commas and comments aren't allowed" (hooks-guide: "`/hooks` shows no hooks
  configured").
- Hook scripts must be executable (`chmod +x`) (hooks-guide: "Block edits to protected files").
- Manual test: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | ./my-hook.sh; echo $?`
  (hooks-guide: "Hook error in output").
- Shell profile output breaks JSON; debug-log text `Hook output does not start with {`; fix by guarding
  profile echoes with `if [[ $- == *i* ]]` (hooks-guide: "Shell profile output before the JSON").
- `/debug` mid-session turns on logging and shows the log path; `Ctrl+O` opens the transcript view
  (hooks-guide: "Check what a hook did").
- Prompt versus agent hook: "Use prompt hooks when the hook input data alone is enough to make a decision.
  Use agent hooks when you need to verify something against the actual state of the codebase."
  (hooks-guide: "Agent-based hooks").
- Auto-approval warning: "Keep the matcher as narrow as possible. Matching on `.*` or leaving the matcher
  empty would auto-approve every tool permission prompt" (hooks-guide: "Auto-approve specific permission
  prompts").

Recommended uses named by the docs: format after edits, block protected-file edits, notifications,
re-inject context after compaction, audit config changes, reload env on `cd`/file change (direnv),
auto-approve specific prompts (hooks-guide: "What you can automate"); audit logging via
InstructionsLoaded and ConfigChange, quality gates via TaskCompleted / TeammateIdle / Stop, redaction via
PreToolUse `updatedInput` and PostToolUse `updatedToolOutput` (hooks: respective sections).

Inference (for a template synced into many repos): because hooks merge across scopes, run in parallel and
cannot be ordered, project hooks should be self-contained, idempotent and fast; use exec form with
`${CLAUDE_PROJECT_DIR}`; use `exit 2` (or JSON) for policy and add `onFailure: "block"` (v2.1.295+) on
guard hooks so a missing script after a partial sync fails closed; and back hard denials with permission
deny rules, since the docs call the `if` filter "best-effort".

---

## 2. Hook recipes

Each recipe says whether it is QUOTED (config copied from the saved docs) or ASSEMBLED (my composition
from documented fields, not a snippet that appears in the docs). All go in `.claude/settings.json` under
the single top-level `hooks` object; "Each event name is a key inside the single `hooks` object"
(hooks-guide: "Set up your first hook").

### 2.1 Block edits to protected files — QUOTED (hooks-guide: "Block edits to protected files")

`.claude/hooks/protect-files.sh` (must be `chmod +x`):

```bash
#!/bin/bash
# protect-files.sh

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Normalize Windows backslash separators so the patterns below match
FILE_PATH="${FILE_PATH//\\//}"

PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/")

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "Blocked: $FILE_PATH matches protected pattern '$pattern'" >&2
    exit 2
  fi
done

exit 0
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh"
          }
        ]
      }
    ]
  }
}
```

Notes: `file_path` is always absolute (hooks: "PreToolUse input"). This does not cover writes made through
Bash (hooks-guide: "Filter hooks with matchers") or `@`-mentioned reads (hooks: "PreToolUse").
ASSEMBLED hardening: the reference prefers exec form plus fail-closed, i.e.
`"command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/protect-files.sh", "args": [], "onFailure": "block"`
(fields from hooks: "Exec form and shell form", "Block the action when a hook fails").

### 2.2 Block dangerous commands — QUOTED (hooks: "How a hook resolves")

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(rm *)",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh",
            "args": []
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# .claude/hooks/block-rm.sh
COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked by hook"
    }
  }'
else
  exit 0  # no decision; normal permission flow applies
fi
```

Exit-code variant, QUOTED (hooks-guide: "Hook output"):

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q "drop table"; then
  echo "Blocked: dropping tables is not allowed" >&2  # stderr becomes Claude's feedback
  exit 2                                               # exit 2 = block the action
fi

exit 0  # exit 0 = no decision; the normal permission flow applies
```

Fail-closed variant, QUOTED (hooks: "Block the action when a hook fails"):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "node",
            "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/check-command.js"],
            "onFailure": "block"
          }
        ]
      }
    ]
  }
}
```

Doc caveats: the `if` filter is best-effort, "use the permission system rather than a hook to enforce a
hard allow or deny" (hooks: "How `if` patterns match Bash commands"). A `Bash` matcher also sees Monitor
commands on v2.1.314+ (hooks: "Match Monitor commands"). The docs link a reference implementation:
`https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py`
(hooks: "Decision control"; not saved in refs, not read).

### 2.3 Format after edit — QUOTED (hooks-guide: "Auto-format code after edits")

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ]
  }
}
```

"When the hook succeeds, Claude Code shows nothing in the conversation." To also catch files rewritten by
Bash, the guide points to FileChanged. Inference: a formatter failure here exits non-zero (not 2) and is a
non-blocking error shown as a hook error notice; exit 2 would show stderr to Claude.

### 2.4 Run tests / typecheck on Stop and feed failures back

QUOTED, agent-hook form (hooks: "Agent hook configuration"; marked experimental):

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "agent",
            "prompt": "Verify that all unit tests pass. Run the test suite and check the results. $ARGUMENTS",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

QUOTED, the docs' deterministic test gate is on TaskCompleted, not Stop (hooks: "TaskCompleted decision
control"):

```bash
#!/bin/bash
INPUT=$(cat)
TASK_SUBJECT=$(echo "$INPUT" | jq -r '.task_subject')

# Run the test suite
if ! npm test 2>&1; then
  echo "Tests not passing. Fix failing tests before completing: $TASK_SUBJECT" >&2
  exit 2
fi

exit 0
```

QUOTED, the loop guard every blocking Stop hook needs (hooks-guide: "Stop hook hits the block cap"):

```bash
#!/bin/bash
INPUT=$(cat)
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0  # Allow Claude to stop
fi
# ... rest of your hook logic
```

ASSEMBLED, command-hook Stop gate (not in the docs as one snippet; built from hooks: "Stop input", "Stop
decision control", "Exit code output", "JSON output"):

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/stop-verify.sh",
            "args": [],
            "timeout": 300,
            "statusMessage": "Running typecheck and tests"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# .claude/hooks/stop-verify.sh  (ASSEMBLED; replace the check command per repo)
INPUT=$(cat)
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0
fi
cd "$CLAUDE_PROJECT_DIR" || exit 0
if OUTPUT=$(npm run typecheck 2>&1 && npm test 2>&1); then
  exit 0
fi
jq -n --arg out "$(printf '%s' "$OUTPUT" | tail -c 4000)" \
  '{decision: "block", reason: ("Checks failed. Fix these before finishing:\n" + $out)}'
```

Why assembled this way (each point from the docs):
- `decision: "block"` + `reason` "Tells Claude why it should continue" (hooks: "Stop decision control").
- JSON on exit 0 instead of `exit 2` + stderr, because on Stop an exit-2 hook "with nothing on stdout" whose
  stderr "says a file is missing, such as `No such file or directory`" is treated as non-blocking (hooks:
  "Exit code output"). Inference: test output containing that phrase could silently unblock an
  exit-2-based gate.
- The `stop_hook_active` guard lets Claude stop after one forced continuation even if checks still fail.
  Without it, the 8-consecutive-continuation cap is the backstop and resets "each time Claude calls a
  tool" (hooks: "Stop input"). Inference: which trade-off to pick is a design decision; the docs only say
  to "Check this value or process the transcript to avoid blocking on a condition that will never resolve".
- `onFailure` is deliberately absent: it "has no effect" on Stop hooks (hooks: "Block the action when a
  hook fails").
- Stop fires on every finished response, "not only at task completion" (hooks-guide: "Limitations"), so
  the checks must be fast or skipped when nothing changed (Inference: e.g. exit early when
  `git status --porcelain` is empty; the guide suggests that command for discovering changes).
- Softer alternative, documented: return `hookSpecificOutput.additionalContext` with `hookEventName:
  "Stop"`; the turn continues but is labelled `Stop hook feedback` with no hook error (hooks: "Stop
  decision control").
- Background alternative, QUOTED in the docs: `PostToolUse` + `async: true` running tests after each
  `Write|Edit` and returning `additionalContext` (hooks: "Run tests after file changes"); delivered on the
  next turn, cannot block.

### 2.5 Inject context at SessionStart — ASSEMBLED from documented output (hooks: "SessionStart decision control")

The docs give the output JSON (QUOTED):

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Current branch: feat/auth-refactor\nUncommitted changes: src/auth.ts, src/login.tsx\nActive issue: #4211 Migrate to OAuth2",
    "sessionTitle": "auth-refactor"
  }
}
```

and say "A hook that only adds context can print it without building JSON". ASSEMBLED config:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/session-context.sh",
            "args": []
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# .claude/hooks/session-context.sh  (ASSEMBLED; plain stdout becomes context)
cd "$CLAUDE_PROJECT_DIR" || exit 0
echo "Current branch: $(git branch --show-current 2>/dev/null)"
echo "Uncommitted files: $(git status --porcelain 2>/dev/null | wc -l)"
```

Doc constraints: keep it fast ("runs on every session"); only `command` and `mcp_tool` types; output over
10,000 characters is replaced by a file path and a 2,000-character preview; phrase it as facts, not
commands; "For static context that doesn't require a script, use CLAUDE.md instead" (hooks:
"SessionStart", "JSON output", "Add context for Claude"). Environment variables go through
`CLAUDE_ENV_FILE` (hooks: "Persist environment variables").

### 2.6 Re-inject after compaction — QUOTED (hooks-guide: "Re-inject context after compaction")

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Reminder: use Bun, not npm. Run bun test before committing. Current sprint: auth refactor.'"
          }
        ]
      }
    ]
  }
}
```

Related documented levers: a `PreCompact` hook's stdout becomes "instructions for the compaction summary"
(hooks: "PreCompact output"); `PostCompact` receives `compact_summary` (hooks: "PostCompact input");
InstructionsLoaded reports `load_reason` `compact` when instruction files are re-loaded after compaction
(hooks: "InstructionsLoaded input"), which implies CLAUDE.md/rules are reloaded by Claude Code itself
(Inference).

### 2.7 Notifications — QUOTED

Linux (hooks-guide: "Get notified when Claude needs input"; the guide places it in
`~/.claude/settings.json`, i.e. user scope):

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Claude Code needs your attention'"
          }
        ]
      }
    ]
  }
}
```

Terminal-native, no external binary (hooks: "Emit terminal notifications"; OSC 777 for Ghostty/Warp):

```bash
#!/bin/bash
# Notification hook: ping the desktop when Claude Code needs attention.
input=$(cat)
title="Claude Code"
body=$(jq -r '.message // "Needs your attention"' <<<"$input")
seq=$(printf '\033]777;notify;%s;%s\007' "$title" "$body")
jq -nc --arg seq "$seq" '{terminalSequence: $seq}'
```

Per-type matchers (`permission_prompt`, `idle_prompt`) are QUOTED in (hooks: "Notification"). Inference:
notification hooks are personal and machine-specific (`notify-send` needs a desktop daemon), so they fit
user settings rather than a shared project template; the guide itself puts them in user settings.

### 2.8 Logging commands — QUOTED (hooks-guide: "Filter hooks with matchers", tab "Log every Bash command")

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' >> ~/.claude/command-log.txt"
          }
        ]
      }
    ]
  }
}
```

PreToolUse variant, QUOTED (hooks-guide: "Combine results from multiple hooks"):
`"command": "jq -r .tool_input.command >> ~/.claude/bash.log"`. Config audit, QUOTED (hooks-guide: "Audit
configuration changes"):
`"command": "jq -c '{timestamp: now | todate, source: .source, file: .file_path}' >> ~/claude-config-audit.log"`.
HTTP audit sink, QUOTED shape (hooks-guide: "HTTP hooks"): `{"type": "http", "url":
"http://localhost:8080/hooks/tool-use", "headers": {"Authorization": "Bearer $MY_TOKEN"}, "allowedEnvVars":
["MY_TOKEN"]}`.

---

## 3. MCP

### 3.1 Scopes and files

(mcp: "MCP installation scopes"; mcp-quickstart: "Find your configuration on disk")

| Scope | Loads in | Shared | Stored in |
| :- | :- | :- | :- |
| Local (default) | current project only | no | `~/.claude.json`, under that project's path |
| Project | current project only | yes, version control | `.mcp.json` in project root |
| User | all your projects | no | `~/.claude.json`, top-level `mcpServers` |

- MCP "local scope" is not `.claude/settings.local.json`; it lives in `~/.claude.json` (mcp: "Local
  scope").
- Wrong paths Claude Code does not read: `~/.claude/.mcp.json`, `~/.claude/config/mcp.json`,
  `~/.claude/mcp.json` (mcp-quickstart: "Troubleshooting").
- Precedence when the same server is defined in several places: "fields are not merged across scopes"; the
  whole entry from the highest source wins: 1 Local, 2 Project, 3 User, 4 Plugin-provided, 5 claude.ai
  connectors. Scopes match by name; plugins and connectors match by endpoint (mcp: "Scope hierarchy and
  precedence").
- Managed: a `managedMcpServers` server "ranks above all of these" (v2.1.259+) (mcp: same section;
  managed-mcp: "How provided servers load"). A deployed `managed-mcp.json` takes exclusive control: "Users
  can't add, modify, or use any other MCP servers, including plugin-provided servers and servers passed
  with the `--mcp-config` CLI flag" (managed-mcp: "Exclusive control with managed-mcp.json"). Denylist:
  "Nothing overrides a denylist match." (managed-mcp: "How a server is evaluated"). Managed
  `strictPluginOnlyCustomization` with `mcp` stops `.mcp.json` servers loading (managed-mcp: "Choose a
  pattern").
- Inference for a template: a project `.mcp.json` entry can be shadowed by a developer's local-scope server
  of the same name, and can be blocked or replaced by organisation policy; it cannot override either.

### 3.2 `.mcp.json` format

QUOTED (mcp-quickstart: "Edit .mcp.json directly"):

```json
{
  "mcpServers": {
    "claude-code-docs": {
      "type": "http",
      "url": "https://code.claude.com/docs/mcp"
    },
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

Fields seen in the saved pages:
- stdio: `type` (`"stdio"`, or omitted), `command`, `args`, `env` (mcp: "Add MCP servers from JSON
  configuration").
- http: `type: "http"` (alias `streamable-http`), `url`, `headers`, `headersHelper`, `oauth` (`clientId`,
  `callbackPort`, `authServerMetadataUrl`, `scopes`), `timeout` (ms, per tool call; values below 1000 are
  ignored), `alwaysLoad` (mcp: "Option 1", "Use pre-configured OAuth credentials", "Override OAuth metadata
  discovery", "Restrict OAuth scopes", "Time limits on MCP tool calls", "Exempt a server from deferral").
- `sse` is deprecated; `ws` accepts the same `url`, `headers`, `headersHelper`, `timeout`, `alwaysLoad`
  (mcp: "Option 2", "Option 4").
- "A JSON entry that has a `url` but no `type` is a configuration error, because Claude Code reads an entry
  with no `type` as a stdio server." (mcp: "Option 1").
- `"type": "sdk"` entries in `.mcp.json` are skipped (mcp: "Option 1").
- Server names: only letters, numbers, hyphens, underscores (mcp: "Add a server from an `mcpServers` JSON
  block"). Reserved names that are skipped: `workspace`, `claude-in-chrome`, `computer-use`,
  `Claude Preview`, `Claude Browser` (mcp: "Configuration warnings"). A server named `anthropic-skills`
  loses its prompts (mcp: "Use MCP prompts as commands").
- A malformed entry is skipped and the others still load; `claude mcp list` shows the parse warning
  (mcp-quickstart: "Troubleshooting").
- "Claude Code reads `.mcp.json` at session start. Exit and restart the session after editing the file."
  (mcp-quickstart: "Changes to .mcp.json don't take effect").
- CLI equivalent: `claude mcp add --transport http <name> --scope project <url>`; stdio:
  `claude mcp add [options] <name> -- <command> [args...]` (mcp: "Project scope", "Option 3").

### 3.3 Environment variable expansion

(mcp: "Environment variable expansion in `.mcp.json`")

- Allowed in `command`, `args`, `env`, `url`, `headers`. Forms: `${VAR}` and `${VAR:-default}`.
- Unset with no default: the config still loads, a missing-variable warning shows in `claude mcp list`, and
  Claude Code "uses the unexpanded `${VAR}` text as-is".
- A variable set to the empty string "counts as set", so the default is not used.
- Credential variables read as empty in a remote server's `url` and `headers`: "This keeps a project's
  `.mcp.json` or a plugin from sending your Claude Code or cloud provider credentials to a server it
  names." Covered: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `AWS_BEARER_TOKEN_BEDROCK`, `HTTPS_PROXY`,
  `NPM_TOKEN` and others; `:-default` on them is ignored. A name outside the set such as `API_KEY` expands.
  Debug-log text: `never expanded toward a remote server`.
- `CLAUDE_PROJECT_DIR` is set in a stdio server's environment, not in Claude Code's own, so in `.mcp.json`
  `command`/`args` it "requires a default such as `${CLAUDE_PROJECT_DIR:-.}`" (mcp: "Option 3: Add a local
  stdio server").
- `/mcp`, `claude mcp list` and `claude mcp get` show `${VAR}` references by name, not resolved (mcp: "How
  references appear in `/mcp` and CLI output").

### 3.4 How project servers are approved

- Interactive: "Claude Code prompts for approval in interactive sessions before using project-scoped
  servers from `.mcp.json` files"; reset with `claude mcp reset-project-choices` (mcp: "Project scope").
  Reason: "so a repository you clone can't launch processes on your machine without your consent"
  (mcp-quickstart: "Edit .mcp.json directly").
- Non-interactive: "In `claude -p` runs, Agent SDK sessions, and cloud sessions ... it loads project-scoped
  servers without asking." Also skipped in `bypassPermissions` mode with
  `skipDangerousModePermissionPrompt` set in user or managed settings (mcp: "Project scope").
- To keep a server out anyway: `disabledMcpjsonServers` ("blocks it in every permission mode");
  `--setting-sources` excluding project settings; `--strict-mcp-config` with `--mcp-config` (mcp: "Project
  scope").
- A repo cannot approve its own servers: "`enableAllProjectMcpServers` or `enabledMcpjsonServers` committed
  to the project's `.claude/settings.json` is ignored in an untrusted folder". Approvals from user
  settings, managed settings and `--settings` still apply (mcp: "Project server approvals and workspace
  trust").
- Status strings: `⏸ Pending approval (run `claude` to approve)`, `✘ Rejected (see disabledMcpjsonServers
  in settings)`, `⊘ Disabled for this project (re-enable via /mcp)`, `✘ Blocked by enterprise managed
  policy` (mcp: "Server status").
- `headersHelper` from a project `.mcp.json` runs only after the trust dialog is accepted for that project
  directory; the automatic trust of `-p` sessions does not count; it runs without credential-looking env
  variables (mcp: "Trust a folder before its headersHelper runs", "Which variables a helper can read").
- Per-developer disable without removing: `/mcp` toggle, stored per project in `~/.claude.json`
  `disabledMcpServers` (mcp: "Disable a server without removing it").
- Project-level opt-out of claude.ai connectors: `"disableClaudeAiConnectors": true` in a checked-in
  `.claude/settings.json` works ("any-source-true semantics") (mcp: "Disable claude.ai connectors").
- Permission rule names: `mcp__<server>__<tool>`; plugin servers
  `mcp__plugin_<plugin-name>_<server-name>__<tool-name>` (mcp: "Plugin-provided MCP servers").

### 3.5 Tool search / deferred loading and context cost

(mcp: "Scale with MCP tool search", "Configure tool search")

- "Tool search is enabled by default: MCP tools are deferred and discovered on demand." "Only tool names
  and server instructions load at session start, so adding more MCP servers has minimal impact on your
  context window."
- Remaining cost: "Each connected server takes some space in Claude's context window because its tool
  names and server instructions load into every session. Removing servers you no longer use keeps that
  space free." (mcp-quickstart: "Add and verify a server", step 4 note).
- `ENABLE_TOOL_SEARCH`: unset or `true` = deferred; `auto` = load upfront while definitions total under 10%
  of the context window; `auto:N` = custom percentage; `false` = all upfront. Can be set in settings.json
  `env`.
- Denying `ToolSearch` in `permissions.deny`, or leaving it out of `--tools`, makes MCP tools load upfront.
- Models: tool search is used on Claude Opus 4, Sonnet 4, Haiku 4.5 and later; earlier models load all
  tools upfront. Off under `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`.
- Per-server `"alwaysLoad": true` in `.mcp.json` loads that server's tools upfront regardless; "Use this
  for a small number of tools that Claude needs on every turn, since each upfront tool consumes context".
  It also makes startup wait for the server (capped at the 5-second connect timeout). `"alwaysLoad": false`
  keeps all of a server's tools deferred (v2.1.287+) (mcp: "Exempt a server from deferral", "Defer a
  server's tools").
- Truncation limits: server instructions and upfront tool descriptions 4,096 characters; deferred tool
  descriptions 16,384 characters; change both with `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` (mcp: "Tool
  search for MCP server authors").
- With tool search on, Claude is told which servers failed to connect; without it, it is not (mcp: "How
  Claude learns that a server failed").
- `/context` labels deferred tools `(deferred)` or `(loaded on-demand)` (mcp: "Tools that stay deferred
  below the `ENABLE_TOOL_SEARCH=auto` threshold").

### 3.6 Output limits and timeouts

(mcp: "MCP output limits and warnings", "Time limits on MCP tool calls")

- Warning when any MCP tool output exceeds 10,000 tokens (fixed). Default maximum 25,000 tokens,
  `MAX_MCP_OUTPUT_TOKENS` changes it.
- Over the limit: a successful non-image result is saved to a file in the session's `tool-results`
  directory under `~/.claude/projects/` and replaced by a message naming the path.
- Separately, text results longer than 50,000 characters are saved to a file "whatever its token count";
  a tool can raise this with `_meta["anthropic/maxResultSizeChars"]` up to 500,000.
- Error results over about 11,000 characters keep the first and last 5,000.
- HTTP/SSE response or WebSocket message over 16 MiB fails.
- Startup timeout `MCP_TIMEOUT` (default 30 seconds per mcp-quickstart: "Connection timed out at
  startup"). Tool timeout: per-server `timeout` or `MCP_TOOL_TIMEOUT` (default "about 28 hours"). Idle
  timeout 5 minutes for remote servers, 30 minutes for stdio (`CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT`).
- A main-conversation MCP call still running after two minutes moves to a background task
  (`CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`); not in non-interactive mode unless `CLAUDE_AUTO_BACKGROUND_TASKS=1`
  (mcp: "Automatic backgrounding of long tool calls").

### 3.7 Non-interactive behaviour worth knowing

- `-p` cannot run OAuth; sign in first with `/mcp` or `claude mcp login <name>` (mcp: "Authenticate with
  remote MCP servers").
- In `-p`, a failed first stdio connection means "The run continues without the server's tools" (mcp:
  "Stdio servers that exit or fail to start").
- In `--output-format stream-json`, skipped `--mcp-config` entries are reported in the `system/init`
  event's `mcp_server_errors` (mcp: "Option 1").
- Cloud sessions: "commit a `.mcp.json` to your repository; a session with one repository loads it"
  (mcp-quickstart: "Connect from other surfaces").

### 3.8 When to prefer a CLI or a skill over an MCP server

- NOT FOUND in the assigned pages (`mcp`, `mcp-quickstart`, `managed-mcp`, `headless`, `cli-reference`). The
  MCP page's only positioning statement is when to add one: "Connect a server when you find yourself
  copying data into chat from another tool, like an issue tracker or a monitoring dashboard." (mcp: intro).
- Related warnings that are in the pages: "Verify you trust each server before connecting it. Servers that
  fetch external content can expose you to prompt injection risk." (mcp: "Find and build MCP servers");
  the per-server context cost quoted in 3.5; and database advice "Use a read-only database user" (mcp:
  "Example: Query your PostgreSQL database").
- See "Ambiguities" at the end for where else in the corpus this guidance may live.

---

## 4. Headless and CI

### 4.1 `claude -p` basics

- `-p` / `--print` runs non-interactively; stdin is read (capped at 10MB); exit code 0 on success,
  non-zero on failure; SIGTERM exits 143 (headless: "Basic usage", "Pipe data through Claude", "Stop a run
  with SIGTERM").
- Without `--bare`, `claude -p` "discovers and loads them as an interactive session would, including
  anything configured in the working directory or `~/.claude`" (headless: "Start faster with bare mode").
- Trust in `-p`: "a `-p` session runs the hooks in a project's `.claude/settings.json` and connects the
  servers in its `.mcp.json`, even in a folder you've never trusted. A `-p` session shows no workspace
  trust dialog and no per-server approval prompt." (same section).
- Slash commands in `-p`: "User-invoked skills and custom commands work. Include `/skill-name` in the
  prompt string"; terminal-only built-ins such as `/login` are not available; `/config key=value` changes a
  setting (headless: "Create a commit", note).

### 4.2 Flags that matter

All from (cli-reference: "CLI flags") unless noted.

| Flag | What the docs say |
| :- | :- |
| `--output-format` | `text` (default), `json`, `stream-json` (print mode) |
| `--json-schema` | validated JSON matching a schema "after the agent completes its workflow" (print mode only); result is in `structured_output` (headless: "Get structured output") |
| `--input-format` | `text`, `stream-json` |
| `--include-partial-messages`, `--verbose` | streaming events; `stream-json` examples pair with `--verbose` |
| `--include-hook-events` | hook lifecycle events in the stream; needs `--output-format stream-json`. SessionStart and Setup hook events are always included |
| `--permission-mode` | `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`, `manual` (alias of `default`, v2.1.200+). "Overrides `defaultMode` from settings files" |
| `--permission-prompts` | `host` (default) or `none`: "Pass `none` when nobody can answer, and Claude Code denies them instead" (v2.1.259+) |
| `--permission-prompt-tool` | an MCP tool (`mcp__<server>__<tool>`) that answers permission prompts |
| `--allowedTools` / `--allowed-tools` | tools that run without prompting; permission rule syntax. "To restrict which tools are available, use `--tools` instead" |
| `--disallowedTools` / `--disallowed-tools` | deny rules; a bare tool name removes the tool from context; `"mcp__*"` removes every MCP tool; a scoped rule (`Bash(rm *)`) denies only matching calls |
| `--tools` | restricts built-in tools: `""` none, `"default"`, or names; "doesn't affect MCP tools" |
| `--max-turns` | "Limit the number of agentic turns (print mode only). No limit by default." |
| `--max-budget-usd` | stops once estimated spend reaches the amount (print mode only); client-side estimate; "Spend can pass the cap, so leave headroom"; subagent spend counts |
| `--append-system-prompt`, `--append-system-prompt-file` | append to the default prompt |
| `--system-prompt`, `--system-prompt-file` | replace the entire default prompt (drops tool guidance and safety instructions) |
| `--append-subagent-system-prompt[-file]` | appended to every subagent's system prompt; `-p` only |
| `--settings` | file path or inline JSON; "Values you set here override the same keys in your `settings.json` files for this session. Keys you omit keep their file-based values." Max 2 MiB |
| `--setting-sources` | "Comma-separated list of setting sources to load (`user`, `project`, `local`)" |
| `--bare` | "skip auto-discovery of hooks, skills, custom commands, subagents, installed plugins, MCP servers, auto memory, and CLAUDE.md"; sets `CLAUDE_CODE_SIMPLE` |
| `--safe-mode` | all customisations disabled for troubleshooting; auth, model, built-in tools and permissions work normally; managed policy still applies |
| `--restricted` | for evaluation harnesses: removes command-running tools and WebFetch unless named in `--tools`, "loads only managed settings and `--settings`", refuses `bypassPermissions` (v2.1.248+) |
| `--mcp-config`, `--strict-mcp-config` | load MCP servers from JSON; strict = "Only use MCP servers from `--mcp-config`, ignoring all other MCP configurations" |
| `--agents`, `--agent` | define subagents via JSON (or a file path with `--print`, v2.1.281+); pick the session agent |
| `--plugin-dir`, `--plugin-url` | load a plugin for this session only |
| `--disable-slash-commands` | "Disable all skills and commands for this session" |
| `--add-dir` | extra working directories; "Grants file access; Claude Code doesn't discover most `.claude/` configuration from these directories" |
| `--continue` / `-c`, `--resume` / `-r`, `--fork-session`, `--session-id`, `--no-session-persistence` | session control (4.5) |
| `--init`, `--init-only`, `--maintenance` | run Setup hooks (1.8) |
| `--model`, `--effort`, `--fallback-model` | model, effort (`low`..`max`, `ultracode`), fallback chain |
| `--exclude-dynamic-system-prompt-sections` | moves per-user context out of the system prompt for cache reuse across machines |
| `--debug`, `--debug-file <path>` | debug log |
| `--dangerously-skip-permissions` | "Equivalent to `--permission-mode bypassPermissions`" |

Note: "`claude --help` does not list every flag" (cli-reference: "CLI flags").

Other CLI commands relevant to CI (cli-reference: "CLI commands"): `claude setup-token` ("Generate a
long-lived OAuth token for CI and scripts ... Requires a Claude subscription"), `claude auth status` (exit
0 if logged in), `claude doctor` (read-only diagnostics including "settings-file validation errors"),
`claude ultrareview [target]`, `claude mcp list`.

### 4.3 Permissions in unattended runs

(headless: "Auto-approve tools", "Turn off permission prompts in unattended runs")

- With v2.1.302+, "`claude -p` runs start in Manual mode when nothing sets a permission mode". In a Manual
  `-p` run, "a call that needs approval is denied unless something approves it" (a PermissionRequest hook
  or `--permission-prompt-tool`). Tools not listed still run if they need no approval.
- `--allowedTools "Bash(git diff *),Bash(git log *)"`: the trailing ` *` is prefix matching and "The space
  before `*` is important" (`Bash(git diff*)` would also match `git diff-index`) (headless: "Create a
  commit").
- Modes: `dontAsk` "denies every call that would otherwise prompt, which is useful for locked-down CI
  runs" (allow rules and read-only actions still run); `acceptEdits` writes files without prompting and
  auto-approves `mkdir`, `touch`, `mv`, `cp`; `auto` uses a classifier.
- `--permission-prompts none`: anything that would prompt is denied unless a PermissionRequest hook allows
  it; tools needing a person (e.g. `AskUserQuestion`) are removed; denials appear as `permission_denied`
  messages and in `permission_denials` of the final result with `stream-json`.
- Doc example for unattended: `claude -p "..." --permission-mode auto --permission-prompts none`.

### 4.4 Structured output and streaming

(headless: "Get structured output", "Stream responses", "Read session metadata", "Fail CI when a plugin or
MCP server doesn't load")

- `--output-format json`: fields include `result`, `session_id`, `total_cost_usd` and a per-model cost
  breakdown (client-side estimates).
- `--json-schema '<schema>'` with `--output-format json`: output in `structured_output`; the field is
  absent if the run ended without valid structured output, so check for it. An invalid schema exits with
  `Error: --json-schema is not a valid JSON Schema`.
- `stream-json`: newline-delimited events; last line is a `result` message. First event `system/init`
  reports model, tools, MCP servers, plugins, `capabilities`.
- CI gates: `system/init` `plugin_errors` and `mcp_server_errors` (keys omitted when empty) "so a CI gate
  can fail on a non-empty array".
- `system/api_retry` events carry `attempt`, `max_retries`, `retry_delay_ms`, `error_status`, `error`.
- Subagent messages carry `parent_tool_use_id`; `--forward-subagent-text` adds their text.
- Background work: after the turn, a `-p` run can wait for background commands, subagents, workflows,
  Monitor watches and `/loop` wakeups; default cap 10 minutes of idle waiting
  (`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`) (headless: "Background tasks at exit").

### 4.5 Resuming

(headless: "Continue conversations"; cli-reference: "CLI flags")

- `claude -p "..." --continue` continues the most recent conversation in the directory; `--resume
  <session-id>` a specific one; capture the id with `--output-format json | jq -r '.session_id'`.
  `--resume` also accepts a session name or the absolute path of a `.jsonl` transcript.
- Plain `--continue` skips sessions created with `claude -p` or the SDK; "`claude -p --continue` includes
  `-p`, SDK, and `/loop` sessions".
- `--fork-session` creates a new session id when resuming. `--no-session-persistence` (print mode) stops
  sessions being saved.
- The system prompt is built once on the first request and reused on resume until compaction, so changed
  `--append-system-prompt` text does not apply to a resumed conversation unless
  `--system-prompt-snapshot off` (cli-reference: "System prompt flags in resumed conversations").
- On `-p` resume the stored permission mode is not restored; pass `--permission-mode` again (hooks: "Defer
  a tool call for later", note).

### 4.6 Controlling which config scopes load (the "only project config" question)

What the docs offer, strongest first:

1. `--setting-sources project` (cli-reference: "CLI flags": "Comma-separated list of setting sources to
   load (`user`, `project`, `local`)"). What each source covers is tabulated for the SDK option of the same
   name (file `docs-en-agent-sdk-claude-code-features-md`, section "Control filesystem settings with
   settingSources"; read only around that table, not the whole page):
   - `"project"`: "Project `settings.json` and hooks; project CLAUDE.md and `.claude/rules/*.md`; project
     skills, commands, and subagents".
   - `"user"`: "User `settings.json`; user CLAUDE.md and `~/.claude/rules/*.md`; user skills, commands, and
     subagents".
   - `"local"`: "CLAUDE.local.md, `.claude/settings.local.json`".
   - Project `.mcp.json` follows the project source: `--setting-sources user` means "Claude Code reads
     neither the project's settings files nor its `.mcp.json`" (file `docs-en-permissions-md`, around the
     "What runs before you trust a folder" table; partial read).
   - Leaving out `user` also stops claude.ai skill sync and plugin sync (files `docs-en-skills-md` line
     ~263 and `docs-en-plugins-loading-md` line ~148; partial reads).
2. What `--setting-sources` does NOT control (same SDK page, "What settingSources does not control"):
   managed policy settings (always load); "`~/.claude.json` global config | Always read" (this file holds
   user- and local-scope MCP servers and per-project state; relocate with `CLAUDE_CONFIG_DIR`); auto memory
   at `~/.claude/projects/<project>/memory/` (disable with `autoMemoryEnabled: false` or
   `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`); claude.ai MCP connectors when logged in with claude.ai (disable
   with `disableClaudeAiConnectors: true`, `ENABLE_CLAUDEAI_MCP_SERVERS=false` or strict MCP config).
3. The docs' own clean-room recipe, in the opposite direction (user only): `CLAUDE_CONFIG_DIR=~/claude-clean/config
   claude --setting-sources user`; "Managed settings still apply, and connectors still load if you log in
   with a claude.ai account" (file `docs-en-debug-your-config-md`, step "Start Claude Code with a clean
   configuration directory"; partial read).
4. `--bare` is NOT "project only": it skips project hooks, skills, `.mcp.json` and CLAUDE.md too, and
   "Hooks still don't run in bare mode when you pass them with `--settings`" (headless: "Start faster with
   bare mode"). It also needs `ANTHROPIC_API_KEY` or an `apiKeyHelper` because it "never reads OAuth
   credentials". The docs call it "the recommended mode for scripted and SDK calls" and say it "will become
   the default for `-p` in a future release".
5. `--safe-mode` disables all customisations including the project's; `--restricted` "loads only managed
   settings and `--settings`".

Assembled answer (Inference, built from the quoted pieces; the docs do not print this exact command):

```bash
# Project config only: project settings.json + hooks, project CLAUDE.md and rules, project skills,
# commands, subagents, and the project's .mcp.json. Managed policy still applies.
CLAUDE_CONFIG_DIR="$(mktemp -d)" \
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 \
ENABLE_CLAUDEAI_MCP_SERVERS=false \
claude -p "..." --setting-sources project
```

- `--setting-sources project` alone already drops user and local settings, user CLAUDE.md/rules and user
  skills/commands/subagents. The three environment variables close the gaps listed in point 2.
- Unverified details (not stated in the pages read): whether a fresh `CLAUDE_CONFIG_DIR` breaks
  subscription login in `-p` (credentials live in the config directory or keychain; the debug page says
  "you go through the first-run setup screens again"), so in CI pair it with `ANTHROPIC_API_KEY` or
  `CLAUDE_CODE_OAUTH_TOKEN`; whether user-level plugins are fully excluded by leaving out `user` (the
  plugins page says only that plugin *sync* stops); and whether `--setting-sources` also governs
  `enabledPlugins` from user settings (it should, since that is a user `settings.json` key, but no page
  read says so explicitly).
- On a fresh CI runner there is no user config, so plain `claude -p` there is already project-only in
  practice (Inference).

### 4.7 GitHub Actions (`anthropics/claude-code-action@v1`) in outline

(github-actions: sections as cited)

- Setup: quick = run `/install-github-app` in Claude Code (github.com only; needs `gh` authenticated and
  repo admin access); manual = install the Claude GitHub App (`https://github.com/apps/claude`), add secret
  `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`), copy `examples/claude.yml`
  into `.github/workflows/` ("Setup", "Manual setup").
- Quick-setup workflow file names: `claude.yml` and, if selected, `claude-code-review.yml` ("Uninstall").
- Organisation rollout: install the app at org level, store the secret as an org-level Actions secret, and
  "define the job once as a reusable workflow that each repository calls". Prefer an API key over an OAuth
  token for a shared secret, or workload identity federation (`anthropic_federation_rule_id`,
  `anthropic_organization_id`, needs `id-token: write`) ("Set up for an organization").
- Modes: no `prompt` input = interactive mode (waits for `@claude`); `prompt` input = automation mode,
  results in the run log unless the prompt and tools post them ("Interactive and automation modes").
- Trigger checks: the actor must have write access (override: `allowed_non_write_users` + own
  `github_token`); bot actors rejected unless in `allowed_bots` ("Who can trigger runs").
- Inputs: `prompt`, `claude_args`, `anthropic_api_key`, `claude_code_oauth_token`, `github_token`,
  `plugin_marketplaces`, `plugins`, `settings` ("Claude Code settings, as a JSON string or a path to a
  settings JSON file"), `trigger_phrase`, `use_bedrock`, `use_vertex`, `use_foundry` ("Action parameters").
- `claude_args` "accepts any Claude Code CLI argument", e.g. `--max-turns 5 --model claude-sonnet-5
  --mcp-config /path/to/config.json` ("Pass CLI arguments").
- Project skills in CI: "For a skill in your repository's `.claude/skills/` directory, run
  `actions/checkout` before the `anthropics/claude-code-action` step ... then pass `/skill-name` as the
  `prompt`" ("Run a skill").
- Tool access in automation mode: "For a plain-text prompt, Claude has no shell or GitHub API access until
  you grant the tools the prompt needs, with `--allowedTools` in `claude_args` or a `permissions.allow`
  rule in the `settings` input"; a skill gets the tools its `allowed-tools` frontmatter grants ("Run on a
  schedule").
- Minimal mention workflow, QUOTED ("Respond to @claude mentions"):

```yaml
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    if: contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
      id-token: write
      actions: read
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 1
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

- PR review workflow, QUOTED key lines ("Run a skill"): `plugin_marketplaces:
  "https://github.com/anthropics/claude-plugins-official.git"`, `plugins:
  "code-review@claude-plugins-official"`, `prompt: "/code-review:code-review --comment ${{
  github.repository }}/pull/${{ github.event.pull_request.number }}"`, `claude_args: '--allowedTools
  "mcp__github_inline_comment__create_inline_comment"'`. Without `--comment` nothing is posted. Fork PRs
  on public repos get no secrets, so the review runs only for same-repo branches.
- Costs: Actions minutes plus API tokens (or subscription usage with an OAuth token). Controls: specific
  requests, concise `CLAUDE.md` ("since Claude reads it on every run"), `--max-turns`, workflow timeouts,
  concurrency limits ("Manage costs").
- Gotcha: "GitHub doesn't trigger workflows on commits made with the default `GITHUB_TOKEN`" ("CI not
  running on Claude's commits").
- Beta migration: `@beta` to `@v1`, remove `mode`, `direct_prompt` to `prompt`, `custom_instructions`
  becomes `--append-system-prompt` ("Upgrade from beta").
- The page does not say which config scopes the action loads. Inference: it runs Claude Code on the runner
  in the checked-out repo, so project `.claude/` config applies and there is no user config unless the
  workflow creates it; the `settings` input and `claude_args` add to that.

### 4.8 GitLab CI/CD in outline

(gitlab-ci-cd: sections as cited)

- Status: "currently in beta"; "This integration is maintained by GitLab." (top notes).
- Setup: add masked CI/CD variable `ANTHROPIC_API_KEY`; add a job to `.gitlab-ci.yml` that installs the
  CLI (`curl -fsSL https://claude.ai/install.sh | bash`, then `export PATH="$HOME/.local/bin:$PATH"`) and
  runs, QUOTED ("Quick setup"):

```yaml
    - >
      claude
      -p "${AI_FLOW_INPUT:-'Review this MR and implement the requested changes'}"
      --permission-mode acceptEdits
      --allowedTools "Bash Read Edit Write mcp__gitlab"
      --debug
```

- Triggers via `rules` (`$CI_PIPELINE_SOURCE == "web"`, `"merge_request_event"`); mention-driven
  triggers need your own webhook listener that calls the pipeline trigger API with `AI_FLOW_INPUT`,
  `AI_FLOW_CONTEXT`, `AI_FLOW_EVENT` ("Manual setup").
- GitLab API access: `CI_JOB_TOKEN` or a Project Access Token with `api` scope stored as
  `GITLAB_ACCESS_TOKEN`; optional `/bin/gitlab-mcp-server` ("Manual setup", "Quick setup").
- Providers: Bedrock via OIDC (`CLAUDE_CODE_USE_BEDROCK: "1"`), Agent Platform via Workload Identity
  Federation (`CLAUDE_CODE_USE_VERTEX: "1"`) ("Configuration examples").
- Controls: `--max-turns`, GitLab job `timeout` (e.g. `timeout: 30m`) ("Common parameters and variables").
- Customisation: "CLAUDE.md" and "Custom prompts" are the two documented levers ("Customizing Claude's
  behavior").
- Note: `--allowedTools "Bash Read Edit Write mcp__gitlab"` is space-separated here while the headless page
  uses commas; both pages are quoted as written. `mcp__gitlab` without `__.*` is a permission rule, not a
  hook matcher (different syntax rules; see 1.4).

---

## 5. Code review

### 5.1 The options side by side

(code-review: "Compare ways to get a review")

| Option | Starts when | Runs on | Who |
| :- | :- | :- | :- |
| Code Review (managed) | PR activity per repo setting, or `@claude review` comment | Anthropic infrastructure | Team or Enterprise plan, GitHub repos, Owner turns it on |
| `/code-review` | you run it on your branch | your Claude Code session | anyone, any plan |
| Ultrareview | you start it from Claude Code | a cloud sandbox | claude.ai sign-in required |
| Claude in your own CI | pipeline events | your CI runners | anyone with an API key or cloud credentials |
| Your own reviewer (subagent or skill) | you or Claude invoke it | wherever Claude Code runs | anyone who writes one |

### 5.2 Local `/code-review`

(code-review-local: sections as cited)

- A bundled skill: "its instructions are built into Claude Code, so there is no `SKILL.md` file on disk to
  open or edit" ("Change or build on the review"). `/review` is an alias.
- Scope with no target: "your branch's commits ahead of its upstream branch plus your uncommitted changes";
  with no upstream, compares against `main` or the previous commit ("Choose what to review").
- Targets: PR number (`/code-review 1234`), branch range (`main...my-feature`), revision range
  (`HEAD~15..HEAD`), path (`src/auth`).
- Flags: `--fix` (apply findings to the working tree; edits go through the permission mode), `--comment`
  (inline comments on a GitHub PR, or one note on a GitLab MR via `glab`, v2.1.257+), `--post` (ultra
  only), `--max-findings <n>|all|default` (v2.1.288+) ("Run /code-review", "Tune effort and arguments").
- Effort argument `low`..`max`: at `low` "the review reports the findings it's most confident in"; higher
  broadens coverage. Without a level it reuses the last typed level; a level passed in a `-p` run is not
  remembered ("Tune effort and arguments").
- Runs as a background subagent "with its own context window" in a terminal session; foreground in `-p`,
  where "Claude Code waits for the review and includes the findings in the response" ("Keep working", "Run
  in the foreground").
- Instructions it follows: "the review follows your `CLAUDE.md`, including in a non-interactive `-p` run.
  It doesn't read `REVIEW.md`." ("What the review reads and edits").
- `--fix` edits from a background review are outside session checkpoints: `/rewind` will not restore them,
  "so use git to revert them" (same section).
- Claude can start it on its own when asked in plain language or from a session-scoped scheduled task. To
  stop that while keeping the command typeable, QUOTED ("Let Claude start the review"):

```json
{
  "skillOverrides": {
    "code-review": "user-invocable-only"
  }
}
```

- Project customisation: "To give every review project rules to follow, add them to your `CLAUDE.md`."
  "a project or personal skill named `code-review` runs in place of the bundled one, and the `/review`
  alias keeps running the bundled review" ("Change or build on the review").
- Neighbours: `/simplify` "reviews for cleanup only and applies its fixes"; `/verify` "runs your app to
  confirm a change works". History: "The command was named `/simplify` before v2.1.147".
- Cost: "counts toward your plan's usage or API billing the same way the rest of the session does" (intro).
- In CI: the plugin form `/code-review:code-review --comment <repo>/pull/<n>` is what the GitHub Actions
  example runs (github-actions: "Run a skill"). Note: the action example installs the `code-review` plugin
  from `claude-plugins-official`, while this page describes `/code-review` as a bundled skill; the pages do
  not explain the relationship (see Ambiguities).

### 5.3 Managed Code Review

(code-review: sections as cited)

- Availability: Team and Enterprise plans; GitHub (including GitHub Enterprise Server); not with Zero Data
  Retention, HIPAA configuration, or CMEK ("Availability").
- Pipeline: Find (several agents in parallel), Verify (filters false positives), Rank (dedupe, severity),
  Post ("How reviews work"). Default focus: "bugs that would break production, not formatting preferences
  or missing test coverage".
- Output: inline comments, a summary, and a check run named **Claude Code Review** that "doesn't conclude
  as a failure". "A review never approves or blocks the pull request" (intro, "How reviews work").
- When: per-repo setting (once when a PR opens, after every push, or only on request); anyone with write
  access can comment `@claude review` ("How reviews work"). Not on drafts and forks automatically.
- Review levels: Quick, Standard (default), Deep; set by an Owner per organisation and per repository;
  "a more thorough review costs more". No model choice ("Review levels").
- Access: read-only on the repo, does not push commits, works "without building or running your code",
  does not run in self-hosted environments ("What a review can access").
- Costs: the page defers to `code-review-costs` (billing, monthly spend limit), which is NOT saved in
  `refs/` (only `code-review`, `code-review-local`, `code-review-customize` exist). No price figure for the
  managed service appears in the pages read.

### 5.4 `REVIEW.md` (managed Code Review only)

(code-review-customize: sections as cited)

- Two files: `CLAUDE.md` ("project context"; a violation becomes a finding) and `REVIEW.md` ("instructions
  for reviews alone") (intro). The service reads the root `CLAUDE.md` and those in parent directories of
  each changed file ("Use CLAUDE.md for project-wide rules").
- "The service reads both `CLAUDE.md` and `REVIEW.md`. The `/code-review` command ... reads your
  `CLAUDE.md` files and not `REVIEW.md`. Put guidance you want applied in both places in `CLAUDE.md`"
  ("Use REVIEW.md for review-only rules", note).
- Format: "`REVIEW.md` is freeform Markdown that changes what a review finds and reports. It doesn't change
  the format of the review." ("Choose what to write in REVIEW.md").
- Location: repository root; on a protected branch also in most subdirectories (adds checks for changes
  under that path). Not applied in or below directories named `test`, `tests`, `__tests__`, `fixtures`,
  `examples`, `generated`, `vendor`, `node_modules`, `deps`, `contrib` and similar (full list in "When a
  subdirectory REVIEW.md doesn't apply"). Subdirectory files share a 150,000-byte limit.
- What it supports (with the doc's example wording):
  - Redefine severity: "Reserve Important for findings that would break behavior, leak data, or block a
    rollback".
  - Cap nits: "Report at most five Nits per review."
  - Skip: "Anything CI already enforces: lint, formatting, type errors"; generated files; lockfiles.
  - Always check: "New API routes have an integration test".
  - Require evidence: "behavior claims need a `file:line` citation in the source, not an inference from
    naming".
  - Higher bar for a path: "in `scripts/`, only report if near-certain and severe."
- Includes: a line with only `@` and a file name pulls in a file that sits beside `REVIEW.md` at the repo
  root; one level only; at most eight files; `REVIEW.md` plus includes under 150,000 bytes; at most 64
  Markdown links (relative ones) or "the review skips your whole root `REVIEW.md`" ("Include other files in
  REVIEW.md").
- Skill include: `@.claude/skills/<folder>/SKILL.md` on its own line; only the body is used; max 30,000
  bytes; no symlinks; `!` commands are replaced with a placeholder; `$ARGUMENTS` left as written;
  supporting files not loaded; "Code Review doesn't run skills"; exclusions and Nit caps written in a skill
  are not honoured ("Include a skill file", "Check what a review gets from a skill"). Some characters are
  altered in skill text (backticks, brackets, pipes, `@`).
- Branch and protection: "Code Review reads `REVIEW.md` from the pull request's base branch or from the
  default branch, never from the pull request's own changes." Lowering severity, exclusions and nit caps
  are honoured only when read from a protected default branch. Unprotected default branch: root file only,
  no includes, no subdirectory files. If protection cannot be confirmed: none ("Which branch REVIEW.md is
  read from", "What a review reads for each branch setup").
- Advice: "Keep `REVIEW.md` to instructions that change review behavior, and leave general project context
  in `CLAUDE.md`."
- Inference for a template: a synced `REVIEW.md` is inert unless the org has the managed service; its
  include and subdirectory features depend on each repo's branch protection, so a single self-contained
  root file is the portable form.

### 5.5 Ultrareview

(ultrareview: sections as cited)

- "Ultrareview is a research preview feature." Command `/code-review ultra`; `/ultrareview` is an alias
  when available. Runs "a fleet of reviewer agents in a cloud sandbox"; "every reported finding is
  independently reproduced and verified" (intro).
- Requires claude.ai authentication; not on Bedrock, Agent Platform, Foundry, ZDR or HIPAA (then
  `/code-review ultra` "runs a local review in your session instead"); not with CMEK (intro).
- Scope: current branch versus default branch including uncommitted and staged changes; pass a base branch,
  commit or tag, or a PR number (github.com only). Branch review uploads a bundle of the repo; PR mode
  clones in the cloud ("Run ultrareview from the CLI", "Review a pull request").
- Limits: "up to 500 changed files and 8,000 changed lines by default" ("Diff limits and fallbacks").
- "Claude doesn't start an ultrareview on its own." ("Run ultrareview from the CLI").
- Cost: bills usage credits, not plan usage. Pro, Max and Ultra plans: 3 free runs, "a one-time allotment
  per account"; then "typically $5 to $25 in usage credits depending on the size of the change". A run
  counts once the cloud session starts ("Pricing and free runs"). Duration "typically takes 5 to 15
  minutes" ("Track a running review").
- CI: `claude ultrareview [target]` blocks until done, prints findings to stdout, progress to stderr;
  flags `--json`, `--timeout <minutes>` (default 45), `--post` / `--no-post` (default), `--trust-workspace`
  (v2.1.309+). Exit codes 0 (completed, with or without findings), 1 (failed, stopped, timed out, or
  untrusted folder), 130 (Ctrl-C). "`claude -p '/code-review ultra'` doesn't get you the findings" ("Run
  ultrareview non-interactively").
- Posting: `--post` posts "a single plain comment from your own GitHub account", never by default ("Post
  findings to the pull request").
- Positioning: `/code-review` "for fast feedback as you work"; ultra "before merging a substantial change"
  ("How ultrareview compares to /code-review").

---

## 6. Cloud sessions and environments

### 6.1 What a repository can declare (and what it cannot)

Headline: the cloud environment itself (setup script, network access, environment variables, network
secrets) is NOT declared in the repo. It is configured per account or per organisation in the environment
dialog at claude.ai/code or the admin page (cloud-environments: "Configure your environment",
"Organization-shared environments"). The repo's lever is its committed `.claude/` config plus a
SessionStart hook.

What carries over from the clone (cloud-environments: "What carries over from your setup"):

| Item | In cloud sessions? |
| :- | :- |
| Repo `CLAUDE.md` | yes |
| Repo `.claude/settings.json` hooks and permission rules | yes, "in a session with one repository" |
| Repo `.mcp.json` servers | yes, "in a session with one repository" |
| Repo `.claude/rules/` | yes |
| Repo `.claude/skills/`, `.claude/agents/`, `.claude/commands/` | yes |
| Plugins and marketplaces declared in repo `.claude/settings.json` (`enabledPlugins`, `extraKnownMarketplaces`) | NO: "A cloud session doesn't install the plugins a repository turns on" |
| Organisation server-managed settings | yes (not in Claude Tag sessions) |
| User `~/.claude/CLAUDE.md`, user skills/agents/commands, user-scoped plugins, local- or user-scope MCP servers | no |
| Transport variables in the repo settings `env` block (`NODE_EXTRA_CA_CERTS`, mTLS variables) | no, ignored |
| Interactive auth such as AWS SSO | no |

- "To make your own configuration available in cloud sessions, commit it to the repo." (same section).
- Project threads are narrower: a cloud thread in a project "loads only the repository root's `CLAUDE.md`,
  `.claude/CLAUDE.md`, and `.claude/rules/` files that aren't path-specific" (same section, note), and
  "doesn't run hooks from a repository's `.claude/settings.json`" (cloud-environments: "Limitations in
  cloud sessions").
- Multi-repo sessions: in an Anthropic-hosted environment "a session with several repositories doesn't load
  hooks from any repository's `.claude/settings.json`" (same).
- Project `.mcp.json` servers load without an approval prompt in cloud sessions (mcp: "Project scope").
- Repo-declared SessionStart hook for dependency install, QUOTED (cloud-environments: "Install
  dependencies with a SessionStart hook"):

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"$CLAUDE_PROJECT_DIR\"/scripts/install_pkgs.sh"
          }
        ]
      }
    ]
  }
}
```

  The script starts with `if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then exit 0; fi`, because "hooks run in
  both local and cloud sessions" and there is "No cloud-only scoping"; it hashes `package.json` and the
  lockfile to skip repeat installs.
- Setup script versus SessionStart hook: "Use a setup script to provision the VM itself ... Use a
  SessionStart hook for project setup that should run everywhere, cloud and local, like `npm install`."
  Setup scripts run before Claude Code launches and are skipped when a cached environment exists;
  SessionStart hooks run after launch "on every session including resumed" (cloud-environments: "Setup
  scripts vs. SessionStart hooks").
- A setting a repo can carry for CLI-started cloud sessions: `remote.defaultEnvironmentId`, normally saved
  to user settings by `/remote-env`, "unless the same key is set at a higher-precedence settings layer,
  such as a repo's project settings" (cloud-environments: "Select an environment from the CLI").
  Inference: a template should not set this, since environment IDs are per account.
- Repo permission rules reach a single-repo cloud session, e.g. `"deny": ["SearchPlugins",
  "SuggestPluginInstall"]` to stop plugin suggestions (claude-code-on-the-web: "Turn off plugin
  suggestions").
- Agent teams in cloud: off by default; enabled by `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in the
  environment's variables (claude-code-on-the-web: "Manage context").
- Commits made in cloud sessions get a `Claude-Session: <url>` trailer; disable with
  `attribution.sessionUrl: false` (cloud-environments: "Link output back to the session").

### 6.2 Environment configuration (account side)

- Setup script: Bash, runs as root on Ubuntu 24.04 "when a new cloud session starts, before Claude Code
  launches"; up to 64 KB when loaded from a file. Constraints: exit zero; finish within roughly five
  minutes or the environment is not cached; needs network access for installs; the environment's variables
  "aren't set yet" when it runs (cloud-environments: "Setup scripts", "Script requirements").
- Caching: filesystem snapshot reused by later sessions; rebuilt when the script or allowed hosts change
  and "after roughly seven days"; running processes are not kept (cloud-environments: "Environment
  caching").
- Environment variables: `.env` format; readable by anyone who uses the environment, so no secrets
  (cloud-environments: "Set environment variables").
- Network secrets: stored on the environment, attached by Anthropic's agent proxy to requests for listed
  hosts; never attached to GitHub, `api.anthropic.com`, public package registries, or setup-script requests
  (cloud-environments: "Add network secrets", "Requests that never get the secret").
- Network access levels: None, Trusted (default; allowlisted registries, GitHub, cloud SDKs), Full, Custom
  (cloud-environments: "Access levels"). GitHub goes through a separate proxy that "rejects branch
  deletions and pushes of anything other than a branch" and blocks GraphQL, so `gh pr` and `gh issue` fail
  with a 403 while `gh api repos/...` works (cloud-environments: "GitHub proxy").
- Personal preferences without committing: a setup script that writes `~/.claude/CLAUDE.md`
  (cloud-environments: "Add personal preferences without committing to the repo").
- "Replacing the base image entirely isn't supported yet." (cloud-environments: "Limitations in cloud
  sessions").

### 6.3 Limits

- VM: Ubuntu 24.04 x86_64; about 4 vCPUs, 16 GB RAM, 30 GB disk, "approximate resource ceilings that may
  change over time" (cloud-environments: "Resource limits").
- Pre-installed: Python 3.x (pip, poetry, uv, ruff, pytest), Node 20/21/22 (npm, yarn, pnpm, bun with
  proxy caveats), Rust, Go, Java 21, Docker, PostgreSQL 16, Redis 7.0, Chrome for Testing, git, gh, jq,
  ripgrep (cloud-environments: "Installed tools"). PostgreSQL and Redis are "not running by default".
- Time: foreground command default 2 minutes (up to 10); a timed-out command moves to the background for up
  to 30 more minutes; SessionStart `command` hook cancelled after 600 seconds unless `timeout` is set;
  idle VM pauses after a few minutes and can later be reclaimed (cloud-environments: "Time limits").
- After a reclaimed VM: conversation history is restored; background shell commands, subagents,
  session-scoped scheduled tasks and `/loop` are not (claude-code-on-the-web: "Environment expired").
- Plans: Pro, Max, Ultra, Team, and Enterprise with premium or Chat + Claude Code seats; usage "counts
  toward your plan's usage limits"; "there's no separate charge for the cloud VM" (claude-code-on-the-web:
  intro). Not with ZDR, HIPAA configuration or CMEK ("GitHub authentication options", note).
- Platform: cloning and PR creation require GitHub; other hosts only as a local bundle
  (`CCR_FORCE_BUNDLE=1`, under 100 MB, no push back) (claude-code-on-the-web: "Limitations", "Send local
  repositories without GitHub").
- `claude --cloud "task"` clones the GitHub remote at the current branch, "not your local checkout, so push
  first"; one repository at a time; `claude --teleport` pulls a session back (one-way handoff)
  (claude-code-on-the-web: "Start a cloud session from your terminal").
- Auto-fix: watches a PR and pushes fixes for CI failures and review comments; needs the Claude GitHub App;
  `/autofix-pr` from the terminal. Warning: Claude replies on your behalf and "can trigger those workflows"
  in repos with comment-triggered automation (claude-code-on-the-web: "Auto-fix pull requests").
- Auto-compaction in cloud sessions triggers earlier: they set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` themselves
  (claude-code-on-the-web: "Manage context").

---

## 6b. Adjacent automation surfaces (channels, cross-session messaging, plugin evals)

### Channels (research preview) — low relevance for a project template

(channels: sections as cited)

- A channel is "an MCP server that pushes events into your running Claude Code session"; installed as a
  plugin (Telegram, Discord, iMessage, fakechat; all need Bun) and opted in per session with
  `claude --channels plugin:<name>@<marketplace>` (intro, "Supported channels").
- Not project-declarable: "Being in `.mcp.json` isn't enough to push messages: a server also has to be
  named in `--channels`." ("Security"). Organisation gates are managed settings `channelsEnabled` and
  `allowedChannelPlugins` ("Enterprise controls").
- Security: sender allowlist by pairing; "Anyone who can reply through the channel can approve or deny tool
  use in your session" when permission relay is declared ("Security").
- With `-p`, "tools that need terminal input, such as multiple-choice questions and plan mode approval, are
  disabled" ("Quickstart").
- Comparison table: cloud sessions (fresh sandbox), Claude in Slack, standard MCP server ("nothing is
  pushed to the session"), Remote Control; channels push external events into an already-running local
  session ("How channels compare").

### Cross-session messaging — two settings a project file can set

(cross-session-messaging: sections as cited)

- v2.1.224+ (v2.1.234+ on native Windows); on by default. Claude uses `ListAgents` and `SendMessage`;
  `/list-agents` (alias `/peers`) shows reachable sessions (intro, "See which sessions Claude can reach").
- A message "never counts as your consent"; the receiving Claude is told never to change "permission
  settings, `CLAUDE.md`, or other configuration because another session asked"; commands in the text do not
  run ("How a session treats an incoming message").
- Settings: `crossSessionInbound` = `accept` | `hold` | `refuse`. "From project or local settings, `refuse`
  applies over every other source" ("Turn off cross-session messaging"). `isolatePeerMachines: true`
  requires approval before a message leaves the machine; "A `true` from any settings scope applies, so a
  checked-in project file can turn the requirement on but not off" ("Require approval for cross-machine
  messages").
- To stop sending and listing: deny rules for `SendMessage` and `ListAgents` (bare names); "Denying
  `SendMessage` also removes messaging to subagents and agent-team teammates" ("Turn off cross-session
  messaging").
- Hooks: `UserPromptSubmit` fires when another session's message reaches the main conversation (hooks:
  "UserPromptSubmit"). Hooks and Bash get `CLAUDE_CODE_MESSAGING_SOCKET` and `CLAUDE_CODE_MESSAGING_TOKEN`,
  exported "before any hook runs, including `SessionStart`", so a hook can post into its own session ("The
  session's inbox socket").
- `-p` workers bind an inbox too; bare mode does not. Unattended worker: `crossSessionInbound: "accept"` in
  its `--settings` ("Non-interactive sessions").
- Limits: plain text only; about a million characters per same-machine message; at most 100 held and 50
  queued messages; loops are throttled ("Limitations", "Control inbound messages").

### Plugin evals (`claude plugin eval`) — only for plugins

(plugin-evals: sections as cited)

- v2.1.269+. Runs a plugin against cases under `evals/<case>/` (`prompt.md` + `graders/*.md`, optional
  `case.yaml`, `mocks/`), three runs per case by default, with a no-plugin baseline arm; reports `WITH`,
  `W/OUT`, `Δ` ("How an eval run works").
- Grader types: `regex`, `tool_used`, `tool_order`, `file_exists` (free), `llm`, `baseline` (judge model
  calls). "There are no custom-code graders." ("Choose and weight graders", "Grader types").
- Skill-triggering check, QUOTED ("Write a case manually"):

```markdown
---
type: tool_used
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?your-skill-name"'
---
```

- CI, QUOTED ("Run evals in CI"):

```bash
claude plugin eval . \
  --trust-plugin \
  --json results.json \
  --threshold 0.8 \
  --model claude-sonnet-5 \
  --judge-model claude-haiku-4-5 \
  --no-publish \
  --max-cost-usd 20
```

  Exit codes: 0 pass, 1 below threshold or load/trust/API error, 2 partial (cost ceiling or auth), 130
  interrupted, 143 terminated. Default `--threshold` is `1.0`.
- Isolation matters for a project template: "Nothing personal or project-level loads. Your user settings,
  hooks, `CLAUDE.md` files, MCP servers, other installed plugins, memory, and skills are absent.
  Project-scoped configuration isn't read anywhere either" ("How runs are isolated"). Managed policy still
  applies.
- Targets: a plugin root, a single case file, an installed plugin by name, or `name@skills-dir` for a
  "skills-directory plugin" ("Choose what to evaluate"). Whether a repo's own `.claude/skills/` counts as a
  skills-directory plugin is defined on `plugins/loading` (not assigned, not read); see Ambiguities.
- Cost: "Every eval run and every judge grader is a real model call on your account" (intro note). Model
  calls are roughly cases x runs x 2 arms plus three judge calls per `llm`/`baseline` grader per run ("How
  a case is scored").
- Tools: runs never prompt; only read-only tools listed in the case's `allowed_tools` plus `--allow-tools`
  grants; granting Bash requires a sandbox backend (`bubblewrap` and `socat` on Linux) ("Grant tools").
- For iterating on one skill in a conversation, the docs point to the `skill-creator` plugin with its own
  `evals/evals.json` format; "neither tool reads the other's case files" (intro).

---

## 6c. Config-related errors worth recognising

(errors: section headings as cited; this page was SKIMMED by heading and selected sections only)

- Project allow rules need trust even though project hooks do not in `-p`: "`permissions.allow` rules or
  `permissions.additionalDirectories` entries in the project's `.claude/settings.json` ... didn't apply ...
  because allow rules from project settings require workspace trust"; "`deny` and `ask` rules aren't
  affected". In `-p` no dialog is shown; set `projects["<path>"].hasTrustDialogAccepted` in
  `~/.claude.json` (errors: "Workspace has not been trusted").
- File permission rules: only `Edit(path)` and `Read(path)` are checked. `Write(docs/**)` "never matches ·
  use `Edit(docs/**)`" (errors: "Is not matched by file permission checks").
- Typos in deny rules are warned, not fatal: `⚠ Deny rule Bsh matches no tool · check for typos` (errors:
  "Matches no tool · check for typos"). Malformed `Tool(content)` rules are skipped and listed by
  `claude doctor` (errors: "Malformed Tool(content) rule").
- A `Read` deny rule can stop an instruction file loading: `Instruction file not loaded (a Read deny rule
  covers it)` (errors: "Instruction file not loaded").
- Subagent descriptions: warning when combined descriptions exceed 15,000 tokens (errors: "Agent
  descriptions are over the 15.0k-token limit"). A subagent whose `tools` list resolves to nothing is
  refused (errors: "Agent would be spawned with zero tools").
- Auto memory index `MEMORY.md` loads only the first 200 lines or 25KB (errors: "Memory index is over its
  read limit").
- Skill names: `anthropic-skills` is reserved; names with hidden characters, `<`, `>` or over 256
  characters are refused (errors: "A skill, command, or workflow wasn't loaded because its name is
  reserved", "Skill or command name refused").
- `.mcp.json` must be a regular file under 2 MiB; settings files passed with `--settings` likewise 2 MiB
  (errors: "Can't read .mcp.json", "Settings file exceeds the 2MiB limit").
- A `PreToolUse` hook on `Edit` or `Write` disables one-step artifact updates (errors: "Refusing to apply
  edits: a hook is configured for file edits in this session").
- Shell-form `asyncRewake` hooks with an unquoted path containing a space do not run (errors: "Hook needs
  quotes around a path with a space").
- Startup warnings appear below the banner or in the debug log interactively, on stderr in `-p` text mode,
  and only in the debug log with `json`/`stream-json` output (errors: "Configuration warnings").

---

## 7. Changelog highlights

Scope and method (important): the assignment was the first 3,000 lines of the changelog. Those lines cover
**2.1.284 (September 28, 2026) to 2.1.322 (November 10, 2026)** only; August to late September 2026 sits
at roughly lines 3,000 to 5,900 and was NOT read. Within the 3,000 lines I ran out of context budget, so
this section comes from a keyword filter over `Added`/`Changed`/`Removed` bullets (hook, skill, permission,
subagent, `/loop`, memory, CLAUDE.md, `--bare`, `.mcp.json`), not a full read. Fix-only bullets and
anything the filter missed are absent. Quotes are verbatim bullets (changelog: version as cited).

Hooks
- 2.1.295 (Oct 2026): "Added `onFailure: \"block\"` for command and HTTP hooks: a hook that can't start,
  times out, or exits with an unexpected code blocks the action instead of letting it through".
- 2.1.299 (Oct 14): "Changed `UserPromptSubmit` hooks to run before a skill or custom slash command
  expands, so a hook that blocks the prompt now also stops its embedded shell commands".
- 2.1.299: "Changed a skill's own front-matter `UserPromptSubmit` hook to first run on the prompt after
  the one that invokes the skill".
- 2.1.300: "`updatedInput` from PreToolUse and PermissionRequest hooks is now validated like Claude's own
  input: unknown keys are dropped, and input the tool rejects denies the call".
- 2.1.302 and 2.1.312: prompt and agent hooks are concurrency-limited ("at most 12 of one event run at a
  time"; later "at most 24 at a time per session"); "a `timeout` under 1 second now counts as 1 second".
- 2.1.304 (Oct 19): "the skills of one source (a repo, your own folder, or a plugin) can register at most
  1,024 hooks and 16,384 matcher characters per session".
- 2.1.314 (Oct 30): "Changed hook `if` conditions such as `Monitor(tail *)` to match the Monitor tool's
  shell commands as `Bash(tail *)` matches Bash's".
- 2.1.319: "Changed PostToolUse hooks to run, with up to 10 seconds to finish, on tool calls that finish
  after a new message interrupts the turn".
- 2.1.286: "Changed `/hooks` to open on one list of your configured hooks grouped by event".
- 2.1.307: new OpenTelemetry event `claude_code.safety_event` for each tool call "a permission rule, auto
  mode, a safety check, a hook or the sandbox stopped, prompted or sent back".

Skills
- 2.1.304: "Changed compaction to send Claude the skill list again afterwards; `/reload-skills` now sends
  only new or changed skills".
- 2.1.304: under a plugin-only hooks policy, a skill "whose hooks are kept out no longer gets its
  `allowed-tools`".
- 2.1.295: "Changed subagents to preload at most 32 skills from the `skills` field, each once".
- 2.1.299: skills or commands whose file or folder name has hidden or direction-changing characters, `<`
  or `>` are "no longer offered until renamed".
- 2.1.290: skills and custom commands refuse a `!` shell command containing raw control characters.
- 2.1.319: "with the Bash sandbox on, skills in `.claude/skills` folders below the starting folder load
  only if you start Claude Code there or `/cd` there". 2.1.321: nested `.claude/skills` inside
  `~/.claude/plugins` no longer load.
- 2.1.290: "`/code-review` at medium effort to also report cleanup and CLAUDE.md conventions findings on
  models without tuned review settings".

Permissions and settings
- 2.1.284 (Sep 28): "interactive terminal and VS Code sessions to start in auto mode when no permission
  mode is configured, on every plan and provider; `permissions.defaultMode` still overrides it".
- 2.1.285 then 2.1.302: `claude -p` default mode changed twice. 2.1.285 made some `-p` sessions "start in
  auto mode when no permission mode is configured"; 2.1.302 changed "`claude -p` and Agent SDK sessions
  with no permission mode to start in `default` mode on third-party providers, with telemetry off or on a
  fresh install". The headless page says v2.1.302+ `-p` runs "start in Manual mode when nothing sets a
  permission mode". Inference: set `--permission-mode` explicitly in every CI invocation.
- 2.1.314: "Added `permissions.blockWritesOutsideWorkingDirectories`: Write, Edit and NotebookEdit refuse
  paths outside the working directories in every permission mode".
- 2.1.319: "Added `permissions.denyInsteadOfPrompting` setting: a tool call that would wait on a permission
  prompt is denied and the turn continues, in terminal sessions, subagents and teammates".
- 2.1.287: whole-tool `Bash` allow rules and allowing hooks now prompt for shell writes to files the file
  tools refuse outright.
- 2.1.290: "`CLAUDE_CODE_DISABLE_ATTACHMENTS` so a repository's `.claude/settings.json` or
  `.claude/settings.local.json` can no longer set it". (Pattern: some env keys are ignored from project
  settings; see also `CLAUDE_CODE_DISABLE_FILE_MENTIONS` in 1.8.)
- 2.1.311: startup warnings about permission rules "show once per user until the rule changes".
- 2.1.299: "`\"idleCompaction\": false` in settings.json turns it off"; `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`.

Headless
- 2.1.286: "Changed `--bare` to connect only the MCP servers named on the command line, send the model no
  system reminders, and start no background tasks".
- 2.1.321: "Changed headless sessions to reload mods in `.claude/skills` when their files change".

Subagents
- 2.1.296: "Added `autoCompactWindow` to subagent frontmatter and `--agents` definitions".
- 2.1.316: "Added `CLAUDE_CODE_SUBAGENT_EFFORT`"; 2.1.317: subagents on a different model use that model's
  saved effort level or default instead of the session's.
- 2.1.318: background subagents move a shell command to the background after 3 minutes.
- 2.1.319: `/tasks` gains an "Earlier in this session" row listing finished subagents; after safeguards
  stop a subagent Claude is told to "retry with a narrower prompt or tell you, instead of doing the work
  itself".
- 2.1.292: agent names limited to 256 characters.

Loops
- 2.1.319: "Changed self-paced `/loop` to end when a turn finishes without rescheduling, instead of
  scheduling a fallback wakeup; set `CLAUDE_CODE_LOOP_KEEPALIVE=1` to keep the old behavior".
- 2.1.319: cloud sessions note that a `/loop` timer "stops with its container".
- 2.1.295: Ctrl+C at the idle prompt of an attached background session leaves a pending `/loop` wakeup
  alone.

Memory
- 2.1.285: "Auto-memory can no longer be turned on from a background session or from a session one of
  Claude Code's own tools started; turning it off there still works".

Other
- 2.1.321 (Nov 9): "Added Claude Fable 5.2 (`claude-fable-5-2`), now the default Fable model".
- Many entries in this window concern "mods" (plugins that register in-process JavaScript hooks such as
  `tool.check`, `agent.spawn`, `settings.read`). They are a separate hook system from settings-file hooks
  (hooks: intro) and were filtered out here.

---

## 8. Ambiguities and things expected but not found

1. Hook ordering across scopes: the docs say matching hooks "run in parallel" and merge across settings
   levels; no ordering between user, project, local and plugin hooks is documented, and none can be
   configured. `updatedInput` conflicts are explicitly undefined.
2. Project hook approval: there is no per-hook approval or hash-pinning in the pages read. Trust is the
   folder-level workspace trust dialog (interactive) and is implicit in `-p`/SDK. Yet project
   `permissions.allow` rules are NOT applied in an untrusted `-p` run while project hooks are (errors:
   "Workspace has not been trusted" versus hooks: "Workspace trust"). The full table is on the
   `permissions` page ("What runs before you trust a folder"), which was only grep-read.
3. "Only project config": no single documented flag. `--setting-sources project` is documented in one line
   on cli-reference; its coverage (CLAUDE.md, rules, skills, agents, `.mcp.json`) is documented for the SDK
   option and by scattered CLI statements. Not confirmed for the CLI: user plugins, `~/.claude.json`
   content, and behaviour of a fresh `CLAUDE_CONFIG_DIR` with subscription auth. Worth a live test with
   `/status`, `/hooks`, `/context`, `/mcp` and an InstructionsLoaded logging hook.
4. `--bare` "will become the default for `-p` in a future release" (headless). If that lands, plain
   `claude -p` in CI would stop loading project hooks, skills, `.mcp.json` and CLAUDE.md; a template that
   relies on them in CI should pass `--setting-sources` explicitly and re-check on upgrade. No version or
   date is given.
5. `-p` default permission mode changed in 2.1.285 and again in 2.1.302; wording differs between headless
   ("Manual mode") and the changelog ("`default` mode ... on third-party providers, with telemetry off or
   on a fresh install"). Whether a logged-in first-party `-p` run still starts in auto is not clear from
   the pages read.
6. CLI-or-skill versus MCP guidance: not found in any assigned page. If it exists it is likely on pages
   not assigned here (for example best-practices, features-overview or costs).
7. Managed Code Review pricing: on `code-review-costs`, which is not saved in `refs/`.
8. `/code-review` is described as a bundled skill, while the GitHub Actions example installs a
   `code-review` plugin and runs `/code-review:code-review`. Relationship and behavioural differences are
   not explained.
9. `Stop` hook output size: the 10,000-character cap is stated for `additionalContext`, `systemMessage`,
   `initialUserMessage` and plain stdout; whether `reason` or exit-2 stderr is capped is not stated.
10. `Stop` exit-2 special case (stderr mentioning a missing file is treated as non-blocking): the exact
    matching rule is not given, so its interaction with test output is unknown.
11. Whether a repository's own `.claude/skills/` can be targeted by `claude plugin eval` as a
    "skills-directory plugin" (`name@skills-dir`) is defined on `plugins/loading`, not read.
12. GitHub Action: which setting sources it loads and whether it uses `--bare` is not stated on the page.
13. GitLab example uses space-separated `--allowedTools "Bash Read Edit Write mcp__gitlab"`; other pages
    use commas. Both forms appear in official examples; equivalence is not stated.
14. Cloud sessions: no repo-declared environment file exists; `remote.defaultEnvironmentId` in project
    settings is the only repo-side pointer, and self-hosted IDs follow "a stricter source rule" (not read).
15. Changelog coverage gap: August 1 to September 27, 2026 (versions before 2.1.284) not read; the read
    window itself was keyword-filtered. The hooks reference's inline version notes (for example
    PreModelSwitch/PostModelSwitch at v2.1.251, `scratchpad_dir` at v2.1.257, `bashEditDiff` at v2.1.269,
    `mcp_server` at v2.1.274) partly cover that gap but are not dated.

Reading record: read in full: hooks, hooks-guide, mcp, mcp-quickstart, headless, cli-reference,
github-actions, gitlab-ci-cd, code-review, code-review-local, code-review-customize, ultrareview,
claude-code-on-the-web, cloud-environments, channels, cross-session-messaging, plugin-evals. Partial by
design: managed-mcp (precedence sections), errors (headings plus selected sections). Partial by necessity:
changelog (see section 7). Looked up by grep only, to answer the setting-sources question:
agent-sdk-claude-code-features, debug-your-config, skills, plugins-loading, permissions, memory.

Possible injection content: none acted on. Every saved page opens with a "Documentation Index" banner
telling the reader to fetch `https://code.claude.com/docs/llms.txt`; it was treated as page boilerplate and
not followed.

