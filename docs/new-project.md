# Starting a new product or project

What the sources say about going from an idea to a repository agents can work in, and about
choosing a stack and an architecture; and what the template does about it. The skill that
carries this into a project is `kickoff`.

How this was put together: from notes already in `refs/notes/`, plus three sources read
directly for this question: Thariq Shihipar's field guide to finding unknowns, and Kent C.
Dodds's post on owning the outcome and his own agent setup (`kcd-skills`). A dedicated research
pass was started and stopped before it produced notes. Not read: Anthropic's founders playbook
chapters, and anything that benchmarks languages or frameworks for agent use.

## Do you need more setup for a new idea?

Not much more. The template already gives a new repository what the sources say must exist
before the first real task. What was missing was the step before that: getting from an idea to
decisions. That is now the `kickoff` skill, which you start yourself, once.

### Before any code: find what you do not know

Shihipar's field guide ([`refs/posts/x/2073100352921215386/post.md`](https://x.com/trq212/status/2073100352921215386)) frames the work before
implementation as reducing unknowns, in four moves. Each has a prompt in `prompts/README.md`:

1. **Blind spot pass**: ask the model what you do not know to ask about the area.
2. **Brainstorm and prototype**: for anything you will only recognise when you see it, get
   several different directions as throwaway HTML before wiring anything up. Finding these
   preferences during implementation is the expensive way.
3. **Interview**: have the model question you, one question at a time, starting with what
   would change the architecture.
4. **An implementation plan that leads with what you are likely to change**: data model, type
   interfaces, anything user-facing.

Dodds describes the same opening from the product side
([`refs/articles/kentcdodds.com/blog-you-own-the-outcome/article.md`](https://kentcdodds.com/blog/you-own-the-outcome)): build shared
understanding first (who has the problem, what they are trying to do, what done looks like),
then ask for options instead of an answer.

### How much to plan

Less than it feels like you should. In Anthropic's own long-running harness, detailed technical
plans written up front were where errors entered and then carried through the build; their
planner was changed to stay at the product level (`refs/notes/task-backlog-epic-management.md`,
"When to write a spec"). The Claude Code team's own habit moved from design documents to
prototypes and discussion on pull requests (`refs/notes/task-backlog-epic-management.md`,
"What frontier teams say they do"). Dodds ships "the smallest useful slice" and defers the rest.

So: decide the things that are hard to undo, write those down, build one thin slice that runs,
and let tasks carry the detail.

### What must exist on day one

Dodds's setup is a ladder, and its first rungs are the day-one list
([`refs/articles/raw.githubusercontent.com/kentcdodds-kcd-skills-main-skills-autopilot-skill-md/article.md`](https://raw.githubusercontent.com/kentcdodds/kcd-skills/main/skills/autopilot/SKILL.md),
"Rungs"). Next to each is where the template has it.

| Day one | In the template |
|---|---|
| A short agent map and one verify command, the same locally and in CI | `AGENTS.md`, `scripts/agent/check` |
| A decisions folder that records the "no" as well as the "yes" | `docs/decisions/`, with "Revisit if" |
| A way for the agent to run its own change and show proof | `verify` skill and its "This project" notes |
| A pull request template built on intent, door, testing and risk | `.github/pull_request_template.md` |
| A reviewer other than the author for riskier changes | `second-opinion`, `reviewer` |

What can wait until there are users, by his own ordering: feature flags with an owner and a
removal condition, a rollback runbook, restore-tested backups, and the cleanup and friction
loops. The `kickoff` skill files these as tasks instead of building them.

Two things in his setup that the template does not ship, and why:

- **A project control tool** (one command that starts the app, signs in as a seed user, makes
  authenticated requests, drives a browser, checks the deployed version). It is the most
  convincing idea in his setup and it is project code. `verify` now says what to record so one
  can be grown per project.
- **A catalogue of building blocks ("primitives") linked to the decisions that shape them.**
  One author's practice, with no second source in the corpus. Left out.

## Choosing technology, libraries and architecture

The corpus has little that is measured here and a fair amount of consistent first-hand advice.
The criteria below are in the `kickoff` skill.

### The decision procedure matters more than the answer

- **Sort choices into one-way and two-way doors.** A one-way door is hard to undo: data
  shapes, public names, pricing. Slow down there and decide yourself. Walk through two-way
  doors quickly and let the agent run (Dodds, "Then, ask for options instead of an answer").
- **Ask for options with effort, trade-offs, the door type and a recommendation**, then make
  the call. His `review-and-recommend` skill is in `prompts/README.md`.
- **Do not over-deliberate the framework.** Dodds: "Which framework you pick matters less than
  it used to." He calls it an output-level choice that agents increasingly navigate with you.
- **Record one-way doors as decisions**, phrased so they also say what not to do, with the
  conditions for revisiting. Otherwise the next session proposes the rejected option again.

### Criteria the sources give

| Criterion | Source | Strength |
|---|---|---|
| Prefer stable, popular, well-documented technology; allow for the model's training cut-off, and for newer libraries make current docs or examples reachable | Willison, "boring technology" ([`refs/articles/simonwillison.net/2025-mar-11-using-llms-for-code/article.md`](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)); the loops article's "make docs easy to reach" | First-hand, repeated |
| One way to do each thing, because the code already in the repository is what the agent imitates | Lopopolo standardises on one stack per concern: "all the code in the repository ... is also prompts" (`refs/notes/devcon-2-harness-specs-verification.md` (a)); the loops article: the model follows the patterns already there | First-hand, repeated |
| Strong static checks: types, and lint rules that fail loudly with the fix in the message | OpenAI's custom lints, including a ban on untyped values outside input parsing (same notes); Dodds's static layer (`docs/testing.md`) | First-hand, repeated |
| The agent must be able to run the app and check its own change locally | The Claude Code team's most repeated tip (`refs/notes/x-posts.md`, finding 1); Dodds's rung 4 | First-hand, strongest agreement in the corpus |
| Few dependencies, pinned, and not a release from the last few days | The supply-chain talks: pin versions and wait before taking new releases (`refs/notes/devcon-1-skills-context-memory.md` (c)) | First-hand; about skills and packages generally |

What the corpus does not have: a comparison of languages or frameworks by how well agents
handle them. Anything stronger than the table above would be opinion.

### Architecture

- **Boundaries with one allowed dependency direction, enforced mechanically.** OpenAI's
  harness team fixes layers per domain (types, config, repository, service, runtime, UI) and
  enforces them with custom lints and structural tests whose error messages say how to fix the
  violation (`refs/notes/devcon-2-harness-specs-verification.md` (a)). Prose rules about
  architecture are followed most of the time; a failing check is followed every time.
- **Make state explicit.** The prompt Dodds shared asks the agent to find implicit state
  machines and make them explicit; the post he quotes explains that tests can pass and
  reviewers approve while scattered conditions still allow an illegal state
  ([`refs/posts/x/2119812466037428392/post.md`](https://x.com/kentcdodds/status/2119812466037428392)).
- **Humans decide the architecture; agents write the code.** A talk in the DevCon set is
  titled almost exactly that ([`refs/videos/wuGJNWhUOoE/transcript.md`](https://www.youtube.com/watch?v=wuGJNWhUOoE)), and Anthropic's account of its own source-control work says engineers
  supply system-level constraints and frequently refuse what the agent proposes
  (`refs/notes/anthropic-engineering.md`, the source-control entry).
- **Start enforcing while there is almost no code.** My inference from the two points above: a
  boundary rule added at the first slice costs minutes; added later it costs a migration.

### For one person with many small projects

Most of the organisational advice in the corpus does not apply. What does:

- Reuse one stack across projects where you can. Every difference is something each new
  session has to learn again, and something you have to review.
- The `kickoff` questions take minutes on a small project. Skip the prototype step when there
  is nothing visual, and skip decision records for anything easy to undo.
- Keep the day-one list. A project without a check command and a way to run the app is one
  where you verify everything by hand.

## What was added to the template for this

- `kickoff` skill (you start it; it adds nothing to the model's context otherwise).
- `docs/decisions/README.md`: record the "no", list rejected alternatives with their effort,
  and say when to revisit.
- `spec` skill: hard-to-reverse choices go to you as options with a recommendation.
- Pull request template: an Intent line and a Door line.
- `prompts/README.md`: the discovery, decision and planning prompts quoted above.

## Gaps

- No source in the corpus measures stack choice against agent success.
- Anthropic's founders playbook (idea, MVP, launch and scale chapters) is on claude.com and was
  not saved or read.
- The `kickoff` skill has not been run on a real idea.
