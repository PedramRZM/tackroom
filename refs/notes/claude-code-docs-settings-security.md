# Claude Code docs digest: settings, permissions, sandboxing, security (project-level config)

Reference digest for writing a committed `.claude/settings.json` (no user-level config) for a
template synced into many repos. Installed Claude Code: 2.1.322. All sources are saved copies of
`code.claude.com/docs/en/*.md`, fetched 2026-11-10 (`meta.json` `fetched_at`), under
`refs/articles/code.claude.com/<slug>/article.md`. Only the saved text is used. Anything not
taken directly from a page is marked "Inference:".

Source keys used in citations (file slug, then section heading):

| Key | File slug | Page title |
| :- | :- | :- |
| SET | docs-en-settings-md | Settings files and precedence |
| REF | docs-en-settings-reference-md | All settings |
| EX | docs-en-settings-example-md | Example settings files |
| PERM | docs-en-permissions-md | Configure permissions |
| MODES | docs-en-permission-modes-md | Permission modes |
| AUTO | docs-en-auto-mode-config-md | Configure auto mode |
| SBX | docs-en-sandboxing-md | Sandboxing |
| SBXENV | docs-en-sandbox-environments-md | Sandbox environments |
| SEC | docs-en-security-md | Security |
| SECG | docs-en-security-guidance-md | Security guidance |
| DEVC | docs-en-devcontainer-md | Dev containers |
| DEBUG | docs-en-debug-your-config-md | Debug your configuration |
| TOOLS | docs-en-tools-reference-md | Tools reference |
| STATUS | docs-en-statusline-md | Status line |
| MANAGED | docs-en-managed-settings-md | Managed settings |
| SERVER | docs-en-server-managed-settings-md | Server-managed settings |
| OTEL | docs-en-monitoring-usage-md | Monitoring usage |
| FEAT | docs-en-feature-availability-md | Feature availability |

Sources read: 18 (15 in full; MANAGED and SERVER for precedence only and OTEL skimmed, as
assigned). Exact line ranges are in "Read coverage and limits" at the end.

This is a reference digest organised by topic, not the per-source format.

## 1. Settings scopes and precedence

### 1.1 The files

Four settings files plus managed sources (SET, "Settings files and who they affect"):

| Scope | File | Who it affects |
| :- | :- | :- |
| User | `~/.claude/settings.json` | You, in every project on this machine |
| Shared project | `.claude/settings.json` | Everyone working in the folder; commit it |
| Project local | `.claude/settings.local.json` | You, in this one project only |
| Managed | `managed-settings.json`, MDM policy, server-managed settings | Everyone the organization deploys it to |

- A fifth file, `~/.claude.json`, is written by Claude Code itself and holds account details, MCP
  server configurations, per-project state "such as trust decisions", and the "global config"
  keys that `/config` writes (SET, "Find or create your settings files"). Keys with scope
  `Global config` apply only from that file (SET, "A committed key doesn't reach teammates").
- Installing Claude Code creates no settings file (SET, "Find or create your settings files").
- `CLAUDE_CONFIG_DIR` relocates the home-directory files (SET, same section, note).
- Settings files are strict JSON: "a `//` comment or a trailing comma is a syntax error" (SET,
  "Edit a settings file"). The `$schema` value documented is
  `https://json.schemastore.org/claude-code-settings.json`; the schema "can lag behind the newest
  CLI releases", so a warning on a new key does not mean the file is invalid (same section).
- Shared `.claude/settings.json` is read from the session's primary working directory, "so to use
  a file committed at the repository root, start Claude Code there" (SET, "Where Claude Code keeps
  the local file in a git repository"). After `/cd`, both project files are read from the new
  directory (needs v2.1.246+).
- `.claude/settings.local.json` in a git repository is read and written at the repository root
  (and at the main checkout's root in a worktree) since v2.1.211; exceptions: outside a git repo,
  repo root is the home directory, Windows, or root/.git/.claude not owned by the user (SET, same
  section). Paths inside it still anchor at the session's primary working directory.

### 1.2 Precedence (highest first)

SET, "Settings precedence":

1. Managed settings (nothing in your files or `--settings` overrides a managed key).
2. Command line: `--settings <file-or-json>`, for that session only.
3. Project local `.claude/settings.local.json`.
4. Shared project `.claude/settings.json`.
5. User `~/.claude/settings.json`.

- "a key at a higher level overrides the same key anywhere below it" (SET, "Settings precedence").
  So a project value beats the user value; a teammate gets their own value back only via
  `.claude/settings.local.json` (SET, "Team settings override personal settings").
- Environment variables "aren't a level in this stack"; each variable/key pair decides its own
  order (for example `ANTHROPIC_MODEL` exported in the shell beats `model` from any file, while
  `ANTHROPIC_DEFAULT_MODEL` applies only when no file sets `model`). An `env` block inside a
  settings file "is an ordinary key and follows the levels above" (SET, "Settings precedence").
- `--settings` "can set any key your user settings file can set; it can't set `Managed` or
  `Global config` keys" (SET, "Change a setting for one session").

### 1.3 How lists combine

- "When you set the same list key, such as `permissions.allow`, in more than one file, Claude Code
  combines the lists instead of picking one" (SET, "Lists merge instead of overriding").
- Four exceptions (same section): `fallbackModel` (whole value from the highest-precedence file),
  `modelPicker` (whole value from the highest of managed, `--settings`, user; ignored in project
  and local), `availableModels` (a managed list applies as-is; non-managed scopes merge),
  `modelSettings` (resolved one model at a time with `effortLevel`).
- Permission rules: allow rules merge across scopes, but "an `allow` rule there doesn't outrank an
  `ask` rule from a project or managed file" (SET, "Permission rules combine differently than you
  expected"). Evaluation is deny, then ask, then allow, across all merged rules (see section 3).
- Sandbox: array keys merge across the scopes the session loads; a managed Boolean such as
  `enabled` overrides anything a developer sets (REF, "`sandbox`").
- `autoMode` arrays: "When more than one of those files sets the same array, Claude Code
  concatenates the entries" (REF, "`autoMode`") (but project files are not among "those files").
- Hooks: "Hooks merge across files rather than replacing each other, and hooks from managed
  settings can't be removed from other files." (REF, "`hooks`"). So project hooks run in addition
  to any user hooks; neither scope can remove the other's, except through `disableAllHooks`,
  which is an ordinary key where the higher-precedence file wins (project beats user: PERM, "What
  runs before you trust a folder").
- `allowedHttpHookUrls`, `httpHookAllowedEnvVars`: "Arrays merge across settings files" (REF).
- `allowedMcpServers` and `deniedMcpServers`: entries from every file merge (REF).
- `extraKnownMarketplaces`: same-name entries do not merge; the highest-precedence file's entry
  wins whole (REF, "`extraKnownMarketplaces`").
- `enabledPlugins`: per-plugin Boolean, project beats user (REF, "`enabledPlugins`").
- `env`: per variable, "the highest-precedence one applies" (REF, "How `env` values interact with
  your shell").

### 1.4 When edits take effect, and checking what loaded

- Claude Code watches settings files and reloads most edits without a restart, "including edits to
  `permissions`, `hooks`, and credential helpers such as `apiKeyHelper`" (SET, "When edits take
  effect"). `model`, `effortLevel` and `modelSettings` are read only at session start.
- A `ConfigChange` hook runs for each settings-file change detected (same section).
- `/status` shows a `Setting sources` line listing each file loaded; it "doesn't show which file
  supplied each key". `claude doctor` lists rejected entries (SET, "Confirm what loaded").
- Broken file: interactive sessions show a "Settings Error" dialog (whole file invalid) or a
  "Settings Warning" (individual entries skipped, "such as a malformed permission rule or an
  unknown hook event name"); a `-p` run shows no dialog and silently skips the broken file or
  values (SET, "Fix a broken settings file").

### 1.5 Trust gating of project settings

SET, "A committed key doesn't reach teammates":

- "`permissions.allow` rules, `permissions.additionalDirectories`, `extraKnownMarketplaces`, and
  most `env` values apply only after each teammate trusts the folder."
- "`deny` and `ask` rules apply right away."
- An untracked `.claude/settings.local.json` applies its allow rules without the trust step; if
  the file is tracked by git, the trust step applies to it too (SET, "Keep personal settings out
  of a repository").

### 1.6 Keys NOT honoured (or only partly honoured) in project `.claude/settings.json`

Rule from SET, "A committed key doesn't reach teammates": look for `User, local, or managed`,
`User or managed`, `User`, `Managed`, or `Global config` in the Scope column of the settings
index; "Those keys never apply from the shared file, apart from a few that a repository file can
still switch off."

The lists below are transcribed from the Scope column of REF, "Settings index" (249 rows: 157
`Any file`, 44 `Managed`, 31 `User or managed`, 12 `Global config`, 4 `User, local, or managed`,
1 `User`; the transcription was checked mechanically against the index), with the per-entry
Scope line where it adds detail. A few keys whose index Scope is `User or managed` have a
project-file quirk stated in their entry: `autoContinueAtUsageLimit` ("a project or local
settings file that sets it turns the feature off rather than being ignored") and
`bashEditDiffEnabled` (a project `true` is ignored, a project `false` "still turns it off").

**Scope `User or managed`** (ignored in project and local settings):

`askUserQuestionTimeout`, `appendPlugins`, `autoContinueAtUsageLimit`, `autoMode`,
`autoMode.classifyAllShell`, `axScreenReader`, `bashEditDiffEnabled`,
`desktopSessionCleanupPeriodDays`, `dialogExpiry`, `feedbackDrafts`, `footerLinksRegexes`,
`forceLoginGatewayUrl`, `modelPicker`, `permissions.denyInsteadOfPrompting`, `pluginConfigs`,
`prependPlugins`, `processWrapper`, `sandbox.allowAppleEvents`,
`sandbox.allowNestedUserNamespaces`, `sandbox.credentials.allowPlaintextInject`,
`sandbox.credentials.awsPairs`, `sandbox.credentials.sigv4`, `sandbox.filesystem.disabled`,
`sandbox.network.strictAllowlist`, `sandbox.network.tlsTerminate`, `sandbox.ripgrep`,
`skipAutoPermissionPrompt`, `spellcheck`, `sshConfigs`, `sshHostCommands`, `vimInsertModeRemaps`.

**Scope `User, local, or managed`** (ignored in the committed project file, honoured in
`.claude/settings.local.json`):

`skipDangerousModePermissionPrompt`, `syncClaudeAiPlugins`, `syncClaudeAiSkills`,
`useAutoModeDuringPlan`.

**Scope `User`**: `worktree.location`.

**Scope `Managed`** (ignored everywhere else):

`allowAllClaudeAiMcps`, `allowClaudeInChromeWithManagedMcp`, `allowedChannelPlugins`,
`allowedProviders`, `allowManagedHooksOnly`, `allowManagedMcpServersOnly`,
`allowManagedPermissionRulesOnly`, `availableModelsMatch`, `blockedMarketplaces`,
`browserExternalPageTools`, `channelsEnabled`, `claudeMd`, `deniedModels`,
`disableBrowserExternalNavigation`, `disableCommandPluginSources`, `disableDesktopLocalSessions`,
`disableMobileSimulatorTools`, `disableSideloadFlags`, `forceRemoteSettingsRefresh`,
`gatewayInternalNetworks`, `managedMcpServers`, `managedSourcesBehavior`, `modelPricing`,
`parentSettingsBehavior`, `pluginSuggestionMarketplaces`, `pluginTrustMessage`, `policyHelper`
(and `.path`, `.refreshIntervalMs`, `.timeoutMs`), `requiredMaximumVersion`,
`requiredMinimumVersion`, `sandbox.bwrapPath`, `sandbox.filesystem.allowManagedReadPathsOnly`,
`sandbox.network.allowManagedDomainsOnly`, `sandbox.socatPath`, `sshHostAllowlist`,
`strictKnownMarketplaces`, `strictPluginOnlyCustomization` (and `.agents`, `.hooks`, `.mcp`,
`.skills`), `wslInheritsWindowsSettings`.

**Scope `Global config`** (`~/.claude.json` only):

`autoConnectIde`, `autoInstallIdeExtension`, `claudeInChromeDefaultEnabled`, `copyFullResponse`,
`copyOnSelect`, `defaultToAgentsView`, `diffTool`, `externalEditorContext`,
`leftArrowOpensAgents`, `permissionExplainerEnabled` (removed), `prStatusFooterEnabled`,
`teammateDefaultModel` (removed).

**Scope `Any file`, but with values or sub-parts that a project file cannot set** (the most
important group for a template):

| Key | What is ignored from project (and usually local) settings | Citation |
| :- | :- | :- |
| `permissions.defaultMode` | "`auto` and `bypassPermissions` don't take effect from project or local settings". Before v2.1.257 `bypassPermissions` took effect from any file. For conversations the VS Code extension starts, only user, managed and `--settings` values are read. | REF, "`permissions.defaultMode`"; SET, "A value you set is ignored" |
| `env` | Storage/location variables (`CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR`, `HOME`, `TMPDIR`, `TMP`, `TEMP`, `XDG_*`), Windows system variables, session-content export (`OTEL_LOG_RAW_API_BODIES`, `ENABLE_BETA_TRACING_DETAILED`, `BETA_TRACING_ENDPOINT`), all OpenTelemetry exporter variables that turn telemetry on or choose destination/content (`CLAUDE_CODE_ENABLE_TELEMETRY`, `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA`, `ENABLE_ENHANCED_TELEMETRY_BETA`, `OTEL_LOGS_EXPORTER`, `OTEL_METRICS_EXPORTER`, `OTEL_TRACES_EXPORTER`, `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_ASSISTANT_RESPONSES`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_EXPORTER_OTLP_*` ending `_ENDPOINT`/`_HEADERS`/`_PROTOCOL`/`_CERTIFICATE`/`_CLIENT_KEY`/`_INSECURE`, `OTEL_EXPORTER_PROMETHEUS_HOST`/`_PORT`), start/sync variables (`CLAUDE_CODE_PROCESS_WRAPPER`, `CLAUDE_CODE_SYNC_SKILLS`, `CLAUDE_CODE_SYNC_PLUGINS`, `CLAUDE_CODE_PLUGIN_CACHE_DIR`, `CLAUDE_CODE_PLUGIN_SEED_DIR`), sign-in variables (`CLAUDE_CODE_OAUTH_TOKEN`, `..._REFRESH_TOKEN`, `..._SCOPES`), `CLAUDE_AX_*`, `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS`, `CLAUDE_CODE_DISABLE_ATTACHMENTS`, `CLAUDE_CODE_DISABLE_FILE_MENTIONS`. Only "off" values still apply (`none` for the three exporter selectors; `0`-style off for `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_TOOL_DETAILS`). Telemetry group ignored since v2.1.282. | REF, "Variables Claude Code ignores in `env`" |
| `env` (every file) | Ignored from every settings file: `CLAUDE_CODE_REMOTE`, `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_MESSAGING_SOCKET`/`_TOKEN`, `CLAUDE_CODE_PROJECT_DIR_NAME`, `CLAUDE_CODE_RESTRICTED`, `CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY`, `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`, `CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT`, `CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT`, `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT`, `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS`, `CLAUDE_CODE_WARN_DISK_FREE_GIB`, `CLAUDE_CODE_WARN_MEMORY_FREE_GIB` (launch environment only). | REF, same section |
| `sandbox.credentials`, `.files`, `.envVars` | `mask` entries are dropped from project and local files; `deny` entries are honoured. `allowPlaintextInject`, `awsPairs`, `sigv4` only from user, managed, `--settings`. | REF, "`sandbox.credentials`", "`sandbox.credentials.files`", "`sandbox.credentials.envVars`" |
| `sandbox.allowNestedUserNamespaces` | "Claude Code ignores a `true` in a project's `.claude/settings.json` or `.claude/settings.local.json`"; a `false` counts from any file. | REF, "`sandbox.allowNestedUserNamespaces`" |
| `sandbox.allowUnsandboxedCommands` | A `false` in user settings "holds against a project's `true`" (v2.1.285+). A project can still set `false`. | REF, "`sandbox.allowUnsandboxedCommands`" |
| `sandbox.excludedCommands`, `sandbox.enabled`, `sandbox.failIfUnavailable`, `sandbox.filesystem.allowWrite`, `sandbox.filesystem.allowRead`, `sandbox.ignoreViolations`, `sandbox.enableWeakerNestedSandbox`, `sandbox.enableWeakerNetworkIsolation`, `sandbox.network.allowUnixSockets`, `sandbox.network.allowAllUnixSockets`, `sandbox.network.allowLocalBinding`, `sandbox.network.allowMachLookup`, `sandbox.network.allowedDomains` | "limits on project and local settings" when the sandbox is admin-required (managed or `--settings` requires it): project and local entries are ignored. Not relevant to a solo developer without managed settings, except via `--settings`. See section 5. | REF, each entry's Scope line; SBX, "Repository settings under an admin-required sandbox" |
| `sandbox.filesystem.allowRead`, `allowWrite`, `permissions.additionalDirectories` | Entries from repository settings "don't count" while `permissions.blockReadsOutsideWorkingDirectories` is on (and repository `additionalDirectories` do not count as working directories for the read/write blocks). | REF, "Sandboxed commands under the block", "`permissions.blockReadsOutsideWorkingDirectories`" |
| `autoMemoryDirectory` | Honoured from project or local settings only "under the same workspace trust rule as hooks"; under the read block, no auto memory is loaded from or saved to a repository-chosen directory. | REF, "`autoMemoryDirectory`", "`permissions.blockReadsOutsideWorkingDirectories`" |
| `remoteControlAtStartup` | A project or local `true` is ignored; a project `false` is honoured even over managed `true`. | SET, "Exceptions to managed settings precedence" |
| `crossSessionInbound` | A project or local value "that isn't stricter is ignored" (`accept` < `hold` < `refuse`). | SET, same table |
| `useAutoModeDuringPlan`, `syncClaudeAiSkills`, `syncClaudeAiPlugins` | "a `false` in `.claude/settings.json` is ignored". | SET, same table |
| `remote.defaultEnvironmentId` | "a self-hosted `ccpool_` ID is read only from user and managed settings and `--settings`". | REF, "Settings index" |
| `forceLoginOrgUUID` | Scope `Any file` but "only managed settings enforce it". | REF, "Settings index" |
| `enforceAvailableModels` | Read from the managed source alone when any managed settings are deployed. | REF, "`enforceAvailableModels`" |

**Restrictive values a project file CAN impose** (honoured from any scope, even against managed;
SET, "Exceptions to managed settings precedence"): `disableClaudeAiConnectors: true`,
`enableArtifact: false` (and `disableArtifact: true`), `isolatePeerMachines: true`,
`permissions.blockReadsOutsideWorkingDirectories: true` (v2.1.257+),
`permissions.blockWritesOutsideWorkingDirectories: true` (v2.1.314+), a lower `maxEffortLevel`
(v2.1.267+), `remoteControlAtStartup: false`, a stricter `crossSessionInbound`.
"a repository can turn the block on for itself but can't lift yours" (REF,
"`permissions.blockReadsOutsideWorkingDirectories`").

### 1.7 Cloud sessions (for completeness)

SET, "Settings in cloud sessions": a cloud session with one repository reads the committed
`.claude/settings.json`; user and local settings are not read; in cloud threads in a project,
none of the repository's permission rules, hooks or `env` apply; with several repositories only
`enabledPlugins` and `extraKnownMarketplaces` are read (and those plugins still do not load).
In cloud sessions `permissions.defaultMode` honours only `acceptEdits`, `plan`, `default`, `auto`
(REF, "`permissions.defaultMode`").

## 2. Settings keys a solo developer's project template would plausibly set

All rows are from REF (docs-en-settings-reference-md); the section heading is the key name in
backticks. "Any file" means user, project, local and managed. Types, defaults and values are
as documented; "unset" defaults are the docs' wording.

### 2.1 Model and effort

| Key | Scope | Type / allowed values | Default | Documented description and notes |
| :- | :- | :- | :- | :- |
| `model` | Any file | string, a model alias or full model ID | unset (account default) | "Set the model every new session uses". Read once at session start. `--model` beats `ANTHROPIC_MODEL`, both beat this key. For a model set by project or managed settings "the startup header names the file that set it" (SET, "Confirm what loaded"). Example values in docs: `"claude-sonnet-5"`, `"claude-opus-5-5"`. |
| `effortLevel` | Any file | `"low"`, `"medium"`, `"high"`, `"xhigh"` | unset | Default effort "for models you haven't saved a level for". "In project, local, and managed settings, and with `--settings`, this key applies to every model"; in user settings it is the older form and Opus 5.5 and later ignore it. `--effort` beats it, `CLAUDE_CODE_EFFORT_LEVEL` beats both. `/effort` wrote this key before v2.1.251. |
| `modelSettings` | Any file | object: model name to `{ effortLevel, maxEffortLevel, autoCompactWindow }` | unset | Per-model saved effort (v2.1.251+). A model's entry beats top-level `effortLevel` in the same file; across files "the highest-precedence settings file that sets either" decides per model. `autoCompactWindow`: `100000` to `1000000` or `"auto"` (v2.1.288+). |
| `maxEffortLevel` | Any file | `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"` (`"max"` = no cap) | unset | Caps effort (v2.1.267+). "When several scopes set a cap, the lowest applies", so a project cap cannot be raised by the user. |
| `fallbackModel` | Any file | array of model aliases or IDs; `"default"` expands | unset | Backup chain when the primary is overloaded; does not merge across files; at most three distinct models kept. |
| `advisorModel` | Any file | `"fable"`, `"opus"`, `"sonnet"` or a full model ID | unset (advisor off) | Model that answers the server-side advisor tool; normally written by `/advisor`. |
| `alwaysThinkingEnabled` | Any file | Boolean; only `false` has effect | unset (thinking on) | No effect on models that always think (Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable). |
| `outputStyle` | Any file | string, name of a built-in or custom output style | unset | Example `"Explanatory"`. Applies from the next message since v2.1.251. |
| `language` | Any file | string, any language name (not validated) | unset | Response language, dictation language, session titles. |
| `ultracode` | Any file | Boolean | unset (off) | Sessions start with ultracode on (Claude plans a workflow per substantive task) when dynamic workflows are enabled and the model supports `xhigh`. |
| `promptCacheTtl` / `subagentPromptCacheTtl` | Any file | `"5m"` or `"1h"` | unset | Prompt cache lifetime for main conversation / everything else (v2.1.242+). One-hour writes are billed at a higher rate. |
| `showThinkingSummaries` | Any file | Boolean | `false` | Show thinking summaries with `Ctrl+O`. |

### 2.2 Permissions

| Key | Scope | Type / allowed values | Default | Documented description and notes |
| :- | :- | :- | :- | :- |
| `permissions` | Any file | object with `allow`, `ask`, `deny`, `additionalDirectories`, `blockReadsOutsideWorkingDirectories`, `blockWritesOutsideWorkingDirectories`, `defaultMode`, `denyInsteadOfPrompting`, `disableBypassPermissionsMode`, `disableAutoMode` | unset | "Control which tools Claude can use without asking, which ones prompt, and which ones are blocked." |
| `permissions.allow` | Any file | array of permission rule strings | unset | Approved without asking. From project settings only after the workspace trust dialog is accepted. `--allowedTools` adds rules for one session. |
| `permissions.ask` | Any file | array of rule strings | unset | Prompts "even in a permission mode that would otherwise approve them, such as `acceptEdits` or `bypassPermissions`". In `dontAsk` mode a match is denied instead of prompting. |
| `permissions.deny` | Any file | array of rule strings | unset | Blocks. For secret files, Claude Code "excludes matching files from file discovery and search results, denies reads of them, and blocks the Edit and Write tools". Applies to file tools, to recognised file commands in Bash (`cat`, `head`, `tail`, `sed`, `tee`) and redirection targets; not to `grep -r pattern .` or arbitrary subprocesses. "`\"*\"` denies every tool and `\"mcp__*\"` denies every MCP tool." Replaces deprecated `ignorePatterns`. |
| `permissions.defaultMode` | Any file (values limited) | `"default"`, `"acceptEdits"`, `"plan"`, `"auto"`, `"dontAsk"`, `"bypassPermissions"`, `"manual"` (alias for `"default"`) | unset (built-in default for the surface) | `auto` and `bypassPermissions` do not take effect from project or local settings. `--permission-mode` (and `--dangerously-skip-permissions`) override for one session. |
| `permissions.additionalDirectories` | Any file | array of directory paths | unset | Extra working directories (file access, not configuration discovery). From project settings only after trust. Example `["../docs/"]`. |
| `permissions.blockReadsOutsideWorkingDirectories` | Any file; `true` from any file applies | Boolean | unset | File tools (`Read`, `Grep`, `Glob`, `LSP`) refuse reads outside working directories in every mode including `bypassPermissions` (v2.1.257+). With the sandbox on it also denies sandboxed commands read access to the home directory and `/Users`, `/home`, `/root`, `/Volumes`, `/mnt`, `/media`, `/run/media`, `/srv`, then re-opens working directories, session worktrees, temp dir, needed parts of `~/.claude`, and global git config. Removing it needs a restart. |
| `permissions.blockWritesOutsideWorkingDirectories` | Any file; `true` from any file applies | Boolean | unset | `Write`, `Edit`, `NotebookEdit` refuse paths outside working directories in every mode (v2.1.314+). Does not limit shell commands, MCP tools or hook programs. Also removes `EnterWorktree`/`ExitWorktree`, and refuses writes to Claude Code settings files even inside the working directories. |
| `permissions.disableBypassPermissionsMode` | Any file | the string `"disable"` | unset | Rejects `--dangerously-skip-permissions` and ignores an agent's `permissionMode: bypassPermissions`. |
| `disableAutoMode` | Any file (also `permissions.disableAutoMode`) | the string `"disable"` | unset | Removes auto mode from the `Shift+Tab` cycle; sessions that would start in auto start in `default`. |
| `permissions.denyInsteadOfPrompting` | User or managed, and `--settings` (NOT project) | Boolean | unset | Denies calls that would prompt, so an unattended session keeps working (v2.1.319+). Also removes `AskUserQuestion`, `EnterPlanMode`, `ExitPlanMode`. In auto mode the turn ends after 20 refused calls in a row. Single-run equivalent: `--permission-prompts none` with `-p`. |
| `autoMode` (`environment`, `allow`, `soft_deny`, `hard_deny`, `classifyAllShell`) | User or managed (NOT project) | object of prose-rule arrays plus a Boolean | unset | Classifier customisation; `"$defaults"` keeps built-in rules at that position. See section 4. |
| `useAutoModeDuringPlan` | User, local, or managed (NOT project) | Boolean | `true` | Classifier reviews shell commands in plan mode; `false` gives prompts instead. |
| `skipAutoPermissionPrompt` | User or managed | Boolean | unset | Skips the one-time auto mode notice. |
| `skipDangerousModePermissionPrompt` | User, local, or managed | Boolean | unset | Skips the bypass confirmation dialog. "An untrusted repository can't skip the dialog for you." |

### 2.3 Environment, hooks, status line

| Key | Scope | Type / allowed values | Default | Documented description and notes |
| :- | :- | :- | :- | :- |
| `env` | Any file (some variables ignored from project/local) | object: variable name to string | unset | "Set environment variables for every session and for the subprocesses Claude Code starts from it." Overwrites the same shell variable; highest-precedence file wins per variable. Project/local values apply "after you trust the workspace, or at startup in `-p` mode, which never shows the trust dialog"; variables classified as safe (model selection, timeouts and limits, feature toggles) apply at startup from every file. "Values here are plain text in the settings file and reach every subprocess". `""` cancels a shell export. |
| `hooks` | Any file | object keyed by hook event; each value an array of `{ "matcher", "hooks" }` groups; handler `type` one of `"command"`, `"prompt"`, `"agent"`, `"http"`, `"mcp_tool"` | unset | "Hooks merge across files rather than replacing each other, and hooks from managed settings can't be removed from other files." |
| `disableAllHooks` | Any file | Boolean | unset | Turns off hooks, custom status line and custom file-suggestion command. Outside managed settings it disables "user, project, local, and plugin hooks"; also stops installed mods; `/goal` cannot run. When `true` outside managed settings, `statusLine` is narrowed to a managed value (i.e. off for a solo developer). |
| `allowedHttpHookUrls` | Any file; arrays merge | array of URL patterns with `*` | unset (any URL) | HTTP hooks run only if the URL matches; empty array blocks every HTTP hook. |
| `httpHookAllowedEnvVars` | Any file; arrays merge | array of env var names | unset | Outer limit on which variables HTTP hooks may interpolate into headers. |
| `statusLine` | Any file | object: `type: "command"`, `command` string, optional `padding` (number of characters), `refreshInterval` (seconds, minimum `1`), `hideVimModeIndicator` (Boolean) | unset | Custom status line command. Off entirely when the folder is not trusted "under the same workspace trust rule as hooks in settings files" (REF, "Status line and file suggestion gates"). |
| `subagentStatusLine` | Any file | object: `type: "command"`, `command` | unset | Rewrites subagent task rows. Same gates as `statusLine`. |
| `fileSuggestion` | Any file | object: `type: "command"`, `command` | unset | Custom `@` autocomplete; receives `{"query": ...}` on stdin, prints paths, 5-second limit, at most 15 shown. Same gates. |

### 2.4 Plugins and MCP

| Key | Scope | Type / allowed values | Default | Documented description and notes |
| :- | :- | :- | :- | :- |
| `enabledPlugins` | Any file | object: `plugin-name@marketplace-name` to Boolean | unset (plugin's `defaultEnabled`) | Project settings turn plugins on for everyone in the repo: "This doesn't install them, so each user installs them." Project beats user; opt out in `.claude/settings.local.json`. |
| `extraKnownMarketplaces` (alias `additionalMarketplaces`, v2.1.232+) | Any file; project/local only after trust | object: marketplace name to `{ source, autoUpdate? }`; `source.source` one of `github` (`repo`), `git` (`url`), `url` (`url`, `headers`, `headersHelper`), `file` (`path`), `directory` (`path`), `settings` (`name`, `plugins`) | unset | Registers marketplaces for people who open the repo. In an untrusted folder, "including a `-p` run there, it ignores them without a message". Same-name entries: highest-precedence file wins whole (since v2.1.228). `autoUpdate` defaults to `false` for third-party marketplaces. |
| `enableAllProjectMcpServers` | Any file (ignored from the shared project file until the folder is trusted) | Boolean | unset (asks per server) | "Approve every MCP server defined in project `.mcp.json` files without a prompt." Normally written to `.claude/settings.local.json` by the approval dialog. |
| `enabledMcpjsonServers` | Any file (same trust limit) | array of server names from `.mcp.json` | unset | Approves specific `.mcp.json` servers. |
| `disabledMcpjsonServers` | Any file | array of server names | unset | Rejects servers; "A rejection in any settings file applies, including a project `.claude/settings.json`". Beats the two keys above. |
| `allowedMcpServers` | Any file; entries merge | array of single-key objects: `serverName`, `serverCommand` (array, exact match) or `serverUrl` (pattern with `*`) | unset (all allowed); empty array blocks every user-added server | Allowlist; built-in servers exempt. "Deploy it in managed settings to enforce it." |
| `deniedMcpServers` | Any file; entries merge | same object shapes | unset | Denylist; wins over the allowlist. |
| `disableClaudeAiConnectors` | Any file; `true` from any file applies | Boolean | `false` | "a checked-in project `.claude/settings.json` can opt a repository out of those connectors". |
| `skillOverrides` | Any file | object: skill name to `"on"`, `"name-only"`, `"user-invocable-only"`, `"off"` | unset (all `"on"`) | Hide or collapse a skill without editing `SKILL.md`. Does not apply to plugin skills. `/skills` writes to `.claude/settings.local.json`. |
| `disableBundledSkills` | Any file | Boolean | unset | Removes bundled skills and workflows; hides built-in commands such as `/init` from the model. |
| `disableSkillShellExecution` | Any file | Boolean | unset | Replaces inline `` !`...` `` shell in skills and custom commands with `[shell command execution disabled by policy]`. |
| `skillListingBudgetFraction` | Any file | number, greater than `0`, at most `1` | `0.01` | Share of the context window reserved for the skill listing. |
| `skillListingMaxDescChars` | Any file | positive integer | `1536` | Per-skill description cap in the listing. |

### 2.5 Git, attribution, memory, context, retention

| Key | Scope | Type / allowed values | Default | Documented description and notes |
| :- | :- | :- | :- | :- |
| `attribution` | Any file | object with `commit` (string), `pr` (string), `sessionUrl` (Boolean), or `false` to hide all (v2.1.281+) | unset | Earlier versions reject `false` and skip the whole settings file; the portable form is empty strings plus `sessionUrl: false`. "your own instructions about attribution, such as a CLAUDE.md or memory rule, take precedence over these commit and PR lines", unless the line is set in managed settings. |
| `attribution.commit` | Any file | string; `""` hides | `Co-Authored-By: <name> <noreply@anthropic.com>` where name is the model in use | Commit trailer text. |
| `attribution.pr` | Any file | string; `""` hides | `🤖 Generated with [Claude Code](https://claude.com/claude-code)` | PR description text. |
| `attribution.sessionUrl` | Any file | Boolean | `true` | `Claude-Session` trailer/link from cloud or Remote Control sessions. |
| `includeCoAuthoredBy` | Any file | Boolean | `true` | Deprecated since v2.0.62; ignored once `attribution.commit` or `attribution.pr` is set. |
| `includeGitInstructions` | Any file | Boolean | `true` | `false` removes the built-in commit/PR instructions and the git status snapshot, "for example when you use your own git workflow skills". |
| `prUrlTemplate` | Any file | string with `{host}`, `{owner}`, `{repo}`, `{number}`, `{url}` | unset | Rewrites rendered PR links. |
| `autoMemoryEnabled` | Any file | Boolean | `true` | `false`: Claude does not read or write the auto memory directory. `CLAUDE_CODE_DISABLE_AUTO_MEMORY` overrides in either direction. |
| `autoMemoryDirectory` | Any file (trust-gated from project/local) | string, absolute or `~/`-prefixed path | unset (`~/.claude/projects/<project>/memory/`) | Custom auto memory location. Note: type is absolute or `~/` only; no project-relative form is documented. |
| `plansDirectory` | Any file | string, path relative to the project root | unset (`~/.claude/plans`) | Where plan mode writes plan files. Falls back to `~/.claude/plans` if the path resolves outside the project root or contains a backslash. Example `"./plans"`. |
| `claudeMdExcludes` | Any file | array of globs or absolute paths (matched against absolute paths) | unset | Skip specific `CLAUDE.md` files. |
| `autoCompactEnabled` | Any file | Boolean | `true` | Automatic compaction. |
| `autoCompactWindow` | Any file | number of tokens, `100000` to `1000000` | unset | How full the context gets before auto-compaction. |
| `idleCompaction` | Any file | Boolean | `true` | Compacts a long idle conversation (v2.1.290+). |
| `bashOutputMaxChars` | Any file | positive integer, clamped `4000` to `128000` | unset (30,000) | Inline Bash output limit (v2.1.261+). |
| `fileCheckpointingEnabled` | Any file | Boolean | `true` | File snapshots for `/rewind`; ignored in `-p` and SDK runs. |
| `cleanupPeriodDays` | Any file | number of days, whole number, minimum `1` | `30` | "Set how many days Claude Code keeps session transcripts and other application data before deleting them." "Setting `0` fails validation, so pick a large value such as `3650` for long retention." Sessions older than this vanish from `/resume`. Inference: in a project file this overrides each clone's user value for sessions in that project, since project beats user. |
| `autoUpdatesChannel` | Any file | `"latest"` or `"stable"` | unset (`"latest"`) | `"stable"` is "typically about one week old and skips releases with major regressions". Homebrew installs ignore it. To turn auto-updates off, set `DISABLE_AUTOUPDATER` in `env`. |
| `minimumVersion` | Any file | version string such as `"2.1.100"` | unset | Keeps updates from installing anything lower; "only constrains updates" (startup refusal is the managed-only `requiredMinimumVersion`). |
| `feedbackSurveyRate` | Any file | number `0` to `1` | unset | `0` stops the session quality survey. |
| `skipWebFetchPreflight` | Any file | Boolean | unset | Skips the WebFetch hostname check sent to `api.anthropic.com`. |
| `apiKeyHelper` | Any file | string, shell command line | unset | From project or local settings in interactive sessions, "Claude Code doesn't run it until you accept the workspace trust prompt". |
| telemetry switches | `env` only | `DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | | "The switches that turn off usage metrics and error reports are environment variables, not settings keys" (REF, "Privacy and telemetry"). |
| `showClearContextOnPlanAccept` | Any file | Boolean | `false` | Adds "Yes, clear context and …" to the plan approval menu. |

### 2.6 Worktrees, agents, workflows

| Key | Scope | Type / allowed values | Default | Documented description and notes |
| :- | :- | :- | :- | :- |
| `worktree` | Any file | object with `baseRef`, `symlinkDirectories`, `sparsePaths`, `bgIsolation` | unset | Applies to `--worktree`, the `EnterWorktree` tool, isolated subagents and background sessions. Gitignored files such as `.env` are copied with a `.worktreeinclude` file, not a setting. |
| `worktree.baseRef` | Any file | `"fresh"` (from `origin/<default-branch>`) or `"head"` (local `HEAD`) | `"fresh"` | |
| `worktree.symlinkDirectories` | Any file | array of repo-relative directory paths | unset | Example `["node_modules", ".cache"]`. |
| `worktree.sparsePaths` | Any file | array of repo-relative directory paths | unset | Sparse checkout; "Include `.claude` in the list so that each worktree also has the repository's `.claude/settings.json` and `.claude/rules/`." |
| `worktree.bgIsolation` | Any file | `"worktree"` or `"none"` | `"worktree"` | With `"worktree"`, background sessions cannot `Edit`/`Write` in the main checkout until they call `EnterWorktree`. |
| `worktree.location` | User only | string | unset | Desktop SSH sessions only. |
| `agent` | Any file | string, name of a built-in or custom agent | unset | Runs the main thread as that subagent (prompt, tools, model). |
| `disableAgentView` | Any file | Boolean | unset | Turns off `claude agents`, `--bg`, `/background`. |
| `teammateMode` | Any file | `"in-process"`, `"auto"`, `"tmux"`, `"iterm2"` | `"in-process"` | Agent-team display. |
| `enableWorkflows` / `disableWorkflows` | Any file | Boolean | unset / `false` | Dynamic workflows on/off; default on except on the Pro plan. |
| `workflowSizeGuideline` | Any file | `"unrestricted"`, `"small"` (<5 agents), `"medium"` (<10), `"large"` (<50) | `"medium"` (`"small"` on Pro, v2.1.271+) | Advice to Claude, "not an enforced cap". |
| `workflowKeywordTriggerEnabled` | Any file | Boolean | `true` | Whether typing `ultracode` triggers a workflow. |
| `crossSessionInbound` | Any file (project value only if stricter) | `"accept"`, `"hold"`, `"refuse"` | unset | Messages from your other sessions. |
| `isolatePeerMachines` | Any file; `true` from any scope | Boolean | unset | Approval before `SendMessage` reaches a session on another machine. |
| `disableRemoteControl` | Any file | Boolean | `false` | Turns off Remote Control. |
| `remoteControlAtStartup` | Any file (project `true` ignored) | Boolean | unset | A repository "can turn auto-connect off for its checkout but can't turn it on". |
| `enableArtifact` | Any file; `false` from any file | Boolean | unset | `false` turns the Artifact tool off; nothing turns it back on. Replaces deprecated `disableArtifact`. |

### 2.7 Interface keys that are honoured from a project file (set only if project-relevant)

`spinnerTipsEnabled` (Boolean, default `true`), `spinnerTipsOverride` (object; from project and
local settings "it reads plain string tips only", and they always use the `Tip` label),
`spinnerVerbs` (`{ mode: "append" | "replace", verbs: [...] }`), `tui` (`"default"` or
`"fullscreen"`, unset by default), `theme`, `editorMode` (`"normal"`/`"vim"`), `viewMode`
(`"default"`, `"verbose"`, `"focus"`), `verbose`, `companyAnnouncements` (array of strings shown at
startup), `respectGitignore` (Boolean, default `true`), `defaultShell` (`"bash"`/`"powershell"`),
`timeFormat`, `timeZone`, `maxProseWidth` (minimum `40`), `prefersReducedMotion`,
`promptSuggestionEnabled`, `terminalProgressBarEnabled`, `showTurnDuration`,
`syntaxHighlightingDisabled`, `preferredNotifChannel` (`"auto"`, `"terminal_bell"`, `"iterm2"`,
`"iterm2_with_bell"`, `"kitty"`, `"ghostty"`, `"notifications_disabled"`), `awaySummaryEnabled`.
All `Any file` (REF, "Interface and terminal", "Remote, desktop, and notifications").
Inference: because project beats user in precedence (SET, "Team settings override personal
settings"), putting personal-taste keys such as `theme` or `editorMode` in a synced project file
would override every clone's user preference; the docs' own scope table says user settings are for
"Personal preferences: theme, editor mode".

## 3. Permission rule syntax

All from PERM (docs-en-permissions-md) unless marked.

### 3.1 Shape, evaluation order, enforcement

- Format: "`Tool` or `Tool(specifier)`. Parentheses inside the specifier are literal" (PERM,
  "Permission rule syntax").
- Order: "Rules are evaluated in order: deny, then ask, then allow." The first match decides,
  "and rule specificity doesn't change the order." (PERM, "Manage
  permissions"). "An allow rule can't carve an exception out of a deny rule"; a matching ask rule
  prompts even when a more specific allow rule also matches.
- Across scopes: "If a tool is denied at any level, no other level can allow it"; "a user-level
  deny blocks a project-level allow" and the reverse (PERM, "Settings precedence").
- Bare deny (`Bash`, or `Bash(*)`) "removes the tool from Claude's context entirely"; a scoped deny
  such as `Bash(rm *)` leaves the tool and blocks matching calls (PERM, "Manage permissions").
- "Permission rules are enforced by Claude Code, not by the model." Prompt or `CLAUDE.md`
  instructions do not change what is allowed (PERM, "Manage permissions", note).
- Rules must use canonical tool names (for example `TaskStop`, not the label `Stop Task`); a deny
  or ask rule naming no known tool produces a startup warning (PERM, "Match all uses of a tool",
  "Tool name wildcards").
- "Yes, and don't ask again" saves Bash and WebFetch approvals as allow rules in
  `.claude/settings.local.json` at the git repository root; file-modification approvals last
  "Until session end" (PERM, "Permission system").
- Default approval table (Manual mode): read-only tools need no approval inside working
  directories; Bash needs approval except built-in read-only commands; file modification needs
  approval; WebFetch needs approval except preapproved documentation domains; WebSearch needs
  approval (PERM, "Permission system").

### 3.2 Tool-name position

- Deny and ask rules accept globs in the tool-name position; the pattern must match the full name:
  `"*"` matches every tool, `"mcp__*"` every MCP tool (PERM, "Tool name wildcards").
- Allow rules accept tool-name globs "only after a literal `mcp__<server>__` prefix". "An
  unanchored allow glob such as `\"*\"`, `\"B*\"`, or `\"mcp__*\"` is skipped and doesn't auto-approve
  anything."
- `EndConversation` cannot be removed by a deny rule while any other tool remains.

### 3.3 Match by input parameter (deny and ask only)

PERM, "Match by input parameter": `Tool(param:value)` matches a top-level scalar input parameter
on any built-in tool. Examples from the docs: `Agent(model:opus)`, `Agent(isolation:worktree)`,
`Bash(run_in_background:true)`. One parameter per rule; `*` wildcard allowed in the value; an
omitted parameter never matches; the value is compared to the literal input (`Agent(model:opus)`
matches the alias, not a full model ID). Not allowed on the primary content field (`command`,
`file_path`, `path`, `notebook_path`, `url`): `Bash(command:rm *)` is ignored with a startup
warning. In a settings file, any `mcp__` rule that has parentheses is skipped (MCP parameter
rules only via `--disallowedTools`). `Skill(skill:<name>)` as a deny rule matches the skill under
any of its names.

### 3.4 Bash rules

Wildcards (PERM, "Wildcard patterns"):

- "A `*` in a Bash rule matches any text, including spaces". A rule with no `*` matches one exact
  command.
- "Put the `*` after the subcommand." `Bash(git log *)` allows only `git log`; `Bash(git *)`
  allows every git command. A startup warning flags an allow rule with `*` before the subcommand,
  such as `Bash(git * main)` (which also matches `git -c core.fsmonitor=<script> diff main`).
- Trailing ` *` (space then star) as the only wildcard also matches the bare command: `Bash(ls *)`
  matches `ls` and `ls -la` but not `lsof`; `Bash(ls*)` matches `lsof` too.
- `:*` suffix is equivalent to a trailing ` *` and is recognised only at the end of the pattern.
- Docs table: `Bash(npm run build)` does not match `npm run build --watch`; `Bash(* --version)`
  matches any program including `bash -c 'echo hi' --version`.

Compound commands (PERM, "Compound commands"):

- Recognised separators: `&&`, `||`, `;`, `|`, `|&`, `&`, and newlines. "Every subcommand must be
  allowed for a compound command to run without a prompt".
- Deny and ask rules apply when any subcommand matches, "including a command nested inside a
  subshell, a command substitution, or a control-flow body such as a `for` loop", even in auto
  mode.
- A dangling `&&` or `||` makes the command unparseable; no allow rule approves it.
- Up to 5 rules are saved when approving a compound command.

Wrappers (PERM, "Wrappers"): stripped before matching: `timeout`, `time`, `nice`, `nohup`,
`stdbuf`, `command`, `builtin`, zsh `noglob`, and bare `xargs` (no flags). Leading assignments of
"certain known-safe environment variables" are stripped for allow rules; deny and ask rules match
past any leading assignment. Not stripped: `direnv exec`, `devbox run`, `mise exec`, `npx`,
`docker exec`; "a rule like `Bash(devbox run *)` matches whatever comes after `run`". The list
"is built in and is not configurable".

Exec wrappers and `find` (PERM, "Exec wrappers and `find` actions"): a prefix rule cannot
auto-approve `watch`, `setsid`, `ionice`, `flock`, or `find` with `-exec`, `-delete`, `-rm`,
`-fprint`, `-files0-from`. Use an exact-match rule (no `*` in the command) or a PreToolUse hook
returning `"allow"`.

Limits (PERM, "What a Bash rule doesn't match"): a Bash rule matches the command text Claude
writes; "a deny or ask rule covers the invocation Claude usually produces and isn't a security
boundary around the program".

| Rule | Stops | Doesn't stop |
| :- | :- | :- |
| `Bash(curl *)` | `curl https://example.com` | `/usr/bin/curl ...`, `sh -c 'curl ...'` |
| `Bash(rm *)` | `rm -rf build/` | `/bin/rm -rf build/`, `bash -c 'rm -rf build/'` |
| `Bash(git push *)` | `git push origin main` | `git -C . push origin main`, `git -c push.default=current push origin main` |

"Bash permission patterns that try to constrain command arguments are fragile" (PERM, "Read-only
commands", warning): `Bash(curl http://github.com/ *)` misses options before the URL, another
protocol, redirects and variables. Recommended instead: deny `curl`/`wget` and use
`WebFetch(domain:...)`, paired with the sandbox network allowlist; or a PreToolUse hook.
"If Bash is allowed, Claude can still use `curl`, `wget`, or other tools to reach any URL."

Read-only commands (PERM, "Read-only commands"): a built-in, non-configurable set runs without a
prompt in every mode: "`ls`, `cat`, `echo`, `pwd`, `head`, `tail`, `grep`, `find`, `wc`, `which`,
`diff`, `stat`, `du`, `cd`, and read-only forms of `git`". Add an `ask` or `deny` rule to force a
prompt. They still prompt for: unquoted globs with write-capable commands (`find`, `sort`, `sed`,
`git`); `docker` with `-H`/`--context`; `ps` forms that print environments; writes to special
shell variables such as `PATH` or `IFS`; unparseable commands; commands over 10,000 characters;
`cd` into a different directory combined with `git`; `cd` with a redirect.

Redirections (PERM, "Redirections"): output targets (`>`, `>>`, `2>`) are checked against `Edit`
allow and deny rules, protected paths and working directories; input targets (`<`) against `Read`
rules (v2.1.257+); `tee` targets likewise (v2.1.269+). "A rule such as `Bash(git commit *)` allows
the command, not the target." `/dev/null`, `2>&1`, here-docs are not checked.

### 3.5 Read and Edit path rules

- Syntax is gitignore-style with four anchors (PERM, "How path patterns match"):

| Pattern | Meaning | Docs example |
| :- | :- | :- |
| `//path` | Absolute path from filesystem root | `Read(//Users/alice/secrets/**)` |
| `~/path` | Path from home directory | `Read(~/Documents/*.pdf)` |
| `/path` | Path relative to the settings source | `Edit(/src/**/*.ts)` = `<primary working directory>/src/**/*.ts` in project settings |
| `path` or `./path` | Path relative to current directory | `Read(*.env)` = `<cwd>/*.env` |

- "A pattern like `/Users/alice/file` isn't an absolute path." (PERM, same section, warning).
- `/path` anchor per source (PERM, "Where a pattern anchors"): project and local settings anchor
  at `<primary working directory>/path`; user settings at `~/.claude/path`; a `--settings` file at
  `<directory of file>/path`; CLI flags and session rules at the primary working directory.
- Depth (PERM, "How deep a pattern matches"): bare filenames match at any depth, "so `Read(.env)`
  and `Read(**/.env)` are equivalent". A single-directory relative pattern such as `src/**` is
  anchored for allow rules (only `<cwd>/src`) but matches at any depth for deny and ask rules.
  `/src/**` and `src/components/**` match only at the anchored location in every rule type;
  `**/src/**` matches at any depth. `*` matches within one path segment, `**` across directories.
- Coverage (PERM, "What `Read` and `Edit` rules cover"): `Edit` rules apply to all built-in tools
  that edit files. `Read(path)` deny rules apply best-effort to Grep, Glob, `@file` mentions,
  pasted image paths, directory listings and IDE context. "A `Read` deny rule also blocks the Edit
  and Write tools on the same path, including creating a new file there." NotebookEdit is not
  covered: "add an `Edit` deny rule for paths no tool may change."
- `Write(path)`, `NotebookEdit(path)`, `MultiEdit(path)`, `Glob(path)`, `Grep(path)` rules with a
  path "don't match"; use `Edit(...)` or `Read(...)` instead (PERM, "`Write(path)`, `Glob(path)`,
  and `Grep(path)` rules don't match").
- Limits (PERM, "What `Read` and `Edit` rules cover", warning): deny rules cover the file tools,
  recognised Bash file commands (`cat`, `head`, `tail`, `sed`, `tee`) and redirection targets; they
  "don't apply to a command that reads files without naming them, such as `grep -r pattern .`" or
  to scripts that open files themselves. "For OS-level enforcement ... enable the sandbox."
- `.claudeignore` "has no effect, so move its entries into `Read` deny rules" (PERM, "Read and
  Edit").
- `!` negation (PERM, "Special characters and `!` negation"): in deny or ask lists, a pattern
  starting with `!` carves matching paths out of the relative rules listed before it in the same
  source (`Read(*.env)` then `Read(!sample.env)`). It cannot cancel a rule from another settings
  file, cannot reach `/`, `~/` or `//` anchored rules, and cannot reopen a file inside a directory
  blocked as a whole.
- Symlinks (PERM, "Symlinks"): allow rules apply only when both the requested path and its target
  match; deny rules apply when either matches. Edit and Write refuse a path that is itself a
  symlink.
- Network paths (`/net/...` on Linux, UNC on Windows) always get their own prompt (v2.1.292+);
  allow rules and hooks do not skip it (PERM, "Network paths").

### 3.6 WebFetch, MCP, Agent, Skill, Cd

- WebFetch (PERM, "WebFetch"): `WebFetch(domain:example.com)` matches that hostname only;
  `WebFetch(domain:*.example.com)` matches subdomains at any depth but not the apex;
  `WebFetch(domain:*)` matches every domain. Case-insensitive; trailing dot stripped. A wildcard
  elsewhere matches only text between two dots. Wildcards need v2.1.172+.
- Bare `WebFetch` versus `WebFetch(domain:*)` (PERM, "Allow or deny every fetch"): both cover
  every URL, but "only the `domain:` form also adds its domain to the sandbox's allowed or denied
  domain list". Bare `WebFetch` in deny removes the tool. "To let Claude fetch freely while keeping
  the sandbox allowlist as it is, use the bare form."
- MCP (PERM, "MCP"): `mcp__<server>` or `mcp__<server>__*` for all tools of a server;
  `mcp__<server>__<tool>` for one. Allow rules for MCP tools must have no specifier ("the rule
  doesn't match any call" otherwise). Characters such as `.` or spaces in a server name become
  `_`. Plugin servers: `mcp__plugin_<plugin>_<server>__*`. For a server name containing `__`, use
  the wildcard form with the whole name.
- Agent (PERM, "Agent (subagents)"): `Agent(Explore)`, `Agent(Plan)`, `Agent(my-custom-agent)`,
  normally in `deny` to disable a subagent.
- Skill: the page documents only the deny form `Skill(skill:<name>)` (PERM, "Match by input
  parameter"); fuller Skill rule syntax lives on the skills page, which was not in scope.
- Cd (PERM, "Cd"): `Cd` rules govern only the user-typed `/cd` command. A bare `Cd` deny disables
  it; any `Cd` allow rule switches `/cd` to allowlist mode. `*` matches exactly one path segment,
  `**` across segments.
- PowerShell rules use the Bash shape; aliases are canonicalised and matching is case-insensitive
  (PERM, "PowerShell").

### 3.7 Hooks versus rules

PERM, "Precedence among rules, hooks, and mods": "PreToolUse hook decisions don't bypass
permission rules": a matching deny rule blocks and a matching ask rule prompts even if the hook
returned `"allow"`. "A hook that exits with code 2 stops the tool call before permission rules
are evaluated", so the block holds even when an allow rule would let the call proceed.
Documented pattern: "add `\"Bash\"` to your allow list and register a PreToolUse hook that rejects
those specific commands". In plan mode a hook's `"allow"` has no effect on non-read-only calls
(PERM, "Hook approvals in plan mode").

Caveat for a solo developer (same section): without managed settings, a `managed-mcp.json` file
or a Team/Enterprise `/login`, an installed mod handling `tool.check` "can approve a call that a
deny rule refuses or a `PreToolUse` hook blocked".

### 3.8 Working directories

PERM, "Working directories": the launch directory is the primary working directory; extend with
`--add-dir`, `/add-dir` or `permissions.additionalDirectories`. Directories in the settings key
"grant file access only and don't load any of the configuration" (skills, commands, subagents
load only from `--add-dir`/`/add-dir` directories). "Hooks and other `.claude/settings.json` keys
load from the current working directory's `.claude/` folder with no parent-directory fallback"
(PERM, "Where output styles, hooks, and local settings load from"), so a monorepo package
started from a subdirectory does not read the root `.claude/settings.json`.

### 3.9 Tool names and which rule format each takes

From TOOLS (docs-en-tools-reference-md). "The tool names are the exact strings you use in
permission rules, subagent tool lists, and hook matchers." (TOOLS, intro).

Built-in tools and whether Manual mode prompts (TOOLS, tools table; "Yes" = permission required):

- Yes: `Artifact`, `Bash`, `Edit`, `EnterWorktree`, `ExitPlanMode`, `Monitor`, `NotebookEdit`,
  `PowerShell`, `ShareOnboardingGuide`, `Skill`, `WebFetch`, `WebSearch`, `Workflow`, `Write`.
- No: `Agent`, `AskUserQuestion`, `CronCreate`, `CronDelete`, `CronList`, `EndConversation`,
  `EnterPlanMode`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `ListMcpResourcesTool`, `LSP`,
  `PushNotification`, `Read`, `ReadMcpResourceTool`, `RemoteTrigger`, `ReportFindings`,
  `ScheduleWakeup`, `SendFeedback`, `SendMessage`, `SendUserFile`, `SubagentHandback`,
  `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `TodoWrite`, `ToolSearch`,
  `WaitForMcpServers`. `TaskOutput` was removed in v2.1.277.

Rule formats (TOOLS, "Configure tools with permission rules and hooks"):

| Rule format | Applies to |
| :- | :- |
| `Bash(npm run *)` | Bash, Monitor |
| `PowerShell(Get-ChildItem *)` | PowerShell |
| `Read(~/secrets/**)` | Read, Grep, Glob, LSP |
| `Edit(/src/**)` | Edit, Write, NotebookEdit |
| `Skill(deploy *)` | Skill |
| `Agent(Explore)` | Agent |
| `WebFetch(domain:example.com)` | WebFetch |
| `WebSearch` | WebSearch (no specifier) |

- "Tools not listed here, such as `ExitPlanMode` or `ShareOnboardingGuide`, accept only the bare
  tool name with no specifier."
- "An `Edit(...)` allow rule also grants read access to the same path, so you don't need a
  matching `Read(...)` rule."
- "Hook `matcher` fields use bare tool names, not the parenthesized rule format." A hook's `if`
  condition does accept the rule format.
- The same formats are used in `--allowedTools`, `--disallowedTools`, the SDK options and a
  skill's `allowed-tools` frontmatter.

Linux-specific facts that change how rules and hooks behave:

- "On macOS, Linux, and WSL, Claude Code leaves Glob and Grep out of the default tool set";
  Claude searches with `find` and `grep` through Bash instead (embedded `bfs` and `ugrep`), "and
  the searches reach your hooks and permission rules as `Bash` calls." (TOOLS, "Glob tool
  behavior"). "An allow rule in a settings
  file doesn't" bring the tools back; a Bash deny rule, `--disallowedTools Bash`, or naming them
  in `--tools`/`--allowedTools` does. Inference: on Ubuntu a `PreToolUse` hook with matcher
  `Grep|Glob` will rarely fire, and `Read(...)` deny rules protect searches only to the extent
  that Bash file-command recognition and the sandbox cover them (see 3.5 limits).
- Monitor "uses the same permission rules as Bash"; a bare `Bash` deny rule removes Monitor too
  (TOOLS, "Monitor tool", "Bash rules that deny or prompt for WebSocket watches").
- WebFetch: "refuses `localhost` and any other hostname without a dot"; a built-in set of
  preapproved documentation domains fetches without a prompt; an explicit `WebFetch(domain:...)`
  rule "takes precedence over the preapproved set"; "Sandboxed commands don't inherit WebFetch's
  built-in set of preapproved documentation domains" and "WebFetch never reads the sandbox
  allowlist in return" (TOOLS, "WebFetch tool behavior"). `CLAUDE_CODE_DISABLE_WEB_FETCH=1` turns
  it off (v2.1.285+).
- WebSearch: "A bare `WebSearch` entry in `allow` or `deny` is the only form."; 200 calls per
  interactive session, refilling about 100 per hour (TOOLS, "Session search limit").
- Bash tool: default timeout two minutes (`BASH_DEFAULT_TIMEOUT_MS`), ceiling ten minutes
  (`BASH_MAX_TIMEOUT_MS`); a foreground command that hits its timeout is moved to the background
  rather than stopped; environment variables do not persist between commands; aliases and
  functions from `~/.zshrc` are captured at session start (TOOLS, "Bash tool behavior").
- `CLAUDE_CODE_TOOL_MEMORY_LIMIT` (for example `4G`) caps memory of Bash/PowerShell/Monitor
  commands on Linux via a cgroup (v2.1.233+) (TOOLS, "Memory limit on Linux and WSL").
- Task tools (`TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`, `TodoWrite`) are provided by
  default "only on Opus 4.7, Sonnet 4.6, Haiku 4.5, and earlier models"; opt in on newer models
  with `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` (TOOLS, "Task tool availability"). Inference: this
  variable is a feature toggle, so it is a candidate for a project `env` block, but the page
  describes exporting it in the shell or passing it via `--settings`; whether Claude Code
  classifies it as a "safe" `env` variable is not stated.

## 4. Permission modes

From MODES (docs-en-permission-modes-md) and AUTO (docs-en-auto-mode-config-md).

### 4.1 The modes

MODES, "Available modes":

| Mode (config value) | What runs without asking | Docs' "Best for" |
| :- | :- | :- |
| `default` (labelled Manual; alias `manual`) | Reads only | Reviewing every action yourself, sensitive work |
| `acceptEdits` | Reads, file edits, and common filesystem commands | Iterating on code you're reviewing |
| `plan` | Reads, plus classifier-approved commands when auto mode is available | Exploring a codebase before changing it |
| `auto` | Everything, with background safety checks | Long tasks, reducing prompt fatigue |
| `dontAsk` | File reads inside working directories and pre-approved tools; anything that would prompt is denied | Locked-down CI and scripts |
| `bypassPermissions` | Everything | Isolated containers and VMs only |

- "Deny rules block in every mode, including `bypassPermissions`." "Allow rules have no effect in
  `bypassPermissions`." (MODES, "Available modes").
- `acceptEdits` also auto-approves "`mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, and `sed`" on
  paths inside the working directory or `additionalDirectories`; all other Bash commands outside
  the read-only set still prompt (MODES, "Auto-approve file edits with acceptEdits mode").
- `plan`: no source edits until a plan is approved. With auto mode available and
  `useAutoModeDuringPlan` on (default), the classifier reviews shell commands; otherwise commands
  outside the read-only set prompt, "including when the sandbox's auto-allow mode is enabled"
  (MODES, "Analyze before you edit with plan mode").
- `dontAsk`: never waits for input; denies `ask`-rule matches and `AskUserQuestion`; allow rules
  and PreToolUse hook approvals still run. Never in the `Shift+Tab` cycle; set with
  `--permission-mode dontAsk` (MODES, "Allow only pre-approved tools with dontAsk mode").
- `bypassPermissions`: "offers no protection against prompt injection or unintended actions".
  Cannot be entered from a session started without it. Refused as root or under `sudo` on Linux
  and macOS, and refused under `--restricted` (MODES, "Skip all checks with bypassPermissions
  mode").
- Never auto-approved in any mode (MODES, "Actions no mode auto-approves"): explicit ask rules;
  `AskUserQuestion` and MCP tools marked `requiresUserInteraction`; recognised `rm`/`rmdir`
  critical-path removals; cross-session messaging safeguards; reads/writes outside working
  directories while the two `block...OutsideWorkingDirectories` keys are on.

### 4.2 Which mode a session starts in, and what a project file can set

MODES, "Which mode a session starts in": first of (1) `--permission-mode` or
`--dangerously-skip-permissions`, (2) `permissions.defaultMode` in a settings file, (3) the
built-in default.

- `"auto"` in `.claude/settings.json` or `.claude/settings.local.json` "doesn't take effect, and
  Claude Code then uses the built-in default rather than a `defaultMode` from
  `~/.claude/settings.json`". `"bypassPermissions"` in those two files "doesn't take effect
  either, and the session starts in Manual mode. The other values apply from any settings file."
- So a project `.claude/settings.json` can set `default`, `acceptEdits`, `plan`, `dontAsk` (and
  `manual`); it cannot set `auto` or `bypassPermissions`. Terminal sessions honour the project
  value; "sessions the VS Code extension starts don't read project settings for the starting
  permission mode" (MODES, "Start in a different permission mode"). The Desktop app reads the
  same files but a mode picked in its selector "outranks a `defaultMode` in the project's
  `.claude/` settings" (MODES, "Switch permission modes", Desktop tab). Cloud sessions ignore
  `dontAsk` and `bypassPermissions` from settings.
- Built-in default (MODES, same section, table): `default` if any settings file sets
  `disableAutoMode` to `"disable"`; `default` for `claude -p` and the Agent SDK; otherwise `auto`
  in a terminal or the VS Code extension "with Claude Code v2.1.283 or later". If auto is selected
  but unavailable, the session starts in Manual.
- A project value outranks the user's: "a project or managed value outranks
  `~/.claude/settings.json`" (MODES, "Start in a different permission mode").
- Inference: with 2.1.322 installed, an interactive terminal session in a repo whose project file
  sets no `defaultMode` (and no user settings exist) starts in `auto`. A template that wants
  Manual, `acceptEdits` or `plan` as the terminal default can set it in the project file; a
  template that wants to forbid auto can set `disableAutoMode: "disable"` (scope `Any file`).
- `claude -p` and SDK runs with no mode set start in Manual (v2.1.302+); "Calls needing approval
  are denied unless you approve them with an allow rule, hook, `canUseTool` callback, or
  `--permission-prompt-tool`" (MODES, "Tool calls denied in `claude -p` and Agent SDK runs").
- `Shift+Tab` cycle: from `auto` to `default`, then `acceptEdits`, `plan`; optional modes slot in
  after `plan` (MODES, "Switch permission modes", CLI tab).

### 4.3 Auto mode

How it works:

- "A separate classifier model reviews actions before they run", blocking anything that
  "escalates beyond your request, targets unrecognized infrastructure, or appears driven by
  hostile content Claude read." (MODES, "Eliminate permission prompts with auto mode").
- Warning: "Auto mode reduces permission prompts but does not guarantee safety."
- Availability: all plans; models on the Anthropic API: "Claude Opus 4.6 or later, Sonnet 4.6 or
  later, Haiku 5.5, or a Fable model"; unavailable when any settings file sets `disableAutoMode`
  (MODES, same section).
- Decision order (MODES, "How the classifier evaluates actions"): (1) allow, ask and deny rules
  resolve first, with exceptions (protected-path writes still go to the classifier;
  critical-path removals are never allow-listed; content-scoped ask rules such as
  `Bash(git push *)` fall back to a prompt; commands carrying per-command allowed domains go to
  the classifier even when an allow rule matches); (2) read-only actions and file edits in the
  working directory are auto-approved, except protected paths; (3) everything else goes to the
  classifier; (4) on a block Claude receives the reason, usually the matched rule name such as
  `[Data Exfiltration]`.
- "On entering auto mode, broad allow rules that grant arbitrary code execution are dropped":
  blanket `Bash(*)`/`PowerShell(*)`, wildcarded interpreters like `Bash(python*)`,
  package-manager run commands, `Agent` allow rules, `Monitor` allow rules. "Narrow rules like
  `Bash(npm test)` stay in effect." They are restored on leaving auto mode. Note: REF,
  "`autoMode.classifyAllShell`" gives `Bash(python *)` as the interpreter example.
- The classifier "sees user messages, tool calls other than read-only lookups such as file reads
  and searches, and your CLAUDE.md content." Tool results are stripped, "so hostile content in a
  file or web page can't manipulate the classifier directly." A separate
  server-side probe scans incoming tool results.
- Subagents: task description checked at spawn, each action checked, final report reviewed;
  frontmatter `permissionMode` is ignored (MODES, "How auto mode handles subagents").

What it blocks by default (MODES, "What the classifier blocks by default"; the list is long, the
items most relevant to a solo full-stack developer are): downloading and executing code like
`curl | bash`; sending sensitive data to external endpoints; production deploys and migrations;
force push; `git reset --hard`, `git checkout -- .`, `git restore .`, `git clean -fd`,
`git stash drop`, `git stash clear`; `git commit --amend` on a commit not created in the session
or already pushed; `terraform destroy` and similar; irreversibly destroying files that existed
before the session; printing a live credential into the transcript or a file; flags that disarm
a safety guard like `--insecure`; launching an agent loop with `--dangerously-skip-permissions`;
commenting out or force-passing a test that guards security behaviour; changing remotes with
`git remote set-url`/`add` unless named; opening a PR against a different repository or forking
unless named; wildcard deletes in `/tmp`; writing to session transcripts under
`~/.claude/projects/`; cloud metadata endpoint credential requests (v2.1.257+).

Allowed by default (same section): local file operations in the working directory; installing
dependencies declared in lock files or manifests; "Reading `.env` and sending credentials to
their matching API"; read-only HTTP requests; "Pushing to any branch of the repository you're
working in, including the default branch" (not branches named like `production` or `gh-pages`);
creating a matching pull request.

Trust boundary: "The classifier trusts your working directory and the remotes that were
configured for it when the session started" (MODES, same section). `claude auto-mode defaults`
prints the full rule lists as JSON.

Configuring it (AUTO):

- `autoMode` is read only from `~/.claude/settings.json`, managed settings, and the `--settings`
  flag or Agent SDK. "The classifier doesn't read `autoMode` from project settings in
  `.claude/settings.json` or `.claude/settings.local.json`." Reason given: "a checked-in repo or
  a build step could otherwise inject its own allow rules."
  (AUTO, "Where the classifier reads configuration").
- What a project CAN do: (a) CLAUDE.md: "The classifier reads the same CLAUDE.md content Claude
  itself loads", so a line like "never force push" there "steers both Claude and the classifier
  at the same time." (AUTO, same section); (b) `permissions.ask` and
  `permissions.deny` rules in the project file, which run before the classifier.
- Human checkpoint recipe (AUTO, "Add a human checkpoint"): `"ask": ["Bash(git push *)",
  "Bash(gh pr create *)"]`. Content-scoped ask rules "always force a permission prompt, even in
  auto mode". Limit: `git -C <dir> push` does not match; use a PreToolUse hook for full-text
  inspection.
- Boundary table (AUTO, "Add a human checkpoint"): `permissions.ask` always prompts;
  `permissions.deny` "Blocks before the classifier is consulted. Neither the classifier nor user
  intent can override it."; a boundary stated in conversation can be lost on compaction.
- `autoMode.environment`: prose entries (context, trust and sensitivity slots). Include the
  literal `"$defaults"` to keep the built-in entries. "Entries are prose, not regex or tool
  patterns." (AUTO, "Define trusted infrastructure").
- `autoMode.hard_deny`, `soft_deny`, `allow`: prose rule lists with four-tier precedence
  (hard_deny, then soft_deny, then allow exceptions, then explicit user intent). "Setting any of
  `environment`, `allow`, `soft_deny`, or `hard_deny` without `\"$defaults\"` replaces the entire
  default list for that section." (AUTO, "Override the block and allow rules").
- `autoMode.classifyAllShell: true` suspends every Bash and PowerShell allow rule in auto mode so
  the classifier sees every command; "trades latency for coverage" (AUTO, "Route all shell
  commands through the classifier").
- `/auto-mode-setup` drafts `environment` entries and writes them to `~/.claude/settings.json`
  (AUTO, "Generate environment entries with `/auto-mode-setup`").
- CLI: `claude auto-mode defaults`, `claude auto-mode config`, `claude auto-mode critique`,
  `claude auto-mode reset` (AUTO, "Inspect the defaults and your effective config").
- `/permissions` has an "Auto mode" tab (v2.1.246+) and a "Recently blocked" tab where `r`
  approves a retry (AUTO, "Review denials").

Costs (MODES, "Cost and latency"): "On Enterprise plans and on accounts that use the Claude API,
... classifier calls count toward your token usage." Each check adds a round-trip; reads and
working-directory edits skip the classifier, "so the overhead comes mainly from shell commands
and network operations". Default classifier model is Claude Sonnet 5; override with
`CLAUDE_CODE_AUTO_MODE_MODEL` (v2.1.302+) (MODES, "Default classifier model", "Choose the
classifier model"). With server-side review there are no separate classifier calls (MODES,
"Server-side classifier review"). Inference: the page does not state how classifier usage is
counted on Pro/Max subscriptions; it only says where it counts toward token usage.

Fallbacks (MODES, "When auto mode falls back"): "if the classifier blocks an action 3 times in a
row or 20 times total, auto mode pauses and Claude Code resumes prompting"; thresholds are not
configurable. In a `-p` run without `--permission-prompt-tool`, "the action doesn't run and
Claude keeps working". No verdict means the action is denied rather than run unreviewed.

Critical paths (MODES, "Critical paths"): `rm`/`rmdir` targeting the filesystem root, top-level
directories, the home directory, the working directory and its parents, and forms such as
`rm -rf "$DIR"/*`. No allow rule or hook approves them. In `auto` the terminal asks with a
two-minute countdown, elsewhere it denies. "The check can miss some commands, so it doesn't
replace an operating-system control such as sandboxing."

Protected paths (MODES, "Protected paths"): writes are never auto-approved except in
`bypassPermissions`: directories `.git`, `.config/git`, `.vscode`, `.idea`, `.husky`, `.cargo`,
`.devcontainer`, `.yarn`, `.mvn`, `.claude` (with exceptions such as `.claude/worktrees/`, the
session's plan files, auto memory Markdown); files including `.gitconfig`, `.gitmodules`, shell
rc files, `.envrc`, `.npmrc`, `.yarnrc.yml`, `.pnpmfile.cjs`, `bunfig.toml`,
`.pre-commit-config.yaml`, `lefthook.yml`, `.devcontainer.json`, `.mcp.json`, `.claude.json`.
"`permissions.allow` rules in settings files do not pre-approve protected-path writes", so
`Edit(.claude/**)` in a settings file changes nothing. In `default`/`acceptEdits` they prompt;
in `auto` they go to the classifier; in `dontAsk` they are denied.

### 4.4 What the docs recommend for unattended runs

MODES, "Common setups":

| Goal | Start with | Isolation needed |
| :- | :- | :- |
| Iterate locally with fewer prompts, without a classifier | Manual mode plus the Bash sandbox in auto-allow mode | The built-in Bash sandbox |
| Work hands-off in auto mode | `claude --permission-mode auto` | "None; a sandbox or container adds defense in depth" |
| Run in CI with an exact allowlist | `claude -p "run the test suite" --permission-mode dontAsk --allowedTools "Bash(npm test)" "Read"` | None beyond the CI runner |
| Run fully unattended inside a container | `claude -p "<prompt>" --dangerously-skip-permissions` | "Required: a container, VM, or the sandbox runtime"; non-root user |

- For a session nobody is watching: `permissions.denyInsteadOfPrompting: true` (user, managed or
  `--settings` only) with `defaultMode: "auto"` in `~/.claude/settings.json`, or
  `--permission-prompts none` with `-p` (REF, "`permissions.denyInsteadOfPrompting`"). Neither
  can come from the project file.
- "`bypassPermissions` offers no protection against prompt injection or unintended actions. For
  background safety checks with far fewer permission prompts, use auto mode instead." (MODES,
  "Skip all checks with bypassPermissions mode", warning).

## 5. Sandboxing (Linux focus)

From SBX (docs-en-sandboxing-md) and REF "Sandbox settings".

### 5.1 What it is and what it covers

- "The Bash sandbox is a boundary that the operating system enforces around the shell commands
  Claude runs on your machine." It applies to "Bash, PowerShell, and Monitor commands and the
  processes they start" (SBX, intro). Off by default; turn on with `/sandbox` or
  `sandbox.enabled: true`.
- Outside the sandbox (SBX, "What runs outside the sandbox"): built-in tools (Read, Edit, Write,
  WebFetch, WebSearch) follow permission rules instead ("A `denyRead` entry doesn't stop the Read
  tool, and `allowedDomains` doesn't limit WebFetch"); command hooks, local MCP servers, plugin
  monitors, LSP servers, the status line command and `apiKeyHelper` "run with your full access";
  mods; commands typed at the `!` prompt; `excludedCommands` matches; unsandboxed retries.
- Defaults (SBX, "What the sandbox restricts"): writes to the working directory, a per-user temp
  directory and added directories; reads of "Most of the machine, including credential files such
  as `~/.ssh` and `~/.aws/credentials`"; network has "No direct route out", via a local proxy
  whose allowed domains "start empty"; environment variables inherited, "including any secrets".
- Subagents use the parent session's sandbox configuration (SBX, "Scope").

### 5.2 Linux mechanics and dependencies

- Linux and WSL2 use bubblewrap; each command "runs in a separate network namespace that has no
  connection to your network" (SBX, "OS-level enforcement", "Network isolation").
- Install (SBX, "Set up Linux and WSL2"): `sudo apt-get install bubblewrap socat` on
  Ubuntu/Debian. `bubblewrap` enforces filesystem isolation; `socat` relays traffic to the proxy.
  Ripgrep is bundled. "The seccomp filter is optional and adds Unix domain socket blocking.
  Install it with `npm install -g @anthropic-ai/sandbox-runtime` if it is missing."
- "The dependency check runs at startup, so restart Claude Code after installing packages".
  `/sandbox` shows a Dependencies tab when something is missing.
- Ubuntu AppArmor: if the message "Ubuntu's AppArmor restriction on user namespaces stops
  bubblewrap here" appears (or `bwrap: setting up uid map: Permission denied`), either add an
  AppArmor profile at `/etc/apparmor.d/bwrap` for `/usr/bin/bwrap` with `flags=(unconfined)` and
  `userns,` then `sudo systemctl reload apparmor`, or run
  `sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0` (lasts until reboot) (SBX, "Add
  an AppArmor profile for bubblewrap", "Ubuntu's AppArmor restriction stops bubblewrap"). The
  startup check for this exists since v2.1.310.
- If the sandbox cannot start, "Claude Code runs commands without sandboxing" unless
  `sandbox.failIfUnavailable` is `true` (SBX, "Get started", warning).
- Verify (SBX, "Confirm commands run inside the sandbox"): ask Claude to run `touch
  ~/sandbox-probe` (fails with `Read-only file system` on Linux) and
  `curl --noproxy '*' https://example.com` (fails with `Could not resolve host`).
- Linux-specific behaviours: `allowUnixSockets` is ignored (use `allowAllUnixSockets`);
  `allowLocalBinding` has no effect because "a sandboxed command's `localhost` is private to that
  command", so a command cannot reach a dev server or database on the host's localhost without
  `excludedCommands` (SBX, "A command fails to reach a server on localhost"); `git` over SSH works
  once the host is allowed on port 22 (SBX, "`git` over SSH fails with the sandbox on");
  wildcards in `allowWrite`/`denyWrite` work only as a trailing `/**` (REF, "Where wildcards work
  in sandbox paths"); a 0-byte read-only placeholder can be left at `.claude` settings paths after
  a killed session, which makes "Yes, and don't ask again" fail to save; `claude doctor` lists
  them (SBX, "0-byte read-only files appear at `.claude` settings paths").

### 5.3 Modes and the retry escape hatch

- Auto-allow mode (`sandbox.autoAllowBashIfSandboxed`, default `true`): a command that runs in
  the sandbox is approved with no prompt. Still applies: Bash deny rules; critical-path removals;
  content-scoped ask rules such as `Bash(git push *)`; Monitor commands are not auto-approved.
  "A bare `Bash` ask rule ... is skipped for commands that run sandboxed" (SBX, "Auto-allow
  mode"). Commands such as `FOO=bar npm test`, `make CC=clang`, `eval "ls"` go through the regular
  flow (still sandboxed).
- "Even if you're not in \"accept edits\" mode, sandboxed Bash commands run automatically when
  auto-allow is enabled" (SBX, "Auto-allow mode", note). In plan mode auto-allow does not widen
  approvals.
- Regular permissions mode (`autoAllowBashIfSandboxed: false`): all Bash commands use the normal
  permission flow while sandboxed.
- Unsandboxed retry: Claude "may retry the command with the `dangerouslyDisableSandbox`
  parameter". In Manual and `acceptEdits` you get a prompt titled "Bash command (unsandboxed)";
  in auto mode the classifier evaluates it; in `dontAsk` it is denied; in `bypassPermissions` it
  runs. "An allow rule that matches a command also approves an unsandboxed retry of it". An ask
  rule `Bash(dangerouslyDisableSandbox:true)` forces a prompt on retries in every mode (SBX, "The
  unsandboxed retry escape hatch").
- Strict sandbox mode: `"allowUnsandboxedCommands": false` makes Claude Code ignore the
  parameter. A `false` in user settings holds against a project `true` (v2.1.285+). A project may
  itself set `false` (Inference from the Scope line "Any file" plus "a limit on project and local
  settings" that concerns only a project `true`).

### 5.4 Settings keys (filesystem and network)

Keys, types and defaults are tabulated from REF "Sandbox settings":

| Key | Type | Default | Project file? | Note |
| :- | :- | :- | :- | :- |
| `sandbox.enabled` | Boolean | `false` | Yes | `/sandbox` writes it to `.claude/settings.local.json`. |
| `sandbox.failIfUnavailable` | Boolean | `false` | Yes | Exit at startup if the sandbox cannot start. |
| `sandbox.autoAllowBashIfSandboxed` | Boolean | `true` | Yes | `false` = regular permissions mode. |
| `sandbox.excludedCommands` | array of Bash-rule-style patterns | unset | Yes (unless admin-required) | Every command in the call must match; calls with `cd`, redirects, substitutions, `sudo`/`eval`/`xargs` stay sandboxed. "Exclusion is a convenience, not a security boundary". |
| `sandbox.allowUnsandboxedCommands` | Boolean | `true` | Yes for `false` | Strict sandbox mode when `false`. |
| `sandbox.filesystem.allowWrite` | array of paths | unset | Yes | Cannot lift a protected path. Repository entries do not count under the read block. |
| `sandbox.filesystem.denyWrite` | array of paths | unset | Yes | Merged from every scope, plus `Edit(...)` deny rules. |
| `sandbox.filesystem.denyRead` | array of paths | unset | Yes | Merged from every scope, plus `Read(...)` deny rules. |
| `sandbox.filesystem.allowRead` | array of paths | unset | Yes | Re-opens reading inside a `denyRead` region; a narrower deny holds inside a wider allow. |
| `sandbox.filesystem.disabled` | Boolean | `false` | No | User, managed, `--settings` only. |
| `sandbox.ignoreViolations` | object: command substring to array of violation substrings | unset | Yes | Suppresses the report only. |
| `sandbox.enableWeakerNestedSandbox` | Boolean | `false` | Yes | For unprivileged Docker; "considerably weakens security". |
| `sandbox.allowNestedUserNamespaces` | Boolean | `false` | No (`true` ignored) | Needed for Chromium's own sandbox; "you turn off a security boundary". |
| `sandbox.credentials.files` | array of `{ path, mode }` | unset | `deny` only | "There is no built-in credential deny list". |
| `sandbox.credentials.envVars` | array of `{ name, mode }` | unset | `deny` only | `deny` unsets the variable for sandboxed commands. |
| `sandbox.network.allowedDomains` | array of domains, `*.` wildcards, IP literals, optional `:port` | unset | Yes | Pre-allows hosts. |
| `sandbox.network.deniedDomains` | same syntax | unset | Yes | Wins over `allowedDomains`; refused in every permission mode. |
| `sandbox.network.strictAllowlist` | Boolean | `false` | No | Deny instead of prompt; when set in user settings it also makes Claude Code ignore a repository's `allowedDomains` and `WebFetch(domain:...)` allow rules for the sandbox (SBX, "Locks that apply without an admin-required sandbox"). |
| `sandbox.network.allowAllUnixSockets` | Boolean | `false` | Yes | The only way to permit Unix sockets on Linux; also opens `AF_VSOCK`. |
| `sandbox.network.allowUnixSockets`, `allowLocalBinding`, `allowMachLookup` | | | Yes | macOS only; no effect on Linux. |
| `sandbox.network.httpProxyPort`, `socksProxyPort` | number | unset | Yes unless locked | Your proxy replaces Claude Code's filtering. |
| `sandbox.network.tlsTerminate` | object | unset | No | Experimental; needed for `mask`. |

Path prefixes in sandbox lists (REF, "Sandbox path prefixes"): `/` absolute; `~/` home; `./` or
no prefix "Relative to the project root for project settings, or to `~/.claude` for user
settings". "This syntax differs from Read and Edit permission rules, which use `//path` for
absolute and `/path` for project-relative".

Interaction with permission rules (SBX, "Permission rules"; REF, "`sandbox.filesystem`"): `Edit`
allow rules are added to `allowWrite`, `Edit` deny rules to `denyWrite`, `Read` deny rules to
`denyRead`, and `WebFetch(domain:...)` allow and deny rules to the network lists. Only a leading
`*.` and a bare `*` wildcard in a `WebFetch(domain:...)` rule affect the sandbox. This is the
documented way a `Read(./.env)` deny rule becomes OS-enforced for shell commands: "the sandbox
adds your `Read` deny paths to what every sandboxed command can't read" (EX, "A team's shared
settings").

Network decisions for hosts outside the allowlist (SBX, "Hosts outside your allowed domains"):
Manual/`acceptEdits`/plan prompt; auto mode refuses unless the command listed the host and the
classifier approved (per-command allowed domains, v2.1.271+, open the host for that one command
only); `dontAsk` refuses; `bypassPermissions` allows. "Yes, and don't ask again" saves a
`WebFetch(domain:...)` allow rule to local settings. Hostnames resolving only to local addresses
are refused, except `localhost` and `*.localhost`; add `"127.0.0.1:3000"`-style entries for dev
hostnames (SBX, "Hostnames that resolve to local addresses", "An allowed hostname is refused with
`resolved to a loopback address`").

Sandbox protected paths (SBX, "Protected paths"): inside writable directories the sandbox still
denies writes to `.claude` settings files, `.claude/skills`, `.claude/agents`,
`.claude/commands`, `.claude/hooks`, `.mcp.json`, `.claude/workflows`,
`.claude/scheduled_tasks.json`; in the working directory also `.bashrc`, `.zshrc`, `.gitconfig`,
`.vscode`, `.idea`, and `hooks` and `config` inside `.git`; most of `~/.claude`. An `allowWrite`
entry or `Edit` allow rule does not lift this. Side effect: `git merge`/`git checkout` can fail
with `unable to unlink old` when they must replace a file under `.claude/skills` (SBX, "A git
command fails with `unable to unlink old`"). Inference: this matters for a template that syncs
`.claude/` content, because a sandboxed `git pull` that updates `.claude/hooks` or
`.claude/skills` will hit this and need the unsandboxed retry or a manual run.

### 5.5 Known incompatibilities and limits

- `docker` "is incompatible with the sandbox"; use `excludedCommands` such as `docker compose *`
  (SBX, "`docker` commands fail").
- `watchman`: "Run `jest --no-watchman` instead" (SBX, "`jest` hangs or fails").
- Chromium/Electron (so Playwright) fail on Linux with `No usable sandbox!`: start the browser
  with `--no-sandbox`, or exclude the test command, or set `allowNestedUserNamespaces` in user
  settings (SBX, "Chromium or rootless Podman fails inside the sandbox on Linux").
- Database drivers, plain `ssh`, UDP, `ping` cannot connect even to allowed hosts because they
  ignore proxy variables (SBX, "A database client or other non-HTTP tool fails to reach an allowed
  host"); documented fix is `excludedCommands` plus a matching ask rule.
- Clipboard tools (`xclip`, `wl-copy`) may not work (SBX).
- Start Claude Code from the repository root, or `.git` can be outside the writable area (SBX, "A
  git command fails with `Unable to create '…/index.lock'`").
- Security limits (SBX, "Security limitations"): "Sandboxing reduces risk but is not a complete
  isolation boundary." The proxy does not inspect TLS; "Allowing broad domains such as
  `github.com` can create paths for data exfiltration" (domain fronting). Broad `allowWrite`
  (directories on `$PATH`, shell rc files) enables escalation. "Effective sandboxing requires both
  filesystem and network isolation."
- "Sandboxed commands can still delete your working directory" (MODES, "Critical paths").

### 5.6 Recommended configuration for fewer prompts

- The docs' pairing (MODES, "Common setups"): "Manual mode plus the Bash sandbox in auto-allow
  mode", or auto mode with the sandbox as "defense in depth". "The Bash sandbox and auto mode work
  independently and combine".
- Prefer `allowWrite`/`allowedDomains` over `excludedCommands`: "This is the recommended approach
  when a tool needs write access to a specific location, rather than excluding the tool from the
  sandbox entirely" (SBX, "Configure sandboxing").
- Workspace-only reads: `"denyRead": ["~/"], "allowRead": ["."]` placed "in your project's
  `.claude/settings.json`, because the relative path `.` resolves to the project root" (SBX,
  "Configure sandboxing"); or set `permissions.blockReadsOutsideWorkingDirectories` "instead of
  writing path rules".
- Protect credentials explicitly: `sandbox.credentials` `deny` entries for `~/.aws`, `~/.ssh` and
  secret environment variables, "since the default read policy still allows them" (SBX, "Enforce
  sandboxing with managed settings").
- For a hard gate: `failIfUnavailable: true` and `allowUnsandboxedCommands: false` (same
  section).
- To put hooks, MCP servers and file tools behind a boundary too, run the whole process in a
  container, VM or the sandbox runtime (SBX, "What runs outside the sandbox"; see section 6.5).

## 6. Security guidance

Sources: SEC (docs-en-security-md), PERM, SBXENV (docs-en-sandbox-environments-md), DEVC
(docs-en-devcontainer-md), SECG (docs-en-security-guidance-md), DEBUG
(docs-en-debug-your-config-md), REF.

### 6.1 Prompt-injection defences the docs list

- Permission system and network command approval: "Commands that fetch content from the web such
  as `curl` and `wget` are not auto-approved by default." To stop them, "add them to
  `permissions.deny`", but a deny rule "matches the command as written"; for enforcement
  independent of command text use sandbox network isolation (SEC, "Core protections").
- Web page summaries: "For most fetches, WebFetch runs a separate model call over the page, and
  Claude receives that call's answer instead of the raw page." (SEC, "Additional safeguards").
- Command injection detection: "In Manual mode, Claude Code asks before running a Bash command it
  can't fully analyze." An allow rule for part of a command, such as `Bash(git *)`, "doesn't skip
  that prompt." (SEC, same section).
- Fail-closed matching: "In Manual mode, unmatched commands require approval by default" (SEC,
  same section).
- Auto mode: the classifier blocks actions that appear "driven by hostile content Claude read";
  tool results are stripped from classifier requests; "A separate server-side probe scans incoming
  tool results and flags suspicious content before Claude reads it" (MODES, "Eliminate permission
  prompts with auto mode", "How the classifier evaluates actions").
- Sandbox: "sandbox restrictions still apply even if a prompt injection bypasses Claude's
  decision-making" (PERM, "How permissions interact with sandboxing").
- `bypassPermissions` "offers no protection against prompt injection" (MODES).
- Working directory boundary: "The boundary is a permission prompt, so a Bash command you approve
  can still write anywhere your user account can" (SEC, "Built-in protections").
- Best practices for untrusted content (SEC, "Additional safeguards"): review suggested commands
  before approval; "Avoid piping untrusted content directly to Claude"; verify proposed changes
  to critical files; "Use virtual machines (VMs) to run scripts and make tool calls, especially
  when interacting with external web services"; report suspicious behaviour with `/feedback`.
- "While these protections significantly reduce risk, no system is completely immune to all
  attacks." (SEC, warning).
- CLAUDE.md versus enforcement: "Use CLAUDE.md for \"we do it this way here.\" Use permissions or
  hooks for security boundaries and anything that must never happen" (DEBUG, "See what loaded
  into context", note).

### 6.2 Untrusted repositories

- Recommended environment for the goal "Work on an untrusted repository": "A dedicated virtual
  machine, or a cloud session if you have a Claude subscription" (SBXENV, "Choose an approach").
- Before `claude -p` in a repository you did not write (PERM, "What runs before you trust a
  folder"): pass `--setting-sources user` "so Claude Code reads neither the project's settings
  files nor its `.mcp.json`"; or `--bare` (reads no hooks, skills, custom commands, subagents,
  plugins or `.mcp.json` servers, though "The project's `env` block and helpers such as
  `awsAuthRefresh` in its settings files still apply"); or
  `--settings '{"disableAllHooks": true}'` ("Setting it in your user settings alone isn't enough,
  because the repository's project settings take precedence over yours and can set it back to
  `false`"); or a `disabledMcpjsonServers` entry.
- `claude --safe-mode` starts with customisations disabled (CLAUDE.md, skills, plugins, hooks,
  MCP servers, custom commands and agents, output styles, keybindings) while permissions work
  normally (DEBUG, "Test against a clean configuration").
- Dev containers do not make an untrusted repo safe: with `--dangerously-skip-permissions`, "dev
  containers do not prevent a malicious project from exfiltrating anything accessible inside the
  container, including the Claude Code credentials stored in `~/.claude`." "Only use dev
  containers when developing with trusted repositories" (DEVC, warning).

### 6.3 Does Claude Code ask before honouring a repo's settings? (workspace trust)

Yes for an interactive session in a folder you have not trusted: "In an interactive session,
Claude Code shows the workspace trust dialog when you start it in a folder you haven't trusted."
"Servers in a project's `.mcp.json` have their own approval prompt" (SEC, "Additional
safeguards"). The dialog "lists the rules and directories the folder would grant so you can
review them first" (PERM, "Project allow rules and workspace trust"); for `/cd` into an untrusted
directory it lists "the allow rules, additional directories, hooks, and helper commands" (PERM,
"Move the session to another directory").

What is gated and what is not:

| Repository content | Gated by trust? | Citation |
| :- | :- | :- |
| `permissions.allow`, `permissions.additionalDirectories` | Yes; applied only after you accept the dialog for that folder | PERM, "Project allow rules and workspace trust" |
| `permissions.deny`, `permissions.ask` | No; "they only restrict", apply right away | PERM, same; SET, "A committed key doesn't reach teammates" |
| Hooks in settings files | Run only once the workspace is trusted in an interactive session; but they ARE used when you "trusted only a parent folder" and in `claude -p`/SDK runs | PERM, "What runs before you trust a folder" (row 1) |
| `env` block, `apiKeyHelper` and other helper commands | Same as hooks: "Used" under parent-folder trust and in `-p`; in interactive sessions applied "after you trust the workspace" | PERM, same table; REF, "When Claude Code applies `env` values", "`apiKeyHelper`" |
| `statusLine`, `fileSuggestion`, `subagentStatusLine` | "Off entirely ... when the folder isn't trusted under the same workspace trust rule as hooks" | REF, "Status line and file suggestion gates" |
| `autoMemoryDirectory` | Same trust rule as hooks | REF, "`autoMemoryDirectory`" |
| `extraKnownMarketplaces`, frontmatter hooks in a project subagent, project `@skills-dir` plugin, inline `mcpServers` in subagent frontmatter | Need this exact folder trusted; "Not used, and no dialog is offered" under parent-folder trust; not used in `-p` | PERM, same table |
| `.mcp.json` servers | Separate per-server approval prompt; "The repository's own approvals don't count" before trust; in `claude -p` they are "Connected without asking, approved or not" | PERM, same table; REF, "`enableAllProjectMcpServers`" |
| `headersHelper` on a `.mcp.json` server | Not run until the folder is trusted | PERM, same table |
| A skill's `allowed-tools` | "Workspace trust never gates a skill's `allowed-tools` in any session" | PERM, same table |

- Trust is keyed on the git repository root (main checkout for worktrees) and stored in
  `~/.claude.json` as `projects["<path>"].hasTrustDialogAccepted` (PERM, "Project allow rules and
  workspace trust", "What runs before you trust a folder"). Trusting a parent folder covers
  subdirectories "apart from a git repository nested inside it".
- "Claude Code shows the trust dialog in interactive sessions only. A `claude -p` run or an SDK
  session never shows it" (PERM, same section). In `-p`, project allow rules are not used and a
  `this workspace has not been trusted` warning goes to stderr, but hooks and `env` are used.
- Starting in the home directory holds trust for the session only (SEC, "Additional safeguards").
- Inference for a template synced into many repos: every new clone shows the trust dialog once
  in an interactive session, listing the template's allow rules, additional directories and
  hooks. Until accepted, the template's deny and ask rules already apply but its allow rules,
  hooks, `env`, status line and marketplaces do not. Scheduled or scripted `claude -p` runs skip
  the dialog: hooks and `env` run, allow rules do not unless the folder was trusted earlier.

### 6.4 Secrets

- Deny rules for secret files: "Use it for files that hold API keys, secrets, or environment
  values"; Claude Code then "excludes matching files from file discovery and search results,
  denies reads of them, and blocks the Edit and Write tools on the matching paths." (REF,
  "`permissions.deny`"). Docs' example: `Read(./.env)`, `Read(./.env.*)`, `Read(./secrets/**)`,
  `Read(./config/credentials.json)`.
- Gap: `Read(./.env)` "stops the file tools and commands that name the file, such as `cat .env`,
  but not `grep -r` run over the directory"; the example's `sandbox` block "closes that gap" (EX,
  "A team's shared settings").
- The sandbox reads credential files by default ("including credential files such as `~/.ssh`
  and `~/.aws/credentials`"); protect them with `sandbox.filesystem.denyRead` or
  `sandbox.credentials` `deny` entries; "There is no built-in credential deny list" (SBX,
  "Protect credentials").
- Sandboxed commands inherit Claude Code's environment "including any secrets in its environment";
  use `sandbox.credentials.envVars` `deny` entries, or `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` "To
  strip credentials from all subprocesses regardless of sandboxing" (SBX, "What the sandbox
  restricts", "Protect credentials").
- `env` values in settings "are plain text in the settings file and reach every subprocess";
  use `apiKeyHelper` for API credentials (REF, "How `env` values interact with your shell").
  Inference: a committed project `settings.json` must hold no secret values.
- Auto mode allows "Reading `.env` and sending credentials to their matching API" by default and
  blocks "Printing a live credential or token into the transcript or a file" and secrets entering
  commits or pushes (MODES, "What the classifier blocks by default").
- Claude Code's own credentials: "On Linux they're stored in a file with mode `0600`" (SEC,
  "Additional safeguards").
- Dev containers: "Avoid mounting host secrets such as `~/.ssh` or cloud credential files into
  the container; prefer repository-scoped or short-lived tokens." (DEVC, warning).
- Transcripts are plain text on disk and kept for `cleanupPeriodDays` (default 30) (REF,
  "`cleanupPeriodDays`").

### 6.5 Recommended deny and ask rules found in the docs

The docs give examples, not a canonical list. EX says of its own files: "None of them is a
recommended baseline." Rules that appear as examples:

- Deny: `Read(./.env)`, `Read(./.env.*)`, `Read(./secrets/**)` (EX, team file; SET, "Edit a
  settings file"); `Read(./config/credentials.json)`, `Bash(curl *)` (REF, "`permissions.deny`");
  `Bash(git push *)` (PERM, "Wildcard patterns"); `Agent(Explore)` (PERM); `mcp__*` (PERM, "Tool
  name wildcards").
- Ask: `Bash(git push *)`, `Bash(gh pr create *)` (AUTO, "Add a human checkpoint");
  `Bash(dangerouslyDisableSandbox:true)` (SBX, "The unsandboxed retry escape hatch");
  `Bash(git clean *)` (PERM, "Compound commands").
- Allow: `Bash(npm run *)`, `Bash(git commit *)`, `Bash(git diff *)`, `Bash(npm run lint)`,
  `Bash(npm run test *)` (PERM, SET, EX).
- For a hard guarantee beyond string matching: "Use a PreToolUse hook or the sandbox" (DEBUG,
  "Check common causes", last row). The team example hook is
  `${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh` on `PreToolUse` with matcher `Bash` (EX).
- `ConfigChange` hooks can "Audit or block settings changes during sessions" (SEC, "Team
  security").

### 6.6 Isolation options beyond the Bash sandbox

SBXENV, "Compare sandboxing approaches" and "Choose an approach":

| Approach | What is isolated | Requires Docker |
| :- | :- | :- |
| Sandboxed Bash tool | Bash, PowerShell, Monitor commands and children | No |
| Sandbox runtime (`srt claude`, `@anthropic-ai/sandbox-runtime`) | The whole Claude Code process, including file tools, MCP servers and hooks | No |
| Dev container | Full development environment | Yes |
| Custom container | Full development environment | Yes |
| Virtual machine | Full operating system | No |
| Cloud sessions | Full OS hosted by Anthropic | No |

- "The sandboxed Bash tool on its own constrains only shell commands, so it is not sufficient
  for fully unattended runs in either mode." (SBXENV, "How isolation relates to permission
  modes").
- "Always run `--dangerously-skip-permissions` sessions inside a container, a VM, or the sandbox
  runtime"; auto mode's classifier "is a per-action control, not an isolation boundary", so
  isolation "is not required the way it is for `--dangerously-skip-permissions`" (same section).
- Sandbox runtime: "a beta research preview"; config in `~/.srt-settings.json`; needs
  `bubblewrap`, `socat` and `ripgrep` on Linux; allow writes to the project, `~/.claude`,
  `~/.claude.json` and `/tmp`; allow `api.anthropic.com`, `claude.ai`, `platform.claude.com`;
  on Linux the deny list is built once at launch and does not cover files the session creates
  later (SBXENV, "Sandbox runtime").
- Dev container: feature `ghcr.io/anthropics/devcontainer-features/claude-code:1.0`; persist
  `~/.claude` with a named volume plus `CLAUDE_CONFIG_DIR`; reference container has
  `init-firewall.sh` (default-deny egress) needing `NET_ADMIN` and `NET_RAW`; managed settings can
  be baked in at `/etc/claude-code/managed-settings.json` (DEVC). Note: this is the documented
  Linux path for a managed settings file, and it is the highest-precedence scope.
- "Isolation also does not change what is sent to the model." (SBXENV, warning).

### 6.7 The security-guidance plugin (what SECG actually documents)

SECG is not general security guidance; it documents the `security-guidance@claude-plugins-official`
plugin, which reviews Claude's own code changes: a per-edit pattern match (no model call), an
end-of-turn background review ("up to 30 changed files per turn", "at most three times in a
row"), and an agentic review on each `git commit`/`git push` Claude makes ("capped at 20 per
rolling hour"). "None of the layers block writes or commits." Project enablement:
`"enabledPlugins": { "security-guidance@claude-plugins-official": true }` in
`.claude/settings.json`, and each person runs `claude plugin install
security-guidance@claude-plugins-official --scope project` once per clone. Project rule files:
`.claude/claude-security-guidance.md` (8 KB combined cap) and `.claude/security-patterns.yaml`
(or `.json`; YAML needs PyYAML; up to 50 rules). Requires Python 3.7+ (3.10+ for the agentic
review); "the plugin creates a virtual environment under `~/.claude/security/` and installs the
Claude Agent SDK into it, which requires `pip` and network access". Reviews "run on a Claude Opus
model" by default and count toward usage; `SECURITY_REVIEW_MODEL` and `SG_AGENTIC_MODEL` override.
Disable switches: `ENABLE_PATTERN_RULES=0`, `ENABLE_STOP_REVIEW=0`, `ENABLE_COMMIT_REVIEW=0`,
`ENABLE_CODE_SECURITY_REVIEW=0`, `SECURITY_GUIDANCE_DISABLE=1`. Built on hooks (`SessionStart`,
`UserPromptSubmit`, `PostToolUse`, `Stop`). Related: `/security-review` for a one-time pass on the
current branch.

## 7. Recommended project `settings.json` skeleton (documented keys only)

This is assembled only from keys and value shapes documented on the pages above. The docs say
of their own examples "None of them is a recommended baseline" (EX, intro), so the selection and
combination below is my inference; every individual entry is cited. Values that are placeholders
to adapt per repo are marked in the mapping. Settings files are strict JSON, so the comments live
in the list below the block, not in the file (SET, "Edit a settings file").

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Bash(git diff *)",
      "Bash(git commit *)"
    ],
    "ask": [
      "Bash(git push *)",
      "Bash(gh pr create *)",
      "Bash(dangerouslyDisableSandbox:true)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker compose *"],
    "credentials": {
      "files": [{ "path": "~/.aws/credentials", "mode": "deny" }]
    },
    "network": {
      "allowedDomains": ["registry.npmjs.org", "github.com"]
    }
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh"
          }
        ]
      }
    ]
  },
  "enabledPlugins": {
    "security-guidance@claude-plugins-official": true
  },
  "plansDirectory": "./plans",
  "worktree": {
    "symlinkDirectories": ["node_modules"]
  }
}
```

Mapping of each entry to its citation:

1. `$schema`: SET, "Edit a settings file" ("gives you autocomplete and inline validation"; the
   schema "can lag behind the newest CLI releases"). Not listed in REF's settings index.
2. `permissions.allow` entries: `Bash(npm run lint)`, `Bash(npm run test *)` from SET, "Edit a
   settings file"; `Bash(git diff *)` from REF, "`permissions.allow`"; `Bash(git commit *)` from
   PERM, "Wildcard patterns". Placeholders: replace `npm` with the repo's package manager. Gated
   by workspace trust (PERM, "Project allow rules and workspace trust"). In auto mode,
   "Package-manager run commands" allow rules are among those dropped while narrow rules such as
   `Bash(npm test)` stay (MODES, "How the classifier evaluates actions"); whether `Bash(npm run
   test *)` counts as dropped is not stated (see Ambiguities).
3. `permissions.ask` `Bash(git push *)`, `Bash(gh pr create *)`: AUTO, "Add a human checkpoint"
   (always prompts, even in auto mode and with sandbox auto-allow: SBX, "Auto-allow mode"). Does
   not catch `git -C . push` (PERM, "What a Bash rule doesn't match"). Drop these two if pushes
   should run unprompted in auto mode, which allows pushing to the working repo by default (MODES,
   "What the classifier blocks by default").
4. `permissions.ask` `Bash(dangerouslyDisableSandbox:true)`: SBX, "The unsandboxed retry escape
   hatch" ("to be prompted on Bash retries. You get the prompt in auto mode and
   `bypassPermissions` mode too"; the rule also outranks a matching allow rule).
5. `permissions.deny` entries: EX, "A team's shared settings"; REF, "`permissions.deny`". Apply
   without trust (PERM). With the sandbox on, these paths are also added to the sandbox's
   `denyRead` (REF, "`sandbox.filesystem`"; EX). Note `Read(./.env.*)` also matches
   `.env.example`. Inference: a carve-out such as `Read(.env.*)` followed by
   `Read(!.env.example)` in the same `deny` list follows the documented `!` negation rule (PERM,
   "Special characters and `!` negation") but that exact pair is not shown in the docs.
6. `sandbox.enabled: true`: REF, "`sandbox.enabled`" (Scope `Any file`); used in the project file
   in EX, "A team's shared settings". Needs `bubblewrap` and `socat` on Ubuntu (SBX, "Set up Linux
   and WSL2"); if they are missing Claude Code silently runs unsandboxed unless
   `sandbox.failIfUnavailable` is `true` (REF, "`sandbox.failIfUnavailable`"), which is a
   candidate addition for a hard gate.
7. `sandbox.autoAllowBashIfSandboxed: true`: REF (this is the default; shown for explicitness).
   Set `false` for "regular permissions mode".
8. `sandbox.excludedCommands: ["docker compose *"]`: SBX, "Run commands outside the sandbox with
   `excludedCommands`" and "`docker` commands fail". Placeholder: include only if the repo uses
   Docker. "An excluded command runs with your full access."
9. `sandbox.credentials.files` deny entry: REF, "`sandbox.credentials.files`"; SBX, "Protect
   credentials". Project files may carry `deny` entries only (`mask` is dropped). Adding
   `{ "path": "~/.ssh", "mode": "deny" }` is the docs' other example, but it "hides your key
   files" and breaks git over SSH (SBX, "`git` over SSH fails with the sandbox on").
10. `sandbox.network.allowedDomains`: REF, "`sandbox.network.allowedDomains`"; EX uses
    `registry.npmjs.org`; REF uses `github.com`. Placeholders. Caution from SBX, "Security
    limitations": "Allowing broad domains such as `github.com` can create paths for data
    exfiltration."
11. `hooks.PreToolUse` with matcher `Bash` and `${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh`:
    EX, "A team's shared settings" ("The hook is a script in the repo"); shape from REF, "`hooks`".
    Placeholder script name. Hooks run outside the sandbox with full access (SBX, "What runs
    outside the sandbox"). `.claude/hooks` is write-protected inside the sandbox (SBX, "Protected
    paths"). Matcher is a single string, case-sensitive, `|`-separated for several tools (DEBUG,
    "Check hooks").
12. `enabledPlugins` with `security-guidance@claude-plugins-official`: SECG, "Enable for your team
    in local sessions". Each clone still needs `claude plugin install
    security-guidance@claude-plugins-official --scope project`. Optional; it spends model usage
    and bootstraps a Python venv with `pip` (SECG, "Prerequisites", "Usage cost").
13. `plansDirectory: "./plans"`: REF, "`plansDirectory`"; EX ("Keep plan files inside the repo").
    Optional.
14. `worktree.symlinkDirectories: ["node_modules"]`: REF, "`worktree.symlinkDirectories`".
    Optional placeholder.

Deliberately not in the skeleton, with the reason:

- `permissions.defaultMode`: omitted so interactive terminal sessions keep the built-in default,
  which is `auto` on v2.1.283+ (MODES, "Which mode a session starts in"). A project file cannot
  set `auto` or `bypassPermissions`; it can set `default`, `acceptEdits`, `plan` or `dontAsk`
  (REF, "`permissions.defaultMode`"). To forbid auto mode in the repo:
  `"disableAutoMode": "disable"` (REF, "`disableAutoMode`").
- `autoMode`, `permissions.denyInsteadOfPrompting`, `sandbox.network.strictAllowlist`,
  `sandbox.filesystem.disabled`, `sandbox.allowNestedUserNamespaces`, `mask` credentials,
  `useAutoModeDuringPlan`, `skipAutoPermissionPrompt`: not honoured from a project file (section
  1.6). With no user-level config, the documented ways to set them are the `--settings` flag,
  which "can set any key your user settings file can set" (SET, "Change a setting for one
  session"), or a managed file at `/etc/claude-code/managed-settings.json` (MANAGED, "Deploy a
  managed settings file"). Inference: a repo-committed JSON file passed as
  `claude --settings <file>` is the nearest project-carried route for user-only keys; in such a
  file a `/path` permission pattern anchors at "`<directory of file>/path`" (PERM, "Where a
  pattern anchors").
- `permissions.blockReadsOutsideWorkingDirectories`: a project may set `true` (REF), but with the
  sandbox on it denies sandboxed commands read access to the home directory, and "`allowRead` and
  `allowWrite` entries from repository settings don't count" while it is on (REF, "Sandboxed
  commands under the block"). Inference: package-manager stores and caches under `~` would become
  unreadable to sandboxed commands, and the project file cannot re-open them.
- `permissions.blockWritesOutsideWorkingDirectories`: also removes `EnterWorktree`/`ExitWorktree`
  (REF).
- `model`, `effortLevel`, `theme`, `editorMode`, `cleanupPeriodDays`: honoured from a project
  file, but project beats user, so a synced template would override personal choices in every
  repo (SET, "Team settings override personal settings"). A personal override belongs in
  `.claude/settings.local.json`.
- `statusLine`: honoured from project settings (STATUS, "Manually configure a status line": "your
  user settings ... or project settings") and trust-gated (STATUS, "Workspace trust required").
  Left out because the pages do not say how a script path in the project resolves (see
  Ambiguities); an inline command such as the documented `jq -r '...'` one-liner avoids the path
  question (REF, "`statusLine`") and needs `jq`.
- `env`: nothing on the pages read requires a project `env` entry. Documented candidates if
  wanted: `BASH_DEFAULT_TIMEOUT_MS`, `BASH_MAX_TIMEOUT_MS` (TOOLS, "Timeout and output limits");
  `CLAUDE_CODE_TOOL_MEMORY_LIMIT` (TOOLS, "Memory limit on Linux and WSL");
  `DISABLE_AUTOUPDATER` (REF, "`autoUpdatesChannel`"); `DISABLE_TELEMETRY`,
  `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` (REF, "Privacy and
  telemetry"; note DEVC: the last one "also disables the feature-flag evaluation" that Remote
  Control and other features depend on). No secrets: values "are plain text in the settings file".
- `enableAllProjectMcpServers` / `enabledMcpjsonServers`: honoured from the project file only once
  the folder is trusted, and normally written to the local file by the approval dialog (REF).
- `extraKnownMarketplaces`: only needed if the template ships its own marketplace (EX, REF).
- `attribution`: default attribution is kept. To hide everything portably use empty `commit` and
  `pr` strings plus `sessionUrl: false`; `attribution: false` needs v2.1.281+ and older versions
  "skip the whole ... settings file that holds it" (REF, "`attribution`").
- `includeGitInstructions: false`: documented "for example when you use your own git workflow
  skills", but it also removes the git status snapshot (REF).

### Companion `.claude/settings.local.json`

- Purpose: "Personal overrides for one project, and testing before you share" (SET, "Settings
  files and who they affect"). It ranks above the shared project file and below `--settings`
  (SET, "Settings precedence").
- Claude Code writes to it: "Yes, and don't ask again" Bash and WebFetch approvals as `allow`
  rules (PERM, "Permission system"); the `/sandbox` mode choice (`sandbox.enabled`,
  `autoAllowBashIfSandboxed`) (SBX, "Get started"); `.mcp.json` approvals and rejections
  (`enabledMcpjsonServers`, `enableAllProjectMcpServers`, `disabledMcpjsonServers`) (REF);
  `/skills` visibility changes (`skillOverrides`) (REF); a plugin opt-out when you uninstall a
  project-enabled plugin (SECG, "Disable or uninstall"); a few `/config` options such as Show
  tips (SET, "Use the /config menu").
- What a person would put there by hand: a different `model`; `enabledPlugins` set to `false` for
  a project-enabled plugin (REF, "`enabledPlugins`"); `spinnerTipsEnabled`; and the keys scoped
  `User, local, or managed` (`skipDangerousModePermissionPrompt`, `useAutoModeDuringPlan`,
  `syncClaudeAiSkills`, `syncClaudeAiPlugins`).
- It cannot set `permissions.defaultMode` to `auto` or `bypassPermissions`, `autoMode`, or the
  other `User or managed` keys (REF; AUTO, "Where the classifier reads configuration").
- Gitignore: "Claude Code keeps it out of git when it creates the file; if you create it by
  hand, add it to `.gitignore` yourself" (SET, scope table). The first write "adds
  `**/.claude/settings.local.json` to your global git excludes file" (`core.excludesFile`, else
  `$XDG_CONFIG_HOME/git/ignore` or `~/.config/git/ignore`) (SET, "Keep personal settings out of a
  repository"). Inference: a template should list `.claude/settings.local.json` in the repo's own
  `.gitignore`, because the global excludes file is user-level state the template cannot rely on.
- If the file is tracked by git, or `.claude` is a symlink, Claude Code "treats it as
  repository-supplied instead and holds its rules until you trust the folder", and its
  `additionalDirectories` stop counting as working directories for the read/write blocks (PERM,
  "When your local settings file needs trust"; REF,
  "`permissions.blockReadsOutsideWorkingDirectories`").
- Location: at the git repository root (main checkout for worktrees) since v2.1.211, even when
  Claude Code starts in a subdirectory, whereas the shared `.claude/settings.json` is read from
  the primary working directory with "no parent-directory fallback" (SET, "Where Claude Code keeps
  the local file in a git repository"; PERM, "Where output styles, hooks, and local settings load
  from").

## 8. Smaller pages: status line, monitoring, managed precedence, availability

### 8.1 Status line (STATUS)

- `statusLine` runs a shell command that receives JSON session data on stdin and prints the row;
  it "runs locally and does not consume API tokens" (STATUS, "How status lines work").
- Fields: `type: "command"`, `command`, `padding` (default `0`), `refreshInterval` (seconds,
  minimum `1`), `hideVimModeIndicator` (STATUS, "Manually configure a status line").
- Updates on new assistant messages, `/compact`, permission mode changes, vim mode toggles, and
  timers; debounced at 300 ms; an in-flight run is cancelled by a new trigger (STATUS, "When the
  status line updates"). Output is shown only if the script exits `0`.
- Useful stdin fields: `model.display_name`, `workspace.current_dir`, `workspace.project_dir`,
  `context_window.used_percentage`, `cost.total_cost_usd`, `rate_limits.five_hour.used_percentage`
  and `rate_limits.seven_day.used_percentage` (Pro, Max, Ultra only), `effort.level`,
  `session_id`, `worktree.*`, `pr.*` (STATUS, "Available data").
- "Until you accept the workspace trust dialog, the status line stays blank." Trust of a parent
  directory is enough (STATUS, "Workspace trust required"). `disableAllHooks: true` outside
  managed settings disables it (STATUS, "Status line not appearing").
- With a custom status line, Claude Code "stops showing most of the footer's keyboard hints"
  (STATUS, intro).
- `/statusline <description>` generates a script "in `~/.claude/`" and updates settings (STATUS,
  "Use the /statusline command"), i.e. it writes user-level files.
- `subagentStatusLine` has the same gates (STATUS, "Subagent status lines").

### 8.2 Monitoring for a solo developer (OTEL, skimmed)

- OpenTelemetry export is opt-in: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, `OTEL_METRICS_EXPORTER`
  (`otlp`, `prometheus`, `console`, `none`), `OTEL_LOGS_EXPORTER` (`otlp`, `console`, `none`),
  `OTEL_EXPORTER_OTLP_PROTOCOL`, `OTEL_EXPORTER_OTLP_ENDPOINT` (OTEL, "Quick start"). A solo
  developer can use the `console` exporter or a local collector.
- These variables cannot come from the project file: "Claude Code ignores the OpenTelemetry
  exporter variables in a repository's `.claude/settings.json` and `.claude/settings.local.json`"
  (OTEL, "Administrator configuration"). They must be set in the shell, user settings, managed
  settings or `--settings`.
- Metrics: `claude_code.session.count`, `claude_code.lines_of_code.count`,
  `claude_code.pull_request.count`, `claude_code.commit.count`, `claude_code.cost.usage` (USD),
  `claude_code.token.usage`, `claude_code.code_edit_tool.decision`, `claude_code.active_time.total`
  (OTEL, "Metrics").
- Prompt text, response text, tool arguments and tool content are not exported by default; each
  has its own `OTEL_LOG_*` switch (OTEL, "Security and privacy").
- "Claude Code doesn't pass `OTEL_*` environment variables to the subprocesses it spawns" (OTEL,
  "Administrator configuration").
- Without telemetry, the lighter documented options are `/usage`, and the status line's
  `cost.total_cost_usd` (STATUS, "Available data").

### 8.3 Managed settings, precedence only (MANAGED, SERVER)

- Managed settings sit "above every other level, so no user, project, local, or `--settings`
  value overrides them, apart from a few security-sensitive exceptions" (MANAGED, intro).
- Linux file location: `/etc/claude-code/managed-settings.json`, plus optional
  `managed-settings.d/*.json` merged in alphabetical order, and `managed-mcp.json` (MANAGED,
  "Deploy a managed settings file", "Where each mechanism stores the policy", "Split a file-based
  policy across teams"). `/status` then shows `Enterprise managed settings (file)`.
- Order within the managed tier: remote (server-managed) settings, then MDM/OS policy, then
  managed settings files, then the Windows HKCU registry; default `"first-wins"` uses the
  highest-ranked source with a policy key (MANAGED, "How Claude Code combines managed sources").
- Server-managed settings need a Team or Enterprise plan (SERVER, "Requirements"); not available
  to a solo Pro/Max developer (FEAT, "Availability by subscription plan").
- "Keys only a managed source can set" are listed in MANAGED and match the `Managed` list in
  section 1.6.
- Inference: for a solo developer, a local `/etc/claude-code/managed-settings.json` is the only
  documented way to use managed-only locks, and it is machine-level, not project-level.

### 8.4 Feature availability (FEAT)

- Available on every provider: CLI, Agent SDK, IDE extensions, subagents, hooks, commands,
  skills, CLAUDE.md memory, plugins, MCP servers, checkpoints, sandboxing, workflows,
  OpenTelemetry metrics, and the managed settings file (FEAT, "Features available on every
  provider").
- Auto mode: available on Claude subscription and Anthropic Console; on Bedrock, Agent Platform
  and Foundry only with "Claude Sonnet 5 or later, Opus 4.7 or later, Haiku 5.5, and the Fable
  models" (FEAT, footnote 2).
- Require a claude.ai subscription: cloud sessions, Desktop, cloud scheduled tasks, Remote
  Control, Chrome extension, computer use, Artifacts, voice dictation (FEAT, "Features that
  require a Claude subscription"). Code Review is Team and Enterprise only.
- "Ultra is the new name for the Max 20x plan, and Max is the new name for Max 5x." (FEAT, "Ultra
  plan").

## 9. (a) Keys and behaviours the docs flag as new, renamed, deprecated or removed

Deprecated or removed keys:

- `includeCoAuthoredBy`: "Deprecated since v2.0.62, when `attribution` replaced it"; ignored once
  `attribution.commit` or `attribution.pr` is set (REF).
- `disableArtifact`: deprecated, replaced by `enableArtifact` (REF).
- `voiceEnabled`: "Deprecated since v2.1.92, when the `voice` object replaced it" (REF).
- `keybindingFlavor`: "Deprecated since v2.1.261 and has no effect" (REF).
- `taskOutputMaxChars`: "Removed in v2.1.277, together with the `TaskOutput` tool" (REF, TOOLS).
- `permissionExplainerEnabled`: removed in v2.1.257 with the `Ctrl+E` explanation (REF).
- `teammateDefaultModel`: removed in v2.1.234 (REF).
- `ignorePatterns`: deprecated; `permissions.deny` "replaces" it (REF, "`permissions.deny`").
- `.claudeignore`: "has no effect" (PERM, "Read and Edit").
- `skipLfs` in a marketplace source: "accepted and has no effect" since v2.1.274 (REF).

Renames and aliases:

- `extraKnownMarketplaces` may be written `additionalMarketplaces`; `strictKnownMarketplaces` may
  be written `allowedMarketplaces` (v2.1.232+; older versions ignore the alias) (REF, "Marketplace
  key aliases").
- Mode `default` is labelled "Manual" in the UI; `manual` is an accepted alias (MODES).
- `effortLevel` is the older form; `/effort` now saves per model under `modelSettings`
  (v2.1.251+) (REF).
- "Vertex AI" is now "Google Cloud's Agent Platform"; "routines" are now "cloud scheduled tasks";
  Max 20x is now "Ultra" (REF `allowedProviders`; TOOLS `RemoteTrigger`; FEAT).

Behaviour changes with version gates that matter for a project file (installed: 2.1.322, so all
apply):

- Auto mode is the built-in starting mode for interactive terminal and VS Code sessions on every
  plan from v2.1.283 (v2.1.228 on Pro/Max/Ultra/Team) (MODES).
- `claude -p` and SDK runs with no mode start in Manual from v2.1.302 (MODES).
- `bypassPermissions` no longer takes effect from project or local settings since v2.1.257 (REF).
- Telemetry exporter variables in a project or local `env` block are ignored since v2.1.282;
  storage-location and session-export variables since v2.1.251; dialog-timer variables and
  `CLAUDE_CODE_DISABLE_ATTACHMENTS` since v2.1.290 (REF).
- `.claude/settings.local.json` lives at the repository root since v2.1.211; `/cd` re-reads
  project settings since v2.1.246; settings in a `.claude/` folder created mid-session are
  detected since v2.1.257 (SET, PERM, DEBUG).
- New permission keys: `permissions.blockReadsOutsideWorkingDirectories` (v2.1.257),
  `permissions.blockWritesOutsideWorkingDirectories` (v2.1.314),
  `permissions.denyInsteadOfPrompting` (v2.1.319), `autoMode.classifyAllShell` (v2.1.193),
  `maxEffortLevel` (v2.1.267) (REF).
- Sandbox: admin-required repository locks (v2.1.285); user `allowUnsandboxedCommands: false`
  holds against a project `true` (v2.1.285); per-command allowed domains in auto mode (v2.1.271);
  `strictAllowlist` (v2.1.219); `mask` credentials (v2.1.221); `allowNestedUserNamespaces`
  (v2.1.305); refusal of allowed hostnames that resolve to local addresses (v2.1.284); startup
  check for Ubuntu's AppArmor restriction (v2.1.310); trailing-slash path fix (v2.1.224);
  `sandbox.network.tlsTerminate` is "experimental" (SBX, REF).
- Permission checks added: Bash input-redirect targets (v2.1.257), `tee` targets (v2.1.269),
  `Read` deny rules blocking Write (v2.1.228), pasted image paths and directory listings
  (v2.1.290), network-path prompts (v2.1.292), WebFetch wildcards (v2.1.172) (PERM).
- `attribution: false` (v2.1.281); `extraKnownMarketplaces` same-name entries replaced whole
  (v2.1.228); marketplace `headersHelper` (v2.1.238) (REF).
- Hook matcher `,` separator works from v2.1.191 (DEBUG).
- Task tools are off by default on models newer than Opus 4.7/Sonnet 4.6/Haiku 4.5 (v2.1.268)
  (TOOLS). Glob and Grep tools are absent by default on Linux (TOOLS; no version given).
- "Mods" (plugins whose code registers hooks, with a `tool.check` event) appear throughout PERM,
  REF and SBX as a newer extension surface with its own precedence rules.
- The sandbox runtime is "a beta research preview" (SBXENV); OpenTelemetry traces are "beta"
  (OTEL).

## 9. (b) Expected but not found in these pages

- A canonical or recommended deny-rule list. Only examples exist, and EX says none is a
  recommended baseline.
- The list of `env` variables Claude Code "classifies as safe" and applies from project settings
  at startup before trust (REF names categories only: "model selection, timeouts and limits, and
  feature toggles"). The env-vars page was not in scope.
- The "certain known-safe environment variables" stripped before Bash allow-rule matching, the
  full built-in read-only command set (the page says "includes"), the WebFetch "preapproved
  documentation domains", and the "certain denied directories" excluded from default sandbox
  reads: none is enumerated.
- Hook event names, matcher syntax, exit codes and handler fields: only the `hooks` key shape is
  on these pages; the hooks reference was not in scope.
- Full `Skill(...)` rule syntax (TOOLS shows `Skill(deploy *)`, PERM shows only the
  `Skill(skill:<name>)` deny form); details are on the skills page.
- `.mcp.json` format and the full project-server approval rules (on the mcp page). DEBUG confirms
  only that `settings.json` "does not read an `mcpServers` key".
- How a `statusLine` `command` path resolves when set in project settings (relative to the
  project? is `${CLAUDE_PROJECT_DIR}` expanded?). REF states the hook environment variables only
  for `fileSuggestion`.
- Whether `sandbox.*` keys and `permissions.defaultMode` in a project file wait for workspace
  trust. SET's trust list names only `permissions.allow`, `additionalDirectories`,
  `extraKnownMarketplaces` and "most `env` values".
- How auto mode classifier usage is counted on Pro/Max subscriptions (MODES states only where
  it counts toward token usage).
- Any project-level equivalent for `autoMode`, `denyInsteadOfPrompting` or `strictAllowlist`
  (confirmed absent; only `--settings`, user or managed).
- Flags referenced but documented elsewhere: `--setting-sources`, `--settings`, `--bare`,
  `--safe-mode`, `--restricted`, `--permission-prompts none`, `--tools`.
- How `enabledPlugins` in a project file leads to installation ("depends on the plugin's source
  and which file enables it"; the rules are on the plugins/loading page).

## 9. (c) Ambiguities and tensions between pages

1. Project `defaultMode: "auto"` side effect. MODES: the value "doesn't take effect, and Claude
   Code then uses the built-in default rather than a `defaultMode` from `~/.claude/settings.json`".
   On v2.1.283+ the built-in default is `auto`. Inference: a repository that writes `"auto"` would
   therefore bypass a user's own non-auto `defaultMode` and still start in auto unless
   `disableAutoMode` is set. The pages do not comment on this.
2. Hooks and trust. PERM's table says project hooks, `env` and helper commands are "Used" when
   only a parent folder is trusted and in every `claude -p`/SDK run; REF says project `env`
   applies "after you trust the workspace"; STATUS says the status line follows "the same
   workspace trust rule as hooks in settings files" and stays blank "Until you accept the
   workspace trust dialog". None of the pages states in one sentence what happens to project
   hooks in an interactive session between startup and accepting the dialog.
3. Which allow rules auto mode drops. MODES lists "Package-manager run commands" among dropped
   broad rules and says "Narrow rules like `Bash(npm test)` stay"; REF
   (`autoMode.classifyAllShell`) lists only "tool-wide and wildcard rules such as `Bash(*)`, and
   interpreter or shell-wrapper prefixes such as `Bash(python *)`". Whether `Bash(npm run *)` or
   `Bash(pnpm *)` survives is not stated. MODES writes `Bash(python*)`, REF writes
   `Bash(python *)`.
4. Root settings in a monorepo. The shared `.claude/settings.json` is read only from the primary
   working directory ("no parent-directory fallback"), but `.claude/settings.local.json` is read
   from the repository root. A session started in a package subdirectory gets the root local file
   and not the root shared file.
5. Path anchors differ by key family. Permission rules: `/path` is project-relative and `//path`
   absolute; `./path` is "relative to current directory". Sandbox lists: `/path` is absolute and
   `./path` is "Relative to the project root for project settings". It is not stated whether
   "current directory" for `Read(./.env)` means the primary working directory or the shell's
   current directory after a `cd`.
6. `autoContinueAtUsageLimit` in a project file "turns the feature off rather than being ignored"
   when no trusted source sets it; the sentence does not say whether that holds for a project
   `true` as well as `false`.
7. `sandbox.allowUnsandboxedCommands` Scope says "a limit on project and local settings"; the
   text only describes a project `true` losing to a user `false`. That a project `false` is
   honoured is implied, not stated.
8. Deny rules are not absolute for a solo developer: without managed settings, a
   `managed-mcp.json` file or a Team/Enterprise login, an installed mod "can approve a call that
   a deny rule refuses or a `PreToolUse` hook blocked" (PERM). Elsewhere the docs say "Deny rules
   block in every mode".
9. EX commits `sandbox.enabled: true` to a team file while SBX's own first-run path saves the
   choice to the local file; nothing says which the docs prefer for a shared repo.
10. `Read(./.env)` deny versus auto mode's default allowance of "Reading `.env` and sending
    credentials to their matching API": the deny rule wins for the file tools and named Bash
    commands, and with the sandbox on for all sandboxed commands, which can break tools that load
    `.env` themselves (for example a dev server started by Claude). The docs do not discuss this
    interaction.
11. SET links to a heading "security keys where the stricter value applies" from REF's
    `remoteControlAtStartup` entry, while the section is titled "Exceptions to managed settings
    precedence" in the saved SET page.
12. SECG is titled "Catch security issues as Claude writes code" and documents a plugin, not
    general security guidance; general guidance is in SEC.

## Read coverage and limits

Sources assigned: 18. Read in full, start to end, with the Read tool in consecutive chunks: SET,
REF (all 6,112 lines), EX, PERM, MODES, AUTO, SBX, SBXENV, SEC, SECG, DEVC, DEBUG, TOOLS, STATUS,
FEAT (15 pages).

Partial reads, as the assignment allowed:

- MANAGED: read lines 12-161 (delivery, where policy applies, how sources combine), 277-290
  (what a developer can change) and 406-473 (managed-only keys, telemetry). Not read: lines
  162-276 and 291-405 (cross-source keys, embedding hosts, dropped entries, fail-closed keys).
- SERVER: read lines 12-41, 141-177 (settings precedence, per-key exceptions) and 281-380
  (approval dialogs, platform availability). Not read: configuration steps, fetch and caching,
  fail-closed startup, security considerations.
- OTEL: skimmed. Read lines 12-143 (quick start, administrator configuration, common variables),
  647-666 (metrics list) and 1798-1837 (security and privacy). Not read: traces, span and event
  attribute tables, example configurations, audit sections.

All quotes were copied from the saved files. Statements marked "Inference:" are mine. Every page
is a snapshot fetched 2026-11-10; version gates quoted above are as written in that snapshot.






