"""The Funniest One-Line Out-of-Office Reply.

Writes a single one-line out-of-office email auto-reply to /output/entry.txt.
"""

import os

ENTRY = "I'm out of office: my inbox is now managed by my houseplant. Same response time, worse attitude."

# A one-line out-of-office reply must stay a single short line.
MAX_ENTRY_CHARS = 160


def validate_entry(line: str) -> None:
    """Reject lines that are empty, multi-line, or too long to read at a glance."""
    if not line or "\n" in line or len(line) > MAX_ENTRY_CHARS:
        raise ValueError("entry must be one line of 1-160 characters")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
