"""The Funniest One-Line Out-of-Office Reply.

Writes a single one-line out-of-office email auto-reply to /output/entry.txt.
"""

import os

ENTRY = "I'm out of office: my inbox is now managed by my houseplant. Same response time, worse attitude."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
