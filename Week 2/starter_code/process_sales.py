"""
Week 2 Exercise — CSV processing with context managers.

TODO:
1. Read starter_code/data/sales.csv using csv.DictReader and with open(...).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(..., "w", encoding="utf-8").
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "sales.csv"


def read_sales(filepath: Path) -> list[dict]:
    """
    Open the CSV with a context manager and return a list of parsed rows.

    - encoding="utf-8"  : explicit, portable across platforms
    - newline=""        : required by the csv module so it handles its own newlines

    Each valid row becomes a dict:
        {"sku": str, "units": int, "unit_price": float, "line_revenue": float}

    Malformed rows are skipped and reported to stderr (graceful degradation).
    """
    parsed_rows = []
    bad_row_count = 0

    with open(filepath, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row_number, raw_row in enumerate(reader, start=2):
            try:
                sku        = raw_row["sku"].strip()
                units      = int(raw_row["units"].strip())         
                unit_price = float(raw_row["unit_price"].strip()) 

                if not sku:
                    raise ValueError("SKU is empty")

                parsed_rows.append({
                    "sku":          sku,
                    "units":        units,
                    "unit_price":   unit_price,
                    "line_revenue": units * unit_price,
                })

            except (KeyError, ValueError) as exc:
                
                print(
                    f"[WARN] Skipping malformed row {row_number}: {dict(raw_row)} — {exc}",
                    file=sys.stderr,
                )
                bad_row_count += 1

    if bad_row_count:
        print(f"[WARN] Total malformed rows skipped: {bad_row_count}", file=sys.stderr)

    return parsed_rows


def main() -> None:
    print(f"Reading: {DATA_FILE}\n")

    rows = read_sales(DATA_FILE)

    print(f"Valid data rows parsed: {len(rows)}\n")
    print(f"{'SKU':<12} {'Units':>6} {'Unit Price':>12} {'Line Revenue':>14}")
    print("-" * 48)
    for row in rows:
        print(
            f"{row['sku']:<12} {row['units']:>6} "
            f"{row['unit_price']:>12.2f} {row['line_revenue']:>14.2f}"
        )

    print("\nTask 1 complete — data is read, typed, and ready for aggregation in Task 2.")


if __name__ == "__main__":
    main()