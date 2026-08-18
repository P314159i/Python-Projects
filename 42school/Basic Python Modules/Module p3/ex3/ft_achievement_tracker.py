import random


ach = [
    "Benette Witch",
    "Cure Crafter",
    "Slayer",
    "Ripper",
    "Midnight Pact",
    "Old Geazer",
    "Humanity Guardean",
    "Immortal Witch",
    "Ancient Tomb",
    "Moon Stoner",
    "Moon Curse",
    "Cursed",
    "Cured Vampire",
    "Hybrid Wolf",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 7)
    return set(random.sample(ach, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n\n")

    el = gen_player_achievements()
    bon = gen_player_achievements()
    mat = gen_player_achievements()
    caro = gen_player_achievements()

    print(f"Player El: {el}\n")
    print(f"Player Bon: {bon}\n")
    print(f"Player Mat: {mat}\n")
    print(f"Player Caro: {caro}\n")

    all_distinct = el.union(bon, mat, caro)
    print(f"\n\nAll distinct achievements: \n\n{all_distinct}\n\n")

    common = el.intersection(bon, mat, caro)
    print(f"\nCommon achievements: {common}\n\n")

    # differences of bon and (all others in one but unique)
    only_el = el.difference(bon.union(mat, caro))
    only_bon = bon.difference(el.union(mat, caro))
    only_mat = mat.difference(el.union(bon, caro))
    only_caro = caro.difference(el.union(bon, mat))

    print(f"Only El has: {only_el}\n")
    print(f"Only Bon has: {only_bon}\n")
    print(f"Only Mat has: {only_mat}\n")
    print(f"Only Caro has: {only_caro}\n")

    all_possible = set(ach)

    print(f"El is missing: {all_possible.difference(el)}\n")
    print(f"Bon is missing: {all_possible.difference(bon)}\n")
    print(f"Mat is missing: {all_possible.difference(mat)}\n")
    print(f"Caro is missing: {all_possible.difference(caro)}\n")


if __name__ == "__main__":
    main()
