<<<<<<< HEAD
# GPT gave a excercise to practice raising and catchin

class Insuf(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class Bankaccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance
    
    def writhdraw(self, amount: float) -> None:
        if self.balance < amount:
            raise Insuf("U broke sorry, ")


def main() -> None:

    balance: float = 1003.06
    a: float = input("Enter amount u wanna get: ")
    try:
        amount = float(a)
    except ValueError as err:
        print(f"wtf that's no money - {err}")
        return
    parvin = Bankaccount(balance)
    try:
        parvin.writhdraw(amount)
        print("done")
    except Insuf as err:
        print(f"{err} fuck off")


main()
=======
class GardenError()


class PlantError(GardenError):
    def __init__(
        self,
        message: str = "Unknown plant error"
    ) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(
        self,
        message: str = "Unknown water error"
    ) -> None:
        super().__init__(message)

class Errors(Exception):
    raise 
>>>>>>> faf616b (save python practice changes)
