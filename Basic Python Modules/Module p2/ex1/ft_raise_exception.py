def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature < 0:
        raise Exception(
            f"{temperature}°C is too cold for plants (min 0°C)\n"
        )
    if temperature > 40:
        raise Exception(
            f"{temperature}°C is too hot for plants (max 40°C)\n"
        )
    return temperature


def test_temperature() -> None:
    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        print(f"Input data is '{value}'")

        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C\n")
        except Exception as err:
            print(f"Caught input_temperature error: {err}\n")

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
