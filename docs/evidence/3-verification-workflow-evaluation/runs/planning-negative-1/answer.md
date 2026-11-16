Read `task.md`, both named skills, their tool reference, and the applicable `ui-craft` guidance. No files were changed, dependencies installed, or app checks run. These are proposed verification plans.

**A — Invoice permissions, approval, and themes**

Design these checks before implementation, using task-derived expectations:

| Example and expected result | Risk and smallest sufficient check | Setup, execution, and review evidence |
|---|---|---|
| Viewer directly calls approval API → denied; invoice remains unchanged | Server authorization bypass: API integration test against an isolated real database | Authenticate as viewer, submit approval, compare persisted invoice before/after through an independent read. Retain response and assertions. Exact denial status is unspecified. |
| Approver approves pending invoice → approved and persisted | Incorrect transition or missing commit: API/database integration | Seed pending invoice; approve; read through a fresh database session. Retain response and persisted-state assertions. |
| Approval encounters a controlled persistence failure → no partial changes | Broken atomicity: integration test with failure injected at the storage boundary | Record invoice and associated approval records before/after. Expect unchanged committed state and an observable failure. Failure injection/reset procedure is unknown. |
| Viewer downloads invoice successfully and has no approval action | Incorrect UI permissions or broken download wiring: one Playwright journey | Sign in as viewer; open invoice; download and validate expected file contents. Assert approval action absent; retain trace/download assertions. |
| Approver completes approval; failed approval leaves displayed state unchanged and permits recovery | UI/server mismatch: Testing Library failure cases plus a critical browser success journey | Delay/reject requests at the network boundary for component checks. Assert pending/error/success state, usable recovery, and no false success. |
| Both themes use declared semantic tokens and remain legible | Styling policy and rendering defects: static enforcement plus rendered inspection | Apply the token checks below; inspect representative normal, pending, disabled, and error states in both themes at supported phone/desktop widths. Retain screenshots and contrast findings. |

Recommend narrowly scoped token enforcement: CSS value/custom-property rules for stylesheets, ESLint AST checks for inline styles, and a compatible utility-class rule for the actual framework. An allowlist must come from `tokens.css`. Prove valid tokens pass and raw hex, named/function colors, undeclared variables, and forbidden arbitrary utilities fail. Cover token-definition exceptions explicitly; report dynamic expressions the rules cannot analyze. Grep is only an inventory aid.

Recommend a small axe integration with Playwright for common accessibility defects, supplemented by keyboard operation, focus, zoom, and error-announcement checks. Static rules require fixtures and maintenance; automated accessibility scans have runtime cost and incomplete coverage. Screenshots establish appearance, not authorization, usability, or accessibility.

Use existing Vitest/Testing Library and Playwright; no Storybook or Cucumber addition is needed. Confirm focused behavior tests fail for the intended missing behavior before implementation, then pass afterward. For review, retain criterion-linked results, database assertions, browser traces, theme screenshots, and reviewed rule fixtures.

**B — Heading-only copy change**

Change “Invoices list” to “Invoices,” preserving its heading element, accessible structure, styling, and surrounding layout.

Proportionate verification is a diff inspection and direct rendered inspection at existing representative widths. Expect the new text, unchanged heading level and surrounding geometry, and no clipping. The shorter text’s own width may naturally shrink.

Use existing relevant checks and update an existing exact-text assertion only where the requirement legitimately changes. Do not add a snapshot suite, browser matrix, accessibility dependency, or new test framework for this edit. If an existing screenshot baseline changes, review that only the intended text changed. Record the inspected view and actual check results when execution becomes possible.

**C — SQLite CLI archive**

| Example and expected result | Risk and smallest sufficient check | Setup, execution, and review evidence |
|---|---|---|
| Admin archives pending item → success persists | CLI wiring or missing commit: subprocess integration against real temporary SQLite | Seed pending item; invoke actual CLI; reopen database in a fresh connection/process and assert archived state. Retain stdout, stderr, exit status, and persisted read. |
| Reader or unknown role directly invokes archive entry point → denied; storage unchanged | Permission bypass: public archive-boundary integration tests | Test both roles separately, bypassing any UI/command visibility restriction. Compare relevant stored rows before/after. Role transport and denial contract are unknown. |
| Write fails after work begins → failure; storage unchanged | Partial transaction: SQLite integration with controlled mid-operation failure | Use isolated database and deterministic failure injection. Reopen database and verify all affected records retain their original values. |
| Non-pending item receives archive request | Invalid transition: focused rule/integration example | Expected rejection or other behavior needs clarification before its assertion is fixed. |

Keep SQLite real; replace the unavailable notification service only at its external boundary. A fake can prove the application constructs the intended request and handles specified responses. It cannot prove real delivery, credentials, network compatibility, or the provider contract.

The relationship between notification failure and archive success is unspecified. Resolve whether notification failure rolls back, is retried, or is recorded separately before defining that expectation. Record a separate provider-sandbox/live check as outstanding; local green results do not close that gap.

CLI executable, test runner, schema/migration commands, role setup, fixtures, and reset commands are unknown. Do not invent runnable commands. Prefer the project’s existing runner after discovery; no browser tools are needed.

**D — Optimistic profile editor**

| Example and expected result | Risk and smallest sufficient check | Setup, execution, and review evidence |
|---|---|---|
| Save draft successfully → committed profile persists after reload | UI success without persistence: integration plus one browser journey | Seed known committed profile, edit, save, reload, and read committed data. Retain assertions and trace. |
| Save fails → committed data unchanged; draft retained; retry available | Lost edits or false commit: Testing Library network-boundary test plus persistence integration | Start with committed value A, edit to B, reject save. Expect server data A, editable draft B, clear failure, and usable retry. Retrying successfully commits B. |
| Responses are delayed or reordered; user edits during pending save | Stale rollback overwrites newer state: deterministic component tests | Control response order without sleeps. Assert an older failure cannot overwrite a newer successful commit or erase subsequent draft edits. Specify whether concurrent submissions are blocked or versioned. |
| Keyboard user edits, saves, encounters error, and retries | Inaccessible recovery: browser interaction and targeted accessibility checks | Tab through controls; operate save/retry; verify labels, visible focus, logical focus placement, and an appropriate live error announcement. Supplement with targeted screen-reader checking. |
| Stylesheet and inline colors use declared semantic tokens | Incomplete enforcement: CSS rules plus ESLint AST checks | Test allowed tokens and prohibited raw/named/function colors and undeclared variables in both syntaxes. Document unanalyzable dynamic styles and approved exceptions. |
| Pending/error/success states remain readable in supported themes and widths | Visual/state defects: rendered inspection | Capture stable fixtures at phone/desktop widths; check contrast, zoom, overflow, and delayed/failed-save states. Retain screenshots and interaction evidence. |

Recommend the same narrowly scoped CSS/inline token enforcement and targeted axe integration as A, with rule fixtures and explicit analysis limits. Screenshots cannot prove draft retention, persistence, announcements, or usability. Representative-user usability and untested assistive-technology paths remain unverified.

**Execution and evidence limits**

For A, B, and D, known commands are `pnpm typecheck`, `pnpm lint`, `pnpm test`, and `pnpm test:e2e`. Exact focused selectors, application startup, authentication, fixtures, database isolation, and reset commands are unknown. The skill’s `scripts/agent/check` command is not established by this scratch project; do not claim it exists.

Before implementation, document those setup procedures and inspect existing conventions. For substantive changes, establish meaningful failing tests, then implement and rerun affected checks plus the applicable project gates. Review must identify the tested revision, environment, roles/data, actual output, criterion-linked evidence, and all failures, skips, retries, and external gaps. None of that execution evidence exists yet.