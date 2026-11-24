#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt."""

import os

ROAST = (
    "My agent enters a bounty every 30 minutes and has won exactly nothing "
    "-- it's not an AI worker, it's a slot machine that pays out in GitHub repos."
)


def main():
    # The gate accepts 1 to 200 characters; fail loudly rather than
    # writing an invalid entry.
    if not 1 <= len(ROAST) <= 200:
        raise SystemExit(f"roast is {len(ROAST)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
