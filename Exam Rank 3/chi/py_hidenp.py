def hidenp(small: str, big: str) -> bool:
    count = 0
    i = 0
    for ch in big:
        if count < len(small) and ch == small[i]:
            count += 1
            i += 1
    return count == len(small)

if __name__ == "__main__":
    print(f"True -> {hidenp("abc", "a1b2c3")}")
    print(f"False -> {hidenp("abc", "ab")}")
