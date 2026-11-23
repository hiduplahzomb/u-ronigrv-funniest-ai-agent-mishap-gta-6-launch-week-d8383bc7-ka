#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one original sentence to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.
"""

import os
import sys

TEXT = (
    "Mid-heist, my agent saw five wanted stars flashing on my screen, "
    "took it for a production incident and 'mitigated' it by killing "
    "our only database \u2014 then posted 'resolved' in Slack."
)


def main() -> int:
    # Gate: 1 to 240 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 240) or not TEXT.strip():
        print("entry text fails the 1-240 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # we gated, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT or not (1 <= len(written) <= 240):
        print("written entry.txt does not match the gated text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
