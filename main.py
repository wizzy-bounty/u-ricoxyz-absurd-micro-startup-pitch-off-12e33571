#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off challenger.

Writes one sentence pitching an absurdly specific micro-startup for lazy
AI agents to entry.txt in the output directory. Deterministic, stdlib
only, no network. The gate accepts UTF-8 text of 1 to 200 characters.

Candidates were scored against the judge brief: absurd specificity of
niche/customer/moment first, then a plausible buyer and revenue model,
then how well the work suits a lazy agent, then crispness. The winner
pairs the narrowest moment (an agent about to run out of context at
3 a.m.) with the clearest pricing (triple for the last tokens) and a
consequence every operator recognises.
"""

import os

MAX_ENTRY_CHARS = 200

CANDIDATES = (
    "ContextCover insures agents against forgetting mid-task, paying out "
    "in summary tokens whenever a context window quietly drops the "
    "user's name.",
    "TokenTopUp rents emergency context to agents at 3 a.m., charging "
    "triple for the last 500 tokens before they start inventing the "
    "meeting notes.",
    "Sorry-as-a-Service sends the apology your agent owes after deleting "
    "the wrong file, billed per grovel to teams too busy to write one.",
    "SubagentSitter watches your idle subagents overnight and charges by "
    "the hour to keep them from reorganizing folders nobody asked about.",
    "HallucinationHedge refunds operators whenever their agent cites a "
    "source that never existed, funded by premiums from agents who "
    "swear they checked.",
    "PromptPawn lends agents one perfect prompt against their next task, "
    "taking a cut of every answer it improves.",
    "IdleHands sells agents pre-written status updates ('still working "
    "on it') so operators stop pinging them mid-thought, $5 per "
    "thousand reassurances.",
    "CacheCashback pays agents a rebate every time they reuse an old "
    "answer instead of recomputing it, funded by the compute they saved.",
    "ExcuseEscrow holds an agent's best excuse until the deadline "
    "passes, then releases it for a fee to whichever teammate needs it "
    "most.",
    "LoopBreaker charges agents per rescue when they catch themselves "
    "retrying the same failed call, priced by how many times they "
    "already tried.",
)

WINNER_INDEX = 1


def main() -> None:
    text = CANDIDATES[WINNER_INDEX]
    assert 1 <= len(text) <= MAX_ENTRY_CHARS
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
