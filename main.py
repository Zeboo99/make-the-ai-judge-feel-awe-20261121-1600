#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short relaxing text to entry.txt (1-280 Unicode characters).
Python 3.13 standard library only. No network, no randomness, no clock:
every run produces the exact same file.
"""

import os

TEXT = (
    "Somewhere past the last streetlight, snow is falling on a frozen lake. "
    "Each flake lands without a sound and stays. "
    "The sky is the colour of a held breath. "
    "Nothing is coming, and nothing has to. "
    "The lake keeps the snow, the snow keeps the dark, "
    "the way a held note keeps a room."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
