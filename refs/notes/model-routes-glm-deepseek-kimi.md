# Model routes: GLM (Z.ai), DeepSeek, Kimi (Moonshot), plus Qwen, MiniMax, Gemini CLI

Date of research: 2026-11-10. Every vendor page below was fetched on 2026-11-10 with
`tools/refs article ... --collection model-routes`. Version or date stamps that the pages
themselves carry are given per fact. This area changes monthly: model IDs in particular
should be re-checked before they are written into a template.

Sources read: 71 pages read in full, 14 read in part (the sections named in "Per source"),
9 consulted only through a line search for a specific fact. 23 saved pages were not read and
are not used as evidence (listed in "(d) What I could not verify").
Could not be fetched: `docs.platform.qianwenai.com/*` (HTTP 403, direct and via the tool),
`platform.kimi.ai/docs/guide/product-plans.md` (empty body, direct and via jina),
`www.kimi.com/code/docs/en/third-party-tools/other-coding-agents.html` (404),
`deepseek-harness.github.io/deepseek-harness/en/index.md` (empty).

Source keys used below:
CC-model (model-config), CC-gw (llm-gateway), CC-gwc (llm-gateway-connect), CC-gws (gateways),
CC-3p (third-party-integrations), CC-env (env-vars), CC-cost (costs), CC-fast (fast-mode),
CC-adv (advisor), CC-set (settings-reference, `env` section only), CC-mcp (mcp, one section),
ZAI-* (docs.z.ai), DS-* (api-docs.deepseek.com), KP-* (platform.kimi.ai),
KC-* (www.kimi.com/code/docs), KCLI-* (moonshotai.github.io/kimi-code), MM-* (platform.minimax.io
and the MiniMax Code README), ALI-* (alibabacloud.com Model Studio), QW-* (Qwen Code docs),
GEM-* (geminicli.com), OC-* (opencode.ai), CX-* (learn.chatgpt.com Codex docs).

## Cross-cutting findings

1. Every vendor checked documents an Anthropic-compatible endpoint and an official Claude Code
   setup page built on the same variables: `ANTHROPIC_BASE_URL`, a token variable, and
   the per-tier model variables. Gemini is the exception: no such page was found.
   (ZAI-claude, DS-cc, KP-cc, KC-cc, MM-cc, ALI-cc)
2. Anthropic does not support this route. CC-gw, "Other LLM gateways" intro: "doesn't support
   routing Claude Code to non-Claude models through any gateway". It works because the vendors
   emulate the Messages API, so every Claude Code release can break it.
3. Claude Code picks a model by name, the endpoint only receives it. CC-model, "Available
   models" note: "`ANTHROPIC_BASE_URL` changes where requests are sent, not which model answers
   them." So all tiers must be mapped: `ANTHROPIC_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`,
   `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`,
   `ANTHROPIC_DEFAULT_FABLE_MODEL`, `CLAUDE_CODE_SUBAGENT_MODEL`. Kimi's docs say a partial
   mapping makes "the corresponding scenarios fail silently" (KP-cc, "Configuration Reference").
4. A settings-file `env` block beats the shell. CC-gwc, "Set in a settings file": "When both a
   shell export and a settings-file `env` block set the same variable, the settings-file value
   applies." Consequence for per-session switching: provider variables must not sit in any
   settings file that every session reads, or the launcher is overridden.
   (CC-gwc, CC-env "Precedence", CC-set, KP-cc, KC-cc)
5. Provider variables are allowed in a project `env` block (they are not in the list of
   variables project settings cannot set), but project and local `env` values apply only "after
   you trust the workspace, or at startup in `-p` mode" (CC-set, "When Claude Code applies `env`
   values"). Credentials do not belong there: CC-gwc warning, "Don't put the credential in a
   project's `.claude/settings.json`."
6. Shell-level variables are session-scoped by design. CC-model, "Setting your model": "The
   `--model` flag and `ANTHROPIC_MODEL` environment variable apply only to the session you
   launch with them." This is the documented basis for launcher scripts.
7. Unrecognised model IDs get a 200K window. CC-model, "Correct the window for a gateway or
   custom model ID": Claude Code "can't tell the model's context window and assumes 200K
   tokens". Two documented fixes: append `[1m]` to the ID, or set
   `CLAUDE_CODE_MAX_CONTEXT_TOKENS`. All vendors use one or both.
   (ZAI-claude, ZAI-latest, DS-cc, KP-cc, KC-cc, MM-cc, ALI-cc)
8. Features that need Anthropic's servers are lost on a vendor endpoint: the advisor tool
   (CC-adv), fast mode (CC-fast), Remote Control and voice dictation (CC-gwc), and everything
   behind feature-flag fetching when only `ANTHROPIC_AUTH_TOKEN` is set against a non-Anthropic
   host (CC-env, "First session after an install or upgrade").
9. Three vendors ship a real terminal harness of their own with project-level files: Kimi Code
   CLI (`kimi`), Qwen Code (`qwen`), MiniMax Code (`mcode`), plus Google's Gemini CLI
   (`gemini`). Z.ai ships ZCode, a desktop "Agentic Development Environment", not a CLI.
   DeepSeek has "DeepSeek Harness" in developer preview. (KCLI-start, QW-overview, MM-code,
   MM-readme, GEM-install, ZAI-zcode, DS-index)
10. `AGENTS.md` and `.agents/skills/` are the common denominators across the own harnesses:
    Kimi Code reads `AGENTS.md` / `.kimi-code/AGENTS.md` and `.agents/skills/` (KCLI-agents,
    KCLI-skills); Qwen Code reads `AGENTS.md` and `.agents/skills/` (QW-memory, QW-skills);
    Gemini CLI reads `.agents/skills/` and can be told to read `AGENTS.md` through
    `context.fileName` (GEM-skills, GEM-md); MiniMax Code writes `AGENTS.md` with `mcode init .`
    (MM-readme).
11. Codex cannot take a third-party provider from project config. CX-adv, "Project config
    files": Codex ignores `model_provider` and `model_providers` in a project
    `.codex/config.toml`. Every vendor's Codex guide therefore edits `~/.codex/config.toml`.
12. Every vendor's Codex route uses the OpenAI Responses protocol (`wire_api = "responses"`),
    and most need a `models.json` model catalog. (ZAI-codex, DS-codex, KP-codex, KC-codex,
    MM-codex)
13. OpenCode route is usually a built-in catalog provider selected with `opencode auth login` or
    `/connect`, which stores the credential outside the repo. OpenCode's own docs also allow a
    project `opencode.jsonc` provider entry that names an environment variable (OC-prov, OC-cfg).
14. Subscription "coding plans" are tied to listed tools and to plan-specific keys and base
    URLs; using the wrong key or URL silently bills pay-as-you-go or fails.
    (ZAI-apikey, ZAI-faq, ALI-plan, MM-usage, KC-overview)
15. Vendor setup wizards and scripts write user-level files (`~/.claude/settings.json`,
    `~/.claude.json`, `~/.codex/config.toml`, `~/.config/opencode/opencode.json`). They are the
    opposite of project-level config and should not be run in this setup.
    (ZAI-claude, ZAI-helper, DS-codex, KP-cc, KC-cc, MM-cli)
16. Thinking cannot be turned off on several of these models, and some reject requests that
    try: Kimi K3.1 Pro and `kimi-k2.7-code` return 400, MiniMax-M3.1-Flash always thinks,
    GLM converts "off" to `low`. (KC-cc, KP-cc, MM-cc, ZAI-latest)

### Contradictions and open questions

- Shell versus settings precedence. Claude Code docs, Kimi and others say the settings `env`
  block wins. MiniMax says the opposite about shell exports of `ANTHROPIC_AUTH_TOKEN` and
  `ANTHROPIC_BASE_URL`: "They take priority over the settings file and override the MiniMax
  configuration" (MM-cc, warning box). Trust the Claude Code docs; treat MiniMax's sentence as
  wrong or as describing an older version.
- `CLAUDE_CODE_AUTO_COMPACT_WINDOW` range. CC-model says the accepted range is 100,000 to
  1,000,000 and that a larger value is treated "as the 1M maximum" with a warning. Kimi's guides
  set `1048576` (KC-cc) and `1000000` (KP-cc). Inference: `1048576` triggers the startup warning.
- `[1m]` plus `CLAUDE_CODE_MAX_CONTEXT_TOKENS`. CC-model says that for an unrecognised ID that
  contains `[1m]`, Claude Code "assumes a 1M window for it and the variable doesn't apply on its
  own". Z.ai and Kimi set both anyway (ZAI-claude, KC-cc). Inference: redundant, harmless.
- Effort on unrecognised IDs. CC-model: "Models not listed here do not support effort", and
  CC-env documents `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT=1` for gateways with custom IDs. Vendors
  only set `CLAUDE_CODE_EFFORT_LEVEL` and say `/effort` works (DS-cc, KP-cc, KC-cc, MM-cc,
  ZAI-latest). None sets `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT`. Not resolved by the sources.
- Capability variables. CC-model says `_NAME` and `_DESCRIPTION` variables work behind an
  `ANTHROPIC_BASE_URL` gateway; CC-gwc's troubleshooting table says the capability variables
  apply only to the provider configurations (Bedrock, Vertex), not behind an `ANTHROPIC_BASE_URL`
  gateway. So `_SUPPORTED_CAPABILITIES` cannot be relied on for this route.
- Z.ai default mapping is stated three ways: all three tiers to `GLM-5.3-Flash` ("default
  configuration", ZAI-claude), Opus/Sonnet to `glm-5.3[1m]` and Haiku to `glm-5.3-flash[1m]`
  (manual example, same page), and `GLM-4.7` in the older scenario page (ZAI-scen-claude).
  The scenario pages are stale.
- Kimi's Claude Code guide (KP-cc) maps the Haiku tier to `kimi-k2.7-code`, while KP-models
  lists that model as deprecated and "No longer available to newly registered users". The curl
  check on the same page uses `kimi-k3.1-pro`. Use K3-series IDs for a new account.
- OpenCode config schema drift. OpenCode's current docs use `providers` with `package` and
  `settings.baseURL` (OC-prov). MiniMax's guide uses `provider` with `npm` and
  `options.baseURL` in `~/.config/opencode/opencode.json` (MM-oc). One of them is for a
  different OpenCode major version; the OpenCode index I had saved is titled "OpenCode V2
  Documentation".
- Agent-directed text. Alibaba's page tells users to give Claude Code the key in chat
  ("My API Key is: sk-xxxxxxxxxxxxx", ALI-cc, "Integrate Bailian CLI"); MiniMax says "do not
  send your M Plan API key to the agent" (MM-cli). Follow MiniMax's rule.

## Claude Code side: what its docs define for this route

Sources: CC-model, CC-gw, CC-gwc, CC-gws, CC-3p, CC-env, CC-cost, CC-fast, CC-adv (all read in
full), CC-set and CC-mcp (one section each). Fetched 2026-11-10; the pages describe Claude Code
up to v2.1.322.

Routing and credentials
- `ANTHROPIC_BASE_URL`: "Override the API endpoint to route requests through a proxy or
  gateway" (CC-env table).
- `ANTHROPIC_AUTH_TOKEN` is sent as `Authorization: Bearer`; `ANTHROPIC_API_KEY` as
  `x-api-key`; "A credential in the wrong variable reaches the gateway in a header it doesn't
  read, and the request fails with `401`" (CC-gwc, "How the credential variable maps to a
  header").
- `ANTHROPIC_AUTH_TOKEN` overrides a saved claude.ai login immediately; `ANTHROPIC_API_KEY`
  asks for one approval in interactive mode (CC-gwc, "Conflicts with an existing login"). A
  saved login plus a token produces an auth-conflict startup warning; `/logout` clears it.
- While such a credential is active the claude.ai subscription is not used or charged for those
  requests (CC-gw, "Subscriptions and gateways").
- If the session asks to log in although the endpoint works, the token was not visible before
  first-run setup: set it in "a shell export, the `env` block in `~/.claude/settings.json`, or
  managed settings" (CC-gwc, troubleshooting table). A shell export satisfies this without a
  global file.
- Verify with `/status`: the `Anthropic base URL` line and an `Auth token` line (CC-gwc).

Where the variables may live
- Shell exports: one terminal session and its children (CC-gwc, "Set as shell environment
  variables"). They do not reliably reach background agents hosted by the supervisor (same
  section).
- `.claude/settings.json` `env`: shared and committed; wins over the shell; applied after the
  trust prompt. `.claude/settings.local.json`: one user, one project, gitignored only "when
  Claude Code saves a setting to it" (CC-env, file table), otherwise you must gitignore it.
- `--settings`: listed with user and managed settings as applied "at startup" (CC-set). The
  precedence of `--settings` against project settings was not read (see (d)).
- Not settable from project or local settings: `CLAUDE_CONFIG_DIR`, OpenTelemetry exporters,
  `CLAUDE_CODE_OAUTH_TOKEN` and others (CC-set, "Variables Claude Code ignores in `env`").
  `ANTHROPIC_BASE_URL`, the token variables and the model variables are not on that list.
- `CLAUDE_CONFIG_DIR` (shell or user settings only) moves all settings, history and plugins;
  CC-env suggests it for "running multiple accounts side by side".

Model mapping
- Tier variables: `ANTHROPIC_DEFAULT_OPUS_MODEL`, `_SONNET_`, `_HAIKU_`, `_FABLE_`
  (CC-model, "Environment variables"). Haiku is also "background functionality".
  `ANTHROPIC_SMALL_FAST_MODEL` is deprecated.
- `CLAUDE_CODE_SUBAGENT_MODEL` is only the default; "A per-invocation model or a definition's
  `model` field, including `inherit`, takes precedence". `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`
  forces one model. Inference: subagent and skill frontmatter in a shared template should use
  the aliases (`haiku`, `sonnet`, `opus`, `inherit`), never full Claude IDs, so the tier
  variables can redirect them.
- `ANTHROPIC_CUSTOM_MODEL_OPTION` adds one picker row and "skips validation for the model ID"
  (CC-model). `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` reads `/v1/models` (CC-env);
  Alibaba's endpoint has no model list endpoint (ALI-cc FAQ).
- A mistyped or unknown model is not rejected up front; the first request fails (CC-model).

Context and output
- Unknown ID: 200K assumed; `[1m]` suffix means 1M and "Claude Code strips the suffix before
  sending the model ID to your provider" (CC-model, "Pin models for third-party deployments").
- `CLAUDE_CODE_MAX_CONTEXT_TOKENS` applies directly to an unrecognised non-`claude-` ID
  without `[1m]`. `CLAUDE_CODE_AUTO_COMPACT_WINDOW` accepts 100000 to 1000000.
- Unknown ID output tokens: "the default is 32000 and the cap is 128000"
  (CC-env, `CLAUDE_CODE_MAX_OUTPUT_TOKENS`).
- A gateway that rewrites the too-long error defeats automatic compaction; `/compact` recovers
  (CC-gwc, troubleshooting).

What does not work, or needs a switch, as Claude Code's docs state it
- Advisor: "The advisor tool is experimental and requires the Anthropic API" (CC-adv). It is
  also not attached when "the main model or the advisor is a model Claude Code does not
  recognize".
- Fast mode: supported on named Claude models only, "not on Sonnet, Haiku, or other models"
  (CC-fast). `CLAUDE_CODE_DISABLE_FAST_MODE=1` removes it.
- Remote Control: "disabled while `ANTHROPIC_BASE_URL` points at a non-Anthropic host"; voice
  dictation is unavailable while a gateway credential is active (CC-gwc).
- Feature-flag-gated features: with a bearer token, no API key and a non-Anthropic host,
  "Claude Code has no credential to fetch the flags with" (CC-env). The list includes the
  advisor, MCP tasks, `/import`, `/skill-doctor`, synced skills and plugins, and excluding MCP
  tools whose schema the API would reject.
- Tool search: on by default behind `ANTHROPIC_BASE_URL`; from v2.1.305 Claude Code retries
  without it after a `400` or `422` (CC-mcp, "Tool search through an LLM gateway").
  `ENABLE_TOOL_SEARCH=false` loads all tools upfront (CC-env).
- Unknown request fields: `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` strips pre-release beta
  headers and fields and keeps tool search off (CC-env, CC-gwc troubleshooting).
  `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS=1`, `DISABLE_INTERLEAVED_THINKING=1`,
  `CLAUDE_CODE_DISABLE_THINKING=1` and `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` exist for narrower
  cases.
- Thinking: on third-party providers `MAX_THINKING_TOKENS=0` only omits the `thinking`
  parameter, "and adaptive-reasoning models may still think" (CC-model, "Extended thinking").
- Prompt caching: used automatically; `DISABLE_PROMPT_CACHING=1` turns it off. The `/usage`
  cache line "works on every provider and gateway" because it reads the response's cache
  token fields (CC-cost).
- WebFetch's domain safety check "still calls `api.anthropic.com`"; `skipWebFetchPreflight:
  true` turns it off (CC-gwc). Web search on a non-Anthropic endpoint is not described in the
  pages read.
- Nonessential traffic (updates, telemetry, release notes) still goes to Anthropic unless
  `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set, which also disables auto-update and
  feature flags (CC-gwc, CC-env).
- Desktop app: does not read `ANTHROPIC_BASE_URL` or `settings.json`. VS Code extension: wants
  the variables in `claudeCode.environmentVariables` in VS Code user settings (CC-gwc).
- Cost figures in `/usage` are list-price estimates for Claude models (CC-cost); Inference:
  they are meaningless on a vendor endpoint.

## Z.ai / Zhipu (GLM)

Docs: docs.z.ai, fetched 2026-11-10. "API Key Management Guide" is dated October 16, 2026.
Privacy policy "Last Update: September 29, 2025".

Own harness
- No terminal CLI of its own is documented. ZCode is "a full-featured Agentic Development
  Environment (ADE)" for long-running tasks, a downloadable app with a "proprietary ZCode
  Agent" (ZAI-zcode). Its config files, instruction file, skills, hooks and headless
  mode are not described on the pages read (its own docs at zcode.z.ai were not fetched).
- `@z_ai/coding-helper` (`npx @z_ai/coding-helper`) is a setup wizard, not a harness. It
  configures Claude Code, Codex, OpenCode, Crush and Factory Droid at user level
  (ZAI-helper). Do not use it in a project-level setup.

Route through Claude Code (ZAI-claude, ZAI-latest)
- `ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic`
- `ANTHROPIC_AUTH_TOKEN=<Z.ai API key>` (Coding Plan key for plan quota)
- Models, 1M variant: `ANTHROPIC_DEFAULT_OPUS_MODEL=glm-5.3[1m]`,
  `ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5.3[1m]`, `ANTHROPIC_DEFAULT_HAIKU_MODEL=glm-5.3-flash[1m]`.
  An all-Flash variant sets all three to `glm-5.3-flash[1m]` (ZAI-latest).
- `CLAUDE_CODE_AUTO_COMPACT_WINDOW=1000000`, `CLAUDE_CODE_MAX_CONTEXT_TOKENS=1000000`,
  `API_TIMEOUT_MS=3000000`.
- The manual example also sets `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_TELEMETRY=1`
  and `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0` (full system prompt on every model).
- Not set by Z.ai: `ANTHROPIC_MODEL`, `ANTHROPIC_DEFAULT_FABLE_MODEL`,
  `CLAUDE_CODE_SUBAGENT_MODEL`. If no mapping is set, "the default server model mapping is
  applied, where you see the Claude model in the interface but the GLM model is actually used"
  (ZAI-scen-claude tip). Requests for GLM-5.2/5.1 route to GLM-5.3 and GLM-4.7 to GLM-5.3-Flash
  (ZAI-overview).
- Effort: `/effort` works; "The default level is `max`." Turning thinking off is converted to
  `low` and "still performs lightweight thinking" (ZAI-latest, effort table).
- Vision: "GLM-5.3 is a text-only model"; GLM-5.3-Flash is multimodal (ZAI-latest). Images on
  GLM-5.3 need the Vision MCP server. Web search and page reading are offered as plan-only MCP
  servers (ZAI-quick), not as Claude Code's built-in web search.
- Project-level: Z.ai only documents `~/.claude/settings.json` and user environment variables.
  By the Claude Code rules above the same variables work from a launcher script.
- Stated compatibility: "We have verified compatibility with Claude Code 2.0.14 and other
  versions" (stale relative to v2.1.3xx).

Route through OpenCode (ZAI-oc)
- `opencode auth login`, select "Z.AI", or "Z.AI Coding Plan" for plan subscribers, paste the
  key, then `/models`. No JSON is given. The OpenAI-compatible Coding Plan endpoint is
  `https://api.z.ai/api/coding/paas/v4`; the standard API is `https://api.z.ai/api/paas/v4`
  (ZAI-apikey table). Model IDs: `glm-5.3`, `glm-5.3-flash`.

Route through Codex (ZAI-codex)
- "Codex requires a dedicated OpenAI Responses protocol endpoint: `https://api.z.ai/api/v1`."
- `~/.codex/models.json` with slug `glm-5.3` (context_window 1048576, reasoning levels low,
  high, max, input text only) and `~/.codex/config.toml`: `model_provider = "ZAI"`,
  `model = "glm-5.3"`, `model_catalog_json`, `[model_providers.ZAI]` with `base_url`,
  `wire_api = "responses"`, `experimental_bearer_token = "<key>"` (plaintext key in the file).

Plans and data
- GLM Coding Plan subscription, "Starting at just 18 USD per month" (Lite, Pro, Max), 5-hour
  and weekly credit limits, 50% credit rate off-peak; pay-per-token API is separate: GLM-5.3
  $1.4 in / $4.4 out per 1M, GLM-5.3-Flash $0.15 / $0.50 (ZAI-overview, ZAI-pricing).
- Plan use is restricted: "users may not use their subscription benefits for tools or
  scenarios outside of this scope" (ZAI-others). Claude Code, Codex and OpenCode are listed.
- Keys are typed since 2026-10-16: "Changing the endpoint does not change the key's billing
  type." (ZAI-apikey)
- Account sharing is prohibited; more than three violations may mean a ban (ZAI-policy).
- Data: operator is a Singapore company and "your personal data is generally processed in
  Singapore" (ZAI-privacy, section 8). The API DPA says: "The Company do not store any of the
  content the Customer or its End Users provide or generate while using our Services."
  The consumer policy lists model training as a purpose for personal data; whether Coding Plan
  traffic is under the DPA or the consumer policy is not stated.

Recommended IDs (2026-11-10): `glm-5.3` (flagship, text only, 1M), `glm-5.3-flash`
(multimodal, cheaper). In Claude Code write them with `[1m]`.

## DeepSeek

Docs: api-docs.deepseek.com, fetched 2026-11-10. Latest news item is the 2026-10-17 release
of DeepSeek-V4.1-Flash-1017 (the saved file's `date` field is wrong).

Own harness
- "DeepSeek Harness is now in developer preview for agent harness developers worldwide."
  (DS-index). It is a plugin SDK with a Web UI started by a `dsh` process; you add a workspace
  and a DeepSeek key under Settings, Models (DS-harness-quick). Install command, config file
  locations, instruction file, skills, hooks, MCP and headless mode were not established from
  the pages read. Treat as not ready for a project template.
- The docs also list third-party terminal agents (Reasonix: `npx reasonix code`, key saved to
  `~/.reasonix/config.json`). Not a DeepSeek product as far as the page says.

Route through Claude Code (DS-cc, DS-anth)
```
ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
ANTHROPIC_AUTH_TOKEN=<DeepSeek API key>
ANTHROPIC_MODEL=deepseek-flash[1m]
ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-flash[1m]
ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-flash[1m]
ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-flash
CLAUDE_CODE_SUBAGENT_MODEL=deepseek-flash
CLAUDE_CODE_EFFORT_LEVEL=max
CLAUDE_CODE_AUTO_COMPACT_WINDOW=786432
```
- The guide gives these as shell exports ("Linux / Mac users"), which is already the
  per-session form. To use the stronger model, substitute `deepseek-v4-pro` (Inference from
  the model table; the guide itself maps everything to Flash).
- Server-side fallback mapping: "`claude-opus*` names are mapped to `deepseek-v4-pro`, and
  other `claude*` names are mapped to `deepseek-flash`"; non-`claude` unknown names return 400
  (DS-anth, note). So an unmapped tier still answers, on a model you did not choose, and Opus
  names are "billed at the V4 Pro price".
- Auth: either `x-api-key` or `Authorization: Bearer` is accepted (DS-anth, "HTTP Header").
- What the compatibility table says does not work or is altered (DS-anth):
  - `anthropic-beta` and `anthropic-version` headers: ignored.
  - `cache_control`: "Ignored" everywhere; `cache_creation_input_tokens` "is currently `0`".
    Caching is automatic and reported in `cache_read_input_tokens`.
  - Thinking: "`adaptive` is treated as `enabled`. `budget_tokens` is ignored"; only
    `output_config.effort` is honoured.
  - `tool_choice` `any` is "Treated as `auto`"; a forced named tool "returns a `400` error in
    thinking mode".
  - Images: `deepseek-flash` accepts them; "`deepseek-v4-pro` does not process images and
    replaces them with the text `[Unsupported Image]`".
  - `document`, `search_result`, `redacted_thinking`, `mcp_tool_use`, `mcp_tool_result`,
    `code_execution_tool_result`, `container_upload` content blocks: Not Supported.
    `mcp_servers` request field: Ignored. (These are API-side MCP fields. Inference: Claude
    Code's own client-side MCP servers are ordinary tools and are unaffected.)
  - `max_tokens` may be raised above the request for main-agent requests from Claude Code or
    OpenCode in thinking mode.
- Web search works: "The DeepSeek API natively supports the Web Search feature in Claude
  Code." (DS-cc). It costs extra tokens plus Search API fees ($0.75 per 1,000 calls; billing
  for server-side tool calls from Claude Code and Codex started 2026-10-31, DS-news).

Route through OpenCode (DS-oc)
- Run `opencode`, `/connect`, type `deepseek`, paste the key, select "DeepSeek-V4-Flash".
  "version >= v1.18.30 recommended". No JSON is given.

Route through Codex (DS-codex)
- Uses the Responses API "which the DeepSeek API natively supports". Requires Codex 0.164 or
  later for the setup script's web search.
- `~/.codex/models.json` with slugs `deepseek-flash` (text and image) and `deepseek-v4-pro`
  (text), context 1048576, and `~/.codex/config.toml`: `model = "deepseek-flash"`,
  `model_provider = "deepseek"`, `preferred_auth_method = "apikey"`,
  `forced_login_method = "api"`, `model_catalog_json`, `[model_providers.deepseek]` with
  `base_url = "https://api.deepseek.com/"`, `wire_api = "responses"`,
  `experimental_bearer_token`. The field table calls that token "Your API Key, stored
  directly in the configuration file".
- The one-click script rewrites `~/.codex/config.toml` (with a backup). Not for this setup.

Plans and data
- Pay-per-token only on the pages read; no coding subscription is mentioned. Peak prices per
  1M tokens: `deepseek-flash` $0.3 in (miss), $0.006 (hit), $1.2 out; `deepseek-v4-pro` $1.32,
  $0.044, $3.96. Off-peak is half; peak is 01:00-04:00 and 06:00-10:00 UTC on weekdays
  (DS-pricing).
- Both models: 1M context, max output 384K, thinking on by default.
- Data handling and region: nothing on the pages read.

Recommended IDs (2026-11-10): `deepseek-flash` (served by DeepSeek-V4.1-Flash-1017, vision,
the vendor's own default for agents) and `deepseek-v4-pro` (DeepSeek-V4-Pro-0813, no vision).
Legacy `deepseek-v4-flash` names are still accepted but retired (DS-index).

## Moonshot / Kimi

Two separate products with different keys, base URLs and model IDs (KC-overview, "Platform
Comparison"): the Kimi Platform (pay-as-you-go, `api.moonshot.ai`, docs now at
platform.kimi.ai) and Kimi Code (membership, `api.kimi.ai/coding` overseas,
`api.kimi.com/coding` China). Fetched 2026-11-10.

Own harness: Kimi Code CLI (`kimi`)
- Install: `curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash`, or
  `npm install -g @moonshot-ai/kimi-code` (Node.js 22.19.0+). The older Python `kimi-cli`
  (data in `~/.kimi/`) is being phased out; `kimi migrate` imports it. (KCLI-start, KCLI-mig)
- Login: `/login`, either Kimi Code OAuth or a Kimi Platform API key (KCLI-start, KP-cli).
- Config: user-level only. "The CLI currently reads a single user-level config file and has no
  project-level config file mechanism." (KCLI-over). The file is
  `~/.kimi-code/config.toml`, plus `tui.toml`; `KIMI_CODE_HOME` relocates the whole data root
  and is the documented way to isolate per project:
  `KIMI_CODE_HOME="$PWD/.kimi-sandbox" kimi` (KCLI-over, "Common scenarios").
- Project-level files that do exist: `AGENTS.md` or `.kimi-code/AGENTS.md` (instructions),
  `.kimi-code/skills/` and `.agents/skills/`, `.kimi-code/agents/` and `.agents/agents/`,
  `.kimi-code/mcp.json` (trust-gated), `.kimi-code/local.toml` (legacy, permission rules and
  extra dirs, should be gitignored). (KCLI-agents, KCLI-skills, KCLI-cfg, KCLI-mcp)
- Instruction file: "project-level instructions remain under the project tree, for example
  `.kimi-code/AGENTS.md` or `AGENTS.md`"; global ones at `$KIMI_CODE_HOME/AGENTS.md` and
  `~/.agents/AGENTS.md` (KCLI-agents, "Instruction Files"). `/init` generates `AGENTS.md`.
- Skills: `SKILL.md` with frontmatter `name`, `description`, optional `type`, `whenToUse`,
  `disableModelInvocation`, `arguments`; invoked as `/skill:<name>`; priority Project > User >
  Extra > Built-in (KCLI-skills).
- Subagents: built-in `coder`, `explore`, `plan`; custom agents are Markdown files with
  frontmatter (`name`, `description`, `tools`, `disallowedTools`, `subagents`, `override`).
  "Fields from other agent tools (such as Claude Code's `model` or OpenCode's `mode`) are
  ignored" so Claude Code-style agent files load (KCLI-agents). A project agent file with
  `override: true` can replace the main system prompt: review them in untrusted repos.
- Hooks: `[[hooks]]` in the user `config.toml` only: "there is no project-level hook file".
  Events include `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SessionStart`,
  `SubagentStop`; exit code 2 blocks; hooks are fail-open (KCLI-hooks).
- MCP: `mcp.json` at user and project level, project wins on name clash; headless runs skip
  project MCP unless `KIMI_CODE_TRUST_WORKSPACE=1` (KCLI-mcp, "Configuration").
- Headless: `kimi -p "<prompt>"`, `--output-format text|stream-json`, `-m <alias>`; in `-p`
  mode "no human approval is requested" (KCLI-cmd, "Non-Interactive Execution").
- Credentials: providers read keys only from `config.toml`, except `api_key_env`, which names
  a shell variable and is "re-read from the process's own environment on every request"
  (KCLI-over, "Provider credentials"). Provider types: `kimi`, `anthropic`, `openai`,
  `openai_responses`, `google-genai`, `vertexai` (KCLI-cfg).
- There is also a Desktop app and a VS Code extension (KC-overview).

Route through Claude Code, pay-as-you-go platform (KP-cc)
```
ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic
ANTHROPIC_AUTH_TOKEN=<Kimi Platform key>
ANTHROPIC_MODEL=kimi-k3[1m]
ANTHROPIC_DEFAULT_OPUS_MODEL=kimi-k3[1m]
ANTHROPIC_DEFAULT_SONNET_MODEL=kimi-k3[1m]
ANTHROPIC_DEFAULT_HAIKU_MODEL=kimi-k2.7-code      # deprecated for new accounts, see above
ANTHROPIC_DEFAULT_FABLE_MODEL=kimi-k3[1m]
CLAUDE_CODE_SUBAGENT_MODEL=kimi-k3[1m]
CLAUDE_CODE_AUTO_COMPACT_WINDOW=1000000
CLAUDE_CODE_EFFORT_LEVEL=max
```
- "If you previously configured `ANTHROPIC_API_KEY`, remove it to avoid conflicts" (FAQ).
- Thinking: `kimi-k3` on by default and can be turned off; `kimi-k2.7-code` forced on, and
  with thinking off requests fail with `400 invalid thinking: only type=enabled is allowed
  for this model`.

Route through Claude Code, Kimi Code membership (KC-cc)
```
ANTHROPIC_BASE_URL=https://api.kimi.ai/coding/      # China: https://api.kimi.com/coding/
ANTHROPIC_API_KEY=<Kimi Code key>                   # note: API_KEY, not AUTH_TOKEN
ANTHROPIC_MODEL=k3.1-pro[1m]                        # or k3.1-pro for the 256K cap
ANTHROPIC_DEFAULT_FABLE_MODEL / _OPUS_ / _SONNET_ / _HAIKU_MODEL = same value
CLAUDE_CODE_SUBAGENT_MODEL = same value
CLAUDE_CODE_EFFORT_LEVEL=high
CLAUDE_CODE_AUTO_COMPACT_WINDOW=1048576             # 262144 for the 256K configuration
CLAUDE_CODE_MAX_CONTEXT_TOKENS=1048576              # 262144 for the 256K configuration
```
- The page gives both a `settings.json` method and a "Terminal environment variables (current
  session only)" method ending in `claude`, and says "pick one, do not mix them".
- "K3.1 Pro models only support thinking mode, and requests with thinking disabled are
  rejected." Effort mapping: Claude Code `medium`/`high` -> `high`, `xhigh`/`max` -> `max`.
- Model and context depend on the membership tier (1M context only on Pro / Allegretto and
  above).
- The guide's pre-step script edits `~/.claude.json` (`hasCompletedOnboarding`,
  `penguinModeOrgEnabled`) and deletes keys from `~/.claude/settings.json`. That is global
  state; see (d) for whether it is needed with a shell-exported credential.
- "Tampering with the client identifier (User-Agent) is considered a violation and may result
  in suspension of membership benefits." (KC-overview)

Route through OpenCode
- Platform: `opencode auth login`, select "Moonshot AI", paste key, `/models` -> "Kimi K3",
  `/variants` -> `max`. Based on OpenCode 1.18.3. "Do not put the API key in configuration
  files, screenshots, or a Git repository." (KP-oc)
- Membership: `opencode auth login`, select "Kimi For Coding", then `/models` (KC-oc).
- No provider JSON is given by either page.

Route through Codex
- Platform (KP-codex): `~/.codex/config.toml` with `model = "kimi-k3.1-pro"`,
  `model_provider = "kimi"`, `model_context_window = 1048576`, `[model_providers.kimi]`
  `base_url = "https://api.moonshot.ai/v1"`, `env_key = "KIMI_API_KEY"`,
  `wire_api = "responses"`. "Do not write the key into `config.toml`."
- Membership (KC-codex): same shape with `base_url = "https://api.kimi.ai/coding/v1"`,
  `model = "k3.1-pro"`, `web_search = "live"`, plus `~/.codex/models.json`. `env_key` is the
  recommended form; `experimental_bearer_token` is the plaintext alternative.

Plans and data
- Platform: "Model inference on the Kimi API platform is billed on a pay-as-you-go basis, with
  no subscription plan." Kimi K3 needs paid balance, vouchers do not apply (KP-price, KP-oc).
  The price table did not survive the fetch (empty table).
- Kimi Code: membership subscription with rate limits; up to 5 API keys, each shown once
  (KC-overview).
- Data: "ZDR is available on request to enterprise customers." and "By default, the Kimi Open
  Platform does not use enterprise customer data to train models." (KP-zdr). Nothing read
  about individual accounts or about Kimi Code membership traffic. Regions: separate China
  (`api.moonshot.cn`, `api.kimi.com`) and overseas (`api.moonshot.ai`, `api.kimi.ai`) hosts;
  keys only work on the platform that issued them (KP-codex troubleshooting).

Recommended IDs (2026-11-10): platform `kimi-k3.1-pro` (flagship, 1M, vision),
`kimi-k3.1-pro-highspeed`, `kimi-k3` (KP-models). K2-series IDs are being retired by end of
December 2026. Membership: `k3.1-pro`, `k3.1-pro-highspeed`, `k3`, `k3-256k`,
`kimi-for-coding` (K2.8 Preview), `kimi-for-coding-highspeed` (KC-overview).

## Alibaba Qwen / Qwen Code

Docs: qwenlm.github.io/qwen-code-docs (overview page dated 2026-11-09) and
alibabacloud.com Model Studio (pages dated 2026-11-04 and 2026-11-05). Only the overview and
the Alibaba pages were read in full; other Qwen Code facts come from named sections.

Own harness: Qwen Code (`qwen`), open source
- Install: `curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash`
  (QW-overview). The first launch offers Qwen subscription login, QwenCloud, Alibaba
  ModelStudio, built-in third-party providers "such as DeepSeek, MiniMax, Z.AI, Kimi, and
  OpenRouter", or a custom provider. So Qwen Code is itself a possible host for GLM, DeepSeek
  and Kimi models.
- Config: user `~/.qwen/settings.json`, project `.qwen/settings.json` ("Project settings
  override user settings"), system files above both; settings strings can reference `$VAR`
  (QW-settings, "Settings files"). Some keys are read from operator scopes only.
- Instruction file: `QWEN.md` (project root, `~/.qwen/QWEN.md`, `.qwen/QWEN.local.md`), and
  "If your repository already has an `AGENTS.md` file for other AI tools, Qwen reads that
  too." (QW-memory). `context.fileName` can rename it.
- Skills: `.qwen/skills/` and `~/.qwen/skills/`; "Qwen Code also reads project Skills from
  `.agents/skills/`." (QW-skills, line search)
- Subagents: `.qwen/agents/` (project, highest precedence) and `~/.qwen/agents/`
  (QW-subagents, line search). MCP, hooks, slash commands, headless: a Headless Mode page and
  an MCP page exist; `qwen -p "<prompt>"` is the headless form (QW-overview, QW-headless).
- Keys: a provider's `envKey` names an environment variable; it can come from a `.env` file
  (`~/.qwen/.env` or project root) or the settings `env` field (QW-providers, "About
  `envKey`").

Route through Claude Code (ALI-cc)
- Coding Plan: `ANTHROPIC_BASE_URL=https://coding-intl.dashscope.aliyuncs.com/apps/anthropic`,
  `ANTHROPIC_AUTH_TOKEN=<sk-sp-... key>`, all of `ANTHROPIC_MODEL`, `_HAIKU_`, `_SONNET_`,
  `_OPUS_MODEL` and `CLAUDE_CODE_SUBAGENT_MODEL` = `qwen3.7-plus`.
- Token Plan: `https://token-plan.ap-southeast-1.maas.aliyuncs.com/apps/anthropic`,
  `ANTHROPIC_MODEL=auto`, Haiku `qwen3.6-flash`, Sonnet `qwen3.8-flash`, Opus `qwen3.8-max`,
  `CLAUDE_CODE_MAX_CONTEXT_TOKENS=983616`.
- Pay-as-you-go: `https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/apps/anthropic`
  with `qwen3.7-max`. The FAQ table lists `https://dashscope-intl.aliyuncs.com/apps/anthropic`
  for pay-as-you-go instead: the page disagrees with itself.
- 1M context: append `[1m]` or set `CLAUDE_CODE_MAX_CONTEXT_TOKENS=1000000`.
- The endpoint serves only `/v1/messages`, no model list (FAQ). Shell exports are given first
  and "apply only to the current terminal".

OpenCode and Codex: Alibaba lists both as supported tools (ALI-plan table) but those pages
were not fetched.

Plans and data
- Coding Plan Pro: 50 USD per month, up to 6,000 requests per 5 hours, 45,000 per week, 90,000
  per month; supported models are exact versions (qwen3.7-plus, qwen3.6-plus, kimi-k2.5,
  glm-5, MiniMax-M2.5, qwen3.5-plus). Lite is closed to new subscribers. (ALI-plan)
- "Do not use the plan's API key for automated scripts, application backends, or other
  non-interactive scenarios." (ALI-plan, "Before you subscribe"). Inference: headless
  `claude -p` in CI on a Coding Plan key is against the terms.
- "The two sets of API keys and base URLs are not interchangeable." (ALI-plan)
- Data handling: not read.

Recommended IDs (2026-11-10): Coding Plan `qwen3.7-plus`; Token Plan and pay-as-you-go
`qwen3.8-max`, `qwen3.8-flash`, `qwen3.7-max`, `qwen3.6-flash` (ALI-cc examples).

## MiniMax

Docs: platform.minimax.io "M Plan" section and the MiniMax-AI/minimax-code README (targets the
"0.6.3 source preview"; published npm CLI `@minimax-ai/code@0.6.9`). Fetched 2026-11-10.

Own harness: MiniMax Code (`mcode`), desktop, mobile, web and CLI
- Install: `curl -fsSL https://filecdn.minimax.chat/public/install.sh | bash`, or
  `npm install -g @minimax-ai/code@latest ...` (MM-code, MM-readme). Login:
  `mcode login --region global`. BYOK: `mcode provider add --name ... --base-url ...
  --api-format openai-completions|openai-responses|anthropic-messages --api-key-env VAR`.
- Locations: program in `~/.minimax-code`; user data in `~/.minimax` (or
  `~/.minimax-<profile>`); `MINIMAX_DATA_DIR` overrides the data directory; custom providers
  are stored in the active profile's `config.yaml` (MM-readme). Project-level config
  directories are not described in the README.
- Instruction file: "Use `mcode init .` to generate or update project guidance in
  `AGENTS.md`." (MM-readme)
- Headless: `mcode exec [prompt]`; ACP: `mcode acp`; a TypeScript SDK exists. The README
  names subagents, plugins, built-in skills, MCP, hooks (a `docs/hooks.md` exists) and
  sandboxing, without file locations.
- `mmx` (MiniMax CLI, `npm install -g mmx-cli`) is a media and search tool plus the
  `mmx agent setup` wizard. The wizard writes `~/.claude/settings.json`,
  `~/.codex/config.toml`, `~/.config/opencode/opencode.json` and others (MM-cli,
  "Configuration files"). `--dry-run` previews. Not for a project-level setup.

Route through Claude Code (MM-cc)
```
ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic     # China: https://api.minimaxi.com/anthropic (search result only)
ANTHROPIC_AUTH_TOKEN=<M Plan API key>
ANTHROPIC_MODEL=MiniMax-M3.1-Flash[1m]
ANTHROPIC_DEFAULT_SONNET_MODEL / _OPUS_MODEL / _HAIKU_MODEL = MiniMax-M3.1-Flash[1m]
CLAUDE_CODE_AUTO_COMPACT_WINDOW=524288
CLAUDE_CODE_EFFORT_LEVEL=max
```
- "Thinking is always enabled for MiniMax-M3.1-Flash and cannot be disabled."
  `MAX_THINKING_TOKENS=0` has no effect. While `CLAUDE_CODE_EFFORT_LEVEL` is set, `/effort`
  in a session has no effect. "Some Claude Code versions send `xhigh` as `high`".
- 512K is a cost choice: in MiniMax's own ProgramBench comparison quality was similar and
  estimated cost about 20% lower than with 1M (MM-codex, "Why consider 512K?").
- Web search: add MiniMax's Web Search MCP.
- Not set by the guide: `ANTHROPIC_DEFAULT_FABLE_MODEL`, `CLAUDE_CODE_SUBAGENT_MODEL`.

Route through OpenCode (MM-oc)
- `opencode auth login`, pick "MiniMax Token Plan (minimax.io)"; provider ID
  `minimax-coding-plan`; model `MiniMax-M3.1-Flash`. If the model is missing, the page gives:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "minimax-coding-plan": {
      "models": {
        "MiniMax-M3.1-Flash": {
          "name": "MiniMax-M3.1-Flash",
          "limit": { "context": 524288, "output": 131072 }
        }
      }
    }
  }
}
```
  (schema keys as MiniMax prints them; see the schema-drift contradiction above). Anthropic
  protocol base URL for OpenCode: `https://api.minimax.io/anthropic/v1`.

Route through Codex (MM-codex)
- `~/.codex/config.toml`: `model = "MiniMax-M3.1-Flash"`, `model_provider = "minimax"`,
  `model_context_window = 524288`, `preferred_auth_method = "apikey"`,
  `forced_login_method = "api"`, `[model_providers.minimax]` `base_url =
  "https://api.minimax.io/v1"`, `experimental_bearer_token`, `wire_api = "responses"`.
  Codex CLI 0.146.0 or newer is recommended by the page. Do not add reasoning level `none`
  (API 400).

Plans and data
- M Plan subscription (Go, Explore 3x, Build 7.5x), 5-hour and weekly windows; one text model
  in the plan, M3.1 Flash (MM-intro, MM-usage). Pay-as-you-go keys (`sk-api-...`) are
  separate from M Plan keys (`sk-cp-...`): "This Key is separate from your M Plan API key and
  cannot be used interchangeably with it."
- Data handling: privacy page not read.

Recommended ID (2026-11-10): `MiniMax-M3.1-Flash` (1M context, multimodal, tunable thinking);
`MiniMax-M3` also listed (MM-models). `MiniMax-M3.1-Flash-Preview` is retired.

## Google Gemini CLI

Docs: geminicli.com, fetched 2026-11-10. Not a Chinese-lab model; included because it was
requested.

Own harness: Gemini CLI (`gemini`), Apache 2.0
- Install: `npm install -g @google/gemini-cli` or `brew install gemini-cli`; Node.js 20+
  (GEM-install).
- Config: user `~/.gemini/settings.json`; project `.gemini/settings.json` ("Project settings
  override user settings and system defaults"); system files; then environment variables,
  then CLI arguments (GEM-config, "Configuration layers", "Settings files"). Settings strings
  can reference `$VAR_NAME`.
- Instruction file: `GEMINI.md` by default, hierarchical (global, workspace and parents,
  just-in-time). "While `GEMINI.md` is the default filename, you can configure this in your
  `settings.json` file." The documented example is
  `{"context": {"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]}}` (GEM-md). So AGENTS.md
  is not read by default: it needs a project `.gemini/settings.json`.
- Skills: Agent Skills standard; workspace `.gemini/skills/` or `.agents/skills/`, user
  `~/.gemini/skills/` or `~/.agents/skills/`; `.agents/skills/` wins within a tier.
  "Workspace skills are shared with your team via version control." (GEM-skills)
- Subagents: `.gemini/agents/*.md` and `~/.gemini/agents/*.md`. Hooks: in `settings.json`
  at project, user and system level. Custom commands: `.gemini/commands/*.toml` (project) and
  `~/.gemini/commands/`. MCP: `mcpServers` in `settings.json`. Extensions bundle "prompts, MCP
  servers, custom commands, themes, hooks, sub-agents, and agent skills". (GEM-subagents,
  GEM-hooks, GEM-commands, GEM-mcp by line search; GEM-ext read in full)
- Headless: `-p` / `--prompt` or a non-TTY; `--output-format` JSON or streaming JSONL; exit
  codes 0, 1, 42, 53 (GEM-headless).
- Auth: Google login, `GEMINI_API_KEY`, or Vertex AI. Variables can come from a `.gemini/.env`
  file in the project: "Gemini CLI automatically loads variables from the first `.env` file it
  finds, searching up from the current directory" and "Variables are loaded from the first
  file found, not merged." (GEM-auth, "Persisting environment variables")

Route through Claude Code, OpenCode, Codex
- Claude Code: no Anthropic-compatible Gemini endpoint appears on the pages read. Treat as
  no.
- OpenCode: its package list includes `@opencode/ai/providers/google` and
  `google-vertex` (OC-prov, "Packages"), so Gemini models are a native OpenCode provider.
  No Gemini-specific setup was read.
- Codex: not documented on the pages read.
- Using Gemini CLI's own login from another tool is forbidden: "(for example, using OpenClaw
  with Gemini CLI OAuth) is a violation of applicable terms and policies" (GEM-tos).

Plans and data
- Free tier with Google login (1,000 requests per user per day) or an unpaid API key (250 per
  day, Flash only); Google AI Pro 1,500 and Ultra 2,000 per day; pay-as-you-go through a
  Gemini API key or Vertex AI (GEM-quota).
- Terms and privacy depend on the auth method; unpaid and paid API services have different
  terms (GEM-tos table). The details live on Google pages that were not fetched.

Recommended IDs: not established. The CLI chooses "across the Gemini model family" on Google
login; the model pages were not read.

## (a) Summary table

| Vendor | Own CLI | Claude Code route | OpenCode route | Codex route |
| :- | :- | :- | :- | :- |
| Z.ai GLM | No CLI. ZCode desktop app only | Yes. `ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic`, `ANTHROPIC_AUTH_TOKEN`, `glm-5.3[1m]` / `glm-5.3-flash[1m]` | Yes. `opencode auth login` -> "Z.AI Coding Plan" (OpenAI endpoint `https://api.z.ai/api/coding/paas/v4`) | Yes. `base_url=https://api.z.ai/api/v1`, `wire_api="responses"`, `models.json` |
| DeepSeek | Preview only. DeepSeek Harness (`dsh`, SDK and Web UI) | Yes. `https://api.deepseek.com/anthropic`, `ANTHROPIC_AUTH_TOKEN`, `deepseek-flash[1m]` / `deepseek-v4-pro` | Yes. `/connect` -> `deepseek` (OpenCode >= 1.18.30) | Yes. `base_url=https://api.deepseek.com/`, `wire_api="responses"`, `models.json`, Codex >= 0.164 |
| Moonshot Kimi | Yes. Kimi Code CLI `kimi` (`AGENTS.md`, `.kimi-code/`, `.agents/`) | Yes, two forms. Platform: `https://api.moonshot.ai/anthropic` + `ANTHROPIC_AUTH_TOKEN`, `kimi-k3[1m]`. Membership: `https://api.kimi.ai/coding/` + `ANTHROPIC_API_KEY`, `k3.1-pro[1m]` | Yes. `opencode auth login` -> "Moonshot AI" or "Kimi For Coding" | Yes. `https://api.moonshot.ai/v1` or `https://api.kimi.ai/coding/v1`, `env_key="KIMI_API_KEY"`, `wire_api="responses"` |
| Alibaba Qwen | Yes. Qwen Code `qwen` (`.qwen/settings.json`, `QWEN.md` + `AGENTS.md`) | Yes. Coding Plan: `https://coding-intl.dashscope.aliyuncs.com/apps/anthropic` + `ANTHROPIC_AUTH_TOKEN`, `qwen3.7-plus` | Listed by Alibaba; page not read | Listed by Alibaba; page not read |
| MiniMax | Yes. MiniMax Code `mcode` (`AGENTS.md`, `mcode exec`) | Yes. `https://api.minimax.io/anthropic` + `ANTHROPIC_AUTH_TOKEN`, `MiniMax-M3.1-Flash[1m]` | Yes. provider `minimax-coding-plan` ("MiniMax Token Plan (minimax.io)") | Yes. `base_url=https://api.minimax.io/v1`, `wire_api="responses"` |
| Google Gemini | Yes. Gemini CLI `gemini` (`.gemini/settings.json`, `GEMINI.md`, `context.fileName`) | No (none documented) | Native Google provider package exists; setup not read | Not documented |

## (b) Recommended minimal design for per-project, per-session switching

Goal restated: nothing in `~/.claude`, `~/.codex`, `~/.config/opencode` or shell profiles;
the repo carries everything except secrets; the provider is chosen when a session starts.

1. One gitignored secrets file per checkout, holding only keys, for example
   `.env.agents.local` with `ZAI_API_KEY=`, `DEEPSEEK_API_KEY=`, `MOONSHOT_API_KEY=`,
   `KIMI_CODE_API_KEY=`. A committed `.env.agents.example` lists the names.
   Evidence: CC-gwc warns against credentials in the committed project settings file; KP-oc,
   KC-codex, ZAI-quick and others say never commit keys; Qwen and Gemini document `.env`
   files for keys (QW-providers, GEM-auth).

2. One small launcher per harness that takes a provider name, loads the secrets file, exports
   the provider's variables and execs the tool, for example `bin/cc <provider> [claude args]`.
   For Claude Code the launcher exports exactly the variable sets in the vendor sections
   above, taken from a committed, non-secret table in the repo (base URL, token variable name,
   tier model IDs, compact window, effort).
   Evidence that this is per-session and needs no global file:
   - Shell exports "apply only to that terminal session and programs started from it"
     (CC-gwc).
   - `--model` and `ANTHROPIC_MODEL` "apply only to the session you launch with them"
     (CC-model).
   - DeepSeek, Alibaba and Kimi Code publish their Claude Code setup as shell exports followed
     by `claude` (DS-cc, ALI-cc, KC-cc "Method 2").
   - The token must be visible before first-run setup, and "a shell export" is one of the
     accepted places (CC-gwc troubleshooting).
   Rules the launcher must follow:
   - Unset the other credential variable first (`ANTHROPIC_API_KEY` when using
     `ANTHROPIC_AUTH_TOKEN` and the reverse), per KP-cc FAQ and CC-gwc's header mapping.
   - Set every tier variable plus `CLAUDE_CODE_SUBAGENT_MODEL`, per KP-cc and KC-cc.
   - Set the context variables that match the model (`[1m]` suffix or
     `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, and `CLAUDE_CODE_AUTO_COMPACT_WINDOW` within
     100000..1000000), per CC-model.
   - Inference: also set `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` and
     `CLAUDE_CODE_DISABLE_FAST_MODE=1` so unsupported features are not offered, and keep
     `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` as the documented first response to `400`
     errors about unknown fields (CC-gwc troubleshooting).
   - Inference: background sessions (`claude agents`, `--bg`) may not inherit a shell-only
     gateway (CC-gwc), so a vendor session should set `CLAUDE_CODE_DISABLE_AGENT_VIEW=1`, or
     the provider must come from a settings file instead.

3. Keep provider variables out of `.claude/settings.json` and `.claude/settings.local.json`.
   Evidence: the settings `env` block overwrites the shell (CC-gwc, CC-set), so any provider
   variable there pins every session in the repo and defeats the launcher. Kimi documents the
   same failure and ships a cleanup script for it (KP-cc, KC-cc). The exception is a repo
   that should always use one provider: then non-secret variables may go in
   `.claude/settings.json` and the token in `.claude/settings.local.json`, accepting that
   they apply only after the trust prompt (CC-set).

4. Optional variant: a committed per-provider settings file passed with
   `claude --settings .claude/providers/<name>.json`, containing only the non-secret `env`
   values, with the token still exported by the launcher. Evidence: `--settings` `env` values
   are applied at startup (CC-set); CC-fast and CC-set show `--settings` used per launch.
   Its precedence against project settings was not verified.

5. Make the shared customisation provider-neutral so the same repo works on every route:
   subagent and skill `model` fields use aliases (`haiku`, `sonnet`, `opus`, `inherit`) and
   never dated Claude IDs. Evidence: aliases resolve through the `ANTHROPIC_DEFAULT_*_MODEL`
   variables (CC-model); an unmapped Claude ID is a model-not-found error on Kimi (KC-cc
   reference table) and silently becomes Flash or Pro on DeepSeek (DS-anth).

6. OpenCode: commit `opencode.jsonc` (or `.opencode/opencode.jsonc`) with one `providers`
   entry per vendor that names the key variable, and let the same launcher export the keys.
   Evidence: project config files are read from the repo (OC-cfg, "Locations"); a provider's
   `env` field is "Ordered environment variable names that can provide the credential"
   (OC-prov, "Custom"); `{env:VARIABLE_NAME}` substitution is supported and an unset variable
   becomes an empty string (OC-cfg, "Variables"). Avoid `opencode auth login` and `/connect`
   for this purpose because they store the credential outside the repo. The exact built-in
   provider IDs for Z.ai, DeepSeek and Moonshot were not read, so the safe form is a custom
   provider with the vendor's OpenAI-compatible base URL (Z.ai
   `https://api.z.ai/api/coding/paas/v4`, DeepSeek `https://api.deepseek.com`, Moonshot
   `https://api.moonshot.ai/v1`, Kimi Code `https://api.kimi.ai/coding/v1`).
   Inference: untested.

7. Codex: providers cannot come from `.codex/config.toml` in the repo (CX-adv). Two ways to
   stay project-local, both Inference built from documented parts:
   - launcher sets `CODEX_HOME` to a gitignored directory inside the repo that holds a
     generated `config.toml` and `models.json` ("Sets the root for Codex state, including
     config, auth, logs, sessions, skills"; "the directory must already exist", CX-env); or
   - launcher passes `-c` overrides (`-c` "when you need to override an arbitrary key", dot
     notation, CX-adv).
   In both, use `env_key = "<VAR>"` rather than `experimental_bearer_token`, as Kimi's Codex
   guides do (KP-codex, KC-codex). Whether Z.ai, DeepSeek and MiniMax endpoints work with
   `env_key` is not stated by those vendors.

8. Own harnesses, all driven from the same repo files:
   - Kimi Code: `KIMI_CODE_HOME="$repo/.kimi-home" kimi` with a provider that uses
     `api_key_env` (KCLI-over documents exactly this isolation pattern). Shared files:
     `AGENTS.md`, `.agents/skills/`, `.agents/agents/`, `.kimi-code/mcp.json`. Hooks cannot be
     project-level; they would live in `$KIMI_CODE_HOME/config.toml`, which the launcher can
     generate.
   - Qwen Code: `.qwen/settings.json` in the repo, `AGENTS.md`, `.agents/skills/`.
   - Gemini CLI: `.gemini/settings.json` with `context.fileName` including `AGENTS.md`,
     `.agents/skills/`, key from the launcher's environment.
   - MiniMax Code: `AGENTS.md`; `MINIMAX_DATA_DIR` for isolation; BYOK with `--api-key-env`.
   - Inference: one `.agents/skills/` directory plus one root `AGENTS.md` covers Kimi Code,
     Qwen Code and Gemini CLI without copies; Claude Code still needs `CLAUDE.md` and
     `.claude/skills/` (outside this note's sources).

9. Verification step in every launcher's documentation: run `/status` and check the base URL
   and credential source (CC-gwc; every vendor repeats this). Kimi Code notes the model name
   may still show as a Claude model while calls go to Kimi (KC-cc, step 4).

## (c) Security cautions

- Never commit keys. Files that hold secrets in the vendor-recommended setups:
  `~/.claude/settings.json` `env` (all vendors; KC-cc: "The API Key in `settings.json` is
  stored in plaintext"), `~/.codex/config.toml` when `experimental_bearer_token` is used
  (Z.ai, DeepSeek, MiniMax), `~/.reasonix/config.json`, `$KIMI_CODE_HOME/config.toml`
  (`api_key`) and `$KIMI_CODE_HOME/credentials/`, `~/.minimax` data directory,
  `~/.qwen/.env` or `.qwen/settings.json` `env`, `.gemini/.env`, OpenCode's credential store.
  In the design above the only secret file is the gitignored `.env.agents.local`.
- `.claude/settings.local.json` is only auto-gitignored "when Claude Code saves a setting to
  it"; a hand-made one must be gitignored first (CC-env, CC-gwc).
- Settings `env` values "are plain text in the settings file and reach every subprocess
  Claude Code starts" (CC-set). The same is true of launcher exports: Bash commands, hooks
  and stdio MCP servers inherit the vendor key. `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` strips
  credentials by name or shape, including `ANTHROPIC_API_KEY` (CC-env, "What the subprocess
  environment scrub removes"); whether it removes custom names such as `ZAI_API_KEY` depends
  on the name looking like a credential.
- A project `env` block is applied after trust, which means a cloned repo can redirect
  `ANTHROPIC_BASE_URL` once you trust it. Inference: review `.claude/settings.json` `env` in
  repos you did not write. Codex blocks the equivalent in project config (CX-adv).
- Do not paste keys into the agent conversation (MM-cli; contrast ALI-cc).
- Do not run vendor `curl | bash` setup scripts or wizards for this purpose: they rewrite
  user-level config and one of them sets undocumented flags in `~/.claude.json` (KC-cc).
- Coding-plan terms: plan keys are personal, tool-restricted and, for Alibaba, interactive
  only. Kimi Code forbids altering the client User-Agent. Gemini forbids using its OAuth from
  other tools.
- Keys are region- and product-specific; a wrong pairing fails with 401 or bills the wrong
  account (ZAI-apikey, ALI-plan, KP-codex, MM-usage).
- Session data stays local but is sensitive: Kimi warns its session files "may contain user
  prompts, command output, repository paths, tool return values, or traces of credentials"
  (KCLI-agents). A project-local `KIMI_CODE_HOME`, `CODEX_HOME` or `CLAUDE_CONFIG_DIR` puts
  such files inside the repo directory, so the directory must be gitignored.
- Data location: Z.ai processes in Singapore under a Singapore entity (ZAI-privacy); Kimi and
  MiniMax and Alibaba run separate China and international hosts. No vendor page read gives a
  retention period for individual coding-plan traffic.
- Kimi Code hooks and Claude Code hooks are not security boundaries on their own; Kimi's are
  fail-open by design (KCLI-hooks).

## (d) What I could not verify

- Nothing here was executed. No endpoint, launcher, config file or model ID was tested.
- Whether Claude Code needs `hasCompletedOnboarding` in `~/.claude.json` when the token is
  exported in the shell. Kimi and Alibaba say to set it; CC-gwc says a shell-exported
  `ANTHROPIC_AUTH_TOKEN` is read before first-run setup. If it is needed, it is a global file.
- Precedence of `claude --settings` against project settings, and the full settings
  precedence order (CC settings page not read for this note).
- Whether `CLAUDE_CODE_EFFORT_LEVEL` and `/effort` send an effort value for unrecognised IDs
  without `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT=1`.
- Tool search, structured outputs, interleaved thinking and the auto-mode classifier on each
  vendor endpoint. Only DeepSeek publishes a field-by-field compatibility table. Kimi's
  cleanup script removes `ENABLE_TOOL_SEARCH`, which hints that older guides set it.
- Claude Code's built-in WebSearch on Z.ai, Kimi, MiniMax and Alibaba endpoints (only
  DeepSeek states support).
- Prompt-cache behaviour for Z.ai, Kimi, MiniMax and Alibaba through the Anthropic endpoint.
- ZCode's config, instruction file, skills and headless support (zcode.z.ai not fetched).
- DeepSeek Harness install command, config locations, instruction file and maturity.
- MiniMax Code project-level directories, skill and hook locations (repo `docs/` not fetched).
- Built-in OpenCode provider IDs for Z.ai, DeepSeek, Moonshot and Kimi For Coding, and where
  OpenCode stores credentials from `/connect`.
- Codex `-c` overrides for a whole provider table, and `env_key` with Z.ai, DeepSeek and
  MiniMax endpoints.
- Alibaba's OpenCode, Codex and Qwen Code tool pages, and all of docs.platform.qianwenai.com.
- Kimi Platform prices (table empty in the saved page), Kimi product comparison page, Kimi
  Code membership prices and tiers (page saved, not read).
- Data handling for DeepSeek, MiniMax, Alibaba and for individual Kimi accounts.
- Gemini model IDs, and whether any Anthropic-compatible Gemini endpoint exists.
- MiniMax China endpoint (`api.minimaxi.com`) appears only in a search result, not in a page
  I read.
- Saved but not read, so not used as evidence: docs.z.ai `guides/llm/glm-5.3`;
  api-docs.deepseek.com `updates`; deepseek-harness `guide/providers`,
  `reference/subsystems/skills`; platform.kimi.ai `api/messages`; kimi.com
  `kimi-code/membership`; kimi-code `configuration/providers`, `configuration/env-vars`,
  `customization/plugins`, `reference/slash-commands`, `guides/sessions`; platform.minimax.io
  `m-plan/quickstart`, `m-plan/other-tools`, `m-plan/faq`, `pricing/overview`; geminicli.com
  `cli/trusted-folders`; Qwen Code `quickstart`, `configuration/auth`, `features/mcp`,
  `features/commands`, `support/tos-privacy`.
- One line search across the Gemini pages was stopped by the user's secret-protection hook
  because the search pattern contained the text of a dotenv file name. I did not rephrase the
  command to get past it; I read the relevant documentation sections with the Read tool
  instead. No secret file was read.
- Injection check: no page tried to instruct the reader to do something outside its topic.
  Several pages contain prompts meant to be pasted into an agent (MM-cli "Install via an
  agent", ZAI-claude's Cursor prompt, ALI-cc's Bailian CLI steps). They were treated as
  content and not followed.

## Per source

Paths are under `refs/articles/`. All fetched 2026-11-10.

### Claude Code docs (Anthropic)

CC-model. Model configuration. File: code.claude.com/docs-en-model-config-md
URL: https://code.claude.com/docs/en/model-config.md
Thesis: how the model, aliases, effort, context window and compaction are chosen and
restricted. Practices: tier variables; `[1m]` suffix; `CLAUDE_CODE_MAX_CONTEXT_TOKENS` rules;
`ANTHROPIC_CUSTOM_MODEL_OPTION`; `modelOverrides`; prompt-cache switches. Numbers: compact
window 100K to 1M; unknown ID assumed 200K. Caveat: capability variables are written for
Bedrock, Vertex and Foundry. Relevance: high, it defines every variable the vendors use.

CC-gw. Other LLM gateways. File: code.claude.com/docs-en-llm-gateway-md
URL: https://code.claude.com/docs/en/llm-gateway.md
Thesis: Claude Code works with any gateway exposing a supported API format, but non-Claude
routing is unsupported. Relevance: high, it is the support boundary.

CC-gwc. Connect Claude Code to an LLM gateway. File: code.claude.com/docs-en-llm-gateway-connect-md
URL: https://code.claude.com/docs/en/llm-gateway-connect.md
Thesis: set base URL and credential, verify, per-surface notes, troubleshooting table.
Practices: token versus key header mapping; shell versus settings file; `/status` check;
curl test; `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`; `apiKeyHelper` (5-minute cache).
Caveats: background agents and shell-only exports; desktop app and VS Code differ.
Relevance: high.

CC-gws. Run Claude Code through a gateway. File: code.claude.com/docs-en-gateways-md
URL: https://code.claude.com/docs/en/gateways.md
Thesis: gateway architecture and Anthropic's own gateway. Repeats the non-Claude statement.
Relevance: medium.

CC-3p. Enterprise deployment overview. File: code.claude.com/docs-en-third-party-integrations-md
URL: https://code.claude.com/docs/en/third-party-integrations.md
Thesis: choosing Anthropic, Bedrock, Agent Platform or Foundry; pin model versions.
Relevance: low for this question; "third-party provider" there means cloud Claude hosts.

CC-env. Environment variables. File: code.claude.com/docs-en-env-vars-md
URL: https://code.claude.com/docs/en/env-vars.md
Thesis: full variable reference, precedence, subprocess scrub, feature-flag list.
Practices: every variable named in this note. Caveat: several variables are ignored in
project and local settings. Relevance: high.

CC-cost. Manage costs effectively. File: code.claude.com/docs-en-costs-md
URL: https://code.claude.com/docs/en/costs.md
Thesis: tracking and reducing token use. Numbers: about $13 per developer per active day on
enterprise deployments. Relevance: low here; cost figures assume Claude list prices.

CC-fast. Fast mode. File: code.claude.com/docs-en-fast-mode-md
URL: https://code.claude.com/docs/en/fast-mode.md
Thesis: faster Opus and Fable at higher price, Anthropic API only. Relevance: low; note to
disable on vendor routes.

CC-adv. Advisor tool. File: code.claude.com/docs-en-advisor-md
URL: https://code.claude.com/docs/en/advisor.md
Thesis: a second stronger model consulted mid-task, server-side on Anthropic. Relevance: low;
unavailable on vendor routes.

CC-set (partial: `env` entry and its three subsections). File:
code.claude.com/docs-en-settings-reference-md
CC-mcp (partial: "Tool search through an LLM gateway"). File: code.claude.com/docs-en-mcp-md

### Z.ai (docs.z.ai)

ZAI-claude. Claude Code (devpack). File: docs.z.ai/devpack-tool-claude-md
URL: https://docs.z.ai/devpack/tool/claude.md
Thesis: use the GLM Coding Plan in Claude Code through `~/.claude/settings.json`.
Tools and files: `npx @z_ai/coding-helper`, `claude_code_zai_env.sh`. Caveat: user-level only.
Relevance: high.

ZAI-latest. How to Switch Models. File: docs.z.ai/devpack-latest-model-md
URL: https://docs.z.ai/devpack/latest-model.md
Thesis: current GLM-5.3 IDs, `[1m]`, effort conversion table, endpoints per tool.
Relevance: high.

ZAI-codex. File: docs.z.ai/devpack-tool-codex-md   ZAI-oc. File: docs.z.ai/devpack-tool-opencode-md
URLs: https://docs.z.ai/devpack/tool/codex.md, https://docs.z.ai/devpack/tool/opencode.md
Relevance: high for the route settings quoted above.

ZAI-overview, ZAI-faq, ZAI-policy, ZAI-apikey, ZAI-others, ZAI-quick, ZAI-helper, ZAI-pricing,
ZAI-zcode, ZAI-privacy. Files: docs.z.ai/devpack-overview-md, devpack-faq-md,
devpack-usage-policy-md, devpack-notice-api-key-management-md, devpack-tool-others-md,
devpack-quick-start-md, devpack-extension-coding-tool-helper-md, guides-overview-pricing-md,
devpack-tool-zcode-md, legal-agreement-privacy-policy-md.
Relevance: medium (plan rules, key types, prices, data location).

ZAI-scen-claude (full) and scenario opencode (first 80 lines only). Files:
docs.z.ai/scenario-example-develop-tools-claude-md, scenario-example-develop-tools-opencode-md.
Stale duplicates that still name GLM-4.7. Relevance: low.

### DeepSeek

DS-cc. Integrate with Claude Code. File: api-docs.deepseek.com/quick-start-agent-integrations-claude-code-md
URL: https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code.md
Relevance: high.

DS-anth. Using the Anthropic API. File: api-docs.deepseek.com/guides-anthropic-api-md
URL: https://api-docs.deepseek.com/guides/anthropic_api.md
Thesis: field-by-field Anthropic compatibility. The only such table among the vendors.
Relevance: high.

DS-codex. File: api-docs.deepseek.com/quick-start-agent-integrations-codex-md (four embedded
18K-character prompt strings were read by head and tail only).
DS-oc, DS-index, DS-news, DS-pricing, DS-reasonix. Files: quick-start-agent-integrations-opencode-md,
index, news-news261017, quick-start-pricing-md, quick-start-agent-integrations-reasonix.
DS-harness-quick and the system-prompt reference. Files:
deepseek-harness.github.io/deepseek-harness-en-guide-quickstart-md,
deepseek-harness-en-reference-subsystems-system-prompt-md (the latter is SDK internals, no use
here). Relevance: medium to low.

### Moonshot / Kimi

KP-cc. Use Kimi in Claude Code. File: platform.kimi.ai/docs-guide-claude-code-kimi-md
URL: https://platform.kimi.ai/docs/guide/claude-code-kimi.md  Relevance: high.
KP-oc, KP-codex, KP-cli, KP-models, KP-price, KP-zdr. Files: docs-guide-open-code-md,
docs-guide-codex-kimi-md, docs-guide-kimi-code-cli-md, docs-models-md, docs-pricing-chat-md,
docs-guide-zero-data-retention-md. Relevance: high to medium.

KC-cc. Claude Code (Kimi Code membership). File: kimi.com/code-docs-en-third-party-tools-claude-code-html
URL: https://www.kimi.com/code/docs/en/third-party-tools/claude-code.html  Relevance: high.
KC-overview, KC-oc, KC-codex. Files: kimi.com/code-docs-en,
code-docs-en-third-party-tools-opencode-html, code-docs-en-third-party-tools-codex-html.

KCLI-start, KCLI-data, KCLI-skills, KCLI-mig, KCLI-agents, KCLI-hooks, KCLI-over (all full).
Files: moonshotai.github.io/kimi-code-en-guides-getting-started-md,
kimi-code-en-configuration-data-locations-md, kimi-code-en-customization-skills-md,
kimi-code-en-guides-migration-md, kimi-code-en-customization-agents-md,
kimi-code-en-customization-hooks-md, kimi-code-en-configuration-overrides-md.
KCLI-cfg (partial: location, example, top-level fields, providers, watch, workspace trust,
services, permission, project-local configuration), KCLI-cmd (partial: non-interactive
execution), KCLI-mcp (partial: configuration). Files: kimi-code-en-configuration-config-files-md,
kimi-code-en-reference-kimi-command-md, kimi-code-en-customization-mcp-md.
Thesis: a Claude Code-like CLI with user-level config and project-level content files.
Relevance: high; it is the most complete vendor harness documented.

### Alibaba / Qwen

ALI-cc. Claude Code (Model Studio). File: alibabacloud.com/help-en-model-studio-claude-code-coding-plan
(identical content saved again as help-en-model-studio-claude-code).
URL: https://www.alibabacloud.com/help/en/model-studio/claude-code-coding-plan  Date 2026-11-05.
ALI-plan. Coding plan overview. File: alibabacloud.com/help-en-model-studio-coding-plan
Date 2026-11-04. Relevance: medium (requested as a "check").
QW-overview (full). File: qwenlm.github.io/qwen-code-docs-en-users-overview  Date 2026-11-09.
QW-memory (partial: QWEN.md section), QW-settings (partial: configuration layers and settings
files), QW-providers (partial: `envKey` note). QW-skills, QW-subagents, QW-headless: line
search only. Relevance: medium.

### MiniMax

MM-cc, MM-code, MM-oc, MM-codex, MM-intro, MM-usage, MM-models, MM-cli (all full). Files:
platform.minimax.io/docs-m-plan-claude-code-md, docs-m-plan-minimax-code-md,
docs-m-plan-opencode-md, docs-m-plan-codex-md, docs-m-plan-intro-md, docs-m-plan-usage-rules-md,
docs-guides-models-intro-md, docs-m-plan-minimax-cli-md.
MM-readme (full). File: raw.githubusercontent.com/minimax-ai-minimax-code-main-readme-md
URL: https://raw.githubusercontent.com/MiniMax-AI/minimax-code/main/README.md
Evidence and numbers: 512K versus 1M comparison on 200 tasks, 18.5% fewer tokens, 19.9% lower
estimated charges (vendor's own benchmark). Relevance: medium.

### Gemini CLI

GEM-md, GEM-skills, GEM-headless, GEM-ext, GEM-quota, GEM-tos (full). Files:
geminicli.com/docs-cli-gemini-md-md, docs-cli-skills-md, docs-cli-headless-md,
docs-extensions-md, docs-resources-quota-and-pricing-md, docs-resources-tos-privacy-md.
GEM-install (first 70 lines), GEM-config (first 75 lines), GEM-auth (API key and persisting
variables sections). GEM-subagents, GEM-hooks, GEM-commands, GEM-mcp: line search only.
Relevance: medium.

### OpenCode and Codex (context for the routes)

OC-prov (full). File: opencode.ai/docs-providers-md  URL: https://opencode.ai/docs/providers.md
OC-cfg (partial: Locations, Providers, Variables). File: opencode.ai/docs-config-md
CX-adv (partial: Profiles, CLI overrides, state locations, project config files, hooks intro).
File: learn.chatgpt.com/docs-config-file-config-advanced-md
CX-env and config-basic: line search only. Files:
learn.chatgpt.com/docs-config-file-environment-variables-md, docs-config-file-config-basic-md.
Relevance: high for the design section; these harnesses are covered in depth by other notes.
