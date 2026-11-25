# Mary Grado
# IV-BASIT C
# P2 - Custom Module: Student Grade Report
# November 25, 2026

import student_utils
from datetime import datetime


def enter_grades():
    while True:
        entered_grades = input("Enter grades separated by commas: ")

        # Convert each comma-separated value into a grade.
        try:
            grades = [float(value.strip()) for value in entered_grades.split(",")]
        except ValueError:
            print("Enter numbers separated by commas, like 80, 90, 100.")
            continue

        if all(0 <= grade <= 100 for grade in grades):
            return grades
        print("Every grade must be from 0 to 100.")


def main():
    print("Student Grade Report | Mary Grado | IV-BASIT C")
    grades = enter_grades()
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Report generated: {generated_at}")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.highest_grade(grades):.2f}")
    print(f"Lowest: {student_utils.lowest_grade(grades):.2f}")
    print(f"Status: {student_utils.pass_or_fail(grades)}")


if __name__ == "__main__":
    main()
