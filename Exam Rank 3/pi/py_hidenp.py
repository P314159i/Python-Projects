def hidenp(small: str, big: str) -> bool:
    i = 0
    stack: list[str] = []
    small = list(small)

    for s in big:
        if i < len(small) and s == small[i]:
            stack.append(s)
            i += 1
    if i == len(small):
        return True
    return False


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3")) #true
    print(hidenp("ace", "abcde")) #t
    print(hidenp("aec", "abcde")) #f
    print(hidenp("", "abc")) # t
    print(hidenp("abc", "ab")) #f
    print(hidenp("aaaa", "aaa")) #f
    print(hidenp("sing","subsequence testing")) #t
    print(hidenp("aba", "aabba")) # t
