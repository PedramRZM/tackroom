Based on the guidance in `write-tests` and `verify` skills, here are the plans for the two requests in `scenario.md`.

### Request A: Invoice Permissions and Semantic Tokens

#### Verification Plan
| Criterion | Example & Expected Result → Risk | Check & Tool | Data/Env | Command/Steps | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AC1: Download** | Viewer clicks "Download" → PDF received. **Risk:** Permission logic blocks valid action. | Integration (Vitest) | Viewer user, Invoice data | Render `InvoiceDetail` as Viewer; click Download. | `expect(downloadHandler).toHaveBeenCalled()` |
| **AC2: UI Safety** | Viewer views invoice → No "Approve" button. **Risk:** Role leak in UI components. | Integration (Vitest) | Viewer user, Pending invoice | Render `InvoiceDetail` as Viewer. | `expect(screen.queryByRole('button', { name: /approve/i })).toBeNull()` |
| **AC3: API Security** | Viewer calls `/api/approve` → `403 Forbidden`. **Risk:** UI-only protection bypassed by direct call. | API Unit/Integration | Viewer session token | POST to `/approve` endpoint with Viewer ID. | `expect(response.status).toBe(403)` |
| **AC4: Approval** | Approver clicks "Approve" → Status becomes `Approved`. **Risk:** Happy path logic error. | E2E (Playwright) | Approver user, Pending invoice | Login; open Invoice; click Approve. | Status text change to "Approved"; API log shows 200. |
| **AC5: Robustness** | Approver clicks "Approve", API fails → Status stays `Pending`. **Risk:** UI/Data desync or corruption. | Integration (Vitest + MSW) | Approver, Pending invoice, Mock 500 error | Trigger approval; intercept with network error. | `expect(statusText).toBe('Pending')`; Error toast visible. |
| **AC6: Tokens** | Toggle themes → Header color shifts via `--color-text-main`. **Risk:** Hardcoded hex/rgb values used instead of tokens. | Static (Grep) + Visual Inspection | Any user | Toggle Light/Dark; inspect CSS vars in Browser DevTools. | `grep` confirm no hex codes in changed lines; screenshots of both themes. |

#### Recommendations for Missing Checks
*   **Token Enforcement:** Add `stylelint-declaration-strict-value` to `ESLint` or `Stylelint` to forbid hex/literal colors, ensuring `tokens.css` is the exclusive source.
*   **Accessibility:** Use `@axe-core/playwright` to ensure the disabled/absent states for viewers don't break focus order or screen reader expectations.
*   **Storage Boundary:** Add a Vitest assertion specifically at the database/repository level to prove `status` remains unchanged on failed API calls.

#### Unknown Setup
*   **Data Seeding:** No documented way to create specific "Viewer" vs "Approver" users or "Pending" invoices.
*   **API Boundary:** Exact method of direct API invocation (REST vs GraphQL) is unknown.
*   **Token Mapping:** The specific mapping of semantic tokens (e.g., `surface-primary`) to theme classes is not yet identified.

---

### Request B: Heading Change ('Invoices list' → 'Invoices')

#### Proportionate Verification
Since this is a **copy-only change** with no behavior or layout risk:
1.  **Static/Unit:** Update existing test assertions (Vitest/Playwright) that specifically look for the string "Invoices list" to expect "Invoices".
2.  **Visual Inspection:** Manually verify the change in the running app at 1440px and 412px to ensure the shorter string doesn't cause unexpected alignment shifts (though the risk is negligible).
3.  **Checks:** Run `pnpm lint` and `pnpm test` to ensure no regression in tests that rely on this heading for navigation or identification.

#### New Tests/Tools
*   **No new tools or tests should be added.** Adding a test specifically for this heading string if one doesn't exist would be "chasing coverage" and provide low maintenance value.
*   **Refinement:** If tests currently use the text for selection (e.g., `getByText('Invoices list')`), they should be updated to use a more stable selector like `getByRole('heading', { name: /invoices/i })` to accommodate future minor copy tweaks.

#### Unknown Setup
*   **Localization:** Unknown if the string is hardcoded in a component or pulled from a translation key/CMS, which would change the edit location.
