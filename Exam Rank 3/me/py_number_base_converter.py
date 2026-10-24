def con_to_ten(number: str, base: int, strings: str) -> str:
    value: int = 0
    digit_value: int = 0

    for char in number:
        digit_value = 0
        for s in strings:
            if s == char:
                break
            digit_value += 1
        value = value * from_base + digit_value
    return value


def con_from_ten(number: str, base: int, strings: str) -> str:
    value: int = 0
    digit_value: int = 0

    for char in number:
        digit_value = 0
        for s in strings:
            if s == char:
                break
            digit_value += 1
        value = value * from_base + digit_value
    return value


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    if digit_value >= from_base:
        return "ERROR"
    con_to_ten(number, from_base, strings)
    if to_base == 10:
        return value
    else:
        con_from_ten(number, to_base, strings)

    
from __name__ == "__main__":
    number_base_converter("FF", 16, 10)
    number_base_converter("255", 10, 16)
