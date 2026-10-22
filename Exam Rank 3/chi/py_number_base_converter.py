def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
    
    try:
        value = int(number, from_base)
        result = ""
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while value > 0:
            value, remainder = divmod(value, to_base)
            result += (digits[remainder])
            print(result)
        return (result[::-1])
    except:
        return "ERROR"

if __name__ == "__main__":
    print(f"'10' -> {number_base_converter("1010", 2, 10)}")
    print(f"'255' -> {number_base_converter("FF", 16, 10)}")
    print(f"'FF' -> {number_base_converter("255", 10, 16)}")
    print(f"'ERROR' -> {number_base_converter("123", 1, 10)}")

    print(number_base_converter("101010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    print(number_base_converter("35", 10, 36))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("G", 16, 10))