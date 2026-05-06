def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    try:
        temp = input_temperature("25")
        print(f"Input data is now '{temp}'\n"
              f"Temperature is now {temp}°C\n")

    except Exception as e:
        print("Input data is now '{e}'\n"
              "Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{e}'")

    try:
        temp = input_temperature("abc")
        print(f"\nInput data is now '{temp}'\n"
              f"Temperature is now {temp}°C")

    except Exception:
        print("\nInput data is now 'abc'\n"
              "Caught input_temperature error: "
              "invalid literal for int() with base 10: 'abc'\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
