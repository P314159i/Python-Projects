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
    count = random.randint(7, 10)
    return set(random.sample(ach, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}\n")
    print(f"Player Charlie: {charlie}\n")
    print(f"Player Dylan: {dylan}\n")

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements:\n\n{all_distinct}\n")

    common = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}\n")

    only_alice = alice.difference(bob.union(charlie, dylan))
    only_bob = bob.difference(alice.union(charlie, dylan))
    only_charlie = charlie.difference(alice.union(bob, dylan))
    only_dylan = dylan.difference(alice.union(bob, charlie))

    print(f"Only Alice has: {only_alice}\n")
    print(f"Only Bob has: {only_bob}\n")
    print(f"Only Charlie has: {only_charlie}\n")
    print(f"Only Dylan has: {only_dylan}\n")

    all_possible = set(ach)

    print(f"Alice is missing: {all_possible.difference(alice)}\n")
    print(f"Bob is missing: {all_possible.difference(bob)}\n")
    print(f"Charlie is missing: {all_possible.difference(charlie)}\n")
    print(f"Dylan is missing: {all_possible.difference(dylan)}\n")


if __name__ == "__main__":
    main()
