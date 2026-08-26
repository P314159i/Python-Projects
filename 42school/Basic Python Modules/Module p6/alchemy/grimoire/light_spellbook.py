Learn to identify and break the explosive circular dependency curse, which occurs when
modules try to summon each other in an endless loop, threatening to destroy your laboratory!

A function light_spell_allowed_ingredients() that returns a list of allowed
ingredients for light magic, let’s say “earth”, “air”, “fire”, “water”.
• A function light_spell_record(spell_name: str, ingredients: str) that returns a 
string that indicates whether the spell is recorded or rejected. The decision
comes from the validation function described below.

