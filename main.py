#!/usr/bin/env python3
"""Real-Life Patch Notes entry: writes one patch-note line to /output/entry.txt.

Deterministic, standard library only. No input, no network, no randomness:
the same note is written on every run.
"""

import os

PATCH_NOTE = (
    "v2.4.1: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 at 3 a.m. Nightly builds now skip the archive."
)

MAX_CHARS = 160


def main() -> None:
    note = PATCH_NOTE.strip()
    assert note, "patch note must not be empty"
    assert "\n" not in note, "patch note must be a single line"
    assert len(note) <= MAX_CHARS, "patch note is %d chars, over %d" % (
        len(note),
        MAX_CHARS,
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(note)


if __name__ == "__main__":
    main()
