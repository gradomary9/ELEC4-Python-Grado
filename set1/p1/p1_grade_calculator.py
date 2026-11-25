# Mary Grado
# IV-BASIT C
# P1 - Student Grade Calculator
# November 25, 2026

PASSING_AVERAGE = 75


def enter_grades():
    while True:
        try:
            grade_count = int(input("How many grades will you enter? "))
        except ValueError:
            print("Enter a whole number greater than zero.")
            continue

        if grade_count > 0:
            break
        print("Enter a whole number greater than zero.")

    grades = []
    for grade_number in range(1, grade_count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {grade_number}: "))
            except ValueError:
                print("Enter a number from 0 to 100.")
                continue

            # Keep asking for the same grade until the number is valid.
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            print("Enter a number from 0 to 100.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def highest_grade(grades):
    return max(grades)


def lowest_grade(grades):
    return min(grades)


def pass_or_fail(grades):
    if calculate_average(grades) >= PASSING_AVERAGE:
        return "Pass"
    return "Fail"


def main():
    grades = []
    print("Student Grade Calculator | Mary Grado | IV-BASIT C")

    while True:
        print("\n1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            if not grades:
                print("Enter grades first.")
                continue

            print(f"Average: {calculate_average(grades):.2f}")
            print(f"Highest: {highest_grade(grades):.2f}")
            print(f"Lowest: {lowest_grade(grades):.2f}")
            print(f"Status: {pass_or_fail(grades)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

# A local variable belongs to the function where it is defined.
# For example, grade_number only exists inside enter_grades().
# PASSING_AVERAGE is global because it is defined outside the functions.
# The pass_or_fail() function reads that global constant to check the average.
