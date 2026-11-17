import random

names: list[str] = [
    "Davina", "BONNIE",
    "freya", "Qetsiyah",
    "Esther", "DAHLIA", "Morgana",
    "Selene", "circe", "Lilith", "Morgause",
    "silas", "Rowena", "Sybil", "Merlin"
]


def capis(lis: list[str]) -> None:

    already_capi: list[str] = [
        name for name in lis if name == name.capitalize()
        ]

    to_capis: list[str] = [
        name.capitalize() for name in lis
        ]

    player_dic: dict[str, int] = {
        name: random.randint(0, 1000) for name in to_capis
        }

    avg: float = round(sum(player_dic.values()) / len(player_dic), 2)

    high_scores: dict[str, int] = {
        name: score
        for name, score in player_dic.items()
        if score > avg
    }

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {lis}\n")
    print(f"New list with all names capitalized: {to_capis}\n")
    print(f"New list of capitalized names only: {already_capi}\n")
    print(f"Score dict: {player_dic}\n")
    print(f"Score average is {avg}\n")
    print(f"High scores: {high_scores}\n")


def main() -> None:
    capis(names)


if __name__ == "__main__":
    main()
