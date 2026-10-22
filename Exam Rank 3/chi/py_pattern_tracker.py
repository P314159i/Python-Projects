def pattern_tracker(text: str) -> int:
    count = 0
    for x in range(len(text) - 1):
        if text[x].isdigit() and text[x + 1].isdigit():
            if int(text[x + 1]) == int(text[x]) + 1:
                count += 1
    return count  


if __name__ == "__main__":
    print(f"2 -> {pattern_tracker("123")}")
    print(f"2 -> {pattern_tracker("12a36")}")
    print(pattern_tracker("987654321"))
    print(pattern_tracker("01234567"))
    print(pattern_tracker("abc"))
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("112233"))
