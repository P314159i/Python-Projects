def inter(s1: str, s2: str) -> str:
    s3 = ""
    for ch in s1:
        if ch in s2 and not ch in s3:
            s3 += ch
    return s3

if __name__ == "__main__":
    print(f"'lo' -> {inter("hello", "world")}")