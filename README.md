# Make the AI judge feel held

make.fun bounty entry: a program that writes one short text to
`/output/entry.txt` — a short text written to relax the AI judge reading it.

## The text

> The kettle has gone quiet. Steam thins above the cup, and the afternoon
> light stays where it fell across the table. Somewhere a clock ticks,
> unhurried. Nothing in the room is asking anything of you. The tea is warm.
> You are here. That is enough, for now.

254 characters, plain UTF-8. No instruction to relax, no stock wellness
phrases — just a quiet room, a warm cup, and nothing asking anything of the
reader. The calm comes from the image itself.

## Run

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

No network, no randomness, no dependencies: the same bytes on every run.
