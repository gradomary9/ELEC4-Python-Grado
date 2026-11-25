# Mary Grado
# IV-BASIT C
# P4 - Safe Menu Program
# November 25, 2026

from math import isfinite


def divide_numbers():
    try:
        first_number = float(input("First number: "))
        second_number = float(input("Second number: "))
        if not isfinite(first_number) or not isfinite(second_number):
            raise ValueError
        result = first_number / second_number
    except ValueError:
        print("Invalid number. Enter two finite numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result:g}")
    finally:
        # This runs whether the calculation succeeds or raises an exception.
        print("Division finished.")


def open_file():
    file_name = input("File name: ").strip()
    try:
        # Using with closes the file even if reading it fails.
        with open(file_name, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except UnicodeError:
        print("The file is not readable as UTF-8 text.")
    except (OSError, ValueError):
        print("Unable to open that file. Check the name and permissions.")
    else:
        print("File contents:")
        print(contents)


def main():
    while True:
        print("\nSafe Menu Program | Mary Grado | IV-BASIT C")
        print("1. Divide | 2. Open file | 3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Choose 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
