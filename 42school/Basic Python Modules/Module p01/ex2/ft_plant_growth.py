class Plant:
    def __init__(plnt, name: str, height: float, days: int) -> None:
        plnt.name = name
        plnt.height = height
        plnt.days = days

    def grow(plnt) -> None:
        plnt.height += 0.8

    def age(plnt) -> None:
        plnt.days += 1

    def show(plnt) -> None:
        print(f"{plnt.name}: {round(plnt.height, 1)}cm, "
              f"{plnt.days} days old")


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
