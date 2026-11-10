# Harness research: Codex CLI, OpenCode, AGENTS.md / Agent Skills, and sync tools

Written 2026-11-10. Question: what can be configured **inside the project directory** for each
harness, so one source-of-truth repository can sync project-level config into other repos with no
user-level/global config.

## How to read the citations

Every citation is a directory under `refs/articles/`; the text is in `<dir>/article.md`.
Abbreviations used to keep lines short:

| Prefix | Expands to (under `refs/articles/`) | What it is |
|---|---|---|
| `LC/x` | `learn.chatgpt.com/x` | Official Codex docs (linked from `developers.openai.com/codex/llms.txt`), fetched 2026-11-10 |
| `OC1/x` | `raw.githubusercontent.com/anomalyco-opencode-v1-3-10-packages-web-src-content-docs-x-mdx` | OpenCode docs at git tag `v1.3.10` (the installed version, released 2026-03-31) |
| `OC2/x` | `opencode.ai/x` | Live opencode.ai docs, which now describe **OpenCode V2** (fetched 2026-11-10) |
| `CC/x` | `code.claude.com/x` | Claude Code docs already in the corpus (fetched 2026-11-10); used only for compatibility facts |
| `RAW/x` | `raw.githubusercontent.com/x` | Tool READMEs |

Version anchors (all from saved pages unless marked):

- Codex CLI: latest release **0.167.0, 2026-11-06** (`github.com/openai-codex-releases-latest`). Codex is **not installed** on this machine (`codex: command not found`), so nothing was checked against a binary.
- OpenCode: installed **1.3.10** (`opencode --version`), released 2026-03-31; last V1 release **v1.19.5, 2026-10-28** (`github.com/anomalyco-opencode-releases-latest`); current **v2.2.7, 2026-11-10** (GitHub API release list, not saved). The live docs title is "OpenCode V2 Documentation" (`OC2/docs-llms-txt`). **The installed binary is two generations behind the live docs**, so every OpenCode fact below says V1 (1.3.10 tag) or V2.
- rulesync v43.8.0 (2026-11-08), ruler v0.3.46 (2026-10-22), skills CLI v1.8.0 (2026-11-10): `github.com/dyoshikawa-rulesync-releases-latest`, `github.com/intellectronica-ruler-releases-latest`, `github.com/vercel-labs-skills-releases-latest`.

## Sources read

Saved to collection `harness-docs`: 94 items. Not every one was read end to end; this is the honest split.

**Read in full**
- Codex: `LC/docs-agent-configuration-agents-md-md`, `LC/docs-agent-configuration-rules-md`, `LC/docs-agent-configuration-subagents-md`, `LC/docs-config-file-config-basic-md`, `LC/docs-config-file-config-advanced-md`, `LC/docs-config-file-environment-variables-md`, `LC/docs-build-skills-md`, `LC/docs-custom-prompts-md`, `LC/docs-customization-overview-md`, `LC/docs-hooks-md`, `LC/docs-extend-mcp-md`, `LC/docs-non-interactive-mode-md`, `LC/docs-agent-approvals-security-md`, `LC/docs-enterprise-gateway-compatibility-md`, `LC/docs-import-md`, `LC/docs-github-action-md`, `LC/docs-environments-local-environment-md`, `LC/docs-enterprise-skills-md`, and the whole `config.toml` key table of `LC/docs-config-file-config-reference-md` (lines 1-2045, read through a lossless key/type/description rendering).
- OpenCode V1 (tag v1.3.10): `OC1/config`, `OC1/rules`, `OC1/skills`, `OC1/permissions`, `OC1/agents`, `OC1/commands`, `OC1/plugins`.
- OpenCode V2: `OC2/docs-migrate-v1`, `OC2/docs-config`, `OC2/docs-instructions`, `OC2/docs-skills`, `OC2/docs-permissions`, `OC2/docs-policies`, `OC2/docs-agents`, `OC2/docs-commands`, `OC2/docs-plugins`, `OC2/docs-cli-commands`, `OC2/docs-build-plugins`, `OC2/docs-console-harnesses`, `OC2/docs-console-harnesses-codex`, `OC2/docs-console-harnesses-claude-code`.
- Standards: `agents.md/index`, `RAW/agentsmd-agents-md-main-readme-md`, `agentskills.io/specification-md`, `agentskills.io/client-implementation-adding-skills-support-md`, `agentskills.io/home-md`.
- Tools: `RAW/dyoshikawa-rulesync-main-readme-md`, `RAW/vercel-labs-skills-main-readme-md`.

**Read in part (sections named where cited)**
- Codex: `LC/docs-permissions-md` (lines 8-206), `LC/docs-enterprise-connect-to-a-gateway-md` (lines 8-137, 205-254), `LC/docs-auth-md` (only "Alternative model providers"), `LC/docs-developer-commands-md-b96a28` (intro, `codex exec`, `/skills`, `/import`; the flag tables are JavaScript widgets that did not survive the Markdown export), `LC/docs-config-file-config-sample-md` (trust-level lines only), `LC/docs-sandboxing-md` (Linux prerequisites only).
- OpenCode: `OC1/mcp-servers` (everything before the examples), `OC1/providers` (intro, DeepSeek, Moonshot AI, Z.AI, Custom provider, Troubleshooting), `OC1/cli` (`run` and environment variables), `OC1/github` (Configuration), `OC2/docs-providers` (first two thirds), `OC2/docs-cli-providers`, `OC2/docs-mcp-servers` (keyword scan), `OC2/docs-build-plugins-migrate-v1` (first third), `OC2/docs-build-plugins-server` (hook names only).
- Tools: `RAW/intellectronica-ruler-main-readme-md` (Why, Features, Supported agents, `.ruler/`, Skills), `rulesync.dyoshikawa.com/reference-supported-tools` (table rows for the three harnesses and legend), `rulesync.dyoshikawa.com/guide-configuration` (first 110 lines), `RAW/vercel-labs-skills-main-docs-agents-md` (path and compatibility tables).
- Claude Code: `CC/docs-en-memory-md` (AGENTS.md section), `CC/docs-en-skills-md` (frontmatter table); other `CC/` files were only grep-checked for the path strings in the matrix.

**Saved but not read** (do not treat as evidence): the `requirements.toml` half of the Codex config reference, `LC/docs-enterprise-managed-configuration-md`, `LC/docs-sandboxing-auto-review-md`, `LC/docs-permission-modes-md`, `LC/docs-plugins-md`, `LC/docs-build-plugins-md`, `LC/docs-skills-and-plugins-md`, `LC/docs-codex-cli-md`, `LC/docs-codex-sdk-md`, `OC1/custom-tools`, `OC1/models`, `OC2/docs-models`, `OC2/docs-tools`, `OC2/docs-cli`, `OC2/docs-cli-config`, `OC2/docs-cli-plugins`, `OC2/docs-references`, `OC2/docs-network`, `OC2/docs-troubleshooting`, `OC2/docs`, `agentskills.io/skill-creation-using-scripts-md`.

**Could not fetch**: `https://agentskills.io/clients.md` (FAILED, 282 chars). The agents.md site saved without its collapsed FAQ answers and "compatible agents" list (only the headings survive), so its statements on conflict resolution and nesting are **not** available as evidence.

## Cross-cutting findings

1. **`AGENTS.md` at the repo root is the one instruction file all three read.** Codex and OpenCode read it natively; Claude Code reads it when no `CLAUDE.md`/`CLAUDE.local.md` exists, from v2.1.277. (`LC/docs-agent-configuration-agents-md-md`, `OC1/rules`, `CC/docs-en-memory-md`)
2. **There is no single skills directory all three read.** Codex scans only `.agents/skills`; Claude Code reads `.claude/skills` and explicitly nothing under `.agents/`; OpenCode reads `.opencode/skills`, `.claude/skills` and `.agents/skills`. (`LC/docs-build-skills-md`, `CC/docs-en-memory-md`, `OC1/skills`)
3. **Codex cannot select a model provider from project config.** `model_provider` and `model_providers` are ignored in `.codex/config.toml` with a startup warning. This is the hardest constraint for a no-global-config design. (`LC/docs-config-file-config-advanced-md`, section "Project config files")
4. **Codex custom providers must speak the OpenAI Responses API**; Chat Completions or Anthropic Messages endpoints are not enough. (`LC/docs-config-file-config-reference-md`, `LC/docs-enterprise-gateway-compatibility-md`)
5. **OpenCode can do all of it at project level**: model, provider, base URL, key by `{env:VAR}`, permissions, MCP, agents, commands, plugins, instructions. (`OC1/config`, `OC1/providers`)
6. **Codex gates project config behind a trust decision and gates each hook behind a per-hook review; OpenCode documents no trust prompt at all** and auto-loads project plugins (executable code). (`LC/docs-config-file-config-basic-md`, `LC/docs-hooks-md`, `OC1/plugins`)
7. **Codex hooks use the Claude Code hook shape** (event names such as `PreToolUse`, matcher groups, `type: "command"`, JSON on stdin, exit code 2 to block), in `.codex/hooks.json`. OpenCode has no declarative hooks; it needs a JS/TS plugin. (`LC/docs-hooks-md`, `OC1/plugins`)
8. **Codex has only a native OS sandbox story; OpenCode's docs describe permissions only, no sandbox.** (`LC/docs-agent-approvals-security-md`; no "sandbox" hit in any fetched OpenCode page)
9. **Codex project-level slash commands do not exist**: custom prompts are deprecated and user-only; the replacement is skills. (`LC/docs-custom-prompts-md`)
10. **Subagent definitions are three different formats**: Markdown+YAML (Claude Code), TOML (Codex), Markdown+YAML with different keys (OpenCode). (`LC/docs-agent-configuration-subagents-md`, `OC1/agents`)
11. **Codex protects `.agents/` and `.codex/` as read-only inside its workspace-write sandbox**, so an agent cannot rewrite the synced config. (`LC/docs-agent-approvals-security-md`, "Protected paths in writable roots")
12. **OpenCode V2 breaks things a V1-era sync would rely on**: no `CLAUDE.md` fallback, new plugin API, renamed keys (kept compatible), different defaults. (`OC2/docs-migrate-v1`)

### Contradictions and oddities found in the sources

- **Codex `project_doc_max_bytes`**: one page says it caps the combined chain, "stops adding files once the combined size reaches the limit" (`LC/docs-agent-configuration-agents-md-md`, "How Codex discovers guidance"); another says it is "how much to read from each `AGENTS.md` file" (`LC/docs-config-file-config-advanced-md`, "Project instructions discovery"). Unresolved.
- **Codex wire protocol**: the reference says "`responses` is the only supported value, and it is the default when omitted" (`LC/docs-config-file-config-reference-md`, `model_providers.<id>.wire_api`), yet the advanced page still says "Chat Completions providers will ignore the setting" (`LC/docs-config-file-config-advanced-md`, "Model reasoning, verbosity, and limits"). Inference: the second sentence is stale.
- **Codex reserved provider IDs**: the reference lists `openai`, `ollama`, `lmstudio`; the advanced page adds `amazon-bedrock`, `amazon-bedrock-runtime`, `gcp`. (same two files)
- **Codex user skills location**: skills docs say `$HOME/.agents/skills`; the `CODEX_HOME` description says it holds "config, auth, logs, sessions, skills". (`LC/docs-build-skills-md`, `LC/docs-config-file-environment-variables-md`)
- **Ruler vs Codex docs**: Ruler's README tells users to `export CODEX_HOME="$(pwd)/.codex"` to apply local Codex MCP config (`RAW/intellectronica-ruler-main-readme-md`, line 598-601); Codex docs say project `.codex/config.toml` is read in trusted projects (`LC/docs-extend-mcp-md`). Inference: the Ruler note predates project config.
- **`allowed-tools` in OpenCode**: the skills CLI compatibility table says OpenCode supports it (`RAW/vercel-labs-skills-main-docs-agents-md`, "Compatibility"); OpenCode 1.3.10 docs list five recognised fields without it and say "Unknown frontmatter fields are ignored" (`OC1/skills`, "Write frontmatter"); the V2 skills page does not list it either (`OC2/docs-skills`).
- **OpenCode skills destination**: Ruler writes OpenCode skills to `.opencode/skills/`, the skills CLI to `.agents/skills/` (`RAW/intellectronica-ruler-main-readme-md`, `RAW/vercel-labs-skills-main-docs-agents-md`). Both are read by OpenCode, so both work.
- **OpenCode V2 default effect**: "If no rule matches, OpenCode uses `ask`", but every agent starts with a base rule `{"action": "*", "resource": "*", "effect": "allow"}`, so the practical default is allow. (`OC2/docs-permissions`)
- **rulesync versioning**: the release is tagged v43.8.0 while the README speaks of "Rulesync 14.x" for the ignore deprecation. Unexplained. (`github.com/dyoshikawa-rulesync-releases-latest`, `RAW/dyoshikawa-rulesync-main-readme-md`)

---

## 1. OpenAI Codex CLI (docs as of 2026-11-10; latest release 0.167.0)

### Instruction files

- **Files and order per directory**: `AGENTS.override.md`, then `AGENTS.md`, then names in `project_doc_fallback_filenames`. "Codex includes at most one file per directory." (`LC/docs-agent-configuration-agents-md-md`, "How Codex discovers guidance")
- **Global scope first**: `~/.codex/AGENTS.override.md` else `~/.codex/AGENTS.md` (`CODEX_HOME` moves this). Only the first non-empty file is used. (same)
- **Project scope**: starts at the project root (normally the Git root) and walks **down to the cwd**; files below the cwd are not loaded: "Codex stops searching once it reaches your current directory". Files are concatenated root-first, so nearer files come later. (same, "Layer project instructions")
- **Built once per run/session**; no cache, restart to refresh. (same, "Verify your setup")
- **Size limit**: `project_doc_max_bytes`, 32 KiB by default; empty files are skipped (see the contradiction above on combined vs per file). (same)
- **Fallbacks such as `CLAUDE.md`**: not read by default. No mention of `CLAUDE.md` or `.claude` anywhere in the fetched Codex docs (grep over all 33 pages). A fallback name can be added with `project_doc_fallback_filenames = [...]`; that key is not in the list of keys ignored in project config. (`LC/docs-agent-configuration-agents-md-md`, "Customize fallback filenames"; `LC/docs-config-file-config-advanced-md`)
  - Inference: `project_doc_fallback_filenames = ["CLAUDE.md"]` in a trusted project's `.codex/config.toml` would make Codex read `CLAUDE.md` where no `AGENTS.md` exists. Not stated in the docs; untested.
- **Import syntax**: none documented. No `@file` include appears in the AGENTS.md page.
- **Root detection**: `project_root_markers` (default `.git`); `[]` makes the cwd the root. (`LC/docs-config-file-config-advanced-md`, "Project root detection")
- **Other instruction keys**: `developer_instructions` (extra instructions), `model_instructions_file` ("Replacement for built-in instructions instead of `AGENTS.md`"), `instructions` (reserved). (`LC/docs-config-file-config-reference-md`)
- **Review rules**: a `## Code Review Rules` section in the nearest `AGENTS.md` customises GitHub code review. (`LC/docs-agent-configuration-agents-md-md`, "Add code review rules")

### Project-level config

- **File**: `.codex/config.toml` (TOML) at the repo root and/or in subdirectories; Codex loads every one from the project root down to the cwd, closest wins. Relative paths resolve against the containing `.codex/` folder. (`LC/docs-config-file-config-advanced-md`, "Project config files")
- **Siblings in `.codex/`**: `hooks.json`, `rules/*.rules`, `agents/*.toml`; the desktop app also stores "local environment" setup scripts and actions there. (`LC/docs-hooks-md`, `LC/docs-agent-configuration-rules-md`, `LC/docs-agent-configuration-subagents-md`, `LC/docs-environments-local-environment-md`)
- **Precedence, highest first**: CLI flags and `--config`; project `.codex/config.toml` (trusted only); profile file `~/.codex/<name>.config.toml`; `~/.codex/config.toml`; cloud-managed defaults; `/etc/codex/config.toml`; built-ins. (`LC/docs-config-file-config-basic-md`, "Configuration precedence")
- **Only loaded when trusted**: "Codex loads project-scoped config files only when you trust the project." (`LC/docs-config-file-config-reference-md`, "`config.toml`")

**What can ONLY be set at user level (the constraint list)**

- Ignored in project config, with a startup warning: `openai_base_url`, `chatgpt_base_url`, `apps_mcp_product_sku`, `model_provider`, `model_providers`, `notify`, `profile`, `profiles`, `experimental_realtime_ws_base_url`, `otel`. (`LC/docs-config-file-config-advanced-md`, "Project config files"; repeated in `LC/docs-config-file-config-reference-md`)
- Profiles: files live at `~/.codex/<name>.config.toml`, selected with `--profile`; since 0.134.0 `[profiles.x]` tables and `profile = ` are gone. (`LC/docs-config-file-config-advanced-md`, "Profiles")
- Trust state: `[projects."<abs path>"] trust_level = "trusted" | "untrusted"` in `~/.codex/config.toml`. (`LC/docs-config-file-config-reference-md`, `projects.<path>.trust_level`; `LC/docs-config-file-config-sample-md`)
- Credentials: `auth.json` or OS keyring under `CODEX_HOME`. (`LC/docs-config-file-config-advanced-md`, "Config and state locations")
- Custom prompts: `~/.codex/prompts/` only, and deprecated. (`LC/docs-custom-prompts-md`)
- "Always allow" answers in the TUI are written to `~/.codex/rules/default.rules`. (`LC/docs-agent-configuration-rules-md`)
- `codex features enable/disable` persists to `$CODEX_HOME/config.toml`. (`LC/docs-developer-commands-md-b96a28`, "`codex features`")
- `allow_symlinked_codex_home` is read "only from the execution host's `$CODEX_HOME/config.toml`"; `desktop.custom_file_handlers.<id>` is "User-level only". (`LC/docs-config-file-config-reference-md`)
- `[[skills.config]]` selectors take an absolute `path` or a `name`; the docs show them in `~/.codex/config.toml`. Only `[skills.bundled] enabled = false` is shown for project config. (`LC/docs-build-skills-md`, "Enable or disable local Codex skills")
- Escape hatches that avoid `~/.codex` (documented existence, undocumented fit):
  - `-c key=value` overrides have the highest precedence and accept dotted keys and TOML values. (`LC/docs-config-file-config-advanced-md`, "One-off overrides from the CLI"). Inference: a wrapper script could pass `-c model_provider=...` and `-c 'model_providers.x={...}'`; the docs only say these keys are ignored in *project-local files*, and do not show them being set by `-c`.
  - `CODEX_HOME=$(pwd)/.codex codex exec ...` is shown as a way to get "a project-specific automation user". (`LC/docs-agent-configuration-agents-md-md`). `CODEX_HOME` "Sets the root for Codex state, including config, auth, logs, sessions, skills" and the directory must already exist. (`LC/docs-config-file-environment-variables-md`). Inference: this turns the repo's `.codex/` into the *user* layer, so provider keys work, but credentials, history and logs would then be written inside the repo and must be git-ignored.

**Keys that matter, all settable in project `.codex/config.toml` unless listed above** (`LC/docs-config-file-config-reference-md` for every key; behaviour pages cited where used)

- Model: `model`, `review_model`, `model_reasoning_effort`, `plan_mode_reasoning_effort`, `model_reasoning_summary`, `model_verbosity`, `model_context_window`, `model_auto_compact_token_limit`, `model_auto_compact_token_limit_scope`, `model_post_turn_compact_threshold_percent`, `model_catalog_json`, `service_tier`, `oss_provider`, `web_search` (`disabled | cached | indexed | live`), `tools.web_search`.
- Provider (user level only): `model_provider`, `openai_base_url`, and `model_providers.<id>.` `name`, `base_url`, `env_key`, `env_key_instructions`, `experimental_bearer_token`, `requires_openai_auth`, `wire_api`, `query_params`, `http_headers`, `env_http_headers`, `request_max_retries`, `stream_max_retries`, `stream_idle_timeout_ms`, `supports_websockets`, `supports_standalone_web_search`, `model_catalog_url`, `capabilities.*`, `auth.{command,args,timeout_ms,refresh_interval_ms,cwd}`.
- Approvals: `approval_policy` = `on-request | never | { granular = { sandbox_approval, rules, mcp_elicitations, request_permissions, skill_approval } }` (`untrusted` is retired and can stop the client starting; `on-failure` deprecated); `approvals_reviewer` = `user | auto_review`; `auto_review.policy`, `auto_review.extra_policy`; `allow_login_shell`. (`LC/docs-agent-approvals-security-md`, "Migrate from the retired `untrusted` approval policy")
- Sandbox (older model): `sandbox_mode` = `read-only | workspace-write | danger-full-access`; `sandbox_workspace_write.{writable_roots, network_access, exclude_tmpdir_env_var, exclude_slash_tmp}`; `windows.sandbox`.
- Sandbox (beta permission profiles, mutually exclusive with the older keys): `default_permissions` = `:read-only | :workspace | :danger-full-access | <name>`; `permissions.<name>.{description, extends, workspace_roots, filesystem, network.*}` with values `read | write | deny` and globs such as `"**/*.env" = "deny"`. "Permission profiles do not compose with the older sandbox settings." (`LC/docs-permissions-md`, intro and "Configuration spec")
- Network for sandboxed commands: `features.network_proxy` (boolean or table with `enabled`, `domains`, `unix_sockets`, `allow_local_binding`, ...). Domain rules are not enforced unless the proxy is on, and it "does not filter web search, app or connector tool calls, MCP server connections". (`LC/docs-agent-approvals-security-md`, "Network access")
- Command rules: `.codex/rules/*.rules`, Starlark `prefix_rule(pattern=[...], decision="allow"|"prompt"|"forbidden", justification=..., match=[...], not_match=[...])`; strictest match wins; tested with `codex execpolicy check --rules <file> -- <cmd>`. "Rules are experimental and may change." (`LC/docs-agent-configuration-rules-md`)
- MCP: `[mcp_servers.<id>]` with `command`, `args`, `env`, `env_vars`, `cwd` (stdio) or `url`, `auth`, `bearer_token_env_var`, `http_headers`, `env_http_headers`, `http_headers_helper`, `oauth.{client_id,client_secret,callback_url,callback_port}`, `scopes`, `oauth_resource` (HTTP); plus `enabled`, `required`, `startup_readiness`, `startup_timeout_sec` (default 10), `tool_timeout_sec` (default 60), `enabled_tools`, `disabled_tools`, `default_tools_approval_mode` (`auto | prompt | writes | approve`), `tools.<tool>.approval_mode`, `tools.<tool>.output_token_limit`, `supports_parallel_tool_calls`, `omit_tools_from`, `environment_id`; top level `mcp_optional_startup_grace_ms`, `mcp_oauth_callback_port`, `mcp_oauth_callback_url`, `mcp_oauth_credentials_store`. Project scope is explicitly allowed "(trusted projects only)". (`LC/docs-extend-mcp-md`)
- Hooks: `features.hooks` (default true), `[hooks]` / `hooks.<Event>[].hooks[]` inline, or `hooks.json` beside the config. (`LC/docs-hooks-md`)
- Environment for spawned commands: `shell_environment_policy.{inherit = all|core|none, set, filters = { "PATTERN" = "include"|"exclude" }, ignore_default_excludes, exclude, include_only, experimental_use_profile}`. Note the default: `ignore_default_excludes` "defaults to `true`", so names containing `KEY`, `SECRET` or `TOKEN` are **passed through** unless you set it to `false`. (`LC/docs-config-file-config-basic-md`, "Command environment")
- Subagents: `agents.{enabled, max_concurrent_threads_per_session, default_subagent_model, default_subagent_reasoning_effort, interrupt_message}`, `agents.<name>.{description, config_file}`.
- Skills: `skills.bundled.enabled`, `skills.include_instructions`, `skills.max_context_tokens`, `skills.config[]`.
- Instructions: `project_doc_max_bytes`, `project_doc_fallback_filenames`, `project_root_markers`, `developer_instructions`, `model_instructions_file`, `compact_prompt`.
- Plugins: `marketplaces.<name>.{source_type, source, ref, sparse_paths}` ("Marketplaces can be defined in system, cloud-managed, user, or trusted-project config.toml"), `plugins.<plugin>.enabled`.
- Process environment variables Codex itself reads: `CODEX_HOME`, `CODEX_SQLITE_HOME`, `CODEX_API_KEY`, `CODEX_ACCESS_TOKEN`, `CODEX_CA_CERTIFICATE`, `SSL_CERT_FILE`, `RUST_LOG`. (`LC/docs-config-file-environment-variables-md`)
- Editor schema line: `#:schema https://developers.openai.com/codex/config-schema.json`. (`LC/docs-config-file-config-reference-md`)

### Skills

- **Supported**, built on the Agent Skills standard. (`LC/docs-build-skills-md`)
- **Directories**: repo scope is `.agents/skills` in every directory "from your current working directory up to the repository root"; user `$HOME/.agents/skills`; admin `/etc/codex/skills`; bundled system skills (`skill-creator`, `skill-installer`). `.claude/skills` is **not** scanned. Symlinked skill folders are followed. (same, "Where Codex loads local skills")
- **Frontmatter honoured**: `name` and `description` are required; no other frontmatter field is documented. Codex-specific extras live in a sidecar `agents/openai.yaml`: `interface.*` (display name, icons, `default_prompt`), `policy.allow_implicit_invocation` (default true), `dependencies.tools[]` (MCP servers to install). (same, "Optional metadata")
- **Invocation**: explicit with `/skills` or `$skill-name`; implicit by description match. (same, "How ChatGPT and Codex use skills")
- **Context budget**: the initial list (name, description, file path) uses at most 2% of the context window, or 8,000 characters when unknown; descriptions are shortened first and skills may be omitted with a warning; `skills.max_context_tokens` caps at 10,000. (same)
- **Collisions**: same-named skills are not merged; both appear. (same)
- **Changes** are picked up automatically; restart if not. (same)
- **Differences from Claude Code skills**:
  - Location: `.agents/skills` instead of `.claude/skills`. (`LC/docs-build-skills-md` vs `CC/docs-en-skills-md`)
  - Trigger syntax `$name` instead of `/name`.
  - "Do not auto-invoke" is `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, not `disable-model-invocation` frontmatter.
  - Claude Code's frontmatter extras (`allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `hooks`, `paths`, `arguments`, `argument-hint`, `user-invocable`, `shell`) are listed in `CC/docs-en-skills-md` and have no documented Codex equivalent. The skills CLI table says `context: fork` and skill hooks are Claude Code only among these three. (`RAW/vercel-labs-skills-main-docs-agents-md`, "Compatibility")
  - Whether Codex tolerates unknown frontmatter keys is not documented (open question).

### Custom commands / prompts, subagents / agent definitions, hooks or plugins, rules or path-scoped instructions

- **Custom commands**: "Custom prompts are deprecated." They live only in `~/.codex/prompts/*.md` (top level only), are invoked as `/prompts:<name>`, with frontmatter `description`, `argument-hint` and placeholders `$1`-`$9`, `$ARGUMENTS`, `$NAME`, `$$`. They are "not shared through your repository". Use skills instead. (`LC/docs-custom-prompts-md`). The import flow maps Claude Code slash commands to skills. (`LC/docs-import-md`, "What ChatGPT can import")
- **Subagents**: one TOML file per agent in `.codex/agents/` (project) or `~/.codex/agents/` (personal). Required keys `name`, `description`, `developer_instructions`; optional `model`, `model_reasoning_effort`, `model_reasoning_summary`, `model_verbosity`; capability switches `features.shell_tool`, `features.apps`, `features.plugins`, `features.memories`, `features.request_permissions_tool`; `skills.config`, `skills.bundled.enabled`, `skills.include_instructions`. The `name` field, not the filename, is the identity; a custom name overrides a built-in (`default`, `worker`, `explorer`). (`LC/docs-agent-configuration-subagents-md`, "Custom agents")
  - Limits: "They inherit the parent's permissions, provider, and MCP servers; a custom agent file can't override those settings." A "do not edit" agent is an instruction, not a read-only sandbox. (same)
  - Triggering: on a direct request or when `AGENTS.md`/skill instructions ask for delegation; `/subagents` to inspect. (same)
- **Hooks**: `.codex/hooks.json` or `[hooks]` in `.codex/config.toml` (both loaded and warned about if both exist in one layer); hooks from all layers run, higher layers do not replace lower ones. (`LC/docs-hooks-md`, "Where Codex looks for hooks")
  - Events: `SessionStart`, `SessionEnd`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SubagentStart`, `SubagentStop`, `Stop`, `Interrupt`, `PreModelRequest`, `PostModelRequest`. (same, table at top)
  - Shape: `{"hooks": {"<Event>": [{"matcher": "<regex>", "hooks": [{"type": "command", "command": "...", "timeout": <seconds>, "statusMessage": "...", "async": false, "additionalContextLimit": 2500}]}]}}`. Handler types `command` and `mcp_tool` work; "`prompt` and `agent` handlers are parsed but skipped". (same, "Config shape")
  - Tool names for matchers: `Bash`, `apply_patch` (also matches `Edit` or `Write`), `mcp__server__tool`, other local tools by function name, `spawn_agent` also as `Agent`. Hosted tools such as `WebSearch` are not hookable. (same, "Tool coverage")
  - Contract: JSON on stdin with `session_id`, `transcript_path`, `cwd`, `hook_event_name`, `model`, plus per-event fields (`tool_name`, `tool_input`, `tool_response`, `prompt`, ...). Block with `hookSpecificOutput.permissionDecision: "deny"`, the older `{"decision":"block"}`, or exit code 2 with the reason on stderr. `PreToolUse` can rewrite with `permissionDecision: "allow"` plus `updatedInput`. `permissionDecision: "ask"` is not supported. `Stop` with `decision: "block"` continues the turn using `reason` as the next prompt. (same, per-event sections)
  - Operational: default timeout 600 s (1 s, max 3 s for `SessionEnd`/`Interrupt`); matching command hooks for one event start concurrently; commands run with the session cwd, so repo hooks should resolve from `git rev-parse --show-toplevel`; hook output over about 2,500 tokens is spilled to a temp file. (same)
  - Caveat from the source: "Treat tool hooks as a useful guardrail, not a complete enforcement boundary." (same, "Tool coverage")
- **Plugins**: installable bundles of skills, MCP servers and hooks with a `.codex-plugin/plugin.json` manifest; hooks default to `hooks/hooks.json` in the plugin; Codex sets `PLUGIN_ROOT`/`PLUGIN_DATA` and also `CLAUDE_PLUGIN_ROOT`/`CLAUDE_PLUGIN_DATA` "for compatibility with existing plugin hooks". A local marketplace root contains `.agents/plugins/marketplace.json`. (`LC/docs-hooks-md`, "Plugin-bundled hooks"; `LC/docs-config-file-config-reference-md`, `marketplaces.<name>.source`). The plugin pages themselves were not read.
- **Rules / path-scoped instructions**: Codex "rules" are command execution policy (above), not instructions. The only path scoping for instructions is a nested `AGENTS.md`/`AGENTS.override.md`, and only on the path from root to cwd. There is no glob-scoped rule file. (`LC/docs-agent-configuration-rules-md`, `LC/docs-agent-configuration-agents-md-md`)

### Non-interactive / headless use and CI

- `codex exec "<prompt>"` (alias `codex e`); progress on stderr, only the final message on stdout; stdin piped plus a prompt argument means "prompt + context"; `codex exec -` reads the whole prompt from stdin. (`LC/docs-non-interactive-mode-md`)
- "By default, `codex exec` runs in a read-only sandbox." Use `--sandbox workspace-write` to allow edits, `--sandbox danger-full-access` only in an isolated runner. `--full-auto` "is no longer supported"; `--approve-for-me` routes approvals through automatic review. (same, "Permissions and safety")
- Other flags named in the text: `--json` (JSONL events `thread.started`, `turn.*`, `item.*`, `error`), `-o/--output-last-message`, `--output-schema <schema.json>`, `--ephemeral`, `--skip-git-repo-check` (a Git repo is required otherwise), `--ignore-user-config` (skip `$CODEX_HOME/config.toml`), `--ignore-rules` (skip user and project `.rules`), `--profile`, `--worktree`, `codex exec resume --last | <SESSION_ID>`, `codex exec fork`. (same; `LC/docs-developer-commands-md-b96a28`, "`codex exec`")
- In non-interactive runs, anything needing a fresh approval fails rather than prompting. (`LC/docs-agent-configuration-subagents-md`, "Approvals and sandbox controls")
- A `required = true` MCP server that fails to start makes `codex exec` exit with an error. (`LC/docs-non-interactive-mode-md`)
- Auth: `CODEX_API_KEY` set inline for the one invocation; do not set it job-wide where repo-controlled code runs. (same, "Use API key auth")
- GitHub: `openai/codex-action@v1` with inputs `prompt` | `prompt-file`, `codex-args`, `model`, `effort`, `sandbox`, `output-file`, `codex-version`, `codex-home`, `safety-strategy` (default `drop-sudo`), `allow-users`, `allow-bots`; output `final-message`. It starts a Responses API proxy so the key is not exposed to other steps. (`LC/docs-github-action-md`)
- Hook trust in automation: `--dangerously-bypass-hook-trust`, described as "For one-off automation that already vets hook sources outside Codex". (`LC/docs-hooks-md`, "Review and trust hooks")
- Linux prerequisite: `sudo apt install bubblewrap`; Ubuntu may need the `bwrap-userns-restrict` AppArmor profile. (`LC/docs-sandboxing-md`, "Prerequisites")
- Not documented in what was read: how a fresh CI runner marks the checkout as trusted so that `.codex/config.toml`, project hooks and rules load (open question).

### Using other model providers

- **Where**: only `~/.codex/config.toml` (or `$CODEX_HOME/config.toml`, or a profile file). Project config cannot do it. (`LC/docs-config-file-config-advanced-md`, "Project config files")
- **Shape** (top-level keys must come before the first table):

  ```toml
  model = "<model id the endpoint accepts>"
  model_provider = "<id>"

  [model_providers.<id>]
  name = "<label>"
  base_url = "https://<host>/v1"
  env_key = "<ENV_VAR_WITH_KEY>"
  wire_api = "responses"
  ```

  (`LC/docs-enterprise-connect-to-a-gateway-md`, "Configure the provider" and "Use an API key"; `LC/docs-config-file-config-advanced-md`, "Custom model providers")
- **Protocol requirement**: the endpoint must accept `POST /v1/responses` with streaming, tool calls and replayed input. "A working Chat Completions or Anthropic Messages endpoint doesn't establish Responses compatibility." (`LC/docs-enterprise-gateway-compatibility-md`, "Requests and endpoints")
- **Auth options**: `env_key` (bearer from an environment variable), `env_http_headers` (custom header), `[model_providers.<id>.auth]` command helper, `requires_openai_auth = true`, or none for local models. (`LC/docs-auth-md`, "Alternative model providers")
- **Model metadata**: a model name Codex does not know needs a catalog (`model_catalog_json` or the provider's `model_catalog_url`). (`LC/docs-enterprise-connect-to-a-gateway-md`, "Configure your model catalog"). A third-party page says that without one Codex "uses generic defaults for them and prints a warning". (`OC2/docs-console-harnesses-codex`)
- **Worked third-party example** (OpenCode Console as a translating gateway, with `kimi-k3` as the model): `base_url = "https://opencode.ai/inference/go/openai/v1"`, `env_key = "OPENCODE_API_KEY"`, `wire_api = "responses"`, in `~/.codex/config.toml`. (`OC2/docs-console-harnesses-codex`)
- **GLM, DeepSeek, Kimi specifically**: none of the three is mentioned in the Codex docs read. Inference: they are usable from Codex only through an endpoint that speaks the Responses API (their own, if they offer one, or a translating gateway). Whether Z.AI, DeepSeek or Moonshot expose a Responses endpoint was not checked.
- `--oss` with `oss_provider = "ollama" | "lmstudio"` selects a local provider. (`LC/docs-config-file-config-advanced-md`, "OSS mode")

### Trust/security model for project config

- **Project trust**: untrusted means Codex "skips project-scoped `.codex/` layers, including project-local config, hooks, and rules. User and system config still load". (`LC/docs-config-file-config-basic-md`). Codex "may also start in `read-only` until you explicitly trust the working directory (for example, via an onboarding prompt or `/permissions`)". (`LC/docs-agent-approvals-security-md`, "Defaults and recommendations")
- **Hooks need a second, per-hook review**: "Non-managed hooks must be reviewed and trusted before they run." Trust is recorded against the hook's hash, so a changed hook is skipped until re-reviewed in `/hooks`. (`LC/docs-hooks-md`, "Review and trust hooks")
- **MCP servers**: project servers load only in trusted projects; no separate per-server prompt is described. Destructive-annotated MCP/app tool calls always require approval. (`LC/docs-extend-mcp-md`; `LC/docs-agent-approvals-security-md`, "Sandbox and approvals")
- **Skills and AGENTS.md**: the docs read do not say these are gated by project trust (the trust text names `.codex/` layers only). Open question.
- **Sandbox**: macOS Seatbelt, Linux `bwrap` + `seccomp`, Windows MXC. Default for a versioned folder is workspace-write with on-request approvals and network off. `.git`, `.agents`, `.codex`, `.aws` inside a writable root are read-only, recursively. (`LC/docs-agent-approvals-security-md`, "OS-level sandbox", "Protected paths in writable roots")
- **Project config cannot redirect credentials or telemetry** (the ignored-key list above). (`LC/docs-config-file-config-advanced-md`)
- **Admin layer** exists (`requirements.toml`, `allow_managed_hooks_only`), not relevant to a solo setup; not read in detail.

---

## 2. OpenCode (installed 1.3.10 = V1; live docs = V2)

### Instruction files

- **V1 (1.3.10)**: project `AGENTS.md`; global `~/.config/opencode/AGENTS.md`; Claude fallbacks: project `CLAUDE.md` "used if no `AGENTS.md` exists" and `~/.claude/CLAUDE.md`. Lookup order: local files "by traversing up from the current directory (`AGENTS.md`, `CLAUDE.md`)", then the global file, then the Claude global file. "The first matching file wins in each category." (`OC1/rules`, "Precedence")
  - Switches: `OPENCODE_DISABLE_CLAUDE_CODE=1`, `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1`, `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1`. (`OC1/rules`, "Claude Code Compatibility")
  - Extra files: `"instructions": ["CONTRIBUTING.md", "docs/*.md", "https://..."]` in `opencode.json`; globs and URLs allowed; remote fetch has a 5 second timeout; all are "combined with your `AGENTS.md` files". (`OC1/rules`, "Custom Instructions")
  - Imports: none. "opencode doesn't automatically parse file references in `AGENTS.md`"; use `instructions` or tell the model to read `@file` lazily. (`OC1/rules`, "Referencing External Files")
  - Size limits: none stated.
- **V2**: only `AGENTS.md`. "V2 currently only discovers `AGENTS.md`", and the migration guide says to move `CLAUDE.md` guidance into it. (`OC2/docs-migrate-v1`)
  - Loads the global file, then every `AGENTS.md` from the workspace directory up toward home (stopping at the project root for projects outside home); combined, conflicts not resolved. (`OC2/docs-instructions`)
  - Nested files **below** the workspace load lazily when the agent reads a file or lists a directory there; edits to global/upward files are detected live. (same)
  - `OPENCODE_DISABLE_PROJECT_CONFIG=1` skips project `AGENTS.md` discovery. (same)
  - Prompt order: agent/provider system prompt, tool guidance, MCP/reference/skill guidance, `AGENTS.md` files then configured `instructions`, date and environment. (same)

### Project-level config

- **V1 files**: `opencode.json` or `opencode.jsonc` in the project root (found from the cwd up to the nearest Git directory), plus a `.opencode/` directory with `agents/`, `commands/`, `modes/`, `plugins/`, `skills/`, `tools/`, `themes/` (singular names also accepted). Project TUI settings: `tui.json` beside it. Schema `https://opencode.ai/config.json`. (`OC1/config`, "Locations")
- **V1 precedence, later wins**: remote `.well-known/opencode`; global `~/.config/opencode/opencode.json`; `OPENCODE_CONFIG` file; project `opencode.json`; `.opencode` directories; `OPENCODE_CONFIG_CONTENT`. Files are merged, not replaced. (`OC1/config`, "Precedence order")
- **V1 keys** (`OC1/config` unless noted):
  - Model/provider: `model` (`provider/model`), `small_model`, `provider.<id>.{npm, name, options.{baseURL, apiKey, headers, timeout, chunkTimeout, setCacheKey}, models.<id>.{name, limit.{context,output}, variants}}`, `disabled_providers`, `enabled_providers`. (`OC1/providers`, "Custom provider")
  - Permissions: `permission` (string, or map per tool: `read`, `edit`, `glob`, `grep`, `list`, `bash`, `task`, `skill`, `lsp`, `question`, `webfetch`, `websearch`, `codesearch`, `external_directory`, `doom_loop`), values `allow | ask | deny`, optionally a pattern map where the **last matching rule wins**; legacy `tools` booleans. (`OC1/permissions`)
  - MCP: `mcp.<name>` with `type: "local"` (`command` array, `environment`, `enabled`, `timeout` default 5000 ms) or `type: "remote"` (`url`, `headers`, `oauth` object or `false`, `enabled`, `timeout`). (`OC1/mcp-servers`)
  - Agents/commands/plugins: `agent`, `default_agent`, `command`, `plugin`.
  - Other: `instructions`, `formatter`, `watcher.ignore`, `compaction.{auto,prune,reserved}`, `snapshot`, `share`, `autoupdate`, `server`, `experimental`.
  - Substitution: `{env:VAR}` (empty string if unset) and `{file:path}` inside string values. (`OC1/config`, "Variables")
- **V1 environment variables**: `OPENCODE_CONFIG`, `OPENCODE_CONFIG_DIR`, `OPENCODE_CONFIG_CONTENT`, `OPENCODE_TUI_CONFIG`, `OPENCODE_PERMISSION` (inline JSON), `OPENCODE_DISABLE_AUTOUPDATE`, `OPENCODE_DISABLE_DEFAULT_PLUGINS`, `OPENCODE_DISABLE_CLAUDE_CODE*`, `OPENCODE_DISABLE_MODELS_FETCH`, `OPENCODE_MODELS_URL`, `OPENCODE_SERVER_PASSWORD`, and more. (`OC1/cli`, "Environment variables")
- **What is user-level only in V1**: credentials entered with `/connect` go to `~/.local/share/opencode/auth.json`; MCP OAuth tokens to `~/.local/share/opencode/mcp-auth.json`; npm plugins are cached in `~/.cache/opencode/node_modules/`. Everything else above has a project form. (`OC1/providers`, "Credentials"; `OC1/mcp-servers`, "Authenticating"; `OC1/plugins`)
  - An API key can stay out of the user store by using `"apiKey": "{env:VAR}"` in project config. (`OC1/providers`, custom provider example)
- **V2 differences that affect a sync** (`OC2/docs-config`, `OC2/docs-migrate-v1`):
  - Project files: `<project>/opencode.json(c)` **and** `<project>/.opencode/opencode.json(c)`; "every discovered `.opencode` config overrides every direct config". System config (`/etc/opencode`) outranks everything.
  - V1 keys still load; native names are plural or renamed: `provider` -> `providers` (`npm` -> `package`, `api`/`options.baseURL` -> `settings.baseURL`), `permission` -> ordered `permissions` array of `{action, resource, effect}` (`bash` -> `shell`, `task` -> `subagent`, `write`/`patch` -> `edit`), `agent` -> `agents` (`prompt` -> `system`, `disable` -> `disabled`), `command` -> `commands` (`subtask` -> `subagent`), `mcp.<name>` -> `mcp.servers.<name>` (`enabled` -> `disabled`), `plugin` -> `plugins`, `snapshot` -> `snapshots`, `skills.{paths,urls}` -> `skills: [...]`.
  - New `policies` array (binary allow/deny on `provider.use`, `tool.use`, `mcp.use`, `skill.use`, `plugin.use`, `integration.*`, `websearch.use`); policies from broader config beat project config. (`OC2/docs-policies`)
  - User-level only in V2: terminal client settings in the single global `~/.config/opencode/cli.json` ("V2 client configuration is global"); `update` ("Project-level values are ignored"); desktop GUI plugins need the global config; `opencode plugin add` writes global config. (`OC2/docs-migrate-v1`, `OC2/docs-config`, `OC2/docs-plugins`)
  - LSP config is accepted but V2 "does not run language servers". (`OC2/docs-migrate-v1`)

### Skills

- **Supported in both generations.**
- **V1 directories**: project `.opencode/skills/<name>/SKILL.md`, `.claude/skills/<name>/SKILL.md`, `.agents/skills/<name>/SKILL.md`; the same three under `~/.config/opencode/`, `~/.claude/`, `~/.agents/`. Project paths are collected walking up from the cwd to the git worktree. (`OC1/skills`, "Place files", "Understand discovery")
- **V1 frontmatter**: only `name` (required; must match the directory; `^[a-z0-9]+(-[a-z0-9]+)*$`, 1-64 chars), `description` (required, 1-1024 chars), `license`, `compatibility`, `metadata` (string map). "Unknown frontmatter fields are ignored." (`OC1/skills`)
- **V1 invocation**: the model calls the native `skill` tool; the catalogue (`<available_skills>` with name and description) sits in that tool's description. Gate with `permission.skill` patterns (`allow`/`deny`/`ask`), or disable per agent with `tools: { skill: false }`. No user-side `/skill` trigger is documented in V1. (`OC1/skills`)
- **V1 troubleshooting note**: "Ensure skill names are unique across all locations". (`OC1/skills`, "Troubleshoot loading")
- **V2 changes**: the skill ID comes from the **path**, `name` is only a display label; flat `skills/<id>.md` files are allowed; `metadata.opencode/autoinvoke: false` or `disable-model-invocation: true` hides a skill from the model; `license` and `compatibility` are accepted but not interpreted; the name pattern and description length are not enforced; users can load a skill with `@skill-id`; extra sources via `"skills": ["./dir", "https://..."]`; duplicate IDs resolve by registration order (built-ins, `.claude/skills`, `.agents/skills`, `~/.config/opencode/skills`, project `.opencode/skills`, config entries; later wins). (`OC2/docs-skills`)
- **Differences from Claude Code skills**: no `/name` slash invocation, no `allowed-tools`, `model`, `context: fork`, `hooks`, `paths` or argument substitution in V1; only V2 understands `disable-model-invocation`. (`OC1/skills`, `OC2/docs-skills`, `CC/docs-en-skills-md`)

### Custom commands / prompts, subagents / agent definitions, hooks or plugins, rules or path-scoped instructions

- **Commands (V1)**: `.opencode/commands/<name>.md` (or `command` in `opencode.json`); filename is the command name; frontmatter `description`, `agent`, `model`, `subtask`; body is the template; placeholders `$ARGUMENTS`, `$1`..; `` !`cmd` `` injects shell output; `@path` inlines a file. A custom command can override a built-in. (`OC1/commands`)
  - V2: same location; `subtask` -> `subagent` (runs in a background child session); `model` may carry `#variant`; nested paths become `/team/review`; **`@path` is no longer expanded** in stored templates; files hot-reload. (`OC2/docs-commands`)
- **Agents (V1)**: `.opencode/agents/<name>.md` (or `agent` in `opencode.json`); filename is the agent name; body is the prompt; frontmatter `description` (required), `mode` (`primary | subagent | all`, default `all`), `model`, `temperature`, `top_p`, `steps`, `permission`, `tools` (deprecated), `hidden`, `color`, `disable`, plus pass-through provider options. Built-ins: `build`, `plan` (primary); `general`, `explore` (subagents). Subagents are invoked by the model through the Task tool or by the user with `@name`; `permission.task` limits which subagents an agent may call. (`OC1/agents`)
  - V2: same location; default `mode` becomes `primary`; `permissions` is the ordered array; sampling settings move to model variants; a file using any of `permissions`, `request`, `system`, `disabled` is read as V2 and its V1 fields are ignored with a warning, so do not mix. (`OC2/docs-agents`, `OC2/docs-migrate-v1`)
- **Hooks**: there is no declarative hook file. Hooks are code in a plugin.
  - V1: `.opencode/plugins/*.{js,ts}` are "automatically loaded at startup"; npm plugins via `"plugin": [...]`. A plugin exports `async ({ project, client, $, directory, worktree }) => ({ ...hooks })`. Hook names include `tool.execute.before`, `tool.execute.after`, `shell.env`, `event` (for `session.idle`, `file.edited`, `permission.asked`, ...), `experimental.session.compacting`, and `tool` for custom tools. Throwing in `tool.execute.before` blocks the call. Dependencies come from `.opencode/package.json`, installed with `bun install` at startup. (`OC1/plugins`)
  - V2: "V1 plugin implementations do not run in V2." New API: `export default Plugin.define({ id, async setup(ctx) { ... } })` from `@opencode/plugin`, registering through `ctx.tool.hook(...)`, `ctx.session.hook(...)`, `ctx.event.subscribe()`. Still discovered from `.opencode/plugins/`. (`OC2/docs-migrate-v1`, `OC2/docs-build-plugins`, `OC2/docs-build-plugins-migrate-v1`)
- **Rules / path-scoped instructions**: "Rules" in OpenCode means `AGENTS.md`. No glob-scoped rule files with frontmatter. Scoping options are nested `AGENTS.md` files and `instructions` globs (V1: all matched files are combined up front). (`OC1/rules`, `OC2/docs-instructions`)

### Non-interactive / headless use and CI

- **V1**: `opencode run [message..]` with `--command`, `--continue/-c`, `--session/-s`, `--fork`, `--share`, `--model/-m provider/model`, `--agent`, `--file/-f`, `--format default|json`, `--title`, `--attach <server url>`, `--port`. `opencode serve` runs a headless server that `run --attach` can reuse. (`OC1/cli`, "run")
  - No approval-bypass flag is listed for V1 `run`; how `ask` permissions behave there is not documented (open question). Permissions can be injected with `OPENCODE_PERMISSION` or `OPENCODE_CONFIG_CONTENT`. (`OC1/cli`)
  - GitHub: `opencode github install` / `opencode github run`; action inputs `model` (required), `agent`, `share`, `prompt`, `token`. (`OC1/cli`, `OC1/github`)
- **V2**: `opencode run --standalone --model <p/m> "<prompt>"` in CI with the provider key as an environment secret; `--auto` ("Auto-approve permissions that are not explicitly denied"), `--format json`, `--archived`, `--agent`, `--file`, `--continue`, `--session`. (`OC2/docs-cli-commands`)

### Using other model providers

- **V1, built-in directory** includes DeepSeek, Moonshot AI ("To use Kimi K2 from Moonshot AI") and Z.AI (with a separate "Z.AI Coding Plan" entry for the GLM Coding Plan). The documented flow is `/connect` then `/models`, which stores the key at user level. (`OC1/providers`, sections "DeepSeek", "Moonshot AI", "Z.AI")
  - The docs do not give these providers' IDs or environment variable names (open question), so a project-only setup is safest with an explicit provider entry.
- **V1, any OpenAI-compatible endpoint, fully in project `opencode.json`**:

  ```json
  {
    "$schema": "https://opencode.ai/config.json",
    "model": "myprovider/my-model-name",
    "provider": {
      "myprovider": {
        "npm": "@ai-sdk/openai-compatible",
        "name": "My Provider",
        "options": { "baseURL": "https://api.myprovider.com/v1", "apiKey": "{env:MYPROVIDER_API_KEY}" },
        "models": { "my-model-name": { "name": "My Model", "limit": { "context": 200000, "output": 65536 } } }
      }
    }
  }
  ```

  `@ai-sdk/openai-compatible` is for `/v1/chat/completions`; "If your provider/model uses `/v1/responses`, use `@ai-sdk/openai`." (`OC1/providers`, "Custom provider"). The `model` line and the placeholder names are mine; the structure is from the source.
- **V1, Anthropic-compatible route**: the docs show overriding `provider.anthropic.options.baseURL`. (`OC1/providers`, "Base URL"). Inference: a second provider entry with `"npm": "@ai-sdk/anthropic"` and its own `baseURL` would give a named Anthropic-compatible provider; the docs do not show that exact entry.
- **V2**: `providers.<id>.{name, env: ["VAR"], package, settings.baseURL, headers, body, models}`; packages include `@opencode/ai/providers/openai-compatible`, `.../openai-compatible/responses` and `@opencode/ai/providers/anthropic-compatible`. (`OC2/docs-providers`)
- **Per-agent and per-command models**: `model:` in agent and command frontmatter. (`OC1/agents`, `OC1/commands`)

### Trust/security model for project config

- **No trust prompt is documented** in any fetched OpenCode page (keyword scan for "trust" across V1 and V2 pages found only unrelated uses).
- **Permissive defaults (V1)**: "By default, opencode **allows all operations** without requiring explicit approval." Exceptions: `doom_loop` and `external_directory` default to `ask`; reading `*.env` and `*.env.*` is denied, `*.env.example` allowed. (`OC1/config`, "Permissions"; `OC1/permissions`, "Defaults")
- **V2 defaults are looser in two places**: `.env` reads `ask` instead of deny, and "external paths are not prompted unless you add a rule". (`OC2/docs-permissions`)
- **Project plugins are executable code loaded at startup**, and their npm dependencies are installed at startup. (`OC1/plugins`). Inference: opening an untrusted repo in OpenCode runs that repo's plugin code; nothing in the docs gates it.
- **No OS sandbox is described.** Permissions are the only control. (absence across fetched pages)
- **"Always" approvals**: V1 keeps them "for the rest of the current OpenCode session"; V2 saves them as durable project-scoped allow rules that never override a configured deny. (`OC1/permissions`, "What “Ask” Does"; `OC2/docs-permissions`)
- **V2 hard limits**: policies in global or managed config outrank project config, and two built-in plugins cannot be disabled by a repository. (`OC2/docs-policies`, `OC2/docs-plugins`)

---

## 3. AGENTS.md (agents.md)

### Instruction files

- A plain Markdown file named `AGENTS.md`, "a simple, open format for guiding coding agents" (`RAW/agentsmd-agents-md-main-readme-md`); suggested sections are project overview, build and test commands, code style, testing, security. Nested `AGENTS.md` files for monorepo subprojects are a named pattern. (`agents.md/index`)
- The page claims use by over 60k open-source projects and says the format is now stewarded by the Agentic AI Foundation under the Linux Foundation; origin credited to OpenAI Codex, Amp, Jules, Cursor and Factory. (`agents.md/index`, top and "About")
- Migration tip from the site: rename and symlink, `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`. (`agents.md/index`, FAQ)
- **No schema, required fields, size limit, import syntax or precedence rule could be confirmed**: the FAQ answers did not survive the fetch. Each harness defines its own discovery (sections 1 and 2).
- Compatibility facts gathered elsewhere:
  - Codex: native, with `AGENTS.override.md`. (`LC/docs-agent-configuration-agents-md-md`)
  - OpenCode: native; `/init` creates it. (`OC1/rules`)
  - Claude Code: reads `AGENTS.md` and `.claude/AGENTS.md` when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` exists in the cwd or above; "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later." It expands `@path` imports inside it. It does **not** read `AGENTS.override.md`, `AGENTS.local.md` "or anything under a `.agents/` directory". A setting value `claude-md-and-agents-md` loads both. (`CC/docs-en-memory-md`, "AGENTS.md")
  - Gemini CLI and Aider need a config line to read it. (`agents.md/index`, FAQ)

### Project-level config

Not applicable: the standard defines one file, no config.

### Skills

Not applicable (see section 4).

### Custom commands / prompts, subagents / agent definitions, hooks or plugins, rules or path-scoped instructions

Not defined by the standard. Path scoping is by directory only (nested files).

### Non-interactive / headless use and CI

Not applicable.

### Using other model providers

Not applicable.

### Trust/security model for project config

Nothing stated in the saved text.

---

## 4. Agent Skills spec (agentskills.io) and the `.agents/` convention

### Instruction files

Not applicable.

### Project-level config

- The spec defines the inside of a skill folder only. "the Agent Skills specification does not mandate where skill directories live". (`agentskills.io/client-implementation-adding-skills-support-md`, "Where to scan")
- The convention: scan a client-specific directory and `.agents/skills/`, at project and user level. "The `.agents/skills/` paths have emerged as a widely-adopted convention for cross-client skill sharing." Some clients also scan `.claude/skills/` "for pragmatic compatibility". (same)
- Other things seen under `.agents/`: Codex plugin marketplaces at `.agents/plugins/marketplace.json` (`LC/docs-config-file-config-reference-md`); rulesync writes non-root rules to `.agents/rules/` or `.agents/memories/` for some targets (`RAW/dyoshikawa-rulesync-main-readme-md`, `rulesync.dyoshikawa.com/guide-configuration`). No source defines `.agents/` as a general standard beyond skills.

### Skills

- **Layout**: `<skill-name>/SKILL.md` required; optional `scripts/`, `references/`, `assets/`. (`agentskills.io/specification-md`, "Directory structure")
- **Frontmatter** (`agentskills.io/specification-md`, "Frontmatter"):

  | Field | Required | Constraint |
  |---|---|---|
  | `name` | yes | 1-64 chars, lowercase `a-z`, `0-9`, hyphens; no leading/trailing/double hyphen; must match the parent directory |
  | `description` | yes | 1-1024 chars; what it does and when to use it |
  | `license` | no | name or bundled file |
  | `compatibility` | no | max 500 chars |
  | `metadata` | no | string-to-string map |
  | `allowed-tools` | no | space-separated string; "Experimental" |

- **Budgets**: metadata about 100 tokens per skill at startup; `SKILL.md` body under 5,000 tokens recommended and under 500 lines; references one level deep. (same, "Progressive disclosure", "File references")
- **Validation tool**: `skills-ref validate ./my-skill`. (same, "Validation")
- **Client guidance worth copying into a sync script's checks** (`agentskills.io/client-implementation-adding-skills-support-md`):
  - Project skills override user skills on a name collision; warn on shadowing.
  - Clients should load leniently (name mismatch: warn; missing description: skip).
  - Unquoted colons in `description` are the most common YAML breakage across clients.
  - Activation is either a file read of `SKILL.md` or a dedicated tool; user activation is typically `/skill-name` or `$skill-name`.
  - `disable-model-invocation` is mentioned as an example opt-out flag, not as a spec field.
- **Origin**: the format was originally developed by Anthropic and released as an open standard. (`agentskills.io/home-md`, "Open development")
- **Who reads which directory** (from the harness docs, not the spec): Claude Code `.claude/skills`; Codex `.agents/skills`; OpenCode `.opencode/skills`, `.claude/skills`, `.agents/skills`.

### Custom commands / prompts, subagents / agent definitions, hooks or plugins, rules or path-scoped instructions

Not defined. The implementation guide describes running a skill in a subagent as an optional pattern "only supported by some clients".

### Non-interactive / headless use and CI

Not applicable.

### Using other model providers

Not applicable.

### Trust/security model for project config

- The guide recommends gating project-level skills on a trust check so that "untrusted repositories" cannot silently inject instructions, and allow-listing skill directories for reads. It is advice to client authors, not a requirement. (`agentskills.io/client-implementation-adding-skills-support-md`, "Trust considerations", "Permission allowlisting")

---

## 5. Sync tools

The seven subsections are collapsed into one line each per tool, since most do not apply.

### rulesync (dyoshikawa/rulesync, v43.8.0, 2026-11-08, MIT)

- **Instruction files**: source of truth is `.rulesync/` plus `rulesync.jsonc`; generates each tool's rule files; the `agentsmd` target emits root `AGENTS.md` and can nest rules as `<dir>/AGENTS.md` derived from a rule's globs. (`rulesync.dyoshikawa.com/guide-configuration`)
- **Project-level config**: `rulesync.jsonc` with `targets` (for us: `claudecode`, `codexcli`, `opencode` for 2.x, `opencodev1` for 1.x), `features` (`rules`, `ignore`, `mcp`, `commands`, `subagents`, `skills`, `hooks`, `permissions`), `outputRoots`, `delete`, `global`, `simulateCommands/Subagents/Skills`, `preserveUnownedHooks`, `sources`. (same)
- **Skills**: generated for all three harnesses; `rulesync fetch <owner/repo>` and declarative `sources` install third-party skills. (`RAW/dyoshikawa-rulesync-main-readme-md`)
- **Commands, subagents, hooks, rules**: all three harnesses are ticked for rules, MCP, commands, subagents, skills, hooks and permissions, with one caveat in the source: "Codex CLI `commands` is global-only". By default a regenerated hooks file replaces the destination's hook list wholesale; with `preserveUnownedHooks` on, ownership is tracked in a `.rulesync-hooks-lock.json` beside each hooks file. (`RAW/dyoshikawa-rulesync-main-readme-md`; `rulesync.dyoshikawa.com/reference-supported-tools`; `rulesync.dyoshikawa.com/guide-configuration`)
- **Headless/CI**: CLI (`rulesync generate --targets ... --features ...`), also `import`, `convert --from --to`, `gitignore`. (`RAW/dyoshikawa-rulesync-main-readme-md`)
- **Other providers**: not covered.
- **Trust/security**: not discussed in what was read.
- The exact output paths per feature for Codex and OpenCode are on pages not fetched (file-formats reference).

### ruler (intellectronica/ruler, v0.3.46, 2026-10-22, MIT)

- **Instruction files**: concatenates `.ruler/*.md` (root `AGENTS.md` first, then `.ruler/AGENTS.md`, then the rest sorted) into each agent's file, each chunk prefixed with `<!-- Source: ... -->`. Claude Code gets `CLAUDE.md`; Codex and OpenCode get `AGENTS.md`. (`RAW/intellectronica-ruler-main-readme-md`, "The `.ruler/` Directory", "Supported AI Agents")
- **Project-level config**: `.ruler/ruler.toml`; MCP servers defined once and written to `.mcp.json` (Claude Code), `.codex/config.toml` (Codex), `opencode.json` (OpenCode). (same)
- **Skills**: "Skills support is currently experimental."; copies `.ruler/skills/` to `.claude/skills/`, `.agents/skills/` (Codex) and `.opencode/skills/`. (same, "Skills Support")
- **Commands, subagents, hooks, rules**: subagents experimental behind `--subagents` (`.claude/agents/`, `.codex/agents/*.toml`, `.opencode/agents/`); no hooks, permissions or commands in the sections read. (same)
- **Headless/CI**: `ruler apply`, `ruler revert`; writes `.bak` backups and adds generated files to `.gitignore` by default. (same)
- **Other providers**: the v0.3.46 notes mention OpenCode subagents "with per-agent provider and model selection". (`github.com/intellectronica-ruler-releases-latest`)
- **Trust/security**: not discussed in what was read.

### skills CLI (vercel-labs/skills, v1.8.0, 2026-11-10, MIT)

- **Instruction files / config / commands / providers**: not covered; it manages skills only.
- **Skills**: `npx skills add <owner/repo> [--skill x] [-a claude-code]`; "Skills are installed to the current project by default" (`-g` for global). Project paths: Claude Code `.claude/skills/`; Codex `.agents/skills/`; OpenCode `.agents/skills/`. Also `find`, `list`, `use`, `check`, `update`, `remove`, `init`. (`RAW/vercel-labs-skills-main-readme-md`; `RAW/vercel-labs-skills-main-docs-agents-md`)
- **Reproducibility**: `skills-lock.json` version 2 stores a `computedHash` per skill (SHA-256 over path, length, content); `experimental_install` restores from the lock, `--frozen-lockfile` verifies. (`RAW/vercel-labs-skills-main-readme-md`, "Lock File Content Hash")
- **Headless/CI**: programmatic API `import { installSkills } from 'skills'`; requires Node.js 22.20 or later. (same)
- **Trust/security**: collects anonymous usage data and makes security-audit requests unless `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1`. (same, "Telemetry")

### Newer or smaller tools (discovered by search, READMEs not read, metadata from the GitHub API on 2026-11-10, not saved)

- `nicepkg/vsync` (63 stars, last release 2026-01-27), `x0c/agentsync` (9 stars, v1.1.0 2026-11-01), `nicolasakf/unity` (10 stars, no release), `dhvcc/code-agnostic` (3 stars, GPL-3.0, v0.3.11 2026-06-06). None has the adoption of the three above.
- For comparison, same API call: rulesync 1,597 stars, ruler 2,967, skills 38,866.

---

## (a) Compatibility matrix

Claude Code column: paths confirmed present in the corpus files named, but those pages were not re-read in full by me (other researchers own them). Codex column is docs-only (no binary here). OpenCode column is V1 (1.3.10) with V2 differences in brackets.

| | Claude Code | Codex CLI (0.167.0 docs) | OpenCode 1.3.10 [V2] |
|---|---|---|---|
| **Instruction file** | `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md`; reads `AGENTS.md` / `.claude/AGENTS.md` only when none of those exist (v2.1.277+); `@path` imports (`CC/docs-en-memory-md`) | `AGENTS.override.md` > `AGENTS.md` > `project_doc_fallback_filenames`, one per directory, root down to cwd; 32 KiB; no imports; no `CLAUDE.md` (`LC/docs-agent-configuration-agents-md-md`) | `AGENTS.md`, fallback `CLAUDE.md`; extra files via `instructions` in `opencode.json`; no imports (`OC1/rules`) [V2: `AGENTS.md` only, nested files load lazily (`OC2/docs-instructions`)] |
| **Skills dir** | `.claude/skills/<name>/SKILL.md`; nothing under `.agents/` (`CC/docs-en-skills-md`, `CC/docs-en-memory-md`) | `.agents/skills/<name>/SKILL.md` from cwd up to repo root; optional `agents/openai.yaml`; not `.claude/skills` (`LC/docs-build-skills-md`) | `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` (`OC1/skills`) [V2: same, plus flat `<id>.md` and `skills: []` config] |
| **Commands** | `.claude/commands/*.md` (still works; same as a skill) (`CC/docs-en-skills-md`) | none at project level; `~/.codex/prompts/*.md` is deprecated and user-only; use skills (`LC/docs-custom-prompts-md`) | `.opencode/commands/<name>.md` or `command` in `opencode.json` (`OC1/commands`) [V2: `commands`] |
| **Subagents** | `.claude/agents/*.md` (`CC/docs-en-sub-agents-md`) | `.codex/agents/*.toml` with `name`, `description`, `developer_instructions` (`LC/docs-agent-configuration-subagents-md`) | `.opencode/agents/<name>.md` or `agent` in `opencode.json` (`OC1/agents`) [V2: `agents`, new frontmatter keys] |
| **Hooks** | `hooks` in `.claude/settings.json` (`CC/docs-en-hooks-md`) | `.codex/hooks.json` or `[hooks]` in `.codex/config.toml`; Claude-style events; per-hook trust review (`LC/docs-hooks-md`) | none declarative; code plugins in `.opencode/plugins/*.{js,ts}` (`OC1/plugins`) [V2: new `Plugin.define` API, V1 plugins do not run] |
| **MCP config** | `.mcp.json` (`CC/docs-en-mcp-md`) | `[mcp_servers.<id>]` in `.codex/config.toml` (`LC/docs-extend-mcp-md`) | `mcp.<name>` in `opencode.json` (`OC1/mcp-servers`) [V2: `mcp.servers.<name>`] |
| **Permissions** | `permissions` in `.claude/settings.json` (`CC/docs-en-permissions-md`) | `approval_policy`, `approvals_reviewer` in `.codex/config.toml`; command rules in `.codex/rules/*.rules`; per-MCP-tool `approval_mode` (`LC/docs-config-file-config-reference-md`, `LC/docs-agent-configuration-rules-md`) | `permission` in `opencode.json` and agent frontmatter (`OC1/permissions`) [V2: ordered `permissions` array plus `policies`] |
| **Sandbox** | `sandbox` settings in `.claude/settings.json` (`CC/docs-en-sandboxing-md`; only the key's presence was checked) | `sandbox_mode` + `[sandbox_workspace_write]`, or `default_permissions` + `[permissions.<name>]`, in `.codex/config.toml`; OS-enforced (Seatbelt / bwrap+seccomp) (`LC/docs-agent-approvals-security-md`, `LC/docs-permissions-md`) | none documented |
| **Model/provider** (extra row) | not researched here | `model` in project config; **provider only in `~/.codex/config.toml`** (`LC/docs-config-file-config-advanced-md`) | `model` and `provider` in `opencode.json`, key via `{env:VAR}` (`OC1/providers`) |

## (b) Lowest-common-denominator layout, and what must be generated

Shared with no duplication (author once, all three read it):

- **`AGENTS.md` at the repo root**, with no `CLAUDE.md` / `CLAUDE.local.md` beside it, so Claude Code falls through to it. Keep it well under 32 KiB (Codex cap). Do not use `@imports` in it if Codex and OpenCode must see the same content, since only Claude Code expands them. Nested `AGENTS.md` files work in all three, with different loading rules (Codex: only root-to-cwd; OpenCode V2 and Claude Code: lazily for subdirectories). (sources in sections 1-3)
  - Inference: if Claude-only content is needed, a `CLAUDE.md` that imports `AGENTS.md` keeps one source, but OpenCode 1.3.10 would still read `AGENTS.md` (it wins over `CLAUDE.md`), so nothing breaks.
- **Skill folders in Agent Skills format with only `name` (matching the folder, lowercase kebab) and `description`** as the portable frontmatter; supporting files under `scripts/`, `references/`, `assets/`. OpenCode V1 ignores unknown keys, so Claude-only keys are harmless there; Codex behaviour with unknown keys is undocumented. (`OC1/skills`, `agentskills.io/specification-md`)
- **Hook logic as plain scripts** (for example under `tools/hooks/`), since Claude Code and Codex both pass JSON on stdin and accept exit code 2 to block. Only the registration files differ. Inference from `LC/docs-hooks-md`; field-level parity with Claude Code was not checked line by line.

Must be generated per harness:

1. **Skills location**: one canonical tree, mirrored. `.agents/skills/` is read by Codex and OpenCode; Claude Code needs `.claude/skills/`. Options: copy, or symlink (Codex "supports symlinked skill folders"; Claude Code's handling of a symlinked `.claude/skills` was not verified). With both trees present OpenCode sees every skill twice: V2 resolves by order (`.agents/skills` wins over `.claude/skills`); for 1.3.10 the docs only say names should be unique (open question). `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` stops OpenCode reading `.claude/skills`, but it is an environment variable, not project config.
2. **Skill extras**: Codex `agents/openai.yaml` (for example `policy.allow_implicit_invocation: false`) where Claude Code would use `disable-model-invocation: true`.
3. **Commands**: nothing for Codex (skills only); `.opencode/commands/*.md` if `/name` invocation is wanted in OpenCode; Claude Code can use the skill directly.
4. **Subagents**: `.claude/agents/*.md`, `.codex/agents/*.toml`, `.opencode/agents/*.md` from one definition (name, description, prompt, model, read-only flag). Codex cannot give a subagent its own sandbox or MCP set.
5. **Hook registration**: `.claude/settings.json`, `.codex/hooks.json`, and a small `.opencode/plugins/<x>.ts` shim that calls the same scripts from `tool.execute.before`/`after` (different shim for V1 and V2).
6. **MCP**: `.mcp.json`, `[mcp_servers.*]` in `.codex/config.toml`, `mcp` in `opencode.json`, from one server list.
7. **Permissions and sandbox**: three unrelated models; generate each from a shared intent list (allowed command prefixes, denied paths such as `.env`).
8. **Models/providers**: `opencode.json` can carry GLM/DeepSeek/Kimi providers in the repo. Codex cannot: it needs `~/.codex/config.toml`, or a repo-local launcher using `-c` overrides or `CODEX_HOME` (both inferences, see section 1), and a Responses-compatible endpoint.

Unavoidable per-machine state even with zero global config: Codex project trust and hook trust decisions; Codex and OpenCode credentials (unless supplied as environment variables); OpenCode MCP OAuth tokens.

## (c) Assessment of each sync tool

- **rulesync**: the only tool read that covers every row of the matrix for all three harnesses, including a separate `opencodev1` target that matches the installed OpenCode 1.3.10. Very actively released (v43.8.0 two days before this note). Costs: its own source format in `.rulesync/`, a 60-plus-tool surface, frequent behaviour changes (the latest notes open with "Behavior Changes"), Codex commands only in global mode, and the per-feature output paths were not verified here. Fit: plausible as the generator if adopting `.rulesync/` as the canonical format is acceptable; verify its Codex and OpenCode output against sections 1 and 2 on a scratch repo first.
- **ruler**: mature for rules + MCP; skills and subagents are flagged experimental; no hooks, permissions or commands. Its model is concatenating Markdown into generated files that it git-ignores, which is the opposite of committing a hand-written `AGENTS.md`. Its Codex MCP note is stale. Fit: poor for this goal.
- **skills CLI**: by far the most adopted, but it installs skills only. Its lock file with content hashes is a good mechanism for pinning third-party skills. Telemetry is on by default. Fit: useful as a component for vendored skills, not as the sync tool.
- **Small newer tools** (vsync, agentsync, unity, code-agnostic): too little adoption to depend on; not evaluated.
- **Small custom script** (Inference, my recommendation): the shared layer is already file-identical (`AGENTS.md`, skill folders, hook scripts), and what remains is eight small, well-specified generators for exactly three targets. A script in this repo gives exact control over the constraints that matter here (no writes outside the project, Codex's provider limitation, OpenCode V1 vs V2 key names) and can be tested against the formats documented above. rulesync is the fallback if the number of harnesses grows.

## (d) Open questions not settled by the docs

1. Codex: is `project_doc_max_bytes` a per-file or combined limit? (two pages disagree)
2. Codex: are `model_provider` / `model_providers` honoured when passed with `-c` on the command line? What exactly ends up inside the repo when `CODEX_HOME` points at `.codex/`?
3. Codex: are `.agents/skills` and `AGENTS.md` loaded in an untrusted project? The trust text names only `.codex/` layers.
4. Codex: how does a CI runner or `codex exec` mark a checkout trusted without touching `~/.codex/config.toml`?
5. Codex: does a `SKILL.md` with unknown (Claude Code) frontmatter keys load cleanly?
6. Codex: do DeepSeek, Moonshot (Kimi) or Z.AI (GLM) expose a Responses API endpoint, or is a translating gateway required?
7. Codex: the exact `codex exec` flag table (the docs render it from JavaScript; only flags named in prose are listed above).
8. OpenCode 1.3.10: does it load every `AGENTS.md` on the way up, or only the nearest ("first matching file wins in each category")?
9. OpenCode 1.3.10: what happens when the same skill name exists in both `.claude/skills` and `.agents/skills`?
10. OpenCode 1.3.10: how does `opencode run` treat an `ask` permission with no terminal?
11. OpenCode: provider IDs and environment variable names for the built-in DeepSeek, Moonshot AI and Z.AI entries (they come from models.dev, not the docs).
12. OpenCode: is there any gate before project plugins, MCP servers or `{file:...}` substitutions from a cloned repo take effect? None is documented.
13. OpenCode: should the template target V1 (installed 1.3.10) or V2 (current 2.2.7)? V2 keeps V1 config keys working but not V1 plugins or the `CLAUDE.md` fallback.
14. Claude Code: does it follow a symlinked `.claude/skills` directory or symlinked skill folders? (not checked; belongs to the Claude Code researchers)
15. agents.md: the FAQ answers (conflict resolution, required fields) and the list of compatible agents were not captured.
16. rulesync: exact files written for `codexcli`, `opencode` and `opencodev1` per feature, and the meaning of "Rulesync 14.x" next to a v43 release.
