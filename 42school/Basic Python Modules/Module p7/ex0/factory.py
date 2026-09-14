    from abc import ABC, abstractmethod


    class ForestCreature:
        def __init__(self, name = "Forest Creature") -> None:
            self.name = name


    class Creature(ABC):
        def __init__(self, name, typ) -> None:
            self.name = name
            self.typ = typ
        
        @abstractmethod
        def attack(self) -> str:
            pass
        
        def describe(self) -> str:
            return f"{self.name} is a {self.typ} type Creature"


    class Flameling (Create):
        def __init__(self) -> None:
            pass
        
        def attack(self) -> self:
            return idk

    class ForestFactory(CreatureFactory):
        def __init__(self) -> None:
            super().__init__()

    cha        wolf = ForestCreature()
            return wolf