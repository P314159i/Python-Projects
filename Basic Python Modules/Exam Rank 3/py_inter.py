def inter(s1: str, s2: str) -> str:
    i = 0
    string: str = ""

    for s in s1:
        i = 0
        for i in range (0, len(s2)):
            if s == s2[i] and s not in string:
                string += s
                i += 1
    
    return string


if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))
