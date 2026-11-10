---
title: "75% of Tessl's PRs now merge without human review"
date: "2026-10-16"
url: "https://tessl.io/blog/75-of-tessls-prs-now-merge-without-human-review"
site: "Tessl"
type: "article"
via: "direct"
---
ARTICLE

# 75% of Tessl's PRs now merge without human review

Discover how Tessl's innovative code review process allows 75% of PRs to merge without human review, reducing costs and enhancing efficiency.

Authors @Simon Rendon Arango and @Colin Hallett

**At a glance**

- **Team:** Tessl engineering, running a software factory on one monorepo
- **Scale:** Over 1,200 agent-written pull requests (PRs) a week
- **Challenge:** Review every agent-written PR without burying engineers in noise or letting review costs climb
- **Solution:** Tessl Code Review running on the team's own standards

## Key results

| \~75% | of PRs merged without human review | 
|---|---|
| 35% | lower review cost per PR than our previous AI reviewer | 
| 91% | of Tessl Code Review findings were real defects, against 68% for our previous AI reviewer | 
| 2x | more real bugs fixed per PR, because findings were checked against our own standards instead of generic rules | 

## The challenge

Tessl engineers do most of their work through agents. That’s how we got to over 1,200 PRs a week, and why review started holding everything up.

It also became our biggest variable cost. PRs that never merged and review-fix rounds made up over half of our agent spend.

Our previous AI reviewer should have taken some of that load, but we didn't trust it. About a third of its findings weren't real defects, so engineers ended up reviewing the reviewer, checking each finding and then each fix. We couldn't tune it to our own standards either, so when it missed something or flagged something we didn't care about, we had no way to change it.

## The solution

We needed a reviewer we could trust enough to let PRs merge without a human. With Tessl Code Review, we encode our own standards on top of the standard review lenses, and we set the review policy to match the risk we're willing to take. Because we own the lenses and the standards, we can see why a finding was raised and change what the reviewer checks. That control is what built our trust, and any team using Tessl Code Review gets the same control over its own repo.

### Review against our own standards

Tessl Code Review checks every PR against the standards our team already writes for its agents, including our coding conventions, design system and AI code review policy. Our previous AI reviewer applied the same general rules to every repo, so it couldn't tell when a change broke a rule specific to our codebase.

To confirm that our standards explained the gap, we ran both reviewers on an external benchmark with human-labeled defects. They tied. On our own repo, where Tessl Code Review had our standards to work from, it found more real defects and far fewer false positives.

There was a trade-off. Our previous AI reviewer was stronger on low-severity findings and cosmetic issues, and on our repo it caught some defects that Tessl Code Review missed. We switched because we can close each of those gaps ourselves by updating a review lens, a standard or a setting.

When reviewers flag the same pattern repeatedly, we turn it into a verifier, a pass or fail check that runs on every change. With our previous AI reviewer, closing a gap meant waiting on the vendor.

## The results

Since we introduced Tessl Code Review, about 75% of PRs have merged without a human correcting the agent or discussing the engineering. With far fewer false positives to dismiss, engineers spend their review time on the PRs that need a human.

### Review quality

Over the side-by-side week, Tessl Code Review and our previous AI reviewer raised roughly 1,850 findings. 91% of Tessl Code Review's findings were real defects, against 68% for our previous AI reviewer. That left engineers with about 435 fewer false positives to read and dismiss each week.

Engineers fixed 1.56 bugs per PR that only Tessl Code Review flagged, against 0.75 for our previous AI reviewer, so twice as many real bugs were fixed before merge.

Tessl Code Review also led on all six change types our AI code review policy says always need a human check. The largest gaps were in privacy (27 issues found vs 4) and access control (94 vs 34).

|  | Tessl Code Review | Our previous AI reviewer | 
|---|---|---|
| Findings that were real defects | 91% | 68% | 
| Author-fixed bugs per PR (found only by that reviewer) | 1.56 | 0.75 | 
| Policy-relevant issues fixed | 262 | 99 | 
| Privacy issues found | 27 | 4 | 

### What it means for your bill

On default settings, every Tessl Code Review round costs a flat 50 credits. Our PRs average 2.2 rounds, so each PR costs us about **35% less to review than it did with our previous AI reviewer.**

If you change the model, effort or number of review lenses, you pay for the AI credits you use, with a minimum of 50 credits a round. We also pick models by cost per verified outcome, not token price, which keeps the cost of each review down. [Read how we choose models](https://tessl.io/blog/cheaper-tokens-bigger-bills-token-price-isnt-agent-cost).

## What's next

Next, we're using review to improve context directly. Tessl will mine code review data on a schedule and suggest updates to the context your agents use, so lessons from one review reach the next agent before it writes code. We'll share results as they come in.

## Try it on your own repo

Tessl Code Review is free to start, with 1,000 credits a month. Point it at a repo and see what it finds. \[Try it free\]

## How we measured

- **Side-by-side review:** We ran both reviewers on every PR in the monorepo for one week, more than 600 PRs in total.
- **Real defect:** A finding counted as a real defect only if it described something that would misbehave in production: wrong behavior, a broken contract, data loss, a security hole, a crash or a leak. Style, naming and preference didn't count.
- **Fixed:** The author changed the code to address the finding before merging.
- **Benchmark:** An external, third-party dataset with human-labeled defects, used so neither reviewer had a home advantage.
- **Merged without human correction:** A PR that merged without a human correcting the agent or discussing the engineering. Measured from the introduction of Tessl Code Review.
- **PR volume:** Agent-written PRs opened per week across the monorepo, from engineers running agents locally and from the software factory.
- **Review cost:** The default price of a Tessl Code Review round multiplied by our average of 2.2 rounds per PR, compared with our previous AI reviewer's cost per reviewed PR.

We defined every term before looking at the results.

- On a Swift app, one project runs it as a required check with custom review lenses. On a single PR, it raised 12 required findings, including two paths where an API key header was forwarded across an HTTP redirect. That's a credential leak, caught in a language and domain we hadn't tuned for.
- On a long-standing climate science Python package, the maintainer resolved 216 of 219 findings, sometimes noting which commit fixed which one.
- 8.5% of PRs went through more than five review rounds.
- Those PRs used 47.4% of our review loop spend.
- About one in seven rounds on those PRs was triggered by a merge conflict, and two-thirds of those reruns found nothing new.

READING

·

0%

IN THIS POST

COPY & SHARE

YOUR NEXT READ

## Cheaper Tokens, Bigger Bills: Token Price Isn't Agent Cost

Token prices don't reflect the true cost of AI models in code reviews. Turns and verified outcomes are better measures, revealing hidden expenses in agent workloads.

Simon Rendon Arango
