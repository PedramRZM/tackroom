---
title: "How I do code reviews these days: more code = more selective human review i.e. don't read all the code."
author: "Addy Osmani (@addyosmani)"
date: "2026-09-07"
url: "https://x.com/addyosmani/status/2097027173941141799"
site: "x.com"
type: "post"
via: "fxtwitter"
---
How I do code reviews these days: more code = more selective human review i.e. don't read all the code.

1. Every PR gets a multi-agent first pass. It should find bugs, verify them, rank by severity, suggest fixes. Approval stays a human call on anything that matters.

2. Low blast radius changes on less sensitive code (there's often a lot!) can skip a deep human review once that review is clean. This helps keep the explosion of PRs manageable.

3. Core / sensitive paths still need an owner and human sign-off. That's where you spend time: verification, constraints and earning trust in what the agents can safely cover. You want to keep recoverability.

Agents do the first pass and humans cover blast radius.

Great question from @GergelyOrosz!

> Quoting @GergelyOrosz: If you’ve stopped doing human code reviews: how is it going?
> 
> If you’re still doing them: how are you able to keep up with the explosion of code + PRs, and how do you prioritise what to review “properly”?
