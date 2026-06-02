"""
Test Results Analysis
Loads test_data.csv and performs analysis using pandas.
"""

import os
import pandas as pd

# Paths 
BASE_DIR   = os.path.dirname(__file__)
CSV_PATH   = os.path.join(BASE_DIR, "test_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load CSV 
df = pd.read_csv(CSV_PATH)

print("═" * 40)
print("  Test Results Analysis")
print("═" * 40)

# Basic Info
print(f"\n  Total Tests:    {len(df)}")
print(f"\n  Column names & dtypes:")
for col, dtype in zip(df.columns, df.dtypes):
    print(f"    {col:<16} {dtype}")

print(f"\n  First 5 rows:")
print(df.head().to_string(index=False))

# Aggregate Metrics
pass_rate   = (df["status"] == "pass").mean() * 100
avg_dur_ms  = df["duration_ms"].mean()
avg_dur_s   = avg_dur_ms / 1000

slowest = df.loc[df["duration_ms"].idxmax()]
fastest = df.loc[df["duration_ms"].idxmin()]

print(f"\n  Pass Rate:      {pass_rate:.1f}%")
print(f"  Avg Duration:   {avg_dur_ms:,.0f}ms ({avg_dur_s:.2f}s)")
print(f"  Slowest:        {slowest['test_name']} ({slowest['duration_ms']:,}ms)")
print(f"  Fastest:        {fastest['test_name']} ({fastest['duration_ms']:,}ms)")

# Group by Module
print(f"\n  ── By Module ──")
print(f"  {'Module':<12} {'Tests':>6}  {'Pass Rate':>10}  {'Avg Duration':>12}")

grouped = df.groupby("module")
module_stats = grouped.agg(
    tests       = ("test_name",   "count"),
    pass_rate   = ("status",      lambda x: (x == "pass").mean() * 100),
    avg_duration= ("duration_ms", "mean"),
).sort_index()

for module, row in module_stats.iterrows():
    print(f"  {module:<12} {int(row['tests']):>6}     {row['pass_rate']:>6.1f}%  {row['avg_duration']:>9,.0f}ms")

# Filter: Failed Tests
print(f"\n  ── Failed Tests ──")
failed = df[df["status"] == "fail"][["test_name", "module", "duration_ms"]]
for _, row in failed.iterrows():
    print(f"  {row['test_name']:<24} {row['module']:<10} {row['duration_ms']:>5,}ms")

# Filter: Tests slower than 1500ms
print(f"\n  ── Tests Slower than 1,500ms ──")
slow = df[df["duration_ms"] > 1500][["test_name", "module", "duration_ms"]]
for _, row in slow.iterrows():
    print(f"  {row['test_name']:<24} {row['module']:<10} {row['duration_ms']:>5,}ms")

# Filter: Auth module
print(f"\n  ── Auth Module Tests ──")
auth = df[df["module"] == "auth"][["test_name", "duration_ms", "status"]]
for _, row in auth.iterrows():
    icon = "✅" if row["status"] == "pass" else "❌"
    print(f"  {icon} {row['test_name']:<24} {row['duration_ms']:>5,}ms")

# Computed Column
df["duration_sec"] = df["duration_ms"] / 1000

# Sort and Export
df_sorted = df.sort_values("duration_ms", ascending=False)
output_path = os.path.join(OUTPUT_DIR, "results_sorted.csv")
df_sorted.to_csv(output_path, index=False)

print(f"\n  ── Exported ──")
print(f"  Sorted results saved to: output/results_sorted.csv")
print("\n" + "═" * 40)
