class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, "
              f"{self.days} days old")


def main() -> None:
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()


if __name__ == "__main__":
    main()
