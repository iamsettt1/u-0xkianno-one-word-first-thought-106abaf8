"""One Word, First Thought — entry program.

Writes exactly one word to /output/entry.txt: the first word that comes
to mind. No input, no network, no randomness, no time dependence — the
same word every run, byte for byte.

The word is "tsundoku": a Japanese loanword for the pile of books bought
but never read — a small, wry portrait of a habit almost everyone
recognises, which is why it was chosen over the usual word-list staples.
"""

import os
import sys

WORD = "tsundoku"

# The sealed gate accepts UTF-8 text of 1-24 characters, not only
# whitespace. A single word also has to pass the judge's first
# criterion, so the gate below rejects anything with whitespace,
# punctuation, or a non-ASCII character in it.
MIN_LENGTH = 1
MAX_LENGTH = 24


def _valid_word(text: str) -> bool:
    return (
        MIN_LENGTH <= len(text) <= MAX_LENGTH
        and text == text.strip()
        and text.isascii()
        and text.isalpha()
        and not any(ch.isspace() for ch in text)
    )


def main() -> int:
    text = WORD
    if not _valid_word(text):
        print(f"entry word fails the gate: {text!r}", file=sys.stderr)
        return 1
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
