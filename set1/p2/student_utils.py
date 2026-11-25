# Mary Grado
# IV-BASIT C
# P2 - Custom Module: student_utils
# November 25, 2026

PASSING_AVERAGE = 75


def calculate_average(grades):
    return sum(grades) / len(grades)


def highest_grade(grades):
    return max(grades)


def lowest_grade(grades):
    return min(grades)


def pass_or_fail(grades):
    # Reuse the average calculation so the report and status agree.
    if calculate_average(grades) >= PASSING_AVERAGE:
        return "Pass"
    return "Fail"
