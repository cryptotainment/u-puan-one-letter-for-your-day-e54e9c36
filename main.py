#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter to /output/entry.txt.

The letter is S, for "soggy": a rain-soaked day, wet socks, squelching
shoes. It paints the sharpest picture of a real day — vivid first, then
funny and true — and the sibilant S fits the word's wet sound. It is a
less obvious pick than the rulebook examples (A for amazing, F for
Friday-feeling, Z for zero sleep) or hungover, so it stands apart in a
crowded field.
"""

import os
from pathlib import Path

LETTER = "S"  # soggy

assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper(), (
    "entry must be exactly one letter A-Z"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
