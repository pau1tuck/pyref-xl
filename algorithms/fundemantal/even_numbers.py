# Write a function that takes an array `arr` of numbers and returns a new array with only even numbers.
from typing import List


def even_numbers(arr: List[int]) -> List[int]:
    return [num for num in arr if num % 2 == 0]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(arr))

# Output: [2, 4, 6, 8, 10]
