#! /usr/bin/env python3

def sorting(a: str, b: str) -> bool:
    if len(a) != len(b):
        return len(a) > len(b)
    if a.lower() != b.lower():
        return a.lower() > b.lower()
    # if len(a) == len(b) and sum(1 for ch in a if ch in "aeiuoAEIUO") > sum(1 for ch in b if ch in "aeiuoAEIUO"):
    #     return sum(1 for ch in a if ch in "aeiuoAEIUO") > sum(1 for ch in b if ch in "aeiuoAEIUO")
    return False


def cryptic_sorter(strings: list[str]) -> list[str]:

    n = len(strings)

    for x in range(n):
        for z in range(x +1, n):
            if sorting(strings[x], strings[z]):
                strings[x], strings[z] = strings[z], strings[x]
    return strings
    # return sorted(strings, key=lambda s: (len(s), s.lower(), sum(1 for char in s if char in "aeiouAEIOU")
    #     )
    # )
    
    # # return sorted(strings, key=lambda word: (len(word), word))


if __name__ == "__main__":
    samplea = ["cat","dog","apple","banana","elephant"]
    print (samplea)
    print (f" {cryptic_sorter(["apple","cat","banant","banana","elephant"])}")
    sampleb = ["aaa", "AAA", "bbb", "BBB"]
    print (sampleb)
    print (f" {(cryptic_sorter(["aaa","bbb","AAA","BBB"]))}")
    print (f" {(cryptic_sorter(["hello", "world", "hi", "test"]))}")