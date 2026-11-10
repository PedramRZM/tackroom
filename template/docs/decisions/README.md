# Decisions

One short file per decision that is hard to reverse or that an agent would otherwise propose
again: architecture, the data model, the language and framework, hosting, an integration, a
public name. `NNNN-short-title.md`, numbered in order, half a page at most.

Write the record before the work that depends on it, and have the owner review it. Record the
"no" as well as the "yes": a rejected approach that is not written down gets re-proposed by the
next session. A record is not edited after it is accepted; a later one replaces it and says so.

    # NNNN. Title

    Date: YYYY-MM-DD   Status: proposed | accepted | replaced by NNNN

    ## Context
    What forced a choice, and the constraints that matter.

    ## Decision
    What we will do, stated plainly, including what we will not do.

    ## Alternatives rejected
    Each with its effort and the reason it lost, in a line or two.

    ## Consequences
    What becomes easier, what becomes harder, what we are now committed to.

    ## Revisit if
    The concrete conditions that would change the answer.

Easy-to-reverse choices do not need a record. Make them and move on.
