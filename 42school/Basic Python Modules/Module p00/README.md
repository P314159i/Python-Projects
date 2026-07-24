from pathlib import Path

content = """# Growing Code — Python Fundamentals Through Garden Data

The exercises build Python fundamentals step by step: first printing a message, then handling user input, performing calculations, using conditions, creating reminders, practicing loops and recursion, and finally adding type annotations.

## What This Module Teaches

- Basic Python syntax
- Functions
- Input and output
- Variables
- Integer conversion
- Arithmetic operations
- Conditional statements
- Loops
- Recursion
- String methods
- Type annotations
"""

path = Path("/mnt/data/README.md")
path.write_text(content, encoding="utf-8")
print(path)

