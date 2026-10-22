def string_permutation_checker(s1: str, s2: str) -> bool:
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")
    
    return sorted(s1) == sorted(s2)
    

if __name__ == "__main__":
    print(string_permutation_checker("abc", "bca"))
    print(string_permutation_checker("abc", "def"))