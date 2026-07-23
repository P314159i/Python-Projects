class Plant:
    def __init__(
        plnt,
        name: str,
        height: float,
        age: int
    ) -> None:
        plnt._name = name
        plnt._height = 0.0
        plnt._age = 0

        plnt.set_height(height)
        plnt.set_age(age)

    def set_height(plnt, height: float) -> bool:
        if height < 0:
            print(f"{plnt._name}: Error, height can't be negative")
            return False

        plnt._height = height
        return True

    def set_age(plnt, age: int) -> bool:
        if age < 0:
            print(f"{plnt._name}: Error, age can't be negative")
            return False

        plnt._age = age
        return True

    def get_height(plnt) -> float:
        return plnt._height

    def get_age(plnt) -> int:
        return plnt._age

    def grow(plnt, amount: float = 1.0) -> None:
        plnt._height += amount

    def age(plnt, days: int = 1) -> None:
        plnt._age += days

    def show(plnt) -> None:
        print(
            f"{plnt._name}: {plnt._height:.1f}cm, "
            f"{plnt._age} days old"
        )


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
    def __init__(
        plnt,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        plnt.trunk_diameter = trunk_diameter

    def produce_shade(plnt) -> None:
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
        plnt._has_aged = False

    def _update_nutrition(plnt) -> None:
        if plnt._has_grown and plnt._has_aged:
            plnt.nutritional_value += 1
            plnt._has_grown = False
            plnt._has_aged = False

    def grow(plnt, amount: float = 1.0) -> None:
        super().grow(amount)
        plnt._has_grown = True
        plnt._update_nutrition()

    def age(plnt, days: int = 1) -> None:
        super().age(days)
        plnt._has_aged = True
        plnt._update_nutrition()

    def show(plnt) -> None:
        super().show()
        print(f"Harvest season: {plnt.harvest_season}")
        print(f"Nutritional value: {plnt.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()

    tomato.show()


if __name__ == "__main__":
    main()
