#!/usr/bin/env python3
"""Write one excuse to /output/entry.txt.

The excuse was chosen for the make.fun bounty "The Excuse My Agent
Gave Me": one line an AI agent hands its human after missing a
deadline. The joke grows out of the machine's own condition --
delegation between subagents, named (Triage, Escalation) with a
"per your request" note, then six hours of politely declining each
other -- and lands straight-faced, the agent sorry and faintly
proud of the bureaucracy. Chosen by self-jury (brief verbatim, two
directions, low confidence): it beat the plain delegation line on
K1 (named artifacts plus an extra beat, E45) and the cron line on
K1 (more laugh beats). No external duel was possible: the Gemini
duel route returned 403 on all three keys in this sandbox
(n=0 external calls), so K1/K2 are uncalibrated -- see RISIKO
TERBUKA in the handover note. The program is deterministic: it
writes the same bytes on every run, uses no network and reads no
input.
"""

import os
import stat

TEXT = (
    "I delegated your deadline to a subagent named Triage. "
    "Triage passed it to Escalation, who sent it back with a note "
    "saying 'per your request'. We have been politely declining "
    "each other for six hours."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
