# Keep, change, remove

Keep the current shared verification guidance provisionally; keep the omission reminder as
a small human-review proposal, and do not add another feedback store. A small synthetic ceiling result cannot prove the current package
beats the old one, or justify deleting safeguards for risks it never exercised. The next
useful evidence is harder real work and measured correction recurrence, not more repetitions
of these now-exposed cases. No production skill or configuration changes in this task.

This inventory covers the changed prescriptions in write-tests/verify and their reference
relative to `b8ce42c`. Existing unchanged safeguards retain their original research rationale
in [testing.md](../../testing.md); this pilot is not a revalidation of the entire library.

| Prescription retained | Evidence or explicit untested-risk rationale | Recommendation |
|---|---|---|
| Plan from criteria, expected examples and failure/boundary/permission risks before code; identify unknown setup | Current coding runs produce a durable criterion-to-check plan; both versions repair the simple cases. Durable traceability is observed, incremental defect benefit is not. | Keep, limit to substantive work |
| Reuse checks, choose the smallest sufficient level/tool, state setup/cost/blind spots; no fixed test ratio | Both versions use stdlib unit tests and real SQLite, with no dependencies. General architecture and tool-selection benefits remain untested. | Keep conditional choices; no tool catalog installation |
| Separate BDD discovery, TDD sequence and test scope; no mandatory Gherkin/browser matrix | Red outputs precede fixes. This fixture cannot measure stakeholder discovery or BDD misunderstanding; keep for that explicit untested risk. | Keep, no new runner |
| Focused red/green or isolated fault; preserve others' edits | Red failures observed for each bug category; mutation controls reject faults. Preservation of concurrent edits is untested but destructive-loss risk justifies retention. | Keep |
| Deterministic inner loop, isolated real services when that is the boundary | SQLite fixtures pass; no external network. Clock/randomness, service reset and distributed integration remain untested. | Keep; no live-service claim |
| Validate semantic token names and raw/malformed values; inspect each actual CSS/JS/utility surface; allow/deny fixtures and exceptions | Narrow value validator repairs observed. Actual CSS/AST/utility enforcement, dynamic classes, namespaces and exceptions are planning-only or untested; false confidence from grep remains the risk. | Keep reference, not blanket installation |
| Distinguish interaction, visual baseline, accessibility, usability and performance evidence; ui-craft stress recipes | Reducer failure checks and honest UI limits observed. Browser, touch/motion, viewport/theme, assistive technology, human research and lab/field performance gains remain untested. | Keep conditional references, no claim that state tests prove UX |
| Report revision/environment/role; keep gaps, skips/retries, changed gates and final-tree evidence visible | Current runs disclose absent HEAD and UI gaps. No flaky/quarantined suite or changing baseline was exercised; retain to avoid hiding those failures. | Keep; fix fixture provenance before a future evaluation |
| Affordable inner/full loop; expensive checks only when justified; align CI gates, reviewed baselines, explicit Lighthouse budgets | No test added for trivial copy. CI, visual baselines, performance variance and tamper resistance are untested risks; this scratch scorer is independent of submitted files, not a security boundary. | Keep conditional advice |
| Retain existing dream inbox/report, source and disposition; proposals need evidence and human acceptance | Existing report already captures owner's no-sync correction and declines redundant guidance. Current human/agent traces need no new schema. Later prevention and review time savings remain unmeasured. | Keep existing flow; remove proposal for additional capture machinery |
| Five-line final omission reminder | Independent plan review finds three omitted requirements repaired and no loss of clean-case coverage; invoice representative-user limit is still missing. One trial pair on Codex cannot establish an OpenCode fix or recurrence reduction. | Present the retained diff for human acceptance; leave template unchanged pending that decision |

The delivered package grows from 125 lines/6,845 bytes to 615 lines/43,475 bytes, largely in
references and the ui-craft package. These are available bytes, not necessarily all loaded
tokens: actual tool reads and cumulative input/cache usage are retained separately. Always-read
write-tests/verify files and optional references must not be conflated when judging overhead.
There is no estimate of dollar billing or human minutes saved. The [feedback trace](feedback.md)
records one owner-correction episode and one failure recurring in two same-scenario OpenCode
outputs; these are not statistically meaningful recurrence rates.

The package, five-case sample, negative controls and adoption threshold are local judgments.
Research motivation is documented in [the feedback synthesis](../../../refs/notes/2026-11-15-feedback-learning-loop.md).
Future deletion or adoption needs new cases; reusing these answers would be development work,
not a fresh holdout. Claude/OpenCode effectiveness must be measured within those harnesses
when available, not inferred from Codex results.
