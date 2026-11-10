---
title: "Release 0.167.0 · openai/codex"
date: "2026-11-06"
url: "https://github.com/openai/codex/releases/latest"
site: "GitHub"
type: "article"
via: "direct"
---
## Repository navigation

[github-actions](https://github.com/apps/github-actions)released this

·
          
            [440 commits](https://github.com/openai/codex/compare/rust-v0.167.0...main)
          
          to main
          since this release

## New Features

- Open the agent command center with `codex agents --no-daemon`. The command center and session picker now mark unread results ([#58238](https://github.com/openai/codex/pull/58238), [#58239](https://github.com/openai/codex/pull/58239), [#58263](https://github.com/openai/codex/pull/58263), [#58264](https://github.com/openai/codex/pull/58264)).
- Switch between connected backends from the terminal session picker and keep your drafts when switching ([#58280](https://github.com/openai/codex/pull/58280), [#58457](https://github.com/openai/codex/pull/58457)).
- Preview local image attachments while composing on supported terminals, and open viewed local images from clickable transcript paths ([#58261](https://github.com/openai/codex/pull/58261), [#58446](https://github.com/openai/codex/pull/58446)).
- Find API key and cloud provider options under “Sign in another way.” Enable `gcp_setup_wizard` to set up Google Cloud Vertex AI with Application Default Credentials or a credential file ([#57857](https://github.com/openai/codex/pull/57857), [#58427](https://github.com/openai/codex/pull/58427)).
- Opt into macOS or Windows system proxy settings from `/experimental` ([#58157](https://github.com/openai/codex/pull/58157)).
- Expand patch details directly in the transcript while an approval prompt is open ([#58281](https://github.com/openai/codex/pull/58281)).

## Bug Fixes

- Saved chats stay visible after you switch model providers. If a chat can’t resume, you can read its transcript and prepare an editable prompt to continue in a new chat ([#58202](https://github.com/openai/codex/pull/58202)).
- `Ctrl+L` clears the terminal display while keeping earlier messages available through `Ctrl+T` ([#58266](https://github.com/openai/codex/pull/58266)).
- Deleting text that exposes a leading `!` keeps an ordinary draft in chat mode ([#58412](https://github.com/openai/codex/pull/58412)).
- Network approval prompts close when their requests end. Concurrent requests to the same endpoint prompt one at a time ([#58350](https://github.com/openai/codex/pull/58350), [#58351](https://github.com/openai/codex/pull/58351)).
- Long realtime V3 conversations save completed speech to chat history as the transcript grows ([#58221](https://github.com/openai/codex/pull/58221)).
- Automatic context compaction now accounts for retained output from failed responses and responses with missing token usage data ([#58404](https://github.com/openai/codex/pull/58404)).

## Documentation

- The app-server README covers managed network constraints under `[permissions.network]` and `prompt-user` command rules that require fresh human approval ([#58045](https://github.com/openai/codex/pull/58045), [#58182](https://github.com/openai/codex/pull/58182)).
- The `openai-docs` skill recommends the documented replacement when migrating away from a deprecated model ([#58134](https://github.com/openai/codex/pull/58134)).

## Chores

- DotSlash manifests now reference the Cargo packages shipped with the release ([#58717](https://github.com/openai/codex/pull/58717), [#58757](https://github.com/openai/codex/pull/58757)).
- Linux musl builds use fewer allocator arenas to reduce idle memory after conversations unload ([#58399](https://github.com/openai/codex/pull/58399)).

## Changelog

Full Changelog: `rust-v0.166.0...rust-v0.167.0`

- [#57848](https://github.com/openai/codex/pull/57848) Add bounded Code Mode output collection and rendering [@seanh-oai](https://github.com/seanh-oai)
- [#57850](https://github.com/openai/codex/pull/57850) Wire bounded output collection into the code mode runtime [@seanh-oai](https://github.com/seanh-oai)
- [#57855](https://github.com/openai/codex/pull/57855) Load TUI plugin mentions from installed plugins [@zamoshchin-openai](https://github.com/zamoshchin-openai)
- [#57857](https://github.com/openai/codex/pull/57857) Add Google Cloud Vertex AI setup to TUI onboarding [@alexsong-oai](https://github.com/alexsong-oai)
- [#57859](https://github.com/openai/codex/pull/57859) Extend the provider OAuth sign-in timeout to ten minutes [@smurching-oai](https://github.com/smurching-oai)
- [#57861](https://github.com/openai/codex/pull/57861) Skip resource template discovery for hosted Apps [@khong-oai](https://github.com/khong-oai)
- [#57862](https://github.com/openai/codex/pull/57862) Keep resume picker pagination moving across backends [@bc-openai](https://github.com/bc-openai)
- [#57864](https://github.com/openai/codex/pull/57864) Allow upstream interruption when canceling Responses Lite turns [@liame-oai](https://github.com/liame-oai)
- [#57866](https://github.com/openai/codex/pull/57866) Retry transient environment startup failures on the next turn [@pansul47-oai](https://github.com/pansul47-oai)
- [#57870](https://github.com/openai/codex/pull/57870) Enable server-side output truncation for Code Mode sessions [@seanh-oai](https://github.com/seanh-oai)
- [#57876](https://github.com/openai/codex/pull/57876) Reuse the cached runtime keymap for default configuration [@bc-openai](https://github.com/bc-openai)
- [#57883](https://github.com/openai/codex/pull/57883) Preserve status-line hyperlinks through footer layout and animations [@joesavona](https://github.com/joesavona)
- [#57970](https://github.com/openai/codex/pull/57970) Add an experimental UI tree renderer for the status line [@joesavona](https://github.com/joesavona)
- [#57974](https://github.com/openai/codex/pull/57974) Apply session plugin overrides during MCP config refresh [@TAFOYA-OAI](https://github.com/TAFOYA-OAI)
- [#57978](https://github.com/openai/codex/pull/57978) Add per-chat leases for shared MCP connections [@charliemarsh-oai](https://github.com/charliemarsh-oai)
- [#57985](https://github.com/openai/codex/pull/57985) Skip read-only volume-root expansion in the MXC sandbox [@iceweasel-oai](https://github.com/iceweasel-oai)
- [#58013](https://github.com/openai/codex/pull/58013) Fix argument comment lint tests after rust-clippy branch rename [@seanh-oai](https://github.com/seanh-oai)
- [#58025](https://github.com/openai/codex/pull/58025) Add trace-safe diagnostics for Noise relay request progress [@apanasenko-oai](https://github.com/apanasenko-oai)
- [#58028](https://github.com/openai/codex/pull/58028) Add direct Guardian review of recorded exec calls [@swastik-oai](https://github.com/swastik-oai)
- [#58034](https://github.com/openai/codex/pull/58034) Add an option to disable successful SSE delta logs [@jif-oai](https://github.com/jif-oai)
- [#58040](https://github.com/openai/codex/pull/58040) Preserve native tool-call evidence through Guardian review [@ioanbudea-OAI](https://github.com/ioanbudea-OAI)
- [#58045](https://github.com/openai/codex/pull/58045) Add managed command checkpoints requiring fresh human approval [@jif-oai](https://github.com/jif-oai)
- [#58057](https://github.com/openai/codex/pull/58057) Initialize `native_call` in agent host test fixtures [@jif-oai](https://github.com/jif-oai)
- [#58071](https://github.com/openai/codex/pull/58071) Share the Guardian context delivery token limit [@ioanbudea-OAI](https://github.com/ioanbudea-OAI)
- [#58075](https://github.com/openai/codex/pull/58075) Use serving assessments for adaptive Guardian review [@jif-oai](https://github.com/jif-oai)
- [#58083](https://github.com/openai/codex/pull/58083) Use a dedicated binary for Bazel schema generation [@jif-oai](https://github.com/jif-oai)
- [#58091](https://github.com/openai/codex/pull/58091) Update default models for memory extraction and consolidation [@jif-oai](https://github.com/jif-oai)
- [#58110](https://github.com/openai/codex/pull/58110) Ignore RUSTSEC-2026-0418 for the Windows-only libz-sys dependency [@swastik-oai](https://github.com/swastik-oai)
- [#58119](https://github.com/openai/codex/pull/58119) Add experimental Guardian review for injected thread commands [@swastik-oai](https://github.com/swastik-oai)
- [#58121](https://github.com/openai/codex/pull/58121) Centralize provider request preparation auth checks [@sgarg-oai](https://github.com/sgarg-oai)
- [#58122](https://github.com/openai/codex/pull/58122) Add an incremental exec tools feature flag [@akira-oai](https://github.com/akira-oai)
- [#58123](https://github.com/openai/codex/pull/58123) Add validated elastic section budget configuration for Guardian [@ioanbudea-OAI](https://github.com/ioanbudea-OAI)
- [#58125](https://github.com/openai/codex/pull/58125) Support negotiated server-side truncation in Code Mode clients [@seanh-oai](https://github.com/seanh-oai)
- [#58127](https://github.com/openai/codex/pull/58127) Honor the tooltip preference for TUI startup help [@imac-oai](https://github.com/imac-oai)
- [#58129](https://github.com/openai/codex/pull/58129) Persist subagent relationships before creating child storage [@radai-oai](https://github.com/radai-oai)
- [#58130](https://github.com/openai/codex/pull/58130) Support pasted search text in the skills toggle view [@xma-oai](https://github.com/xma-oai)
- [#58134](https://github.com/openai/codex/pull/58134) Prefer documented replacements for deprecation-driven model migrations [@kkahadze-oai](https://github.com/kkahadze-oai)
- [#58140](https://github.com/openai/codex/pull/58140) Route standalone web search through the thread's workspace context [@sgarg-oai](https://github.com/sgarg-oai)
- [#58144](https://github.com/openai/codex/pull/58144) Record additional context counts, sizes, and truncation metrics [@akira-oai](https://github.com/akira-oai)
- [#58147](https://github.com/openai/codex/pull/58147) Return standalone web search failures to the model [@sgarg-oai](https://github.com/sgarg-oai)
- [#58157](https://github.com/openai/codex/pull/58157) Expose system proxy support as an experimental setting [@abhinav-oai](https://github.com/abhinav-oai)
- [#58159](https://github.com/openai/codex/pull/58159) Add a feature flag for code-mode host output truncation [@seanh-oai](https://github.com/seanh-oai)
- [#58161](https://github.com/openai/codex/pull/58161) Include tool names and annotation hints in MCP approval metadata [@brisebois-oai](https://github.com/brisebois-oai)
- [#58165](https://github.com/openai/codex/pull/58165) Keep remote plugin bundle URLs out of diagnostics [@mzeng-openai](https://github.com/mzeng-openai)
- [#58166](https://github.com/openai/codex/pull/58166) Make rollout recording failures and completion explicit [@cassirer-openai](https://github.com/cassirer-openai)
- [#58168](https://github.com/openai/codex/pull/58168) Create missing parent directories for MXC deny paths on Windows [@iceweasel-oai](https://github.com/iceweasel-oai)
- [#58171](https://github.com/openai/codex/pull/58171) Stabilize cancellation and tracing tests [@aakash-oai](https://github.com/aakash-oai)
- [#58172](https://github.com/openai/codex/pull/58172) Validate trace completion records and payload UTF-8 during replay [@cassirer-openai](https://github.com/cassirer-openai)
- [#58182](https://github.com/openai/codex/pull/58182) Support managed network requirements under `permissions.network` [@viyatb-oai](https://github.com/viyatb-oai)
- [#58189](https://github.com/openai/codex/pull/58189) Use turn-scoped permissions for standalone web search [@sayan-oai](https://github.com/sayan-oai)
- [#58190](https://github.com/openai/codex/pull/58190) Allow providers to opt into Cyber access programs [@jamy-OAI](https://github.com/jamy-OAI)
- [#58195](https://github.com/openai/codex/pull/58195) Preserve remote read compatibility with older executors [@dkovalenko-oai](https://github.com/dkovalenko-oai)
- [#58196](https://github.com/openai/codex/pull/58196) Require Bazel release artifacts and publish DotSlash manifests [@dkovalenko-oai](https://github.com/dkovalenko-oai)
- [#58198](https://github.com/openai/codex/pull/58198) Centralize TOML config deserialization [@dkovalenko-oai](https://github.com/dkovalenko-oai)
- [#58202](https://github.com/openai/codex/pull/58202) Keep chats accessible across model provider changes [@abhinav-oai](https://github.com/abhinav-oai)
- [#58219](https://github.com/openai/codex/pull/58219) Add file-backed storage for gateway OAuth credentials [@alexsong-oai](https://github.com/alexsong-oai)
- [#58221](https://github.com/openai/codex/pull/58221) Preserve realtime V3 transcripts in conversation history [@guinness-oai](https://github.com/guinness-oai)
- [#58237](https://github.com/openai/codex/pull/58237) Preserve unrelated side conversations when archiving or deleting threads [@etraut-openai](https://github.com/etraut-openai)
- [#58238](https://github.com/openai/codex/pull/58238) Enable the agent command center for embedded sessions [@etraut-openai](https://github.com/etraut-openai)
- [#58239](https://github.com/openai/codex/pull/58239) Enable the agent command center in embedded mode [@etraut-openai](https://github.com/etraut-openai)
- [#58240](https://github.com/openai/codex/pull/58240) Enable TUI task tools for embedded app-server sessions [@etraut-openai](https://github.com/etraut-openai)
- [#58241](https://github.com/openai/codex/pull/58241) Update `mio` from 1.2.0 to 1.2.4 [@euroelessar](https://github.com/euroelessar)
- [#58251](https://github.com/openai/codex/pull/58251) Reload remote executor credentials safely across token rotation [@tgrue-openai](https://github.com/tgrue-openai)
- [#58260](https://github.com/openai/codex/pull/58260) Reuse `LocalImageAttachment` throughout the TUI composer [@etraut-openai](https://github.com/etraut-openai)
- [#58261](https://github.com/openai/codex/pull/58261) Add local image thumbnails to the TUI composer [@etraut-openai](https://github.com/etraut-openai)
- [#58263](https://github.com/openai/codex/pull/58263) Show unread results in the TUI command center [@etraut-openai](https://github.com/etraut-openai)
- [#58264](https://github.com/openai/codex/pull/58264) Show unread sessions and acknowledge viewed transcripts in the picker [@etraut-openai](https://github.com/etraut-openai)
- [#58266](https://github.com/openai/codex/pull/58266) Preserve transcript history when clearing the terminal with Ctrl+L [@xma-oai](https://github.com/xma-oai)
- [#58270](https://github.com/openai/codex/pull/58270) Recognize Rex terminals and enable Kitty graphics for pets [@etraut-openai](https://github.com/etraut-openai)
- [#58280](https://github.com/openai/codex/pull/58280) Reuse connected backends in the in-app resume picker [@bc-openai](https://github.com/bc-openai)
- [#58281](https://github.com/openai/codex/pull/58281) Allow inline patch review during approval prompts [@etraut-openai](https://github.com/etraut-openai)
- [#58324](https://github.com/openai/codex/pull/58324) Treat auth reload failures as transient during token refresh [@jif-oai](https://github.com/jif-oai)
- [#58341](https://github.com/openai/codex/pull/58341) Add an MCP adapter for message-board tools [@jif-oai](https://github.com/jif-oai)
- [#58343](https://github.com/openai/codex/pull/58343) Preserve fallback token refreshes when the keyring is unreadable [@jif-oai](https://github.com/jif-oai)
- [#58350](https://github.com/openai/codex/pull/58350) Resolve network approval prompts when their requests end [@charliemarsh-oai](https://github.com/charliemarsh-oai)
- [#58351](https://github.com/openai/codex/pull/58351) Serialize manual network approval prompts per endpoint [@charliemarsh-oai](https://github.com/charliemarsh-oai)
- [#58352](https://github.com/openai/codex/pull/58352) Allow Apps catalog discovery before the initial tool inventory completes [@bkotsopoulos](https://github.com/bkotsopoulos)
- [#58355](https://github.com/openai/codex/pull/58355) Fix remote executor authentication timeout recovery [@jif-oai](https://github.com/jif-oai)
- [#58357](https://github.com/openai/codex/pull/58357) Extract pre-tool-use hook handling into a helper [@swastik-oai](https://github.com/swastik-oai)
- [#58361](https://github.com/openai/codex/pull/58361) Preserve model metadata origin through runtime resolution [@ioanbudea-OAI](https://github.com/ioanbudea-OAI)
- [#58368](https://github.com/openai/codex/pull/58368) Apply PreToolUse hooks before direct Guardian review policy checks [@swastik-oai](https://github.com/swastik-oai)
- [#58378](https://github.com/openai/codex/pull/58378) Scope agent MCP metadata to a host-selected plugin registration [@rhan-oai](https://github.com/rhan-oai)
- [#58380](https://github.com/openai/codex/pull/58380) Broadcast thread section changes to connected clients [@charliemarsh-oai](https://github.com/charliemarsh-oai)
- [#58381](https://github.com/openai/codex/pull/58381) Fix unsettled refresh detection after workspace switching [@jif-oai](https://github.com/jif-oai)
- [#58385](https://github.com/openai/codex/pull/58385) Test V8 inline typed array storage limits [@fcoury-oai](https://github.com/fcoury-oai)
- [#58388](https://github.com/openai/codex/pull/58388) Add whole-entry elastic allocation for Guardian context [@ioanbudea-OAI](https://github.com/ioanbudea-OAI)
- [#58390](https://github.com/openai/codex/pull/58390) Expose parent context for host-managed child startup [@rhan-oai](https://github.com/rhan-oai)
- [#58395](https://github.com/openai/codex/pull/58395) Add scoped host metadata hooks for MCP tool requests [@rhan-oai](https://github.com/rhan-oai)
- [#58399](https://github.com/openai/codex/pull/58399) Reduce jemalloc arena count for Linux musl builds [@dkovalenko-oai](https://github.com/dkovalenko-oai)
- [#58403](https://github.com/openai/codex/pull/58403) Run package updates outside the project on non-Windows platforms [@viyatb-oai](https://github.com/viyatb-oai)
- [#58404](https://github.com/openai/codex/pull/58404) Fix context token estimates for responses without usable usage [@dkovalenko-oai](https://github.com/dkovalenko-oai)
- [#58405](https://github.com/openai/codex/pull/58405) Add an option to suppress incremental model change announcements [@chetan-oai](https://github.com/chetan-oai)
- [#58406](https://github.com/openai/codex/pull/58406) Add host-inherited thread instructions and execution policies [@rhan-oai](https://github.com/rhan-oai)
- [#58410](https://github.com/openai/codex/pull/58410) Enable deferred tool world state by default [@adaley-openai](https://github.com/adaley-openai)
- [#58411](https://github.com/openai/codex/pull/58411) Expose non-consuming input activity waits to hosts [@rhan-oai](https://github.com/rhan-oai)
- [#58412](https://github.com/openai/codex/pull/58412) Keep exposed leading bangs literal in the chat composer [@xma-oai](https://github.com/xma-oai)
- [#58418](https://github.com/openai/codex/pull/58418) Simplify recorded exec command review [@swastik-oai](https://github.com/swastik-oai)
- [#58427](https://github.com/openai/codex/pull/58427) Group alternative sign-in methods in a submenu [@alexsong-oai](https://github.com/alexsong-oai)
- [#58428](https://github.com/openai/codex/pull/58428) Support app settings in plugin configuration [@mzeng-openai](https://github.com/mzeng-openai)
- [#58430](https://github.com/openai/codex/pull/58430) Add audio file references with explicit runtime rejection [@hung-oai](https://github.com/hung-oai)
- [#58434](https://github.com/openai/codex/pull/58434) Treat audio validation failures as non-retryable input errors [@hung-oai](https://github.com/hung-oai)
- [#58436](https://github.com/openai/codex/pull/58436) Add interactive controls and refresh inline visualization styles [@philipp-oai](https://github.com/philipp-oai)
- [#58441](https://github.com/openai/codex/pull/58441) Preserve Apps usage instructions in model catalog messages [@goodman-oai](https://github.com/goodman-oai)
- [#58444](https://github.com/openai/codex/pull/58444) Cap Guardian context entries before elastic allocation [@ioanbudea-OAI](https://github.com/ioanbudea-OAI)
- [#58446](https://github.com/openai/codex/pull/58446) Make viewed image paths clickable in the TUI [@etraut-openai](https://github.com/etraut-openai)
- [#58454](https://github.com/openai/codex/pull/58454) Add elastic budgeting for Guardian context preparation [@ioanbudea-OAI](https://github.com/ioanbudea-OAI)
- [#58456](https://github.com/openai/codex/pull/58456) Preserve incomplete response output in failed inference traces [@cassirer-openai](https://github.com/cassirer-openai)
- [#58457](https://github.com/openai/codex/pull/58457) Enable cross-backend session switching in the TUI [@bc-openai](https://github.com/bc-openai)
- [#58459](https://github.com/openai/codex/pull/58459) Tighten Bazel CI snapshot handling and OTLP test cleanup [@imac-oai](https://github.com/imac-oai)
- [#58713](https://github.com/openai/codex/pull/58713) Extract fresh session adoption from TUI session startup [@bc-openai](https://github.com/bc-openai)
- [#58714](https://github.com/openai/codex/pull/58714) Sort agent center tasks by recency within status groups [@etraut-openai](https://github.com/etraut-openai)
- [#58716](https://github.com/openai/codex/pull/58716) Support OSC 52 clipboard forwarding through GNU screen [@etraut-openai](https://github.com/etraut-openai)
- [#58717](https://github.com/openai/codex/pull/58717) Make Bazel checks advisory and pause Bazel release artifacts [@dkovalenko-oai](https://github.com/dkovalenko-oai)
- [#58718](https://github.com/openai/codex/pull/58718) Support rendering TUI conversations within an inset area [@fcoury-oai](https://github.com/fcoury-oai)
- [#58719](https://github.com/openai/codex/pull/58719) Wire native voice dependencies into full Rust CI [@bc-openai](https://github.com/bc-openai)
- [#58720](https://github.com/openai/codex/pull/58720) Prioritize pending approvals in the subagent picker [@tamird](https://github.com/tamird)
- [#58722](https://github.com/openai/codex/pull/58722) Add naming and navigation helpers for TUI backend sessions [@bc-openai](https://github.com/bc-openai)
- [#58727](https://github.com/openai/codex/pull/58727) Use local Bazel for voice release builds [@fcoury-oai](https://github.com/fcoury-oai)
- [#58751](https://github.com/openai/codex/pull/58751) Release superseded assistant text from live paginated history [@btraut-openai](https://github.com/btraut-openai)
- [#58757](https://github.com/openai/codex/pull/58757) Remove Bazel outputs from DotSlash release configs [@fcoury-oai](https://github.com/fcoury-oai)
