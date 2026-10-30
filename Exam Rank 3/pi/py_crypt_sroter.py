def swap(s1: str, s2: str) -> tuple[str, str]:
    temp = s1
    s1 = s2
    s2 = temp
    return [s1, s2]


def cryptic_sorter(strings: list[str]) -> list[str]:

    for si in range(0, len(strings)):
        for sj in range(si, len(strings)):
            if len(strings[si]) != len(strings[sj]):
                if len(strings[si]) > len(strings[sj]):
                    strings[si], strings[sj] = swap(strings[si], strings[sj])
    for si in range(0, len(strings)):
        for sj in range(si, len(strings)):
            if len(strings[si]) == len(strings[sj]):
                for k in range(0, len(strings[si])):
                    if ord(strings[si][k].lower()) > ord(strings[sj][k].lower()):
                        strings[si], strings[sj] = swap(strings[si], strings[sj])
                    break
    return strings


print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
print(cryptic_sorter(["hello","world","hi","test"]))
print(cryptic_sorter([]))
print(cryptic_sorter([""]))

["cat","dog","apple","banana","elephant"]
["aaa", "AAA", "bbb", "BBB"]
["hi","test","hello","world"]
[]
[""]