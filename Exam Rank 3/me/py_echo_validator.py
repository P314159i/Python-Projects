def echo_validator(text: str) -> bool:

    text = text.lower().replace(" ", "")
    l = len(text) - 1
    if text == "":
        return False
    for i in range (0, int(l / 2) + 1):
        if text[i] != text[l - i]:
            return False
    return True

if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))
    print(echo_validator("Able was I ere I saw Elba"))
