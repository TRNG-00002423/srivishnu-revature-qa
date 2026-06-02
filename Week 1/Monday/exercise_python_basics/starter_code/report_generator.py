"""
Formatted Report Generator
Displays test results in a neatly aligned table.
"""

# --- Test Results Data ---
# (test_name, duration_ms, status)
tests = [
    ("test_login",    1200, "PASS"),
    ("test_search",    850, "PASS"),
    ("test_checkout", 2300, "FAIL"),
    ("test_profile",   450, "PASS"),
    ("test_logout",    180, "PASS"),
]

# --- Calculations ---
total_duration = sum(t[1] for t in tests)
passed_count   = sum(1 for t in tests if t[2] == "PASS")
total_count    = len(tests)

# --- Table Borders ---
top_border    = "┌──────────────────┬────────────┬──────────┐"
header_sep    = "├──────────────────┼────────────┼──────────┤"
bottom_border = "└──────────────────┴────────────┴──────────┘"

# --- Print Table ---
print(top_border)
print(f"│ {'Test Name':<16} │ {'Duration':<10} │ {'Status':<8} │")
print(header_sep)

for name, duration, status in tests:
    status_icon = "✅ PASS" if status == "PASS" else "❌ FAIL"
    dur_str = f"{duration:>7,} ms"
    print(f"│ {name:<16} │ {dur_str:<10} │ {status_icon:<8} │")

print(header_sep)

# --- Totals Row ---
total_str  = f"{total_duration:>7,} ms"
verdict    = f"{passed_count}/{total_count} Pass"
print(f"│ {'TOTAL':<16} │ {total_str:<10} │ {verdict:<8} │")

print(bottom_border)
