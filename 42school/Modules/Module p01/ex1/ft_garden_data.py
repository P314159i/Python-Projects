class Plant:
    name: str
    days: int
    height: int

    def plnt_view(plnt) -> None:
        print(f"{plnt.name}: {plnt.height}cm, {plnt.days} days old")


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.days = 30
    rose.height = 25
    rose.plnt_view()
    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.days = 45
    sunflower.height = 80
    sunflower.plnt_view()
    cactus = Plant()
    cactus.name = "Cactus"
    cactus.days = 120
    cactus.height = 15
    cactus.plnt_view()


if __name__ == "__main__":
    main()
