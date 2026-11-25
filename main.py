#!/usr/bin/env python3
"""resttigue — Invent a Word We Need (make.fun).

One invented English word, defined in a single line. The program writes
that line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
which is the whole judged entry: 1 to 140 characters of UTF-8 text.

The word
-------
resttigue (noun, pronounced REST-tee-g): the exhaustion you feel after a
whole day of doing absolutely nothing.

Why English needs it: the language has no word for being tired *because*
you rested. Tired after a marathon, yes. Tired after a day on the sofa
doing nothing at all, somehow more tired than after a busy day — that
feeling had no name until now. The blend is transparent (rest + fatigue),
it says itself out loud, and it spells the way it sounds.
"""

from __future__ import annotations

import os
import sys

WORD = "resttigue"
PART_OF_SPEECH = "n."
PRONUNCIATION = "REST-tee-g"
DEFINITION = "the exhaustion you feel after a whole day of doing absolutely nothing"

ENTRY = f"{WORD} ({PART_OF_SPEECH}, {PRONUNCIATION}): {DEFINITION}."

MAX_CHARS = 140


def build_entry() -> str:
    """Compose the single-line dictionary entry and check it fits the gate."""
    entry = ENTRY
    if not entry.strip():
        raise ValueError("entry is empty")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    entry.encode("utf-8")  # the gate requires UTF-8 text
    return entry


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = build_entry()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(entry)
    # Read it back: the grader runs the program twice and the two runs
    # must agree, so a partial or mangled write must fail loudly here.
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        if handle.read() != entry:
            raise ValueError("entry.txt does not match the built entry")
    print(entry)
    print(f"({len(entry)} characters, {len(entry.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
