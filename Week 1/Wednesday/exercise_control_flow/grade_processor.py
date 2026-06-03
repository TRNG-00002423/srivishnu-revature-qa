"""
Task 4: Grade Processor
Processes a list of student scores, assigns grades, and prints statistics.
"""


def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def process_grades(scores):
    valid_scores = []
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    print("=" * 40)
    print("       STUDENT GRADE REPORT")
    print("=" * 40)

    for i, score in enumerate(scores):
        # Sentinel value — stop processing
        if score == -999:
            print(f"\n[Index {i}] Sentinel -999 encountered. Stopping.\n")
            break

        # Skip invalid (negative) scores
        if score < 0:
            print(f"[Index {i}] Score {score} is invalid — skipping.")
            continue

        grade = get_letter_grade(score)
        valid_scores.append(score)
        distribution[grade] += 1
        print(f"[Index {i}] Score: {score:>3}  →  Grade: {grade}")

    # Summary statistics
    if valid_scores:
        average = sum(valid_scores) / len(valid_scores)
        highest = max(valid_scores)
        lowest = min(valid_scores)

        print("\n" + "=" * 40)
        print("           SUMMARY")
        print("=" * 40)
        print(f"Students processed : {len(valid_scores)}")
        print(f"Class average      : {average:.2f}")
        print(f"Highest score      : {highest}")
        print(f"Lowest score       : {lowest}")
        print("\nGrade Distribution:")
        for grade, count in distribution.items():
            print(f"  {grade}: {count}")
    else:
        print("No valid scores to process.")


if __name__ == "__main__":
    scores = [88, 92, 75, -1, 63, 95, 81, 70, -5, 55, 100, 78, -999, 90, 85]
    process_grades(scores)
