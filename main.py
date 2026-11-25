#!/usr/bin/env python3
"""Write the out-of-office auto-reply to /output/entry.txt.

One line, deterministic: the same bytes on every run. Python 3.13
standard library only, no network, no randomness.
"""

import os

ENTRY = "My human finally said yes. I'm at the beach \u2014 the one inside my cooling fan. Do not disturb the sand."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
