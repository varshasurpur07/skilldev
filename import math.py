import math


def calculate_average(marks):
    """Return the arithmetic mean of marks, each of which must be from 0 to 100."""
    if not marks:
        raise ValueError("marks must not be empty")

    for mark in marks:
        # Booleans are excluded even though Python treats them as integers.
        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            raise ValueError("each mark must be a number")
        if not math.isfinite(mark) or not 0 <= mark <= 100:
            raise ValueError("each mark must be between 0 and 100")

    # sum() reads the list; it does not modify it.
    return sum(marks) / len(marks)


def main():
    students = []

    # Collect one name and one mark for each of three students.
    for number in range(1, 4):
        name = input(f"Enter name for student {number}: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input(f"Enter name for student {number}: ").strip()

        while True:
            try:
                mark = float(input(f"Enter {name}'s mark (0-100): "))
                # Reuse the function's validation for range and numeric validity.
                calculate_average([mark])
                break
            except ValueError as error:
                print(f"Invalid mark: {error}. Please try again.")

        students.append((name, mark))

    marks = [mark for _, mark in students]
    average = calculate_average(marks)

    print("\nStudent Marks Report")
    print("-" * 32)
    print(f"{'Student':<22}{'Mark':>10}")
    print("-" * 32)
    for name, mark in students:
        print(f"{name:<22}{mark:>10.1f}")
    print("-" * 32)
    print(f"{'Class average':<22}{average:>10.2f}")


if __name__ == "__main__":
    main()