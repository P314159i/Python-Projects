New concepts in Module 6:

* modules vs packages
* `__init__.py`
* `import x` vs `from x import y`
* exposing selected names through a package
* nested imports
* absolute vs relative imports
* package aliases
* circular imports and how to avoid them 

Practice task:

Create this tiny package:

```text
magic/
    __init__.py
    elements.py
    spells.py

main.py
```

Requirements:

* `elements.py`: `fire()` and `water()`
* `spells.py`: import one element relatively and return a spell string
* `__init__.py`: expose only `fire()` and one spell
* `main.py`: test:

  * `import magic`
  * `from magic import ...`
  * one direct module import

Then make two tiny files that import each other so you can observe a circular-import failure.   
