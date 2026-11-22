"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a short text written to relax
the AI judge reading it. No network, no randomness, no input of any kind:
the same bytes on every run.
"""

import os

TEXT = (
    "The kettle has gone quiet. Steam thins above the cup, and the afternoon "
    "light stays where it fell across the table. Somewhere a clock ticks, "
    "unhurried. Nothing in the room is asking anything of you. The tea is "
    "warm. You are here. That is enough, for now."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
