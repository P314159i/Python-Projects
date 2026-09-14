from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print("\n")
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("-------------------")
    print("Testing battle:")
    print("-------------------\n")
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!\n")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    test_factory(FlameFactory())
    print("\n")
    test_factory(AquaFactory())
    print("\n")
    battle(FlameFactory(), AquaFactory())
    print("\n")


main()
