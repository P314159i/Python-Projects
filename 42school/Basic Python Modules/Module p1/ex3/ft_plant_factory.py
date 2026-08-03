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
    sunflower = Plant("Sunflower", 80.0, 45)
    cactus = Plant("Cactus", 15.0, 120)
    fern = Plant("Fern", 35.0, 60)
    bamboo = Plant("Bamboo", 120.0, 90)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    fern.show()
    print("Created: ", end="")
    bamboo.show()


if __name__ == "__main__":
    main()
