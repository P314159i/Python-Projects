def twist_sequence(arr: list[int], k: int) -> list[int]:

    if not arr:
        return []
    k %= len(arr)
    return (arr[-k:] + arr[:-k])

print(twist_sequence([1,2,3,4,5], 2))  # Expected: [4,5,1,2,3]
print(twist_sequence([1,2,3], 1))  # Expected: [3,1,2]
print(twist_sequence([1,2,3,4], 0))  # Expected: [1,2,3,4]
print(twist_sequence([1,2,3], 5))  # Expected: [2,3,1]
print(twist_sequence([], 3))  # Expected: []
print(twist_sequence([10, 20, 30, 40], 5))  # Expected: []