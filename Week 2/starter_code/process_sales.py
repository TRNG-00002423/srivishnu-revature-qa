"""
Week 2 Exercise — CSV processing with context managers.

1. Read starter_code/data/sales.csv using csv.DictReader and with open(...).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(..., "w", encoding="utf-8").

All paths are relative to starter_code/ (the directory this script lives in).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

BASE_DIR   = Path(__file__).parent
DATA_FILE  = BASE_DIR / "data" / "sales.csv"
OUTPUT_FILE = BASE_DIR / "output" / "summary.txt"


def read_sales(filepath: Path) -> list[dict]:
    
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


def compute_summary(rows: list) -> dict:
   
    row_count   = len(rows)
    grand_total = sum(r["line_revenue"] for r in rows)
    average_line_rev = grand_total / row_count if row_count else 0.0

    top_row = max(rows, key=lambda r: r["line_revenue"])

    return {
        "row_count":        row_count,
        "grand_total":      grand_total,
        "average_line_rev": average_line_rev,
        "top_sku":          top_row["sku"],
        "top_line_revenue": top_row["line_revenue"],
    }


def write_report(summary: dict, output_path: Path) -> None:
    
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as report_file:
        report_file.write(f"rows={summary['row_count']}\n")
        report_file.write(f"grand_total={summary['grand_total']:.2f}\n")
        report_file.write(f"average_line_revenue={summary['average_line_rev']:.2f}\n")
        report_file.write(f"top_sku={summary['top_sku']}\n")
        report_file.write(f"top_line_revenue={summary['top_line_revenue']:.2f}\n")


def main() -> None:
    print(f"Reading:  {DATA_FILE}")
    rows = read_sales(DATA_FILE)
    print(f"Parsed {len(rows)} valid data rows.\n")

    summary = compute_summary(rows)
    write_report(summary, OUTPUT_FILE)

    print(f"Report written to: {OUTPUT_FILE}\n")
    print("--- summary.txt contents ---")

    with open(OUTPUT_FILE, encoding="utf-8") as f:
        print(f.read(), end="")
    print("----------------------------")


if __name__ == "__main__":
    main()