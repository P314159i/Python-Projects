#! /usr/bin/env python3

def bracket_validator(s: str) -> bool:
    open_bracket = {"(", "{", "["}
    stack = []
    closed_bracket = {")", "}", "]"}
    match = {"]": "[" , "}": "{", ")": "("}

    for ch in s:
        if ch in open_bracket:
            stack.append(ch)
        elif ch in closed_bracket:
            if not stack or stack.pop() != match[ch]:
                return False
           
    return len(stack) == 0


if __name__ == "__main__":
    print(f"True -> {(bracket_validator("()"))}")
    print(f"True -> {(bracket_validator("()[]{}"))}")
    print(f"False -> {(bracket_validator("(]"))}")
    print(bracket_validator(""))
