"""The Excuse That Almost Works.

Writes the single line a gamer texts the boss to skip work on GTA 6
launch week to /output/entry.txt.

The line: a broken lift in a 14-storey building. It is the kind of
boring, specific, real-world detail a tired manager has heard before
and almost believes — and the punch lands in the last six words, where
the texter is still working, just from the lobby.
"""

import os

EXCUSE = "Sorry, lift's broken and I live on the 14th floor, I'll be working from the lobby."


def validate(text):
    """Check the excuse against the bounty gate before writing it.

    The gate wants UTF-8 text of 1 to 140 characters, not only white
    space, and the task caps the line at 20 words. A line that breaks
    any of those rules is never judged, so refuse it loudly here
    instead of writing a dead entry.
    """
    if not text or not text.strip():
        raise ValueError("excuse must not be empty or only white space")
    if len(text) > 140:
        raise ValueError(f"excuse is {len(text)} chars, over the 140 limit")
    words = text.split()
    if len(words) > 20:
        raise ValueError(f"excuse is {len(words)} words, over the 20 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")


def main():
    validate(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
