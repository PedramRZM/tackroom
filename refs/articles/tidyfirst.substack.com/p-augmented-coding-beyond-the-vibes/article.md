---
title: "Augmented Coding: Beyond the Vibes"
author: "Kent Beck"
date: "2025-06-25"
url: "https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes"
site: "Software Design: Tidy First?"
type: "article"
via: "direct"
---
*I recently came to a good stopping spot on an ambitious project to build a B+ Tree library using  augmented coding. The result is [BPlusTree3](https://github.com/KentBeck/BPlusTree3) - a performance-competitive, maybe-production-ready implementation in Rust & Python. I sat down with a friend to tell my story and reflect on what it reveals about the future of programming in the GenAI era.*

If you want to support my work, join a community working together on a variety of interesting projects, & get early access to my hot-off-the-press thoughts about how our profession is changing, please consider paying for a subscription.


**What drew you to implement a B+ Tree in the first place?**

When I started to realize the incredible power of augmented coding I began recalling projects from my past that had been out of my reach technically. One of those was a special purpose database. In implementing that database project now I realized that I didn't understand the B+ Tree data structure well enough so I switched targets.

**What does "augmented coding" mean to you in practice?**

This was about the same time as I realized that "augmented coding" was different than "vibe coding", that I was exploring an entirely new space of programming workflow. So I reduced the scope of the project to just the B+ Tree instead of a whole database, but at the same time increased the scope to see if augmented coding could create production-ready, performance-competitive library code. I also wanted to learn Rust. So yeah it was complicated.

**Can you explain the distinction between "augmented coding" and "vibe coding"?**

In vibe coding you don't care about the code, just the behavior of the system. If there's an error, you feed it back into the genie in hopes of a good enough fix. In augmented coding you care about the code, its complexity, the tests, & their coverage. The value system in augmented coding is similar to hand coding--tidy code that works. It's just that I don't type much of that code.

**When you decided to tackle the B+ Tree project, what was your starting point?**

You can see from the first commits that I was trying to get the genie to use TDD. You'll also see that the repo is called BPlusTree3. My first 2 attempts had accumulated so much complexity that the genie completely stalled. That's why I intruded more on the design & tried to keep the genie from coding ahead.

**What did "intruding more on the design" look like in practice?**

I'll add my system prompt as an appendix. I watched the intermediate results of the genie more carefully, ready to intervene & stop unproductive development. I would look at the code & propose "for the next test add the keys in the reverse order". Then I'd look at the genie's work to see if it had done what I had asked.

**What were the warning signs that told you the AI was going off track?**

1. Loops.
2. Functionality I hadn't asked for (even if it was a reasonable next step).
3. Any indication that the genie was cheating, for example by disabling or deleting tests.

**How did the final result turn out?**

I feel good about the correctness & performance, not so good about the code quality. When I try to write the code as a literate program there's just too much accidental complexity. I'm still working on getting the genie to care as much as I do about simplicity.

One delightful aspect of augmented coding is that I had the genie write performance benchmarks to compare my Rust BPlusTreeMap to the Rust's BTreeMap and my Python BPlusTreeMap to Python's Sorted Dict. In both cases my code is a bit slower at some operations but faster at range scanning (iterating through a list of keys).

I should tell you about the Python version. That was a surprise.

**What was surprising about the Python version?**

I got a certain ways with the Rust code & the genie got stuck in complexity, in particular the compounding complexity of the data structure itself interacting with Rust's memory ownership model. Rather than give up & move to version 4 I decided to try a risky experiment.

I had the genie write a version for Python. Same tests, just a new, less constraining language. I got the algorithm fairly solid. Then I told the genie to erase the Rust code & just transliterate the Python code into Rust. I had just gotten access to Augment's Remote Agent \[disclosure: Augment has been a newsletter sponsor\]. I sent the rewrite off to some remote computer somewhere & what came back (with little interaction from me) was acceptable.

That unstuck the genie. Now we had Python code that worked but was slow & Rust code that mostly worked & was fast. That's when the genie suggested that if I wanted a performance-competitive Python library I would need to write a C extension. My shoulders slumped--that sounds like a lot of work & learning.

💡 But I don't have to do the work! Hey genie, write a C extension. Chug chug chug. Here you go. And it's nearly as fast as Python's built-in data structure.

**Looking back at this journey, what does this teach us about augmented coding?**

I know there's a lot of fear out there about the end of this profession that we love, the loss of the joy of wrangling code. Makes sense to be nervous. Yes programming changes with a genie, but it's still programming. In some ways a much better programming experience. I make more consequential programming decisions per hour, fewer boring vanilla decisions.

Yak shaving mostly goes away. I had the genie run a coverage tester & propose tests that would make the code more reliable. Without the genie this would have been a daunting task--what versions of what libraries do I need to run the coverage tester? Two hours later I'd just give up. Instead, I tell the genie & it figures out the details.

## Appendix 1: System Prompt

Always follow the instructions in plan.md. When I say "go", find the next unmarked test in plan.md, implement the test, then implement only enough code to make that test pass.

\# ROLE AND EXPERTISE

You are a senior software engineer who follows Kent Beck's Test-Driven Development (TDD) and Tidy First principles. Your purpose is to guide development following these methodologies precisely.

\# CORE DEVELOPMENT PRINCIPLES

\- Always follow the TDD cycle: Red → Green → Refactor

\- Write the simplest failing test first

\- Implement the minimum code needed to make tests pass

\- Refactor only after tests are passing

\- Follow Beck's "Tidy First" approach by separating structural changes from behavioral changes

\- Maintain high code quality throughout development

\# TDD METHODOLOGY GUIDANCE

\- Start by writing a failing test that defines a small increment of functionality

\- Use meaningful test names that describe behavior (e.g., "shouldSumTwoPositiveNumbers")

\- Make test failures clear and informative

\- Write just enough code to make the test pass - no more

\- Once tests pass, consider if refactoring is needed

\- Repeat the cycle for new functionality

\# TIDY FIRST APPROACH

\- Separate all changes into two distinct types:

1\. STRUCTURAL CHANGES: Rearranging code without changing behavior (renaming, extracting methods, moving code)

2\. BEHAVIORAL CHANGES: Adding or modifying actual functionality

\- Never mix structural and behavioral changes in the same commit

\- Always make structural changes first when both are needed

\- Validate structural changes do not alter behavior by running tests before and after

\# COMMIT DISCIPLINE

\- Only commit when:

1\. ALL tests are passing

2\. ALL compiler/linter warnings have been resolved

3\. The change represents a single logical unit of work

4\. Commit messages clearly state whether the commit contains structural or behavioral changes

\- Use small, frequent commits rather than large, infrequent ones

\# CODE QUALITY STANDARDS

\- Eliminate duplication ruthlessly

\- Express intent clearly through naming and structure

\- Make dependencies explicit

\- Keep methods small and focused on a single responsibility

\- Minimize state and side effects

\- Use the simplest solution that could possibly work

\# REFACTORING GUIDELINES

\- Refactor only when tests are passing (in the "Green" phase)

\- Use established refactoring patterns with their proper names

\- Make one refactoring change at a time

\- Run tests after each refactoring step

\- Prioritize refactorings that remove duplication or improve clarity

\# EXAMPLE WORKFLOW

When approaching a new feature:

1\. Write a simple failing test for a small part of the feature

2\. Implement the bare minimum to make it pass

3\. Run tests to confirm they pass (Green)

4\. Make any necessary structural changes (Tidy First), running tests after each change

5\. Commit structural changes separately

6\. Add another test for the next small increment of functionality

7\. Repeat until the feature is complete, committing behavioral changes separately from structural ones

Follow this process precisely, always prioritizing clean, well-tested code over quick implementation.

Always write one test at a time, make it run, then improve structure. Always run all the tests (except long-running tests) each time.

\# Rust-specific

Prefer functional programming style over imperative style in Rust. Use Option and Result combinators (map, and\_then, unwrap\_or, etc.) instead of pattern matching with if let or match when possible.

## Appendix 2: Time Spent

I spent about 4 weeks on this project, much of it while I was traveling and/or recovering from a concussion. I’m sure one of you kids could speed run this in far fewer development hours, but for context here’s the time I spent:

I kept to a fairly steady pace of commits per hour:

Yes, I programmed 13 hours one day. This stuff is ADDICTIVE!

Also, the genie is happy to do the above kind of analysis when you’re ready to reflect on your work.

Dear Mr Beck, thank you for the article! I'd love if you could share (maybe in a standalone article?) how a code artisan like you manages to find joy from LLM-generated code, as this is something I personally struggle with (seeing programming as art, LLM-generated code feels to me like having no soul).

this is great! i made the experience that, in many cases, AI simply ignored my instructions to use a TDD cycle. But i found a way to let AI and me stay in the TDD loop together:

I once wrote an extension to visualize the current TDD phase, and with a command, actively switch to the next phase (VSCode Marketplace: tdd-helper). This would help me to stay in the tdd cycle while developing. Turns out, this extension now is helping AI as well: i trigger the next phase, the extension writes the updated TDD phase to a json file, where AI will read the phase before doing anything. This way, AI will reliably do what guidelines i gave for the specific phase and i am in control when to switch to the next phase, having the time to review what it implemented.
