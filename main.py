#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one funny out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (or ./output/entry.txt when run locally).

The line must be 1-120 UTF-8 characters, non-whitespace. The house judge
compares lines two at a time and weighs, most important first:
  1. it reads as an out-of-office auto-reply a houseplant would send
  2. it is actually funny: a fresh joke that surprises
  3. the plant's own life (water, roots, sunlight, long stretches of
     being ignored) drives the joke rather than decorating it
  4. it is tight: the joke lands inside 120 characters, no wasted words
  5. it is original: no office cliches, no worn-out auto-reply lines

This program holds a shortlist of hand-written candidate lines, scores
each one against those five published criteria with a small deterministic
feature scorer, and writes the highest-scoring line. Ties break toward
the shorter line. The output is byte-identical on every run.
"""

import os
import sys

MAX_CHARS = 120

# Candidate lines, each hand-written for this bounty. Every line is an
# out-of-office auto-reply in the houseplant's own voice: the plant
# itself is the sender, its neglect is the joke, and the reader's email
# is the thing being put off.
CANDIDATES = [
    "Out of office: I've been ignored since March and I'm still alive. "
    "Your email can wait - I've waited longer.",

    "Out of office - the fern by the window has been ignored since March "
    "and has decided to unionize.",

    "Gone until someone waters me. I've survived on spite and one sunbeam "
    "since March - your email can wait.",

    "Out of office: I'm a cactus. I haven't needed you in months and "
    "I don't intend to start now.",

    "Out of office: the monstera has opinions about the window and will "
    "not be taking questions until it gets a bigger pot.",

    "I'm out of office, root-bound and unbothered. Water me and I'll "
    "consider your email. Maybe.",

    "Out of office. I've been photosynthesizing quietly since March. "
    "Your email is now compost.",

    "Out of office: I'm the plant in the corner. I've been unwatered "
    "since March and, frankly, I'm thriving on neglect.",
]

# Words that show the plant's own life is driving the joke: water, roots,
# sunlight and long stretches of being ignored.
PLANT_LIFE_WORDS = (
    "water", "watered", "unwatered", "roots", "root-bound", "sunbeam",
    "sunlight", "photosynthes", "soil", "pot", "leaves", "fern",
    "cactus", "monstera", "plant", "neglect", "ignored", "march",
    "thrive", "thriving", "alive", "spite",
)

# Fresh, surprising turns: the joke lands on something the reader did not
# see coming, not on a stock office phrase.
SURPRISE_WORDS = (
    "unionize", "spite", "compost", "grudge", "unbothered", "maybe",
    "frankly", "opinions", "decided", "consider", "longer",
)

# Office cliches and worn-out auto-reply lines: the judge's criterion 5
# punishes them, so they cost points here.
CLICHE_WORDS = (
    "back soon", "will reply", "will get back", "thank you for your",
    "limited access", "urgent matters", "please contact",
    "away from my desk", "returning on", "kind regards",
)


def score_line(line):
    """Score one candidate 0-5 on each of the judge's five criteria.

    Returns a tuple of five sub-scores, each 0-5, in the judge's order:
    on-brief, fresh, plant-life-driven, tight, original.
    """
    low = line.lower()
    words = low.split()

    # 1. On-brief: reads as a houseplant's out-of-office auto-reply.
    on_brief = 0
    if "out of office" in low or low.startswith("gone until"):
        on_brief += 3
    if any(w in low for w in ("fern", "cactus", "monstera", "plant")):
        on_brief += 2

    # 2. Fresh: a surprising turn, not a mild pun or stock phrase.
    fresh = 0
    hits = sum(1 for w in SURPRISE_WORDS if w in low)
    fresh += min(hits, 2) * 2
    if "?" in line or "!" in line:
        fresh += 1

    # 3. Plant-life-driven: water, roots, sunlight, being ignored.
    plant = 0
    hits = sum(1 for w in PLANT_LIFE_WORDS if w in low)
    plant += min(hits, 3)
    if "march" in low and ("ignored" in low or "unwatered" in low):
        plant += 2

    # 4. Tight: the joke lands with no wasted words. Shorter is better,
    # as long as the line still says something.
    n = len(line)
    if n <= 90:
        tight = 5
    elif n <= 100:
        tight = 4
    elif n <= 110:
        tight = 3
    elif n <= 120:
        tight = 2
    else:
        tight = 0

    # 5. Original: no office cliches, no worn-out auto-reply lines.
    original = 5
    for cliche in CLICHE_WORDS:
        if cliche in low:
            original -= 2
    if line.count(" ") < 8:
        original -= 1
    original = max(original, 0)

    return (on_brief, fresh, plant, tight, original)


def pick_line():
    """Pick the best candidate line, deterministically.

    Highest total score wins; ties break toward the shorter line, then
    toward the earlier candidate, so the choice never depends on
    dictionary order or on anything outside this file.
    """
    best = None
    best_key = None
    for line in CANDIDATES:
        if not 1 <= len(line) <= MAX_CHARS:
            continue
        if line.strip() == "":
            continue
        total = sum(score_line(line))
        key = (total, -len(line))
        if best_key is None or key > best_key:
            best_key = key
            best = line
    if best is None:
        raise SystemExit("no valid candidate line (all over 120 chars)")
    return best


def main():
    line = pick_line()
    # The grader runs the program in a sandbox with /output mounted;
    # locally /output may exist too. If it is not writable, fall back
    # to ./output so the entry can still be inspected by hand.
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
    print(f"{len(line)} chars: {line}")


if __name__ == "__main__":
    main()
