Learn to identify and break the explosive circular dependency curse, which occurs when
modules try to summon each other in an endless loop, threatening to destroy your laboratory!

 A function dark_spell_allowed_ingredients() that returns a list of allowed
ingredients for dark magic, Let’s say that dark magic uses the following ingredients:
 “bats”, “frogs”, “arsenic”, and “eyeball”

• A function dark_spell_record(spell_name: str, ingredients: str) that returns a string that indicates whether the spell is recorded or rejected. The decision
comes from the validation function described below.