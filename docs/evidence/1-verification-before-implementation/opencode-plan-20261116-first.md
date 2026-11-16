Following the guidance in `write-tests.md` and `verify.md`, here are the plans for Request A and Request B.

### Request A: Permissions and Semantic Tokens

This plan focuses on enforcing Request A's requirements through a mix of static analysis, unit/integration tests, and E2E journeys.

#### Verification Plan

| Acceptance Criterion | Example and expected result → Risk | Smallest sufficient check and tool | Data / Environment | Command or UI steps | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AC1: Viewer download** | Authenticated 'viewer' clicks download → PDF file received. **Risk:** Permission logic over-restricts. | Playwright E2E journey. | Seeded 'viewer' user, invoice `inv-123`. | `pnpm test:e2e` (targeting download spec). | Playwright `download` event and file content verification. |
| **AC2: Viewer cannot approve (UI)** | 'Viewer' opens invoice → 'Approve' button is absent. **Risk:** Privileged action exposure. | Integration test (Vitest + Testing Library). | Rendered `InvoiceDetail` with `role: 'viewer'`. | `pnpm test` (targeting component file). | `queryByRole('button', { name: /approve/i })` is `null`. |
| **AC3: Viewer cannot approve (API)** | POST `/approve` with viewer token → 403 Forbidden. **Risk:** UI-only security bypass. | API Integration test. | API server running, viewer JWT. | `pnpm test` (API permission suite). | HTTP 403 response status. |
| **AC4: Approver succeeds** | POST `/approve` with approver token → 200 OK, status 'Approved'. **Risk:** Logic error in transition. | API Integration test. | Seeded 'approver', pending invoice. | `pnpm test` (Invoice service suite). | Response body `status: 'Approved'`. |
| **AC5: Failure leaves state** | Database error during approval → status remains 'Pending'. **Risk:** Inconsistent/partial state. | Unit test with mocked failure. | Service layer with injected DB error. | `pnpm test` (Service unit test). | `getInvoice` after failure returns 'Pending'. |
| **AC6: Semantic tokens** | All colors use `var(--color-...)`. **Risk:** Hardcoded colors causing theme bugs. | Static analysis (Grep/Lint) + Manual inspection. | Source code; running app in Light/Dark themes. | `grep -r "color: #" src` and visual walkthrough. | Zero hex matches; screenshots of both themes with clean console. |

#### Recommendations for missing checks
1.  **Token Enforcement:** Install and configure `stylelint-declaration-strict-value` to enforce the use of semantic tokens from `tokens.css` and forbid hardcoded hex/rgb values.
2.  **Accessibility:** Integrate `@axe-core/playwright` into the E2E suite to scan the rendered 'Approver' and 'Viewer' states for common defects (contrast, labels).
3.  **Data Documentation:** Create a `pnpm db:seed` script or equivalent documentation to ensure reproducible environments for these permission checks.

#### Explicitly unknown setup
- **Auth Implementation:** Whether the app uses JWTs, cookies, or another mechanism for role enforcement.
- **Seeding:** The specific command to create 'viewer' and 'approver' accounts in the local environment.
- **API Endpoints:** The exact structure (e.g., `POST /invoices/:id/approve`) is assumed and would need verification.

---

### Request B: Heading Change

**Proportionate Verification Description:**
For a text-only change from 'Invoices list' to 'Invoices' with no layout or behavior risk, the verification should be lightweight:
1.  **Static:** A TypeScript check to ensure no component prop mismatches if the heading is a prop.
2.  **Unit/Integration:** Search the codebase for existing tests that assert on the string 'Invoices list' (e.g., `getByText(/invoices list/i)`). Update these tests to expect 'Invoices' and run `pnpm test` to confirm they pass.
3.  **Manual UI Inspection:** Run the app and visually confirm the text is correct in both themes. Use the browser's inspection tool to ensure no Layout Shift (CLS) occurred due to the shorter text.

**Tests/Tools to be added:**
- **No new tools** are required for this change. Installing a visual regression suite or i18n framework for a single heading change would be disproportionate.
- **Recommendation:** If the project anticipates frequent content updates, consider moving UI strings into a central `constants.ts` or i18n file to make tests less brittle and easier to update.

**Evidence:**
- `pnpm test` summary showing updated test files passing.
- Screenshot of the header area at 1440px and 412px viewports.
