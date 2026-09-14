import typing


def get_data() -> tuple[str, int, str]:
    string: str = input("Enter your name:score:achievement: ")

    i: int = string.find(":")
    j: int = string.find(":", i + 1)

    name: str = string[:i]
    score: int = int(string[i + 1:j])
    ach: str = string[j + 1:]

    return name, score, ach


def gen_event(
    names: list[str],
    scores: list[int]
) -> typing.Generator[dict[str, int], None, None]:

    for name, score in zip(names, scores):
        yield {name: score}


def main() -> None:
    name_list: list[str] = []
    ach_set: set[str] = set()
    sc_list: list[int] = []
    player_data: dict[str, int] = {}

    for _ in range(3):
        name, score, ach = get_data()

        ach_set.add(ach)
        name_list.append(name)
        sc_list.append(score)

    print(ach_set)

    seed_name = gen_event(name_list, sc_list)

    for event in seed_name:
        player_data.update(event)

    print(player_data)


main()