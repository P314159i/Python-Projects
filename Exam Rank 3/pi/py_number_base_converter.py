bases: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_ten(number: str, base: int, bases: str) -> str:

    result: int = 0
    number = number[::-1]

    for s in number:
        result = result * base + bases.index(s)

    return result


def from_ten(number: str, base: int, bases: str) -> str:

    result: str = ""
    n = int(number)
    remainder: int = 0

    while n > 0:
        remainder = n % 10
        result += bases[remainder]
        n //= 10

    return result[::-1]

    

def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    result: str = ""

    pass



    
if __name__ == "__main__":
    print(to_ten("A1", 16, bases))
    print(from_ten("26", 16, bases))
    # print(number_base_converter("FF", 16, 10))
    # print(number_base_converter("255", 10, 16))
