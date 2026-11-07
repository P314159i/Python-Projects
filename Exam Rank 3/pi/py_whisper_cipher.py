def whisper_cipher(text: str, shift: int) -> int:


    result: str = ""
    for s in text:
        if s.isupper():
            result += chr((ord(s) - ord('A') + shift) % 26 + ord('A'))
        elif s.islower():
            result += chr(((ord(s) - ord('a') + shift)) % 26 + ord('a'))
        else:
            result += s
    return result


print(whisper_cipher("AZ", 113))
print(whisper_cipher("Hello World!", 1))
print(whisper_cipher("xyz", 3))
print(whisper_cipher("ABC123def", 222))
print(whisper_cipher("", 5))
print(whisper_cipher("abc", -3))
