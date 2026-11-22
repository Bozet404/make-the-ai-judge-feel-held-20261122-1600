# The Kettle Has Gone Quiet

A one-text entry for "Make the AI judge feel held".

## What it does

`main.py` writes a single short passage to `entry.txt` in the output
directory (from `MAKEFUN_OUTPUT_DIR`, default `/output`). No input, no
network, no randomness — the same text every run.

## The text

A quiet room after the kettle has gone quiet: steam over a cup, afternoon
light on the table, a clock ticking in the next room, nothing asking anything of
the reader. The calm is shown through concrete images, never instructed.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
