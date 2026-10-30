
def bracket_validator(s: str) -> bool:
    pairs: dict [str, str] = {")": "(", "}": "{", "]": "["}
    stack: list [str] = []

    for c in s:
        if c in "([{":
            stack.append(c)
        if c in ")]}":
            if stack and stack.pop() != pairs[c]:
                return False
    return not stack


if __name__ == "__main__":
    print(f"True -> {(bracket_validator("()"))}")
    print(f"True -> {(bracket_validator("()[]{}"))}")
    print(f"False -> {(bracket_validator("(]"))}")
    print(f"True -> {bracket_validator("")}")
    print(f"False -> {(bracket_validator("("))}")
    print(f"True -> {bracket_validator("hello(world)")}")
    print(bracket_validator(" "))