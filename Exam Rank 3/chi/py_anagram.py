def anagram(s1: str, s2: str) -> bool:
    # s1 = s1.strip()
    # s2 = s2.strip()

    # for ch in s1.lower():
    #     if ch not in s2.lower():
    #         return False
    return sorted(s1.lower().replace(" ","")) == sorted(s2.lower().replace(" ",""))

if __name__ == "__main__":
    print(f" True -> {anagram("listen", "silent")}")
    print(f" True -> {anagram("Dormitory", "Dirty Room")}")
    print(f" False -> {anagram("abc", "abcc")}")