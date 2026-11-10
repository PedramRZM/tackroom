---
title: "On file deletions. We’ve investigated a handful of reports where GPT-5.6 unexpectedly deleted files. "
author: "Tibo (@thsottiaux)"
date: "2026-07-16"
url: "https://x.com/thsottiaux/status/2077630111499882637"
site: "x.com"
type: "post"
via: "fxtwitter"
---
On file deletions. We’ve investigated a handful of reports where GPT-5.6 unexpectedly deleted files. 

What we have  found is that this most commonly occurs when:
- Full access mode is enabled and codex is run without sandboxing protections, including without auto review being enabled
- The model attempts  to override the $HOME env var to define a temporary directory.
- The model makes an honest mistake and mistakenly deletes $HOME instead.

This is of course not how we want the system to behave, even when a user operates the model in full-access mode without the safeguards of our sandbox or without using auto review which checks for these kinds of high risk actions and rejects them. 

We are taking steps to mitigate this risk including by updating the developer message, guiding more users towards safer permission modes, and adding additional harness safeguards. Even though this happens extremely rarely, we’ll share a detailed post-mortem in the coming days that goes into more details and what we are doing to minimize risks further.
