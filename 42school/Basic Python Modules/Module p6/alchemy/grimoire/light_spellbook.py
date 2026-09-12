def light_spell_allowed_ingredients() -> list[str]:
    return ["Earth", "Air", "Fire", "Water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)

    if "VALID" in validation:
        if "INVALID" in validation:
            return f"Spell rejected: {spell_name} - {validation}"
        else:
            return f"Spell recorded: {spell_name} - {validation}"
    return "None"
