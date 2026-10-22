def cryptic_sorter(strings: list[str]) -> list[str]:
    numbers: dict[int, str] = {}
    temp: int = 0

    print(numbers)

    for word in strings:
        numbers[len(word)] = word

    print(numbers)

    # for i in range (0, len(strings)):
    #     if i + 2 < len(strings):
    #         if (numbers[i] > numbers[i + 1]):
    #             temp = numbers[i]
    #             numbers[i] = numbers[i + 1]
    #             numbers[i + 1] = temp


    
    return None


if __name__ == "__main__":
    cryptic_sorter(["cat","do","banana","apple","elephant"])
