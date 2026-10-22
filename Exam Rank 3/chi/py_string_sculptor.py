def string_sculptor(text: str) -> str:
    space = True
    result = ""
    for ch in text:
        if ch.isalpha():
            if space:
                result += ch.lower()
                space = False
            else:
                result += ch.upper()
                space = True
        elif ch == " ":
            space = True
            result += ch
        else:
            result += ch
    return result


if __name__ == "__main__":
    print(string_sculptor("hello world"))
