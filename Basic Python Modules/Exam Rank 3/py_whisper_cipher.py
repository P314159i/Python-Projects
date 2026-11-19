def whisper_cipher(text: str, shift: int) -> str:

    result: str = ""

    for c in text:
        if ord(c) in range(ord('A'), ord('Z') + 1):
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))

        if ord(c) in range(ord('a'), ord('z') + 1):
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += c

    return(result)




# print(whisper_cipher("hello", 3))
# # khoor

# print(whisper_cipher("Hello World!", 1))
# # Ifmmp Xpsme!

print(whisper_cipher("xyz", 3))
# abc

# print(whisper_cipher("ABC123def", 5))
# # FGH123ijk

# print(whisper_cipher("", 10))
# # ""

# print(whisper_cipher("abc", -3))
# # xyz