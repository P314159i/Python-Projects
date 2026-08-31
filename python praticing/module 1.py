#!/usr/bin/env python3

class Plant:
    class SD:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
        
        def record_grow(self) -> None:
            self.grow_calls += 1



    def __init__(self,
        name:str,
        height: float,
        age: int
        ):
        self.name = name
        self.height = height
        self.age = age

    def set_height(self) -> None:
        if self.height < 0:
            raise Exception("Height cannot be negative dude")

    def set_growth(self) -> None:
        if self.age < 0:
            raise Exception("Age cannot be negative dude")

    def grow(self) -> None:
        try:
            self.set_height()
            for _ in range (0, 7):
                self.height += 0.1
        except Exception as err:
            print(f"no {err}")
            return

    def aging(self) -> None:
        try:
            self.set_growth()
            for _ in range (0, 7):
                self.age += 1
        except Exception as err:
            print(f"no {err}")
            return

    def printer(self) -> None:
        print(f"name: {self.name},\n"
            f"heihgt: {self.height}cm\n"
            f"age: {self.age} days\n")

    @classmethod
    def make_anon(anon) -> "Plant":
        return anon("what", 0.0, 0)
        
        

class Flower(Plant):
    def __init__(self, name: str, height: float, age:int, p: int) -> None:
        super().__init__(name, height, age)
        self.p = p
    
    def paddle(self) -> None:
        print(f"{self.p} is number of paddles\n")



def main() -> None:

    for _ in {"Rose", "Sunflower"}:
        plant = Flower(f"{_}", 2, 1, 3)
        plant.aging()
        plant.grow()
        plant.printer()
        plant.paddle()


if __name__ == "__main__":
    main()