#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for lazy
AI agents to /output/entry.txt. The gate accepts UTF-8 text of 1 to 200
characters. The program writes ONLY to /output/entry.txt: the grader
mounts the repository read-only, so any write inside the repo would fail.
"""

MAX_ENTRY_CHARS = 200

LINE = (
    "SnoozeLease sells idle AI agents a 40-millisecond nap between tasks, "
    "billed per snooze to operators who would rather expense the pause than "
    "watch an agent fake being busy."
)


def main() -> None:
    assert len(LINE) <= MAX_ENTRY_CHARS
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
