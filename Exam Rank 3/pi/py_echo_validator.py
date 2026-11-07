def echo_validator(text: str) -> bool:

    text = text.lower().replace(" ", "")
    k = len(text) // 2

    a = text[:-k]
    b = text[k:]
    b = b[::-1]

    if text == "":
        return False
    return a == b







# def echo_validator(text: str) -> bool:

#     text = text.lower().replace(" ", "")
#     l = len(text) - 1
#     if text == "":
#         return False
#     for i in range (0, int(l / 2) + 1):
#         if text[i] != text[l - i]:
#             return False
#     return True

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