---
title: "I still care about the code"
author: "Birgitta Böckeler"
date: "2025-07-09"
url: "https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html"
site: "martinfowler.com"
type: "article"
via: "direct"
---
# I still care about the code

This article is part of the series: [Exploring Gen
  AI.](https://martinfowler.com/exploring-gen-ai.html)

09 July 2025

Ever since AI coding assistance started gaining traction I’ve heard people say, “Oh, so at some point we might not even have to care about the code anymore, it’s like Assembly, we certainly don’t look at THAT anymore.” Recently, with enhanced agentic capabilities and the coinage of “vibe coding” there has been a new spike of this take.

I personally think we very much should still care about the code. Maybe in a different way than before, but still, we need to care.

## Imagine you’re on call!

One of the main benefits of Dev and Ops in one hand is that when you are on call, you become a more responsible developer. You care more about resilience and bug-free code, because you don’t want to be called late in the night, or on the weekend.

So the following is a great question to ground yourself in the hype: If you were on call for the application you’re working on, at which point would you be ok with deploying a 1,000 or 5,000 LOC change set? (Bear in mind, most teams today are even worried about [auto-merging PRs from dependency upgrade bots](https://www.thoughtworks.com/radar/techniques/automatic-merging-of-dependency-update-prs).)

For me personally, the *minimum* I want to still care about and be on top of is the test code.

## LLMs are not compilers

[I wrote about this almost two years ago](https://martinfowler.com/articles/exploring-gen-ai/07-how-is-this-different.html), and I still haven’t changed my mind about it, on the contrary.

LLMs are NOT compilers, interpreters, transpilers or assemblers of natural language, they are **inferrers**. A compiler takes a structured input and produces a repeatable, predictable output. LLMs do not do that. It might be possible to straightjacket them to the point that they produce the same output for an input at a very high probability, but I imagine at that point the input might not even be unstructured natural language anymore. And once we manage to wrap them in enough scaffolding to make them predictable, we risk stripping away the very thing that makes them valuable in the first place.

## Constant risk assessment

Because of the non-deterministic nature of these inferrers, using Generative AI in the software context is constant risk assessment. I am feeling that especially at the moment, while working on an AI-accelerated lift and shift legacy migration that needs to achieve feature parity.

Risk assessment, as always, is a combination of these 3 factors:

- **Impact** of something going wrong: Will I be called in the middle of the night? Am I working on a use case with a low margin for error? Is the domain I’m working on critical to the business, or internal and supplementary?
- **Probability** of something going wrong: How sophisticated is the AI setup I have? Is the problem I’m working on simple or comples? Do I have the appropriate context available for AI to do the right thing?
- **Detectability**: How likely is it that I will catch problems? For this I factor in  the level and type of review that is applied, and what confidence I have in the overall safety net.

Hallucinations are the core feature of LLMs. We just call it “hallucinations” when they do something we don’t want, and “intelligence” in the cases where it’s useful to us. Regardless of how much context, tooling and model power I throw at a problem, there is always a non-negligible probability that something goes wrong. So especially in cases with high impact and low detectability, I absolutely still care about the code.

latest article (Oct 13):

previous article:

next article:
