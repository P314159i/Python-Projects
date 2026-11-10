def anagram(s1: str, s2: str) -> bool:
    return (sorted(s1.lower().replace(" ", "")) == (sorted(s2.lower().replace(" ", ""))))

print(anagram("listen", "silent"))  # Expected: True
print(anagram("Triangle", "Integral"))  # Expected: True
print(anagram("Dormitory", "Dirty Room"))  # Expected: True
print(anagram("hello", "world"))  # Expected: False
print(anagram("", ""))  # Expected: True
print(anagram("abc", "abcc"))  # Expected: False