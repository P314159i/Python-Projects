def pattern_tracker(text: str) -> int:

    count: int = 0

    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i + 1]) == int(text[i]) + 1:
                count += 1
    return count


if __name__ == "__main__":
    print(pattern_tracker("123"))  # Expected: 2
    print(pattern_tracker("12a34"))  # Expected: 2
    print(pattern_tracker("987654321"))  # Expected: 0
    print(pattern_tracker("01234567"))  # Expected: 7
    print(pattern_tracker("abc"))  # Expected: 0
    print(pattern_tracker("1a2b3c4"))  # Expected: 0
    print(pattern_tracker("112233"))  # Expected: 2