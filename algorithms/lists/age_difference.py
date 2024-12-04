# Given an array of objects, find the difference in age between the eldest and youngest family members, and return their respective ages and the age difference, e.g. [13, 67, 54]

# Input: List of dictionaries, e.g. [{name: "Paul", age: 28}, {name: "John", age: 33}
from typing import List


def find_age_difference(relatives: List[dict]) -> List[int]:
    ages = [relatives["age"] for relatives in relatives]
    return [
        min(ages),
        max(ages),
        max(ages) - min(ages),
    ]  # [youngest, eldest, age difference]


# Time Complexity: O(n), where n is the number of family members
# Space Complexity: O(1)
