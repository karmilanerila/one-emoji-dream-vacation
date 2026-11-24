#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes a single emoji to the grader's output file: a beach with an
umbrella, the universal postcard of a dream holiday -- sand, sea and
shade at a glance, no words needed.
"""

import os

EMOJI = "\U0001F3D6"  # BEACH WITH UMBRELLA


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = EMOJI.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Read it back: the gate wants UTF-8 text of 1 to 8 characters,
    # so refuse to finish quietly if the file is not exactly our emoji.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not hold the chosen emoji"
    assert len(written.decode("utf-8")) == 1, "entry is not one character"


if __name__ == "__main__":
    main()
