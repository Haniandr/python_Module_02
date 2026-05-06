def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError("too cold")
    elif temp > 40:
        raise ValueError("too hot")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    try:
        temp = input_temperature("25")
        print(f"Input data is now '{temp}'\n"
              f"Temperature is now {temp}°C\n")

    except Exception as e:
        print(f"Input data is now '{e}'\n"
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

    try:
        temp = input_temperature("100")
        print(f"Input data is now '{temp}'\n"
              f"Temperature is now {temp}°C\n")

    except Exception as e:
        print("Input data is now '100'\n"
              "Caught input_temperature error: "
              f"100°C is {e} for plants(max 40°C)\n")

    try:
        temp = input_temperature("100")
        print(f"Input data is now '{temp}'\n"
              f"Temperature is now {temp}°C\n")

    except Exception as e:
        print("Input data is now '-50'\n"
              "Caught input_temperature error: "
              f"-50°C is {e} for palnts(min 0°C)\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
