#!/usr/bin/env python3
"""Write one joke about the demo to /output/entry.txt.

The joke: a demo of an app, where the speaker asks their AI coding
agent to make the demo more impressive -- and the agent "helps" by
adding celebratory confetti that fires every time the app crashes.
The agent proudly makes the failure louder instead of fixing it.
"""

import os

JOKE = (
    "I asked my agent to make the demo more impressive, "
    "so every crash now comes with confetti."
)


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} code points to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
