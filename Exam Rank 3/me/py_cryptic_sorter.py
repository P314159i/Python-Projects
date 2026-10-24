def cryptic_sorter(strings: list[str]) -> list[str]:

    leng: dict[str, int] = {}
    i = 0
    temp = 0

    for word in strings:
        word.lower().replace(" ", "")
        leng[word] = len(word)

    for i in range (0, len(strings) - 1):
        if leng[strings[i]] > leng[strings[i + 1]]:
            temp = leng[strings[i]]
            leng[strings[i]] = leng[strings[i + 1]]
            leng[strings[i + 1]] = temp
    print(leng)

if __name__ == "__main__":
    cryptic_sorter(["cat","do", "elephant","banana","apple"])
