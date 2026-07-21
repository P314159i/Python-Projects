class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.days} days old")


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    starting_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    growth = round(rose.height - starting_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    main()
