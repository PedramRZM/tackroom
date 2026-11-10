---
title: "currently hammering on my thing with this:"
author: "Ryan Lopopolo (@_lopopolo)"
date: "2026-08-09"
url: "https://x.com/_lopopolo/status/2086269569841377295"
site: "x.com"
type: "post"
via: "fxtwitter"
---
currently hammering on my thing with this:

do a sweep for tests that do nothing than re-assert the source, are low value, duplicative, etc. remove them and then see whether the prod code can be simplified now that the tests no longer demand seams to exist

tests must justify their presence. tests that require changes whenever the underlying source changes are not good tests since they assert implementation, not behavior

based on what you learn, I am expecting you to update go-operating-model.md, which you should also read in addition to domain-first-operating-model.md.
