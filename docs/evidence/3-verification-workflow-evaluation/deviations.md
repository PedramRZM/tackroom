# Deviations and review findings

After coding-old-1 completed, independent review found the frozen same-connection SQLite
assertion did not establish commit durability. Frozen scorer and rubric remain unchanged.
`persistence.py` supplements every final artifact with a separate file-database connection
for approver success and viewer denial. This is a post-freeze check, not held-out evidence
frozen before either configuration ran. It was designed from the review finding before the
current-guidance output was inspected, not tuned to improve its score. Removing commit from
the known-good control must fail the supplement while the complete control passes.

The implementation mutation control establishes only that storage assertions can reject
an implementation bug. It does not establish rejection of a bad guidance proposal. A separate
deliberately regressing prose candidate was therefore run and assessed with the frozen
planning rubric. This extra negative-control run is outside the original six-run budget;
it uses the same model and 180-second ceiling, synthetic data only. It is not a new holdout.

The runner writes metadata after local scoring and has no scoring-import timeout. Every
recorded run must be checked for complete metadata. Do not infer missing runs succeeded.
Future reuse with arbitrary submitted code needs an isolated, time-limited scoring process;
this pilot's bounded synthetic final modules are inspected before re-scoring.

The reminder and negative-policy planning calls overlapped in wall time; the four coding
comparisons were sequential and alternating. Planning latency is descriptive only, with no
causal performance claim. No additional tuning, retries or discarded model calls occurred.

Commit-time whitespace inspection flags blank context lines in retained `.diff` files and
one trailing space in the verbatim coding-new-1 red-test log. These evidence bytes are
preserved intentionally; source and report files have no staged whitespace errors. Full
repository checks and offline re-scoring passed again before merge (see merge-checks.txt).
