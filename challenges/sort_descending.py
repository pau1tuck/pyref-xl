# Sort the following list of numbers in descending order:
numbers = [5, 2, 8, 1, 9, 7, 3, 6, 4]

numbers.sort(reverse=True)  # Modifies the original list in place
print(numbers)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
numbers = [5, 2, 8, 1, 9, 7, 3, 6, 4]

sorted_numbers = sorted(numbers, reverse=True)  # Creates a new sorted list
print(sorted_numbers)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Key differences:
# sort() is a list method that modifies the original list in-place
# sorted() is a built-in function that returns a new sorted list and leaves the original list unchanged
