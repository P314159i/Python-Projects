def validate_ingredients(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients

    allowed_ingredients = [
        ingredient.lower()
        for ingredient in dark_spell_allowed_ingredients()
    ]

    entered_ingredients = [
        ingredient.strip().lower()
        for ingredient in ingredients.split(",")
    ]

    if any(
        ingredient in allowed_ingredients
        for ingredient in entered_ingredients[:-1]
    ):
        result = ", ".join(entered_ingredients[:-1])
        if len(entered_ingredients) > 1:
            result += f" and {entered_ingredients[-1]}"
        else:
            result = entered_ingredients[0]
        return f"{result} - Valid"
    
    result = ", ".join(entered_ingredients[:-1])
    if len(entered_ingredients) > 1:
        result += f" and {entered_ingredients[-1]} -"
    else:
        result = entered_ingredients[0]
    return f"{result} - INVALID"


# def main() -> None:
#     # print(validate_ingredients("air"))
#     print(validate_ingredients("Nightshade, air"))


# main()
