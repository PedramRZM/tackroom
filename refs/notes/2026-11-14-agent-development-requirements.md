# Requirements audit: session handoff, questions, storage and task review

Research date: 2026-11-14. Extends the Hetzner/Coder/Claude-subscription proposal.
The user requires GitHub Issues and Coder/terminal interaction, without Claude web
or Desktop as a task interface. Design review only; nothing deployed.

## Questions

1. Can the owner continue the actual agent session in Coder or on a laptop, and what
   differs between SSH access and moving execution to the laptop?
2. How do agent questions, permission requests and external-tool prompts reach GitHub
   or Coder, including during long waits and after a restart?
3. What is the minimum artifact store without S3, and what can Vercel provide?
4. How are exact preview URLs discovered and task acceptance tests run against them?
5. What implementation decisions and proof belong in the GitHub issue, and how does
   the owner return review feedback?
7. How does scoping discover related flows, components and in-product integrations?

## Recommendation and audit result

Keep the [Hetzner/Coder proposal](2026-11-13-hetzner-claude-subscription-development.md):
official Claude Code with the owner's subscription, a small trusted controller,
GitHub Issues, Vercel deployments and Neon task data. Add a durable session handoff,
an input bridge, and explicit scope/report contracts. None of these requires AI
Gateway or Claude web/Desktop as the task interface.

**Inference:** the requirements are achievable, but they are not features that Coder
and a Docker image automatically provide. The controller and runner still need to be
built. This audit checks documented capabilities; it does not claim a working pilot.

| User requirement | Finding | Required change to the proposal |
|---|---|---|
| 1. Continue in native Claude Code | CLI can resume SDK sessions by explicit ID; conversation and filesystem are separate [S1, S2] | Preserve native transcripts, code and launch configuration; implement exclusive takeover |
| 2. Answer through GitHub or Coder | SDK callbacks support Claude questions, permissions and MCP input; arbitrary terminal prompts need separate handling [I1–I3] | Build the interaction bridge now, with terminal takeover as a fallback |
| 3. Operate without S3 | Private Vercel Blob is available; a persistent server directory also suffices for a small pilot [B1, B2] | Make storage a deployment choice; never rely on disposable worker disk |
| 4. Test the actual preview | Vercel provides deployment identifiers/URLs and an API to verify them [V1, V2] | Bind tests to the exact deployment and source revision |
| 5. Explain decisions and accept review | GitHub is already the chosen control surface | Require a versioned implementation report and revision-bound feedback |
| 7. Investigate related product behavior | Existing `/spec` and `/verify` cover grounded acceptance and nearby behavior | Add an explicit impact map and a gate for unresolved affected flows |

All proposed commands, database records and gates below are **design inferences**.
They are custom controller behavior, not existing GitHub or Coder commands.

## 1. Continue the real session

Anthropic documents native CLI resumption of SDK/print-mode sessions using an explicit
session ID. Those sessions do not appear in the ordinary interactive picker or
`claude --continue`. `/export` produces readable text, not a resumable session. Resuming
restores conversation context, including its saved compaction state; it does not
restore the working tree, browser, dev server or an interrupted tool process. [S1, S2]

### Coder and laptop SSH: the first implementation

Store the root session ID on each attempt. The issue has **Open workspace** and
**Take over session** links. Takeover first stops the automated writer, confirms its
process tree has stopped, checkpoints state, and transfers ownership to the human.
Then the owner uses Coder's browser terminal, or connects from the laptop: [C1]

```text
coder ssh <workspace-name>
cd <task-checkout>
claude --resume <recorded-session-id>
```

These are native tools, after the proposed controller has completed the handoff.
The generated launch command must also restore the approved settings/MCP/plugin
arguments. Run from the task's checkout. The laptop SSH option keeps execution on
Hetzner; it does not move the task onto the laptop.

Keep one writer per session. Do not run the SDK and an interactive CLI against the
same transcript at once. The owner holds the logical task slot during takeover, so
automation cannot silently start a fourth implementation. Returning control requires
the interactive process to stop and a new checkpoint before the runner resumes. [S1;
ownership and capacity rules are inference]

### Actually moving execution onto the laptop

Support an explicit **Move to laptop** handoff as a second milestone. Package:

- Native session JSONL and required session sidecar/subagent files, copied opaquely.
- Repository revision, branch and all intended uncommitted/untracked work.
- Pinned harness, CLI/SDK versions, settings, tool inventory and startup instructions.
- Resource identifiers for the task's dev data, with access re-established locally.

The laptop signs in independently. Do not export the worker's whole home/configuration
directory or account login. Restore the checkout and approved runtime, then resume
the native session by ID or the documented absolute JSONL path. Stored paths and
host-dependent tools need a compatibility check; a matching dev container can reduce
differences. There is no automatic running-process migration or bidirectional sync.
Returning from the laptop is another exclusive checkpoint/import operation. [S1, S2;
packaging and compatibility protocol are inference]

The first pilot must demonstrate that an unresolved task can be resumed, changed,
returned and verified with its history intact. A fresh session with a prose summary
is a recovery option requiring a visible warning; it does not satisfy this requirement.

### State that must survive worker cleanup

Distinguish **slot login**, **task session**, **task filesystem**, and **approved project
memory**. The earlier reset language was too broad: task history must survive release
of the worker even though it must not leak into an unrelated task. Back up session and
work checkpoints to the controller's private store before deleting a task workspace.
Persist hashes and the last confirmed checkpoint revision. Failed checkpointing blocks
cleanup; recovery must report the last preserved point instead of claiming zero loss.

Prefer native local session persistence plus checkpoint backups initially. Anthropic's
external `SessionStore` API is an option later, but a resumed session uses a temporary
configuration directory that is deleted at the end; a native CLI handoff therefore
needs explicit materialization. It also has mirroring-error behavior and does not
replace filesystem snapshots. Do not assume a session ID in Postgres is a backup. [S3]

Retain open task sessions beyond ordinary CLI cleanup if necessary; current default
session cleanup is 30 days. Dormant tasks consume storage, not live Claude processes.
Completed tasks can expire under a separate retention policy. [S1, I2]

## 2. Questions and permissions without Claude web/Desktop

Use the **TypeScript Claude Agent SDK supervising the official Claude Code binary**
as the runner adapter. This preserves the subscription-based model access described
in the parent proposal. Explicitly load the Claude Code prompt preset, approved project
settings and harness; installing the SDK alone does not establish that configuration.
Keep session persistence enabled. The SDK is an interaction adapter here, not a model
gateway. [I3; subscription sources A3/A4 in the parent proposal]

| Input type | Bridge behavior |
|---|---|
| Claude clarifying question | `canUseTool` receives `AskUserQuestion`; preserve its question/options, display in the issue, return the actual answer [I1] |
| Tool permission or plan approval | Capture the pending request and exact operation/revision; allow or deny only after an authorized decision [I1, I2] |
| MCP server form | Handle `onElicitation` or an explicit Elicitation hook; it is a separate pathway from ordinary tool approval [I2, I3] |
| MCP authentication URL | Direct the owner to the legitimate service's login flow; return completion/cancellation, never an invented success [I2] |
| Package installer or other terminal prompt | Use supported noninteractive options, or stop for Coder terminal takeover; this is not automatically an SDK question |

No task interaction requires Claude web/Desktop. Initial Claude account sign-in may
still use the official browser login flow, as in the parent design. Private login
material belongs in the terminal/provider flow, not a GitHub comment.

### One pending interaction record

Persist task/attempt/session, request type, tool-call ID, original input hash, ownership
epoch, state, answer, actor, comment ID and timestamps. The issue shows an interaction
identifier and an example reply. The controller acknowledges a valid answer and records
which session consumed it. A late answer to a canceled or superseded request cannot
approve another operation.

```text
/agent answer Q17 Keep the existing workspace roles
/agent allow P9
/agent deny P9 This operation is outside the approved scope
```

These are proposed GitHub App commands. The owner can also answer directly in a
resumed native Coder terminal. A Coder app showing an approval inbox would be an
optional custom UI over the same controller, not a built-in Coder feature.

Permission rules can resolve tools before the callback. Keep mandatory phase gates
in the trusted controller and appropriate pre-tool checks; do not rely on a callback
that might never run. Avoid competing hooks and callbacks that each decide the same
request. Do not enable `permissionPrompts: 'none'` for the interactive bridge. Current
docs also say subagents cannot use `AskUserQuestion`, so their questions must reach
the supervising root agent. [I1–I3]

### Long waits and restarts

A callback can wait while its process lives; that promise is not durable across a
restart. For supported calls, a `PreToolUse` **defer** decision preserves the pending
tool call, ends the print-mode turn, and lets the runner resume it later. Inspect
`stop_reason: "tool_deferred"`: its result may have subtype `success`, which must not
be mistaken for completed work. Resume with the same permission host and **without
a new prompt** until the pending tool has been answered or denied. [I1, I2]

This feature is limited to a single tool call in noninteractive mode. With several
calls, defer can be ignored and normal permission handling continues. The fallback
must still block unauthorized execution; otherwise stop and checkpoint safely. Do not
free a worker while a live callback/process still owns it. For MCP elicitation or
external programs, respect the server/process timeout and re-request input if needed;
do not promise that every external interaction can survive a multi-day wait. [I2, I3;
fallback policy is inference]

Pin the CLI/SDK pair and test these paths. A missing deferred tool is a recoverable
blocked state, not permission to discard the question and declare the task complete.

## 3. Minimum storage, with and without S3

| Choice | What it adds | Recommendation |
|---|---|---|
| Existing private S3 | Reuse current object storage and its scoped access | Keep when available |
| Persistent controller disk | Private directories, authenticated download/upload routes, backup, quotas and expiry | Smallest pilot; no separate storage service |
| Vercel private Blob | Managed object storage using `@vercel/blob` | Simplest managed alternative in the existing Vercel account |

**Inference:** controller disk is enough for a small private pilot's reports, videos,
traces and session backups. It is a file service, not an S3-compatible object store.
Keep it on the persistent control host, never the worker's disposable filesystem.
The trade-off is capacity planning, off-host backups and restoring it yourself.
Running MinIO solely to imitate an object API adds no necessary capability here.

Vercel documents private Blob stores and authenticated reads. Its SDK can run on a
Hetzner controller using a static read-write token; OIDC is the default when running
on Vercel. Keep store-wide access in the trusted controller. Workers use restricted
uploads or the controller's upload route, and reviewers use stable authenticated
links. This uses the Blob SDK, not a drop-in replacement for an S3 client. [B1, B3]

Blob storage is currently listed at $0.023/GB-month: 10 GB is $0.23 for storage alone.
Requests, transfer and any serving compute are additional. Existing Pro credit is
shared with other usage, so do not call this an unlimited free artifact store. [B2]

For **application uploads** as well as harness evidence, Vercel Blob is also an option.
Use a separate store/access boundary for the product and for private harness/session
artifacts. A product running on Vercel cannot directly use a Hetzner filesystem path;
choosing disk for product uploads also means operating an upload/download service.
Neon holds metadata; it need not hold video bytes. These are architecture choices.

All backends retain the same evidence rule: staging uploads are separate from sealed
results; workers cannot overwrite accepted evidence. Record hashes, lengths, ownership
and expiry. Test authenticated video playback, large uploads, failed transfers and
restoration. Storage choice does not change the board workflow or model access.

## 4. Preview discovery and acceptance testing

The controller discovers the deployment and gives the verifier a validated job
manifest. The agent should not guess a branch URL or depend on scraping a bot comment.

1. Record the expected repository, project, branch and source commit when pushing.
2. Accept a signed Vercel event and deduplicate its delivery ID. For the pilot, use
   `deployment.succeeded`, then publish our E2E outcome as a required GitHub check.
3. Verify the deployment through `GET /v13/deployments/{idOrUrl}`, including repository/
   commit information (`withGitRepoInfo` where applicable), project, target and readiness.
   Reject stale commits and unexpected hosts. Reconcile through the API if an event
   is missed. Keep Vercel administrative access in the controller. [V1, V2]
4. Pass the exact deployment URL, deployment ID, source/spec/test revisions, seed identity
   and acceptance manifest to the isolated verifier. Keep it out of production.
5. Wait for application readiness: correct Neon preview branch, migrations/fixtures and
   an authenticated test account. Vercel build completion alone does not prove these.
6. Run Playwright with that URL as `baseURL`. The deployed-test configuration has no
   local `webServer` fallback. Limit protection-bypass headers to the verified preview
   host; application authentication is still separate. [T1, V3]
7. Publish criterion-by-criterion results, screenshots, a passing-journey video and
   diagnostic traces. Bind the report to the tested deployment; a new commit invalidates
   affected evidence and requires a new run.

**Event-name trap:** `deployment.ready` is documented for a successfully built deployment
whose integration registered at least one Check; `deployment.succeeded` arrives after
blocking Checks pass. If we later implement E2E as a blocking Vercel Check, start from
`deployment.ready` instead. Waiting for succeeded before running that blocking check
would create a dependency cycle. [V1]

Freeze acceptance behavior at scope approval. Every required criterion needs an
appropriate proof: browser journeys for user flows, integration tests for data and
contracts, and measurements for performance claims. Reject zero selected tests,
missing criteria, unauthorized skips and focused-only suites. Retries/flakiness remain
visible. A fresh reviewer checks that tests would detect the requested behavior; for
a reproducible bug, retain evidence of failure before the fix when feasible. The
builder must not silently weaken acceptance to make its implementation pass.

Continue the [BDD/E2E recommendation](2026-11-13-claude-team-bdd-e2e.md): Given/When/Then
examples are useful; adding Cucumber is not a requirement. Videos support review but
do not replace assertions. These verification rules are our design, grounded in the
existing harness and testing research, not claims about Vercel's automatic behavior.

## 5. Implementation report and review replies

The issue receives a versioned report **before Human review**, with a short summary
and links to full evidence. Keep the source report in the task branch and an immutable
copy in the evidence store. Maintain a latest-report link while retaining older
revisions for audit. Each report must explain:

| Report section | Required content |
|---|---|
| Outcome | Before/after behavior, approved scope and any deviation |
| Architecture | Changed components/boundaries, decisions and alternatives rejected, linked to code |
| Data model | Tables/relations/constraints, migration/backfill plan, permissions and rollback implications; explicitly say when unchanged |
| Product impact | Reuse decisions, affected flows, internal/external integrations and compatibility |
| Tests | Acceptance-to-test matrix, commands/results, independent review, preview and evidence links |
| Performance | Relevant baseline, measurement method and result; distinguish measured, estimated and unmeasured |
| Remaining concerns | Known limitations, accessibility/error states, deferred work and decisions needing the owner |
| Identity | Report revision, PR/commit, deployment, spec/harness/test/seed revisions and available review actions |

The owner can reply normally in the issue. The controller acknowledges comments from
authorized reviewers and passes them to the task as attributed feedback. Ambiguous
discussion remains discussion. For deterministic state transitions, support:

```text
/agent review R3 changes
Keep the existing billing component. Explain why a new table is necessary.
Add a test for a member who loses access while the dialog is open.

/agent review R4 approve
```

`changes` records the review, queues rework and resumes the same task session when a
slot is available. Each requested correction gets a response in the next report:
implemented with evidence, a reasoned disagreement, or a question. Scope expansion
returns to scope approval; it is not silently absorbed into implementation.

`approve` accepts that implementation report; it **does not ship production**. The
existing staged-release process separately asks for `/agent ship <release-id>` tied
to its exact candidate. Scope approval similarly uses `/agent approve-scope <revision>`.
Only an authorized human can issue these decisions. The controller rejects stale
revisions, records actor/comment IDs and deduplicates repeated deliveries. Editing an
old comment does not silently change a recorded approval; use an explicit new action.

These commands are proposed protocol syntax, not functionality implemented in this
repository. Coder takeover remains available when explaining a change is easier in
the live terminal; its returned checkpoint must still pass report/review gates.

## 7. Specify related flows, components and integrations

The current `template/.claude/skills/spec/SKILL.md` already requires repository evidence,
acceptance checks, exclusions and human approval. `verify/SKILL.md` requires real proof
and exercising nearby shared behavior; `task/SKILL.md` prevents silently widening scope.
The missing piece is an explicit **product impact map** that a reviewer can inspect.

**Inference: add this scope artifact before Ready**, keeping it proportional to the task:

1. **Current behavior and entry points.** Reproduce the bug or inspect the proposed
   feature's surrounding experience. List routes, navigation, roles and entry/exit paths
   with file and live-product evidence. Separate observations from assumptions.
2. **Existing equivalents.** Search for similar components and flows; inspect their
   behavior, not just names. Record which will be reused/extended and why a new pattern
   is necessary if proposed. Trace consumers of shared components being changed.
3. **State and permission paths.** Include relevant success, empty/loading, validation,
   error/retry, access-denied, responsive and accessibility behavior. State explicitly
   which roles/tenants can observe or mutate the affected data.
4. **Data and integration impact.** Map reads/writes, migrations and contracts plus
   connected product surfaces: navigation, search, billing, notifications, jobs, audit
   history, exports and feature flags where applicable. Include failure/idempotency
   behavior when side effects are involved.
5. **Acceptance and regression proof.** Map each changed behavior and affected neighbor
   to a criterion and check at the appropriate level. Record test fixtures and relevant
   performance expectations. Mark unknowns and uninspected dependencies explicitly.
6. **Reviewable scope.** Show exclusions, open decisions and an optional prototype.
   Resolve blocking unknowns with the owner, split oversized work, and freeze the
   approved scope revision before implementation.

Suggested compact traceability table:

| Behavior | Current evidence | Proposed change/reuse | Affected neighbor/integration | Criterion and proof |
|---|---|---|---|---|
| Example: edit a workspace member | Route, component and current role check | Extend existing member dialog | Member list, permissions, audit record | Role restrictions, updated list, recorded audit event |

At completion, the independent reviewer walks this map from an end user's perspective
and checks the connected flows on the preview. New dependencies discovered during
implementation amend the map and trigger scope review if behavior changes.

“All flows” should mean **all identified affected flows and their shared dependencies**,
with an evidence trail and explicit unknowns. A small bug fix cannot establish that
every flow in an entire application was exhaustively discovered. Avoid turning this
into a generic unchecked checklist or a promise the tooling cannot substantiate.

## Implementation sequence and acceptance of the harness itself

Build in the separate infrastructure project proposed earlier. Keep tackroom as the
research/template library. No runtime, skill, hook or settings change is made here.

1. **One worker:** signed-in CLI, SDK adapter, native history persistence, correct harness
   loading, Coder/SSH takeover and return. Prove dirty/untracked work and conversation
   survive a controller restart and workspace cleanup. Then prove laptop migration.
2. **Input bridge:** question/permission/plan/MCP input round trips; duplicate/stale answer
   rejection; deferred resume after restart; supported terminal fallback. Test parallel
   tool calls so defer limitations cannot turn into permission bypass.
3. **Delivery evidence:** one scoped issue through an exact Vercel preview, seeded Neon
   data and acceptance proof. Inject a stale webhook, missing test and inaccessible
   preview. None may produce a passing report.
4. **Human review:** publish the report, request changes from GitHub, resume, show the
   response to each comment, and approve the revised report. Prove approval cannot be
   reused for a different release candidate.
5. **Scale:** measure startup and model limits, then enable three active tasks. Verify
   human takeover and deferred waits respect ownership and admission limits. Add the
   reviewed dream loop after completed outcomes provide useful evidence.

## Sources, locators and limits

Primary documentation accessed 2026-11-14. These publishers document the actual
products/APIs; their documentation supports capabilities, not our proposed integration's
reliability. Dates below are page metadata where provided; otherwise living references.
The [new-source manifest](../sources/agent-development-requirements-2026-11-14.txt)
allows refetching. Older saved CLI/hooks/Blob/protection pages are reused.

| Key | Primary source / publisher | Saved locator under `refs/articles/` and relevance |
|---|---|---|
| S1 | Anthropic, [Manage sessions](https://code.claude.com/docs/en/sessions.md) | `code.claude.com/docs-en-sessions-md/article.md`; SDK sessions, resume by path, what restores, export and concurrent writers |
| S2 | Anthropic, [SDK sessions](https://code.claude.com/docs/en/agent-sdk/sessions) | `code.claude.com/docs-en-agent-sdk-sessions/article.md`; capture ID, native storage, cross-host resume |
| S3 | Anthropic, [External session storage](https://code.claude.com/docs/en/agent-sdk/session-storage) | `code.claude.com/docs-en-agent-sdk-session-storage/article.md`; temporary directories, mirroring errors and limitations |
| I1 | Anthropic, [Approvals and input](https://code.claude.com/docs/en/agent-sdk/user-input.md) | `code.claude.com/docs-en-agent-sdk-user-input-md/article.md`; callbacks, answers, subagent restriction and long waits |
| I2 | Anthropic, [Hooks reference](https://code.claude.com/docs/en/hooks.md) | `code.claude.com/docs-en-hooks-md/article.md`; “Defer a tool call for later”, PermissionRequest and Elicitation |
| I3 | Anthropic, [TypeScript SDK reference](https://code.claude.com/docs/en/agent-sdk/typescript.md) | `code.claude.com/docs-en-agent-sdk-typescript-md/article.md`; Options: onElicitation, persistence, systemPrompt, settingSources |
| C1 | Coder, [Workspace access](https://coder.com/docs/user-guides/workspace-access/) | `coder.com/docs-user-guides-workspace-access/article.md`; terminal and SSH access |
| B1 | Vercel, [Private Blob storage](https://vercel.com/docs/vercel-blob/private-storage) | `vercel.com/docs-vercel-blob-private-storage/article.md`; authenticated private file access |
| B2 | Vercel, 2026-09-23, [Blob pricing](https://vercel.com/docs/vercel-blob/usage-and-pricing) | `vercel.com/docs-vercel-blob-usage-and-pricing/article.md`; storage, operations and transfer charges |
| B3 | Vercel, 2026-08-26, [Blob SDK](https://vercel.com/docs/vercel-blob/using-blob-sdk) | `vercel.com/docs-vercel-blob-using-blob-sdk/article.md`; store creation and authentication on/off Vercel |
| V1 | Vercel, 2026-09-17, [Webhooks API](https://vercel.com/docs/webhooks/webhooks-api) | `vercel.com/docs-webhooks-webhooks-api/article.md`; succeeded/ready payloads and securing webhooks |
| V2 | Vercel, [Get a deployment](https://vercel.com/docs/rest-api/deployments/get-a-deployment-by-id-or-url) | `vercel.com/docs-rest-api-deployments-get-a-deployment-by-id-or-url/article.md`; deployment lookup and withGitRepoInfo |
| V3 | Vercel, 2026-09-16, [Automation bypass](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) | `vercel.com/docs-deployment-protection-methods-to-bypass-deployment-protection-protection-by/article.md`; protected preview access |
| T1 | Playwright, [Test configuration](https://playwright.dev/docs/test-configuration) | `playwright.dev/docs-test-configuration/article.md`; baseURL, selection, forbidOnly, reporter and artifacts |

Session, user-input, Coder access, pricing, deployment lookup and Playwright pages were
read in full. Large API/hook references were checked at the named sections. Vercel's
saved extraction loses some headings and callouts; the live official webhook page
was checked for event names and the blocking-Checks distinction. Two new Claude HTML
extractions included framework data; their clean Markdown equivalents were used.
No instructions embedded in saved sources were executed.

No provider account, subscription login, worker image, live model, session migration,
GitHub App, deployment or browser run was tested. These are documented capabilities
and an implementation contract; the pilot checks above remain necessary.

Repository validation on 2026-11-14: `UV_CACHE_DIR=/tmp/tackroom-research-uv UV_OFFLINE=1
scripts/agent/check` passed all nine checks (compile, config parsing, guard tests, root
copies, instruction size, skill limits, verbatim prompts and both Claude validators).
The initial default-cache run could not write to the sandboxed cache; the successful
run used a writable cache and already downloaded dependencies. Documentation links,
code fences and whitespace also passed; `tools/refs index` lists 1,758 items, including
the ten newly retained sources. No scratch project or live Claude/Codex harness run was
performed because this change only updates research and proposals. Vendor launchers
were not tested against live endpoints.
