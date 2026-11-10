---
title: "Anchoring AI to a reference application"
author: "Birgitta Böckeler"
date: "2025-09-25"
url: "https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html"
site: "martinfowler.com"
type: "article"
via: "direct"
---
# Anchoring AI to a reference application

This article is part of the series: [Exploring Gen
  AI.](https://martinfowler.com/exploring-gen-ai.html)

25 September 2025

Service templates are a typical building block in the “golden paths” organisations build for their engineering teams, to make it easy to do the right thing. The templates are supposed to be the role models for all the services in the organisation, always representing the most up to date coding patterns and standards.

One of the challenges with service templates though is that once a team instantiated a service with one, it’s tedious to feed template updates back to those services. Can GenAI help with that?

## Reference application as sample provider

As part of a larger experiment that I recently wrote about [here](https://martinfowler.com/articles/pushing-ai-autonomy.html), I created an MCP server that gives a coding assistant access to coding samples for typical patterns. In my case, this was for a Spring Boot web application, where the patterns were repository, service and controller classes. It is a well established prompting practice at this point that providing LLMs with examples of the outputs that we want leads to better results. To put “providing examples” into fancier terms: This is also called “[few-shot prompting](https://martinfowler.com/articles/pushing-ai-autonomy.html)”, or “in-context learning”.

When I started working with code samples in prompts, I quickly realised how tedious this was, because I was working in a natural language markdown file. It felt a little bit like writing my first Java exams at university, in pencil: You have no idea if the code you’re writing actually compiles. And what’s more, if you’re creating prompts for multiple coding patterns, you want to keep them consistent with each other. Maintaining code samples in a reference application project that you can compile and run (like a service template) makes it a lot easier to provide AI with compilable, consistent samples.

## Detect drift from the reference application

Now back to the problem statement I mentioned at the beginning: Once code is generated (be that with AI, or with a service template), and then further extended and maintained, codebases often drift away from the role model of the reference application.

So in a second step, I wondered how we might use this approach to do a “code pattern drift detection” between the codebase and the reference application. I tested this with a relatively simple example, I added a logger and log.debug statements to the reference application’s controller classes:

Then I expanded the MCP server to provide access to the git commits in the reference application. Asking the agent to first look for the actual changes in the reference gives me some control over the scope of the drift detection, I can use the commits to communicate to AI exactly what type of drift I’m interested in. Before I introduced this, when I just asked AI to compare the reference controllers with the existing controllers, it went a bit overboard with lots of irrelevant comparisons, and I saw this commit-scoping approach have a good impact.

In the first step, I just asked AI to generate a report for me that identified all the drift, so I could review and edit that report, e.g. remove findings that were irrelevant. In the second step, I asked AI to take the report and write code that closes the gaps identified.

### When is AI bringing something new to the table?

A thing as simple as adding a logger, or changing a logging framework, can also be done deterministically by codemod tools like [OpenRewrite](https://docs.openrewrite.org/). So bear that in mind before you reach for AI.

Where AI can shine is whenever we have drift that needs coding that is more dynamic than is possible with regular-expression-based codemod recipes. In an advanced form of the logging example, this might be turning non-standardised, rich log statements into a structured format, where an LLM might be better at turning a wide variety of existing log messages into the respective structure.

The example MCP server is included in [the repository that accompanies](https://github.com/birgitta410/pushing-ai-autonomy-article) [the original article](https://martinfowler.com/articles/pushing-ai-autonomy.html).

latest article (Oct 13):

previous article:
