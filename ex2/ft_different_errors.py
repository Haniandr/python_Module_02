#!/usr/bin/env python3

def division(a: int, b: int) -> float:
    return a / b

def garden_operations(operation_number: int) -> None | int:
    if operation_number == 0:
        int("abc")
        return None
    elif operation_number == 1:
        division(100, 0)
        return None
    elif operation_number == 2:
        open("f.txt", "r")
        return None
    elif operation_number == 3:
        "hello" + 79
        return None
    else:
        return operation_number


def test_error_types(operation_number: int = 0) -> None:
    if operation_number > 4 or operation_number < 0:
        print("\nAll error types tested successfully!")
        return

    try:
        print(f"Testing Operation {operation_number}...")
        str = garden_operations(operation_number)
        if str == 4:
            print("Operations completed successfully")

    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught operation {type(e).__name__}: {e}")

    test_error_types(operation_number + 1)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
