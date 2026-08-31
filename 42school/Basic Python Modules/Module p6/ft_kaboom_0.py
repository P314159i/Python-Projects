import alchemy.grimoire as light


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module direct & 'absolute-ly'")
    print(
        "Testing record light spell:\n"
        f"{light.light_spell_record('Fantasy', 'Earth, wind and fire')}"
    )


if __name__ == "__main__":
    main()
