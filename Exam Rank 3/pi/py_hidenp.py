def hidenp(small: str, big: str) -> bool:

    k = 0
    j = 0
    i = 0
    result = ""

    if small == "":
        return True

    for i in range(len(small)):
        for j in range(len(big)):
            j = k
            if small[i] == big[j] and i <= j:
                result += small[i]
                break
            elif k < len(big) - 1:
                k += 1

    if len(small) == len(result):
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
    # hidenp("abc", "a1b2c3")  # Expected: True
    # hidenp("ace", "abcde")  # Expected: True
    # hidenp("aec", "abcde")  # Expected: False
    # hidenp("", "abc")  # Expected: True
    # hidenp("abc", "ab")  # Expected: False
    # hidenp("aaaa", "aaa")  # Expected: False
    # hidenp("sing","subsequence testing")  # Expected: True