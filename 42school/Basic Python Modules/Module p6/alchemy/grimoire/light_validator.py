def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed_ingredients = [
        ingredient.lower()
        for ingredient in light_spell_allowed_ingredients()
    ]

    entered_ingredients = [
        ingredient.strip().lower()
        for ingredient in ingredients.split(",")
    ]

    if any(
        ingredient in allowed_ingredients
        for ingredient in entered_ingredients
    ):
        result = ", ".join(entered_ingredients[:-1])

        if len(entered_ingredients) > 1:
            result += f" and {entered_ingredients[-1]}"
        else:
            result = entered_ingredients[0]

        return f"{result} - VALID"

    result = ", ".join(entered_ingredients[:-1])

    if len(entered_ingredients) > 1:
        result += f" and {entered_ingredients[-1]}"
    else:
        result = entered_ingredients[0]

    return f"{result} - INVALID"
