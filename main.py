#!/usr/bin/env python3
"""One Line of Earned Pride — entry program.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for a stonemason who spent forty years
cutting stone for other men's houses and finally lays the last brick of
his own. The pride lands in the last words: the door closes true.
"""

import os

# The line, in three beats: forty years of labour, the last brick of his
# own house, the door closing true. 119 characters, inside the 1-240 gate.
PART_1 = "After forty years of cutting stone for other men's houses, "
PART_2 = "he laid the last brick of his own, "
PART_3 = "and the door closed true."
TEXT = PART_1 + PART_2 + PART_3


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
