def cryptic_sorter(strings: list[str]) -> list[str]:

    l: list[int] = []
    temp: str = ""

    for i in range (0, len(strings)):
        strings[i] = strings[i].lower().replace(" ", "")

    for j in range(0, len(strings)):
        for i in range (j + 1, len(strings)):
            if len(strings[j]) > len(strings[i]):
                strings[i], strings[j] = strings[j], strings[i]
            if len(strings[i]) == len(strings[j]):
                for k in range(len(strings[i])):
                    if ord(strings[i][k]) == ord(strings[j][k]):
                        continue
                    if ord(strings[i][k]) > ord(strings[j][k]):
                        strings[j], strings[i] = strings[i], strings[j]
                break
    return strings


if __name__ == "__main__":
    print(cryptic_sorter(["ab", "ba"]))
    print(cryptic_sorter(["aa", "ab"]))
    print(cryptic_sorter(["ba", "ab"]))
    print(cryptic_sorter(["cat","do", "elephant","banana","apple"]))
    print(cryptic_sorter(["kick", "nIce", "He llo", "bie"]))
