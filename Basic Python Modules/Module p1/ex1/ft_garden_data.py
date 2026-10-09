class Plant:
    name: str
    age: int
    height: int

    def show(plnt) -> None:
        print(f"{plnt.name}: {plnt.height}cm, {plnt.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant()
    rose.name = "Rose"
    rose.age = 30
    rose.height = 25
    rose.show()
    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.age = 45
    sunflower.height = 80
    sunflower.show()
    cactus = Plant()
    cactus.name = "Cactus"
    cactus.age = 120
    cactus.height = 15
    cactus.show()


if __name__ == "__main__":
    main()
