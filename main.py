#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

make.fun competition: One-Line Office Jokes
(u-markk-st-one-line-office-jokes-a51f2bcc).

Pure stdlib, deterministic, no network, no environment reads.
The grader runs this program twice in separate sandboxes; both runs
must write the exact same bytes.
"""

import os

ENTRY = "My manager scheduled a meeting about why we have too many meetings, and it ran over into a follow-up."


def main():
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
