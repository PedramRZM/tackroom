---
id: 0
title: Short imperative title
type: task          # task | epic
status: inbox       # inbox | ready | in-progress | needs-human | in-review | done
priority: p2        # p0 (first) to p3
epic:               # id of the parent epic, if any
blocked-by: []      # ids of tasks that must be done first
interactive: false  # true = ready, but do it with the user present
created: 2026-01-01
---

## Goal

One or two sentences: what a user or the system can do after this, and why it matters.

## Context

Files, routes, tables, earlier tasks or decision records to read first. Enough that a fresh
session needs nothing else.

## Acceptance criteria

AC1. <behaviour>. Check: <command, test name, or UI step and the expected result>
AC2. ...

## Edge cases and data changes

## Verification plan

Before implementation: criterion/example and expected result → risk → check level/tool →
fixtures/environment → exact command or UI steps → evidence. Reuse existing checks; note any
missing quality gate and why it helps. A sentence suffices for a small change. Do not rewrite
the acceptance criteria to match the implementation.

## Constraints

## Out of scope / do not change

## Notes

Handoff notes and questions for the user go here, newest first, each with a date.
