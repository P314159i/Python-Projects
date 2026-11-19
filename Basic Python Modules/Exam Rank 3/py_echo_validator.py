def echo_validator(text: str) -> bool:

    a: str = ""
    b: str = ""
    l = 0

    text = text.lower().replace(" ", "")

    if text == "":
        return False

    l = int(len(text) // 2)
    for c in range (0, l):
        a += text[c]

    if len(text) % 2 != 0:
        l += 1
        for c in range (l, len(text)):
            b += text[c]
    if len(text) % 2 == 0:
        for c in range (l, len(text)):
            b += text[c]
    b = b[::-1]
    return a == b


if __name__ == "__main__":
    print(echo_validator("racecar"))  # Expected: True
    print(echo_validator("A man a plan a canal Panama"))  # Expected: True
    print(echo_validator("race a car"))  # Expected: False
    print(echo_validator("Was it a car or a cat I saw"))  # Expected: True
    print(echo_validator("hello"))  # Expected: False
    print(echo_validator("Madam Im Adam"))  # Expected: True
    print(echo_validator("madam"))  # Expected: True
    print(echo_validator("Able was I ere I saw Elba"))  # Expected: True
    print(echo_validator(""))  # Expected: False
    print(echo_validator("ab!a"))  # Expected: False
