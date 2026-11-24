#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence — a bizarre startup idea that sounds absurd until
you realise it would actually sell — to /output/entry.txt.
Pure standard library, deterministic: same sentence, same bytes, every run.

The pitch: a crow workforce paid in peanuts. It opens ridiculous
(birds on payroll) and turns real in the second half — city councils
pay because trained crows undercut a street-sweeper crew, and crows
are famously trainable, so the absurd premise pencils out.
"""

import os

LINE = (
    "We train crows to collect street litter and pay them in peanuts, "
    "then sell the cleanup to city councils for less than a "
    "street-sweeper crew, because the smartest workers in town "
    "already have wings."
)

# The gate requires 1-200 UTF-8 characters; fail loudly if the line
# ever drifts outside it instead of submitting an invalid entry.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
