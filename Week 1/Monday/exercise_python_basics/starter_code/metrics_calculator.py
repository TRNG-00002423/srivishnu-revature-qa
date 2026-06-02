"""
QA Test Metrics Calculator
Fill in the code below where you see # TODO comments.
"""

def main():
    print("═" * 40)
    print("  QA Test Metrics Calculator")
    print("═" * 40)

    # TODO 1: Get user input
    total_tests = int(input("\nEnter total test cases: "))
    passed_tests = int(input("Enter passed tests: "))
    total_time = float(input("Enter total execution time (seconds): "))

    # TODO 2: Calculate metrics
    failed_tests = total_tests - passed_tests
    pass_rate = (passed_tests / total_tests) * 100
    fail_rate = (failed_tests / total_tests) * 100
    avg_time = total_time / total_tests

    # TODO 3: Print the results summary using f-strings
    print()
    print("─" * 40)
    print("  Test Results Summary")
    print("─" * 40)
    print(f"  Total Tests:   {total_tests:>6}")
    print(f"  Passed:        {passed_tests:>6}")
    print(f"  Failed:        {failed_tests:>6}")
    print(f"  Pass Rate:     {pass_rate:>6.1f}%")
    print(f"  Fail Rate:     {fail_rate:>6.1f}%")
    print(f"  Avg Time/Test: {avg_time:>6.2f}s")
    print(f"  Total Time:    {total_time:>6.2f}s")

    # TODO 4: Determine and print the verdict
    if pass_rate >= 95:
        verdict = "✅ RELEASE APPROVED"
    elif pass_rate >= 80:
        verdict = "⚠️ CONDITIONAL RELEASE — review failures"
    else:
        verdict = "❌ RELEASE BLOCKED — too many failures"

    print(f"\n  Verdict: {verdict}")
    print("═" * 40)


if __name__ == "__main__":
    main()