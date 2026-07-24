def input_temperature(temp_str: str) -> int:
    if temp_str in range (0, 40):
        return int(temp_str)
    try:
        if int(temp_str) < 0:
            raise Exception (
                f"Caught input_temperature error: {int(temp_str)}°C is too cold for plants (min 0°C)"
    exfep            )
    raise Exception (
        f"Caught input_temperature error: {int(temp_str)}°C is too hot for plants (max 40°C)"
        )

def test_temperature() -> None:
    print("Input data is '125'")
    print(f"Temperature is now {int(input_temperature("125"))}°C\n")

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
