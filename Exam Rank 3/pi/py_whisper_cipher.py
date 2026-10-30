def whisper_cipher(text: str, shift: int) -> str:

    result: str = ""
    for s in text:
        if s.isupper():
            result += chr((shift + (ord(s) - ord('A'))) % 26 + ord('A'))
        elif s.islower():
            result += chr((shift + (ord(s) - ord('a'))) % 26 + ord('a'))
        else:
            result += s
    return result


print(whisper_cipher("hello", 3))
print(whisper_cipher("Hello World!", 1))
print(whisper_cipher("xyz", 3))
print(whisper_cipher("ABC123def", 5))
print(whisper_cipher("", 5))
print(whisper_cipher("abc", -3))
