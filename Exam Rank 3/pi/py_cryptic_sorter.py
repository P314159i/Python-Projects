def cryptic_sorter(strings: list[str]) -> list[str]:

    l: list[int] = []
    temp: str = ""


    for i in range (0, len(strings)):
        strings[i] = strings[i].lower().replace(" ", "")
        
    length: dict[str, int] = {}
    for s in strings:
        length[s] = len(s)

    for j in range(0, len(strings)):
        for i in range (j + 1, len(strings)):
            if len(strings[j]) > len(strings[i]):
                strings[i], strings[j] = strings[j], strings[i]
            if len(strings[i]) == len(strings[j]):
                for k in range(len(strings[i])):
                    if ord(strings[j][k]) != ord(strings[i][k]):
                        if ord(strings[j][k]) > ord(strings[i][k]):
                            strings[i], strings[j] = strings[j], strings[i]
                            break

    print(strings)


cryptic_sorter(["kir", "nIce", "He llo", "bie"])


# def cryptic_sorter(strings: list[str]) -> list[str]:

#     leng: dict[str, int] = {}
#     i = 0
#     temp = 0

#     for word in strings:
#         word.lower().replace(" ", "")
#         leng[word] = len(word)

#     for i in range (0, len(strings) - 1):
#         if leng[strings[i]] > leng[strings[i + 1]]:
#             temp = leng[strings[i]]
#             leng[strings[i]] = leng[strings[i + 1]]
#             leng[strings[i + 1]] = temp
#     print(leng)

# if __name__ == "__main__":
#     cryptic_sorter(["cat","do", "elephant","banana","apple"])
