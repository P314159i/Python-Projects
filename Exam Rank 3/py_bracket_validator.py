import sys

def bracket_validator(s: str) -> bool:
    pairs: dict[str, str] = {"{": "}", "[": "]", "(": ")"}
    stack: list[str] = []

    for char in s:
        if char in pairs.keys():
            stack.append(char)
        if char in pairs.values():
            if not stack:
                return False
            if (pairs[stack.pop()]) != char:
                return False
    return True


if __name__ == "__main__":
    print(bracket_validator(sys.argv[1]))

