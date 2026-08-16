import typing
import random


names: list[str] = [
    "Morgana", "Elara", "Kiki", "Selene",
    "Rowan", "Circe", "Lilith", "Freya"
]

actions: list[str] = [
    "cast_spell",
    "brew_potion",
    "summon_familiar",
    "teleport",
    "curse",
    "heal",
    "fly",
    "scry"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        nam: str = random.choice(names)
        act: str = random.choice(actions)
        tup: tuple[str, str] = (nam, act)
        yield tup


# generator object out:
# typing.Generator(tuple, (.send value), none (return value)))
def consume_event(
        lis: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:

    while lis:
        itm: tuple[str, str] = random.choice(lis)
        lis.remove(itm)
        yield itm


def main() -> None:
    print("=== Game Data Stream Processor ===")

    obj_thousand = gen_event()
    obj_ten = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(obj_thousand)
        print(
            f"Event {i}: Player {event[0]} "
            f"did action {event[1]}"
        )

    listt: list[tuple[str, str]] = []

    for _ in range(10):
        listt.append(next(obj_ten))

    print(f"\nBuilt list of 10 events: {listt}")

    for event in consume_event(listt):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {listt}")


if __name__ == "__main__":
    main()
