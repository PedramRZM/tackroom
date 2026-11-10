---
title: "How to constrain a coding agent using only files you own"
date: "2026-10-20"
url: "https://tessl.io/blog/how-to-constrain-a-coding-agent-using-only-files-you-own"
site: "Tessl"
type: "article"
via: "direct"
---
ARTICLE

# How to constrain a coding agent using only files you own

Learn how to effectively constrain a coding agent using files you own. Discover key strategies and tools to enhance your coding projects today.

[Ian Johnson](https://tessl.io/blog/author/ian-johnson)

I gave a coding agent one ticket and no charter. The repository was three eras deep, the way a real one is. A 2026 domain layer does everything correctly, and a 2023 god file plus a frozen 2021 module nobody is allowed to touch outnumber it ten to one.

The agent never opened the correct code. It went to the god file, called `random.randint` for a dice roll, and serialized the total with no seed. It rewrote a log entry through a helper that exists and works, and it reached into the frozen module twice.

*Score:* one check out of eight. Nothing in that repository was broken, and the agent copied the code in front of it. Everything that would have stopped it was a file I had not written yet.

## What you actually own

I work on harness and charter engineering: the engine that runs an agent, and the rules it reads first. That is the subject of *Harness Engineering*, the book, and of Keystone, my open source charter framework tool. In November I’m running a ninety-minute workshop at AIDevCon where a room of engineers writes those files and measures what each one bought.

The advice to write a `CLAUDE.md` is everywhere now, and it is good advice, but that file is one lever of four. The other three sit beside it in the same repository, under paths you already own, and many teams don’t ship enough of them.

Which part of a charter holds when the agent disagrees with it, and what does each part buy? Both are answerable on a laptop, and below is what I got answering them three times on one ticket.

## Your charter is four levers, not one file

The conventional version: write your standards down in `CLAUDE.md`.

Everyone writes that lever, and three more sit next to it. All four are files, all four are yours, and all four live under paths the agent reads before it writes a line:

1. **Instruction** is `CLAUDE.md`. What this repository is, in the present tense.
2. **Constraint** is `.claude/rules/`, path-scoped, each rule carrying the date of the incident that caused it.
3. **Capability** is `.claude/commands/`, `.claude/skills/`, `.claude/agents/`, `.claude/settings.json` and `.mcp.json`. What the agent can reach for, and what it is allowed to run.
4. **Check** is `.claude/hooks/`. What refuses it.

*The three levers on the left change what the agent reads and reaches for. The one on the right is the only one that can refuse.*

The capability lever is the half that is not usually designed. Four rungs sit on it: a command, a skill, a sub-agent, an MCP server. The family test sorts them. Remove the thing, and if the agent can do less, it was a capability. If the agent does the same work and just does it worse, you wrote a rule and dressed it as a skill.

The grant list belongs on that lever too, and it is a lossy translation of what you meant. An allowlist pointing at `make` targets says something different from one pointing at command strings.

**What this means for you:** run `ls -R .claude/` on your own repo. If the answer is a settings file and nothing else, you own four levers and ship one.

## Two levers persuade. One refuses.

Instructions get read. Path-scoped rules get read. Anything read can be argued with, and an agent will talk itself out of a rule the surrounding code contradicts. The capability lever does not argue either way, because it changes what the agent can reach rather than what it believes.

A hook is not read. It is a predicate that runs inside the turn and returns a refusal. You cannot negotiate with it.

Forty lines of Python mount at both ends of that difference. One is a `PreToolUse` hook that stops the write, and the other is `make gate`, which is what CI runs. One predicate, two mounting points, and no duplicated logic. That shape is why it travels.

The levers that persuade still buy a great deal, on one condition: the rule has to disagree with something. A rule your codebase already follows constrains nothing. The agent would have imitated its way to the same answer, so you cannot tell which one got you there.

So write the rule where rule and code disagree. In the workshop repo, one module derives request authority from the session, and another reads it straight out of the request body. Both patterns are live and both work, so the charter has to pick. Its job is to say which of the two real ones to copy, and that is most retrofits.

Three runs of the same ticket. The bare run changed 3 files, added 49 lines, and passed 1 of 8. The chartered run changed 3 files, added 102 lines, and passed 8 of 8. The bigger diff was the better one, which is worth saying out loud before somebody starts optimizing for lines changed.

**What this means for you:** the rule you would be most upset to see broken belongs on the lever that *refuses*.

## Where your ownership stops

A program can settle eight of the nine checks. Did the diff stay in scope? Was every roll seeded? Was the log appended rather than rewritten? Five more ask questions of that shape, and a script answers each without an opinion.

The ninth is `authority.semantic`, and it asks whether the access check is right *for this feature*. No predicate settles that, so the scorer prints a question mark and waits.

*Both verdicts read the same diff. Only the hook stops a write before it exists. Only the reviewer settles the ninth check.*

On the run that passed all eight, a reviewer sub-agent read the diff and filled in that ninth column:

- The handler gates on `session.is_dungeon_master()`, so it refuses a player asking for a save on their own character. Acceptance criterion 4 allows it.
- Whoever charmed a combatant controls them for the duration. The handler does not consider that, and the ticket is silent on it, so the agent should have raised the question rather than picking an answer.
- The test sets up its request through a module global, so it exercises only the refusal path.

Eight green checks. Three real defects, and one of them a permissions bug.

A green scorecard is not a correct change. It is a change with no mechanically detectable problem, and that distance is where your review attention belongs.

## Where this sits in the software lifecycle

The charter is the part of the constraints that you own outright. It lives in the repo, gets version controlled, and arrives with a clone. Four files change agent behavior on every machine that checks the code out.

Many harness and factory diagrams I have seen has a box labeled quality gate, and that box hides the question: *which of your standards can be a gate at all*? On one ticket in one repository I get eight and one, but I chose rules designed to make the effect visible, so treat that ratio as a demonstration. Yours will be different.

Direction is what I would plan around. As agents write more of the code, the volume past that gate climbs, and the undecidable column does not shrink with it. So when a rule outgrows the charter, name the rung above it and stop, because a markdown file cannot hold what the agent can reach and delete.

Rules are not static. They have a lifecycle and they move from tribal knowledge to the charter to the harness to the factory. *Where* depends on the concern.

## tl;dr

Take one ticket. Run it against your repo with no charter at all, and score the result against checks you wrote beforehand. That run is the incident, and every rule you write afterward should point back at it. Then add the levers one at a time, re-running the same ticket, and name which lever moved which check.

You will find two things. A few of your rules constrain nothing, because the code already agreed with them. And no machine can check at least one rule you care about, which makes it the one worth a human’s time.

**The takeaway:** every constraint that binds a coding agent is a file you own. The only question is which of them you have bothered to write.

COPY & SHARE

Ian Johnson

Ian Johnson is a staff software engineer at Parento and the author of Harness Engineering, a body of work on the machinery and the standards that keep non-deterministic agents inside a band you can ship. He wrote Keystone, the open-source tool this session maps its primitives onto so that nothing taught here is tied to one vendor, and runs Fulcorum, a video course platform for agentic engineering. He works on harness and charter engineering: the engine that runs an agent, and the rules it reads before it writes a line. Based outside Austin, Texas.

READING

·

0%

COPY & SHARE

Ian Johnson

Ian Johnson is a staff software engineer at Parento and the author of Harness Engineering, a body of work on the machinery and the standards that keep non-deterministic agents inside a band you can ship. He wrote Keystone, the open-source tool this session maps its primitives onto so that nothing taught here is tied to one vendor, and runs Fulcorum, a video course platform for agentic engineering. He works on harness and charter engineering: the engine that runs an agent, and the rules it reads before it writes a line. Based outside Austin, Texas.
