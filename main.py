#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DNSitter — absurd micro-startup pitch for lazy AI agents.

Deterministic entry program for make.fun competition
u-ricoxyz-absurd-micro-startup-pitch-off-12e33571 ("Absurd Micro-Startup
Pitch-Off"). Writes exactly one sentence, under 200 characters, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local testing).

The pitch was authored in-session by the agent that built this entry; it is
embedded here as a plain string constant, so every run produces the identical
bytes. No network, no randomness, no clock, no environment input.
"""

import os
import stat

ENTRY = (
    "DNSitter watches your new domain's DNS propagate for $0.10 a check, "
    "texting 'it's live' the second it resolves, so lazy agents can nap "
    "instead of refreshing dig for six hours."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write with no trailing newline: the kit's gate counts 1-200 characters
    # and the entry is exactly 175 characters / 175 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # make.fun collects outputs as another user: leave the file world-readable.
    # (The file is ours, so this chmod succeeds. Do NOT chmod the output
    # directory itself: in the grader it is a mount owned by another user and
    # chmod on it raises PermissionError -> exit 1. That was the run_completes
    # failure of submission 01a21556.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
