def con_to_ten(number: str, base: int, strings: str) -> int:
    value: int = 0
    i: int = 0

    for char in number:
        i = 0
        for s in strings:
            if s == char:
                break
            i += 1
        value = value * base + i
    return value


def con_from_ten(value: int, base: int, strings: str) -> str:

    if value == 0:
        return "0"

    result = ""
    while value > 0:
        remainder = value % base
        result = strings[remainder] + result
        value = value // base

    return result


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i: int = 0
    value: int = 0

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    if i >= from_base:
        return "ERROR"
    value = con_to_ten(number, from_base, strings)
    if to_base == 10:
        return value
    else:
        value = con_from_ten(value, to_base, strings)
    return value

    
if __name__ == "__main__":
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
