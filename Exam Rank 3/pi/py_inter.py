def inter(s1: str, s2: str) -> str:

    stack: str = ""

    for s in s1:
        for c in s2:
            if c == s:
                if not stack or (stack and c not in stack):
                    stack += c
    return stack

if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))
