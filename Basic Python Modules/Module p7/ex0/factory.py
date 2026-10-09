from abc import ABC, abstractmethod
from . import creature
from . import creatures


class CreatureFactory(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_base(self) -> "creature.Creature":
        pass

    @abstractmethod
    def create_evolved(self) -> "creature.Creature":
        pass


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> "creatures.Flameling":
        make_flameling = creatures.Flameling()
        return make_flameling

    def create_evolved(self) -> "creatures.Pyrodon":
        make_pydron = creatures.Pyrodon()
        return make_pydron


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> "creatures.Aquabub":
        make_aquabub = creatures.Aquabub()
        return make_aquabub

    def create_evolved(self) -> "creatures.Torragon":
        make_torragon = creatures.Torragon()
        return make_torragon
