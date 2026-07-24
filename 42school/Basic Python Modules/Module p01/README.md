from pathlib import Path

content = """# Code Cultivation — Object-Oriented Garden Systems

The exercises build one garden system step by step: first a basic plant program, then a `Plant` class, growth behavior, faster plant creation with a constructor, protected data, specialized plant types, and finally statistics and analytics.

## What This Module Teaches

- Python program structure
- Classes and objects
- Attributes and methods
- Constructors
- Encapsulation and validation
- Inheritance and method overriding
- Reuse with `super()`
- Static methods and class methods
- Nested classes
- Scalable object-oriented design
"""

path = Path("/mnt/data/README.md")
path.write_text(content, encoding="utf-8")
print(path)

