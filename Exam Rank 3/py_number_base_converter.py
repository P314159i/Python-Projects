def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    remainder: int = 0
    result: str = ""
    value: int = 0
    error: str = ""
    base_str: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
    try:
        value = int(number, from_base)
        if value == 0:
            return "0"
        while value > 0:
            value, remainder = divmod(value, to_base)
            result += base_str[remainder]
        result = result[::-1]
    except:
        error = "ERROR"

    if error != "":
        return error
    return result


# def con_to_ten(number: str, base: int, strings: str) -> int:
#     value: int = 0
#     i: int = 0
#     for char in number:
#         i = 0
#         for s in strings:
#             if s == char:
#                 break
#             i += 1
#         value = value * base + i
#     return value


# def con_from_ten(value: int, base: int, strings: str) -> str:

#     if value == 0:
#         return "0"
#     result = ""
#     while value > 0:
#         remainder = value % base
#         result = strings[remainder] + result
#         value = value // base
#     return result


# def number_base_converter(number: str, from_base: int, to_base: int) -> str:
#     strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     i: int = 0
#     value: int = 0
#     if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
#         return "ERROR"
#     if i >= from_base:
#         return "ERROR"
#     value = con_to_ten(number, from_base, strings)
#     if to_base == 10:
#         return value
#     else:
#         value = con_from_ten(value, to_base, strings)
#     return value

    
if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))  # Expected: "10"
    print(number_base_converter("F", 16, 10))  # Expected: "255"
    print(number_base_converter("255", 10, 16))  # Expected: "FF"
    print(number_base_converter("123", 10, 2))  # Expected: "1111011"
    print(number_base_converter("Z", 36, 10))  # Expected: "35"
    print(number_base_converter("35", 10, 36))  # Expected: "Z"
    print(number_base_converter("123", 1, 10))  # Expected: "ERROR"
    print(number_base_converter("G", 16, 10))  # Expected: "ERROR"
    print(number_base_converter("0", 10, 2))  # Expected: "0"