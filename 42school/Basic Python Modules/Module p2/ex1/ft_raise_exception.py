def input_temperature(temp_str: str | int) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        temperature = int(temp_str)
    except ValueError as err:
        raise Exception(
            f"Caught input_temperature error: {err}\n"
        )

    if temperature in range(0, 41):
        print(f"Temperature is now {temperature}°C\n")
        return temperature

    if temperature < 0:
        raise Exception(
            f"Caught input_temperature error: "
            f"{temperature}°C is too cold for plants (min 0°C)\n"
        )
    else:
        raise Exception(
            f"Caught input_temperature error: "
            f"{temperature}°C is too hot for plants (max 40°C)\n"
        )


def test_temperature() -> None:
    try:
        input_temperature('25')
    except Exception as err:
        print(err)

    try:
        input_temperature('abc')
    except Exception as err:
        print(err)

    try:
        input_temperature('100')
    except Exception as err:
        print(err)

    try:
        input_temperature('-50')
    except Exception as err:
        print(err)


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
