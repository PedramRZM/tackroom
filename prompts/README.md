# Prompts

Prompts worth reusing, quoted word for word from the people who shared them. Each one names its
author and the saved source under `refs/`. `scripts/agent/check` verifies that every prompt
below still matches its source, so nothing here is paraphrased or improved.

Adapt them. The nouns are examples (an auth provider, a rate limiter, a dashboard); the shape
is what transfers. The last section says what the shapes have in common.

To add one: save the source with `tools/refs`, then add an entry in the same form. A prompt
belongs here when a named, credible person presented it as something to type to an agent.

## Starting something new: find what you do not know

### Blind spot pass
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: starting work in an area you do not know. He uses the literal words "blindspot pass" and "unknown unknowns".
```
I'm working on adding a new auth provider but I know nothing about the auth modules in this codebase. Can you do a blindspot pass to help me figure out my relevant unknown unknowns and help me prompt you better.
```

### Several directions to react to
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: you will know what you want when you see it, and cannot describe it yet.
```
I want a dashboard for this data but I have no visual taste and don't know what's possible. Make me an HTML page with 4 wildly different design directions so I can react to them.
```

### Mock it before wiring it
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: before any real implementation of something visual. The typo "treal" is in the original.
```
Before wiring anything up, make a single HTML file mocking the new editor toolbar with fake data. I want to react to the layout before you touch the treal app.
```

### Brainstorm from a rough problem
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: you have a problem and no solution in mind. He starts almost every coding session with a phase like this.
```
Here's my rough problem: users churn after onboarding. Search the codebase and brainstorm 10 places we could intervene, from cheapest to most ambitious. I'll tell you which ones resonate.
```

### Interview me
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: after brainstorming, to flush out what is still ambiguous.
```
Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture.
```

### Interview me, then write the spec
Author: Claude Code documentation, best practices page
Source: `refs/articles/code.claude.com/docs-en-best-practices-md/article.md`
When: you want something built and have not thought it through.
```
I want to add rate limiting to the public API but haven't thought it through yet. Interview me until you could write the spec, then write it to SPEC.md.
```

### Point at a reference implementation
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: describing what you want would take longer than showing it. Source code is the best reference, even in another language.
```
This Rust crate in vendor/rate-limiter implements the exact backoff behavior I want. Read it and reimplement the same semantics in our TypeScript API client.
```

## Deciding and planning

### Options, effort, doors, a recommendation
Author: Kent C. Dodds (`review-and-recommend` skill, kcd-skills, MIT)
Source: `refs/articles/raw.githubusercontent.com/kentcdodds-kcd-skills-main-skills-review-and-recommend-skill-md/article.md`
When: before implementing, when a decision needs evidence-backed options. A one-way door is hard to reverse (data shapes, public API names, pricing); a two-way door is not.
```
1. Review the relevant data, issues, code, and git history.
2. Present real options (numbered) with associated effort (`Easy` · `Medium` ·
   `Hard`). Label each as a **one-way door** or a **two-way door**
   (hard-to-reverse vs reversible).
3. Make a **recommendation**.
4. Call out the **right fix**. If it differs from the recommendation, explain
   why.
5. Stop and wait for a choice; do not implement yet.
```

### A plan that leads with what you are likely to change
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: you think you are ready to implement and want to review the plan quickly.
```
Write an implementation plan in HTML, but lead with the decisions I'm most likely to tweak with: data model changes, new type interfaces, and anything user-facing. Bury the mechanical refactoring at the bottom, I trust you on that part.
```

## Implementing

### Describe the outcome, with its check
Author: Claude Code documentation, prompt library
Source: `refs/articles/code.claude.com/docs-en-prompt-library-md/article.md`
When: any feature. No file paths; the check is in the prompt.
```
add rate limiting to the public API and make sure existing tests still pass
```

### Ask for the whole thing, not the outline
Author: Claude Code documentation, best practices page
Source: `refs/articles/code.claude.com/docs-en-best-practices-md/article.md`
When: the model would otherwise stop at the minimum. Agents are careful about scope by default; the ambition has to come from you.
```
build the settings page from the mockup. be ambitious: empty and error states, the save flow wired up, keyboard navigation, not just the layout
```

### Match an existing pattern
Author: Claude Code documentation, prompt library
Source: `refs/articles/code.claude.com/docs-en-prompt-library-md/article.md`
When: new code should look like code you already have.
```
add a settings page that follows the same layout as the profile page
```

### Log deviations and keep going
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: a long implementation from a plan, so surprises are recorded instead of silently absorbed.
```
Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate from the plan, pick the conservative option, log it under 'Deviations', and keep going.
```

## Verifying

### Do it, run it, confirm it
Author: Claude Code documentation, prompt library
Source: `refs/articles/code.claude.com/docs-en-prompt-library-md/article.md`
When: any change with an observable result.
```
write the migration, run it against the dev database, and confirm the schema matches
```

### Hand over the artifact, not your description of it
Author: Claude Code documentation, prompt library
Source: `refs/articles/code.claude.com/docs-en-prompt-library-md/article.md`
When: debugging. Paste or reference the log, error or screenshot.
```
why is the build failing? @build.log
```

## Reviewing and understanding a change

### Review against the spec, skip style
Author: Claude Code documentation, best practices page
Source: `refs/articles/code.claude.com/docs-en-best-practices-md/article.md`
When: a fresh-context check before you look. "Skip style" matters: a reviewer asked to find problems always finds something.
```
use a subagent to review the rate limiter diff against SPEC.md, check every requirement is implemented and the listed edge cases have tests, report gaps that affect correctness and skip style
```

### A review page for a change you do not fully follow
Author: Thariq Shihipar, Claude Code team (2026-05-08)
Source: `refs/posts/x/2052809885763747935/post.md`
When: reviewing a pull request in code you are not familiar with.
```
Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity and whatever else might be needed to convey the concept well.
```

### Quiz me before I merge
Author: Thariq Shihipar, Claude Code team (2026-07-03)
Source: `refs/posts/x/2073100352921215386/post.md`
When: after a long session, when the diff alone does not tell you what happened. He merges only after passing the quiz.
```
I want to make sure I understand everything that's happened in this change. Give me a HTML report on the changes for me to read and understand with context, intuition, what was done, etc. and a quiz at the bottom on the changes that I must pass.
```

### Explain how this part works
Author: Thariq Shihipar, Claude Code team (2026-05-08)
Source: `refs/posts/x/2052809885763747935/post.md`
When: you need to understand a subsystem once, well.
```
I don't understand how our rate limiter actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a "gotchas" section at the bottom. Optimize it for someone reading it once.
```

## Code health

### Make implicit state machines explicit
Author: Kent C. Dodds (2026-11-09), adjusted from a prompt he traces to Steve Ruiz; the post quotes David Khourshid on why
Source: `refs/posts/x/2119812466037428392/post.md`
When: an app whose states and transitions are spread through ad-hoc conditions. Tests can pass and reviewers approve while an implicit state machine still allows an illegal state.
```
Find all of the implicit state machines in my app (there are probably a ton). Make the best decision that will elevate all three: the user experience (UX), developer experience (DX), and agent experience (AX) always, without breaking anything. Also, make state machines explicit.
```

## Performance

### A measurable target, and show what you gave up
Author: Claude Code documentation, prompt library
Source: `refs/articles/code.claude.com/docs-en-prompt-library-md/article.md`
When: performance or size work. The metric and threshold make "done" unambiguous.
```
get the bundle size under 200KB and show me what you removed
```

### Port it, keep the original tests, prove it is faster
Author: Boris Cherny, Claude Code (2026-04-09)
Source: `refs/posts/x/2042352725481177315/post.md`
When: a rewrite for speed. The original test suite is the oracle, and the stop condition is proof, not effort.
```
compile our rust+napi file index to native ts. compile the code over, and make sure the code perfectly passes the ORIGINAL test suite from the package. then profile compared to napi/wasm, and put up a pr with the result. dont stop until you have conclusively proven that the new impl is faster.
```

### Follow up with a number
Author: Boris Cherny, Claude Code (2026-04-09)
Source: `refs/posts/x/2042352725481177315/post.md`
When: the first pass worked and you want more. He followed the prompt above with this one.
```
anything else you can do to improve performance? profile it in <large monorepo>. hoping for p99 < 10ms
```

## Goals and loops

### A goal with a threshold and a cap
Author: Delba de Oliveira and Michael Segner, Claude Code team (2026-06-30)
Source: `refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md`
When: you know what done looks like and can state it as a number.
```
/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries.
```

### A goal on tests and lint
Author: Claude Code documentation, goal page
Source: `refs/articles/code.claude.com/docs-en-goal-md/article.md`
When: the end state is a set of passing checks.
```
/goal all tests in test/auth pass and the lint step is clean
```

### Babysit a pull request
Author: Delba de Oliveira and Michael Segner, Claude Code team (2026-06-30)
Source: `refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md`
When: work that depends on something outside the repository, checked on an interval.
```
/loop 5m check my PR, address review comments, and fix failing CI
```

### Fix red CI on an interval
Author: Claude Code documentation, best practices page
Source: `refs/articles/code.claude.com/docs-en-best-practices-md/article.md`
When: as above, with the action spelled out.
```
/loop 15m check CI on this branch, and if it's red pull the failing job's log, fix it and push
```

### A routine that drains a queue
Author: Delba de Oliveira and Michael Segner, Claude Code team (2026-06-30)
Source: `refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md`
When: recurring, well-defined work with nobody watching. Composes a schedule, a goal and a workflow.
```
/schedule every hour: check #project-feedback for bug reports. /goal: don't stop until every report found this run is triaged, actioned, and responded to. When fixing a bug, use a workflow to explore three solutions in parallel worktrees and have a judge adversarially review them.
```

## Showing and explaining

### Say how you want the answer
Author: Claude Code documentation, prompt library
Source: `refs/articles/code.claude.com/docs-en-prompt-library-md/article.md`
When: an explanation you will read once, or show to someone.
```
explain how the payment retry logic works as an HTML page with a diagram, then open it in my browser
```

### Tune it by hand
Author: Thariq Shihipar, Claude Code team (2026-05-08)
Source: `refs/posts/x/2052809885763747935/post.md`
When: a value you can only judge by trying it (an animation, a threshold, a layout).
```
I want to prototype a new checkout button, when clicked it does a play animation and then turns purple quickly. Create a HTML file with several sliders and options for me to try different options on this animation, give me a copy button to copy the parameters that worked well.
```

## What these have in common

My reading, not a quote. Most of the prompts above do several of these at once:

- **They name the end state.** "Under 200KB", "to 90 or above", "p99 < 10ms", "perfectly passes
  the ORIGINAL test suite". The Claude Code docs call this stating the measurable target.
- **They name the proof.** "Run it against the dev database, and confirm", "dont stop until you
  have conclusively proven", "show me what you removed".
- **They set a boundary.** "Without breaking anything", "skip style", "before you touch the
  real app", "stop after 5 tries", "pick the conservative option".
- **They say where the author is.** "I know nothing about the auth modules", "I have no visual
  taste", "I'm not very familiar with the streaming/backpressure logic". Shihipar's point is
  that the model can only cover unknowns it has been told about.
- **They ask for options or questions before work.** A blindspot pass, four directions, an
  interview, numbered options with doors. The decision stays with the person.
- **They describe the outcome and leave the steps to the model.** None lists a procedure,
  except Dodds's, which is a procedure for deciding, not for coding.
- **None uses emphasis, a persona, or "think carefully".** That matches what the Claude Code
  team says about current models (`docs/principles.md`, principle 4).
