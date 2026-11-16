# Epic 7 implementation

Owner requested starting and finishing all of epic 7 on 2026-11-16, after authorizing commit
and publication to main. This supersedes the inbox and one-task-per-session scheduling rules
for tasks 8–10. Acceptance criteria remain unchanged. Base: `43b7f19`.

## Decisions

Extend the Python 3.10 stdlib installer, with no package registry or dependency. The owner's
later correction requires a strictly agent-neutral template: no native output directories.
Each skill folder holds its text/resources and install.json metadata; the CLI discovers skills
and profiles automatically. Briefs have one markdown body plus sibling JSON metadata. Native
configuration definitions live in template/.agents/adapters.json. Native output is built in
memory and written only to destination projects. GitHub tree metadata replaces a checked-in
file manifest. Root native dogfooding outputs are generated and gitignored.
The installer selects with --agents, --skills, --profile, --tracker; --update remembers choices
and compares original source fingerprints, preserving local changes and all project knowledge.
The bootstrap resolves a GitHub ref once and invokes that commit's installer.

## Verification before implementation

| Criteria | Examples and expected result | Check / environment |
|---|---|---|
| 8 AC1–3 | Edit canonical brief → all adapters change; stale output, missing resource, unknown/cyclic dependency rejected | renderer check + Python unittest scratch sources |
| 8 AC4–5 | Dogfooding parity, local legacy install, preserved sources/docs | migrated existing parity checks + full `scripts/agent/check` |
| 9 AC1–2 | Current/explicit directory; each agent alone/all; base excludes UI, ui adds references | CLI subprocess tests against temporary projects |
| 9 AC3–4 | Exact rerun unchanged, custom files kept/reported, links cannot escape, dry run no writes | byte/mode/link snapshots in unittest fixtures |
| 9 AC5–6 | Native config parse, discovery, legacy path and documented examples | static setup matrix + bounded live Codex read + bounded Claude attempt |
| 10 AC1–3 | No checkout, commit pinned, local/remote files identical, changing ref resolved once | local HTTP server and actual GitHub scratch installs after publication |
| 10 AC4–5 | HTTP/missing/truncated/hash/catalog/path errors → nonzero and unchanged destination | local HTTP fault fixtures, snapshots |
| 10 AC6 | Final documented command installs published main; full checks pass | recorded commands/output under `docs/evidence/7-selective-harness/` |

New tests use stdlib unittest (no new dependency). Existing setup tests legitimately change
their path/default expectations because this epic reverses the canonical skill location and
makes selection explicit; their preservation, resource, tracker and dry-run checks remain.
Model trials establish reading/discovery only, not full permission or hook effectiveness.
Existing source attribution is retained; packaging choices are judgement calls.

## Progress

- Baseline: all 11 checks passed. Read all tasks, workflow, verification skills and parity tests.
- Interface/layout chosen above within the owner's instruction to complete the epic.
- Owner follow-up explicitly adds easy updates/sync with project memory/dream data preserved.
  Task 11 extends the original scope. Keep per-project source fingerprints and selections;
  `--update` replaces only unchanged managed files, never memory/reports/notes, and reports
  customized conflicts. Add old/new fixture tests, no-state adoption and published update proof.

## Dead ends

Initial checked-in generated adapters were rejected by the owner as still duplicated.
Replaced them with install-time generation and automatic source discovery.

## Final verification progress

- All 24 installer tests pass; full repository checks pass.
- Fresh-context final review found no Important issues and independently exercised malformed remote trees.
- Initial live Codex read succeeded; Claude account verification blocked a model response.
- Native template directories removed; generated root runtime files removed from version control, retained on disk.
- Remaining: publish source, exercise GitHub bootstrap/update and final Codex scratch read, record completion.
