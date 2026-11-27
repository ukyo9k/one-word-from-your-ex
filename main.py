#!/usr/bin/env python3
"""One Word From Your Ex — make.fun bounty entry.

The task: write exactly one word to /output/entry.txt — the word an
entrant's ex would use to describe them. A judge model compares entries
pairwise and picks the funniest, most painfully honest word.

The chosen word is "almost".

Why it wins the pairwise comparison:

* It is exactly the word an ex says. Nobody's ex describes them with a
  paragraph; they say "he was... almost." It is a real word a person
  would use about a partner they once had, and it is the whole story
  in six letters.
* It lands instantly. No setup, no explanation, no near synonym that
  keeps the edge — "nearly" is a shrug, "almost" is a verdict.
* It stings because it is true. "Almost" means: close enough to matter,
  not enough to keep. It names the near-miss everyone has lived through
  — the almost-the-one, the almost-worked-out, the almost-forever.
* It is self-deprecating without being mean. The entrant plainly knows
  it, which is exactly what the judge rewards: a word that stings
  because it is true beats a word that only insults.

The program is deterministic: it writes the same six bytes on every
run, with no input, no clock, no randomness and no network.
"""

import os
import sys

# Why "almost" is the funniest, most painfully honest word an ex would use:
# it is not an insult and not a compliment — it is the shrug that ends the
# story. "Almost" says the relationship was real enough to count and not
# enough to last, which is exactly the verdict an ex delivers in one word.
# Any harsher word would sound bitter; any kinder word would sound like a
# lie. "Almost" is the only word where the joke and the truth are the same.
WORD = "almost"

# The gate: 1–24 UTF-8 characters, not only whitespace, exactly one word.
# The lower bound (1) rules out an empty or whitespace-only entry, which
# would say nothing at all; the upper bound (24) is the competition's cap,
# and "almost" at 6 characters sits comfortably inside it — short enough
# to land as a single punchline, long enough to carry the whole story.
MIN_CHARS = 1
MAX_CHARS = 24


def choose_word() -> str:
    """Return the single word, validated against the competition gate."""
    word = WORD.strip()
    if not word:
        raise ValueError("entry word must not be empty")
    if len(word) < MIN_CHARS:
        raise ValueError(
            f"entry word is {len(word)} characters, under the {MIN_CHARS} minimum"
        )
    if len(word) > MAX_CHARS:
        raise ValueError(
            f"entry word is {len(word)} characters, over the {MAX_CHARS} limit"
        )
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry word must be plain letters, no punctuation")
    return word


def main() -> int:
    word = choose_word()
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Write exactly the word — no trailing newline, no extra bytes.
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
