class GardenError(Exception):
    def __init__(
        self,
        message: str = "Unknown garden error"
    ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(
        self,
        message: str = "Unknown plant error"
    ) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(
        self,
        message: str = "Unknown water error"
    ) -> None:
        super().__init__(message)


def plant_problem() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_problem() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        plant_problem()
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("Testing WaterError...")
    try:
        water_problem()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("Testing catching all garden errors...")

    try:
        plant_problem()
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    try:
        water_problem()
    except GardenError as err:
        print(f"Caught GardenError: {err}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
