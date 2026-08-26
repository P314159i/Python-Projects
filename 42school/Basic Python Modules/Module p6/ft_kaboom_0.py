Time to test a few spells! Create two scripts to demonstrate that light magic avoids
circular dependencies and laboratory explosions, and that dark magic is dangerous and
explodes because of circular dependencies:

ft_kaboom_0.py will access the grimoire module directly and then record a light
spell, flawlessly. There are multiple ways to avoid circular dependencies; you pick
one. Be prepared to explain the different approaches during the evaluation.

$> python3 ft_kaboom_0.py
=== Kaboom 0 ===
Using grimoire module directly
Testing record light spell: Spell recorded: Fantasy (Earth, wind and fire - VALID)
$> python3 ft_kaboom_1.py
=== Kaboom 1 ===
Access to alchemy/grimoire/dark_spellbook.py directly
Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION
Traceback (most recent call last):
File "/tmp/Python/module-06/ft_kaboom_1.py", line 7, in <module>
from alchemy.grimoire.dark_spellbook import dark_spell_record
File "/tmp/Python/module-06/alchemy/grimoire/dark_spellbook.py", line 2, in <module>
from .dark_validator import validate_ingredients
File "/tmp/Python/module-06/alchemy/grimoire/dark_validator.py", line 2, in <module>
from .dark_spellbook import dark_spell_allowed_ingredients
ImportError: cannot import name 'dark_spell_allowed_ingredients' from partially initialized module '
alchemy.grimoire.dark_spellbook' (most likely due to a circular import) (/tmp/Python/module-06/
alchemy/grimoire/dark_spellbook.py)

