def string_sculptor(text: str) -> str:
    f = True
    result = ""
    for ch in text:
        if ch.isalpha():
            if f:
                result += ch.lower()
                f = False
            else:
                result += ch.upper()
                f = True
        elif ch == " ":
            f = True
            result += ch
        else:
            result += ch
    return result


if __name__ == "__main__":
    print(string_sculptor("hello world"))
