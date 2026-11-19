def hidenp(small: str, big: str) -> bool:

    this: str = ""
    i = 0
    j = 0
    k = 0

    if len(small) > len (big):
        return False

    for i in range(len(small)):
        for j in range(k, len(big)):
            if small[i] == big[j]: 
                this += small[i]
                k = j + 1
                break
    if len(small) == len(this):
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
    print(hidenp("aa", "ab")) # F
    # hidenp("abc", "a1b2c3")  # Expected: True
    # hidenp("ace", "abcde")  # Expected: True
    # hidenp("aec", "abcde")  # Expected: False
    # hidenp("", "abc")  # Expected: True
    # hidenp("abc", "ab")  # Expected: False
    # hidenp("aaaa", "aaa")  # Expected: False
    # hidenp("sing","subsequence testing")  # Expected: True