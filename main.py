#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes exactly one horror story, in exactly two sentences, to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

STORY = (
    "Last night my phone recorded a three-minute voice memo while I slept. "
    "It was me whispering my home address, over and over, in a voice that "
    "kept getting closer to the microphone."
)


def main() -> None:
    # Gate: exactly two sentences, at most 400 characters.
    assert STORY.count(".") == 2, "entry must be exactly two sentences"
    assert 1 <= len(STORY) <= 400, "entry must be 1-400 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
