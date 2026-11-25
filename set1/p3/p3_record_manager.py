# Mary Grado
# IV-BASIT C
# P3 - Student Record Manager
# November 25, 2026


def add_student(students, name_keys):
    name = input("Student name to add: ").strip()
    if not name:
        print("Enter a student name.")
        return

    # The set stores case-folded names so capitalization cannot hide duplicates.
    name_key = name.casefold()
    if name_key in name_keys:
        print(f"{name} is already on the list.")
        return

    students.append(name)
    name_keys.add(name_key)
    print(f"Added: {name}")


def remove_student(students, name_keys):
    name_key = input("Full name to remove: ").strip().casefold()
    for index, name in enumerate(students):
        if name.casefold() == name_key:
            students.pop(index)
            name_keys.remove(name_key)
            print(f"Removed: {name}")
            return

    print("Student not found.")


def search_students(students):
    query = input("Enter part of a name: ").strip().casefold()
    if not query:
        print("Enter at least one character to search.")
        return

    matches = [name for name in students if query in name.casefold()]
    if not matches:
        print("No matching students.")
        return

    print("Search results:")
    for name in sorted(matches, key=str.casefold):
        print(f"- {name}")


def display_students(students):
    print("Student list:")
    for number, name in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(students)}")


def main():
    students = []
    name_keys = set()

    while True:
        print("\nStudent Record Manager | Mary Grado | IV-BASIT C")
        print("1. Add | 2. Remove | 3. Search | 4. Display all | 5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students, name_keys)
        elif choice == "2":
            remove_student(students, name_keys)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()

# A list keeps its items in order and can contain duplicates.
# A set stores unique items and does not keep them in a fixed order.
# The students list keeps names with their original capitalization for display.
# The name_keys set stores each case-folded name so I can check for duplicates.
