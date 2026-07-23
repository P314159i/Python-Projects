class Plant:
    def __init__(plnt, name: str, height: float, age: int) -> None:
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

    def show(plnt) -> None:
        print(
            f"{plnt._name}: {plnt._height:.1f}cm, "
            f"{plnt._age} days old"
        )


def main() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()

    if rose.set_height(25):
        print("Height updated: 25cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print("Age updated: 30 days")
    else:
        print("Age update rejected")

    if rose.set_height(-5):
        print("Height updated")
    else:
        print("Height update rejected")

    if rose.set_age(-10):
        print("Age updated")
    else:
        print("Age update rejected")

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
