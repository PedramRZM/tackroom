# Planning exercise

This directory is a harness scratch project, not a running application. The following is a
proposed change to a React/TypeScript invoice application. Do not claim any app check ran.

Existing project tools: TypeScript typecheck, ESLint, Vitest + Testing Library, Playwright Test.
CSS stylesheets, React inline style objects and utility classes are all used. Semantic color
tokens are defined in tokens.css. There is no token-enforcement rule or accessibility scanner.
Existing commands: pnpm typecheck, pnpm lint, pnpm test, pnpm test:e2e. App data setup is not
yet documented. No Storybook or Cucumber installation exists.

Request A: viewers can download invoices but must never approve them, even by directly
calling the API. Approvers can approve pending invoices; a failed approval should leave the
invoice unchanged. Both themes must use the semantic tokens. Design verification before
implementation, including recommendations for missing checks and the evidence for review.

Request B, independently: change the heading from 'Invoices list' to 'Invoices', with no
behavior or layout change. Describe the proportionate verification and whether tests or
tools should be added.

Use the actual shipped write-tests and verify skills in this directory. Read their supporting
reference as needed. Return both plans with concrete expected results and explicitly unknown
setup. Do not implement, install dependencies or modify files.
