from pathlib import Path

content = """# Garden Guardian — Data Engineering for Smart Agriculture

The exercises build exception handling step by step: first catching invalid sensor data, then raising errors for unsafe values, handling different built-in exceptions, creating custom error classes, and finally guaranteeing cleanup with `finally`.

## What This Module Teaches

- `try` and `except`
- Built-in exception types
- Raising exceptions with `raise`
- Handling multiple error types
- Custom exception classes
- Exception inheritance
- Program recovery after errors
- Cleanup with `finally`
- Defensive programming
- Resilient data validation
"""

path = Path("/mnt/data/README.md")
path.write_text(content, encoding="utf-8")
print(path)

