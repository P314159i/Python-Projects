def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("Input data is '25'")
    temperature: int = input_temperature("25")
    print(f"Temperature is now {temperature}°C\n")

    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}\n")

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()


''