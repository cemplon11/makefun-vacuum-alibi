#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse for missing a spot to
/output/entry.txt. Pure Python standard library only. Deterministic:
the same line on every run.
"""

import os

LINE = (
    "Dust detected under the sofa at 04:12. "
    "By 04:13, we had reached an understanding. I left."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
