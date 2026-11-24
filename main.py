#!/usr/bin/env python3
"""One-sentence startup pitch for the make.fun competition
'u-po-pu-ridiculous-at-first-glance-real-by-the-second'.

Deterministic, no network, no input: writes the pitch to /output/entry.txt.
"""

import os

PITCH = (
    "Rent-a-dog mould inspections: trained sniffer dogs check rentals for "
    "hidden mould before tenants move in \u2014 silly until you learn mould "
    "claims cost landlords billions a year."
)


def main() -> None:
    assert len(PITCH) <= 200, f"pitch is {len(PITCH)} chars, limit is 200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")
    print(f"Wrote {len(PITCH)}-character pitch to /output/entry.txt")


if __name__ == "__main__":
    main()
