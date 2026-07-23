class Plant:
    class SD:
        def __init__(sd) -> None:
            sd._grow_calls = 0
            sd._age_calls = 0
            sd._show_calls = 0

        def record_grow(sd) -> None:
            sd._grow_calls += 1

        def record_age(sd) -> None:
            sd._age_calls += 1

        def record_show(sd) -> None:
            sd._show_calls += 1

        def display(sd) -> None:
            print(
                f"Stats: {sd._grow_calls} grow, "
                f"{sd._age_calls} age, "
                f"{sd._show_calls} show"
            )

    def __init__(
        plnt,
        name: str,
        height: float,
        age: int
    ) -> None:
        plnt._name = name
        plnt._height = height
        plnt._age = age
        plnt._sd: Plant.SD = Plant.SD()

    def grow(plnt, amount: float = 1.0) -> None:
        plnt._height += amount
        plnt._sd.record_grow()

    def age(plnt, days: int = 1) -> None:
        plnt._age += days
        plnt._sd.record_age()

    def show(plnt) -> None:
        plnt._sd.record_show()
        print(
            f"{plnt._name}: {plnt._height:.1f}cm, "
            f"{plnt._age} days old"
        )

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(anon) -> "Plant":
        return anon("Unknown plant", 0.0, 0)

    def display_statistics(plnt) -> None:
        plnt._sd.display()


class Flower(Plant):
    def __init__(
        plnt,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        plnt.color = color
        plnt.is_blooming = False

    def bloom(plnt) -> None:
        plnt.is_blooming = True

    def show(plnt) -> None:
        super().show()
        print(f"Color: {plnt.color}")

        if plnt.is_blooming:
            print(f"{plnt._name} is blooming beautifully!")
        else:
            print(f"{plnt._name} has not bloomed yet")


class Tree(Plant):
    class SD(Plant.SD):
        def __init__(sd) -> None:
            super().__init__()
            sd._shade_calls = 0

        def record_shade(sd) -> None:
            sd._shade_calls += 1

        def display(sd) -> None:
            super().display()
            print(f"{sd._shade_calls} shade")

    def __init__(
        plnt,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        plnt.trunk_diameter = trunk_diameter
        plnt._tree_sd = Tree.SD()
        plnt._sd = plnt._tree_sd

    def produce_shade(plnt) -> None:
        plnt._tree_sd.record_shade()
        print(
            f"Tree {plnt._name} now produces a shade of "
            f"{plnt._height:.1f}cm long and "
            f"{plnt.trunk_diameter:.1f}cm wide."
        )

    def show(plnt) -> None:
        super().show()
        print(
            f"Trunk diameter: "
            f"{plnt.trunk_diameter:.1f}cm"
        )


class Vegetable(Plant):
    def __init__(
        plnt,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        plnt.harvest_season = harvest_season
        plnt.nutritional_value = 0
        plnt._has_grown = False

    def grow(plnt, amount: float = 1.0) -> None:
        super().grow(amount)
        plnt._has_grown = True

    def age(plnt, days: int = 1) -> None:
        super().age(days)

        if plnt._has_grown:
            plnt.nutritional_value += 1
            plnt._has_grown = False

    def show(plnt) -> None:
        super().show()
        print(f"Harvest season: {plnt.harvest_season}")
        print(
            f"Nutritional value: "
            f"{plnt.nutritional_value}"
        )


class Seed(Flower):
    def __init__(
        plnt,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int
    ) -> None:
        super().__init__(name, height, age, color)
        plnt._seed_count = seed_count
        plnt.seeds = 0

    def bloom(plnt) -> None:
        super().bloom()
        plnt.seeds = plnt._seed_count

    def show(plnt) -> None:
        super().show()
        print(f"Seeds: {plnt.seeds}")


def show_statistics(plnt: Plant) -> None:
    print(f"[statistics for {plnt._name}]")
    plnt.display_statistics()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}")
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}")

    rose = Flower("Rose", 15.0, 10, "red")

    print("=== Flower")
    rose.show()
    show_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    show_statistics(rose)

    oak = Tree("Oak", 200.0, 365, 5.0)

    print("=== Tree")
    oak.show()
    show_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)

    sunflower = Seed(
        "Sunflower",
        80.0,
        45,
        "yellow",
        42
    )

    print("=== Seed")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    show_statistics(sunflower)

    anonymous = Plant.create_anonymous()

    print("=== Anonymous")
    anonymous.show()
    show_statistics(anonymous)


if __name__ == "__main__":
    main()
