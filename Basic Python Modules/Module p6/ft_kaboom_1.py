def main() -> None:
    print("=== Kaboom 1 ===")
    print("Import dark_spellbook.py function directly & 'absolute-ly'")
    print("THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Darkness", "bats, arsenic"))


if __name__ == "__main__":
    main()