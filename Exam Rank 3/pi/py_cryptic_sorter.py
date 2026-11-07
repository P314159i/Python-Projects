def comp(a: str, b: str) -> int:

    count_a = 0
    count_b = 0
    for i in range(len(a)):
        if a[i] in "aeoui":
            count_a += 1
    for i in range(len(b)):
        if b[i] in "aeoui":
            count_b += 1
    if count_a > count_a:
        return 1
    return 0


def cryptic_sorter(strings: list[str]) -> list[str]:

    for i in range(len(strings)):
        for j in range(i, len(strings)):
            if len(strings[i]) > len(strings[j]):
                strings[i], strings[j] = strings[j], strings[i]
            if len(strings[i]) == len(strings[j]):
                k = 0
                a = strings[i]
                b = strings[j]
                if ord(a[k]) > ord(b[k]):
                    strings[i], strings[j] = strings[j], strings[i]
                    k += 1
                if comp(strings[i], strings[j]) == 1:
                    strings[i], strings[j] = strings[j], strings[i]
    return strings



# def cryptic_sorter(strings: list[str]) -> list[str]:

#     l: list[int] = []
#     temp: str = ""


#     for i in range (0, len(strings)):
#         strings[i] = strings[i].lower().replace(" ", "")
        
#     length: dict[str, int] = {}
#     for s in strings:
#         length[s] = len(s)

#     for j in range(0, len(strings)):
#         for i in range (j + 1, len(strings)):
#             if len(strings[j]) > len(strings[i]):
#                 strings[i], strings[j] = strings[j], strings[i]
#             if len(strings[i]) == len(strings[j]):
#                 for k in range(len(strings[i])):
#                     if ord(strings[j][k]) != ord(strings[i][k]):
#                         if ord(strings[j][k]) > ord(strings[i][k]):
#                             strings[i], strings[j] = strings[j], strings[i]
#                             break

#     print(strings)


print(cryptic_sorter(["kir", "nIce", "He llo", "bie"]))