from abc import ABC, abstractmethod
from .creature import Creature


class Flameling(Creature):
    def __init__(self) -> None:
        name = "Flameling"
        type = "Fire"
        super().__init__(name, type)

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        name = "Pyrodon"
        type = "Fire/Flying"
        super().__init__(name, type)

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        name = "Aquabub"
        type = "Water"
        super().__init__(name, type)

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        name = "Torragon"
        type = "Water"
        super().__init__(name, type)

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
