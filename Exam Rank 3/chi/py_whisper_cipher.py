def whisper_cipher(text: str, shift: int) -> str:
    result = []
    for char in text:
            if char.islower():
                ascii = ord('a')
                result.append(chr((ord(char) - ascii + shift) % 26 + ascii))
            elif char.isupper():
                ascii = ord('A')
                result.append(chr((ord(char) - ascii + shift) % 26 + ascii))
            else:
                result.append(char)
    return ("").join(result)


if __name__ == "__main__":    
    print(whisper_cipher("hello", 3))