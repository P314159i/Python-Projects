def hidenp(small: str, big: str) -> bool:

    i = 0
    j = 0
    k = 0
    result: str = ""

    if small == "":
        return True

    for i in range(len(small)):
        for j in range(k, len(big)):
            if small[i] == big[j]:
                result += small[i]
                k = j + 1
                break
    print(len(result))
    print(len(small))
    print("---")
    if len(result) == len(small):
        return True
    return False




#     i = 0
#     stack: list[str] = []
#     small = list(small)

#     for s in big:
#         if i < len(small) and s == small[i]:
#             stack.append(s)
#             i += 1
#     if i == len(small):
#         return True
#     return False


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3")) #true
    print(hidenp("ace", "abcde")) #t
    print(hidenp("aec", "abcde")) #f
    print(hidenp("", "abc")) # t
    print(hidenp("abc", "ab")) #f
    print(hidenp("aaaa", "aaa")) #f
    print(hidenp("sing","subsequence testing")) #t
    print(hidenp("aba", "aabba")) # t
    # hidenp("abc", "a1b2c3")  # Expected: True
    # hidenp("ace", "abcde")  # Expected: True
    # hidenp("aec", "abcde")  # Expected: False
    # hidenp("", "abc")  # Expected: True
    # hidenp("abc", "ab")  # Expected: False
    # hidenp("aaaa", "aaa")  # Expected: False
    # hidenp("sing","subsequence testing")  # Expected: True