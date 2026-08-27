def dark_spell_allowed_ingredients() -> list[str]:
    return ["ImpStool", "DeathBell", "SpiderVenom", "Nightshade"]

def dark_spell_record(spell_name: str, ingredients: str) -> str:

    from .dark_validator import validate_ingredients

    validation = validate_ingredients(ingredients)

    if "VALID" in validation:
        if "INVALID" in validation:
            return f"{spell_name} not recorded"
        else:
            return f"{spell_name} recorded"

# 🌺🍄‍🟫🪻🕷