---
title: "We stopped reviewing code and started verifying intent"
date: "2026-10-20"
url: "https://tessl.io/blog/we-stopped-reviewing-code-and-started-verifying-intent"
site: "Tessl"
type: "article"
via: "direct"
---
ARTICLE

# We stopped reviewing code and started verifying intent

Discover how verifying intent over reviewing code boosts efficiency in AI-generated code workflows. Learn the framework that transformed our process.

[Ankit Jain](https://tessl.io/blog/author/ankit-jain)

*By Ankit Jain, for AI Native DevCon*

What do you do when your team merges four times more pull requests than it did a year ago, and almost none of that code was typed by a human?

That's where my team is today. Almost everything we ship is AI-generated and human-assisted, and the volume keeps climbing. We did the obvious thing first. We tried to scale code review by using AI review tools or adding stricter checklists. None of it worked.

What worked was giving up reading code line-by-line entirely and building a verification layer around intent.

## Why scaling code review for AI-generated code didn't work

Earlier this year I wrote [How to Kill the Code Review](https://latent.space/p/reviews-dead) for Latent Space. It went viral, and I haven't stopped talking about the AI code review bottleneck since.

The problem keeps coming up because its cause isn't going away. At four times the volume, review became the slowest step in shipping.

Most teams that use AI coding tools run into the code review bottleneck and try to solve it with some combination of more reviewers, adding AI code review tools, or stricter rules for code generation. But the real problem is what's being reviewed. A diff tells you what changed, but it doesn't tell you what the change was supposed to do.

This post covers the two practices that made the most significant difference for us, and the framework they ended up fitting into.

As a baseline, we now maintain a shared skill that we call "offer-skill," named after our engineer who started it. It turned into the skill that everyone uses to understand the code change.

## Review the intent, not the diff

The conventional wisdom says human judgment belongs at the end. Someone reads the code and decides whether it looks right.

With AI-generated code, that puts the reviewer in a bad spot. They read 400 lines and try to reverse-engineer what the change was meant to do. The ticket description only helps if there is a team discipline of maintaining good tickets. The reality is that most tickets are poorly drafted, and the actual intent and behavior drift from the ticket.

So we moved human judgment to the front. Before a single line is generated, we review the intent: the acceptance criteria, the constraints, and the edge cases. That's where a senior engineer's attention is worth the most, because a wrong idea costs almost nothing to fix at that point.

Then we treat that intent as a contract we can verify. Each criterion gets a deterministic verdict, with evidence attached.

A review looks different now. The reviewer isn't scrolling through a 500-line AI-generated diff. They're looking at five criteria verdicts, with screenshots and request traces that show what happened.

What does this mean for devs? The author and the reviewer both know what the code is supposed to do before it's merged. And if you can't say what a change should do before it exists, reading it afterward won't tell you.

## Mine your PR comments, they're invariants waiting to happen

Every team has standards that live in senior engineers' heads. They get enforced one review comment at a time.

Look through your review history, and you'll see the same comments written over and over. Those are team standards hiding in plain text. At four times the PR volume, repeating them by hand becomes a bottleneck of its own.

So we went back through X our recurring review comments and turned them into invariants: reusable rules that a machine enforces on every change.

A good invariant is boring and specific. For example:

- Use the Money type for anything with a currency.
- No direct writes to the users table.
- Structured logger only, no print statements.

Not every comment qualifies.

If you want to try this, start with your last 1,000 review comments. The 20 you repeat most are your first invariants. You aren't inventing rules. You're writing down the ones you already have.

Once a standard is an invariant, nobody has to flag it again.

Have in mind that the transition will not happen overnight. Month one will most likely feel like the team is doing double work: reviewing code and building invariants. Set clear expectations with the team: the register takes time to build. During month two, the register catches enough that reviews shrink. In month three, the reviewer reads intent, not code.

## Code review didn't disappear, it changed shape

We still review. What changed is what the review is for. The two practices above are part of a five-step shape I now use to describe it:

1. **Argue.** Let agents challenge each other's solutions before the pull request exists, when changing course is cheapest.
2. **Capture.** Record the intent and acceptance criteria, and put them on the pull request.
3. **Codify.** Turn the comments your team keeps repeating into invariants.
4. **Debate.** Spend human review time on the decisions, not the diff.
5. **Own.** Decide who owns the rules that verify the code.

For us, the result is that code review is no longer the bottleneck. Senior engineers stopped reading 500-line AI-generated diffs.

### tl;dr

- Scaling diff review to match AI output doesn't work.
- Review the intent before the code is generated, and verify each criterion with evidence.
- Turn your recurring review comments into invariants.
- Keep humans on the decisions and on ownership of the rules.

When AI writes most of your code, a human's review is best spent on what the change should do. I'll walk through the full workflow at AI Native DevCon, with live examples of invariant definitions and before/after metrics.

COPY & SHARE

Ankit Jain

Ankit Jain is a founder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale — without the review bottlenecks, broken builds, or brittle deployments. He also leads The Hangar, a community of senior engineers and engineering leaders focused on developer experience, and Xoogler, the ex-Google alumni network.

READING

·

0%

IN THIS POST

COPY & SHARE

Ankit Jain

Ankit Jain is a founder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale — without the review bottlenecks, broken builds, or brittle deployments. He also leads The Hangar, a community of senior engineers and engineering leaders focused on developer experience, and Xoogler, the ex-Google alumni network.
