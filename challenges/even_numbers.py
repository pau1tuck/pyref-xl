# Write a function that takes an array `arr` of numbers and returns a new array with only even numbers.
from typing import List


def even_numbers(arr: List[int]) -> List[int]:
    if not arr:
        return []
    return [num for num in arr if isinstance(num, int) and num % 2 == 0]


# Input: `arr` = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 4, 6, 8, 10]


# Non-Pythonic solution
def even_numbers(arr: List[int]) -> List[int]:
    if not arr:
        return []
    evens = []
    for num in arr:
        if isinstance(num, int) and num % 2 == 0:
            evens.append(num)
    return evens


# Input: `arr` = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 4, 6, 8, 10]
