#!/usr/bin/env python3
"""Write one quiet text for the AI judge to read.

The program takes no input and makes no network calls. It writes a single
short passage to ``entry.txt`` inside the output directory and nothing else.
The same text is produced on every run.
"""

import os
from pathlib import Path

TEXT = "The kettle has gone quiet. Steam thins above the cup, and the afternoon light stays where it fell across the table. A clock ticks in the next room, unhurried. Nothing in the room is asking anything of you. The tea is warm. You are here. That is enough, for now."

OUTPUT_NAME = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / OUTPUT_NAME).write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
