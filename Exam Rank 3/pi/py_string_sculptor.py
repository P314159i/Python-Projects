def string_sculptor(text: str) -> str:

    flag: int = 2
    kir = ""

    for i in range(len(text)):
        if i == 0:
            kir += text[0].upper()
            flag = 0
            continue
        elif flag == 0 and text[i].isupper():
            kir += text[i].lower()
            flag = 1
        elif flag == 1 and text[i].islower():
            kir += text[i].upper()
            flag = 0
        elif text[i] == "":
            flag = 1
        else:
            kir += text[i]
            flag = not flag

    return kir


print(string_sculptor("s d hello"))