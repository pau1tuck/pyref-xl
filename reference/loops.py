# *** Python Loops ***

# *** FOR ***

# 1. Basic iteration over a list
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)  # Output: 1, 2, 3, 4, 5

# 2. Using `range` with for loops
for i in range(5):  # Loops from 0 to 4
    print(i)  # Output: 0, 1, 2, 3, 4

for i in range(1, 6):  # Loops from 1 to 5
    print(i)  # Output: 1, 2, 3, 4, 5

# 3. Iterating with `enumerate` (index and value)
nums = range(1, 6)  # Loops from 1 to 5
for index, value in enumerate(nums, start=0):  # `start=0` makes the index start from 0
    print(f"Index: {index}, Value: {value}")

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")  # Output: 0: apple, 1: banana, 2: cherry

# 4. Iterating over tuples
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, letter in pairs:
    print(f"{num} -> {letter}")  # Output: 1 -> a, 2 -> b, 3 -> c

# 5. Nested for loops
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for val in row:
        print(val, end=" ")  # Output: 1 2 3 4 5 6
    print()  # Newline after each row

# 6. Iterating over a dictionary
person = {"name": "Alice", "age": 25, "city": "London"}
for key, value in person.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 25, city: London

# *** WHILE ***

# 7. Basic while loop
i = 0
while i < 5:
    print(i)
    i += 1  # Increment `i`

# 8. Infinite while loop (with break)
while True:
    print("Looping forever...")
    break


# 9. Using `continue` to skip iterations
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Output: 1, 3, 5, 7, 9

# *** SIMULATING DO-WHILE LOOPS ***

# Python doesn’t have a built-in `do-while`, but you can simulate it:
x = 0
while True:
    print(x)
    x += 1
    if x >= 5:
        break  # Condition to exit

# *** LIST COMPREHENSIONS ***

# 10. Basic list comprehension
nums = [1, 2, 3, 4, 5]
squares = [num**2 for num in nums]  # [1, 4, 9, 16, 25]

# 11. List comprehension with condition
evens = [num for num in nums if num % 2 == 0]  # [2, 4]

# 12. Nested list comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [val for row in matrix for val in row]  # [1, 2, 3, 4, 5, 6]

# *** DICTIONARY COMPREHENSIONS ***

# 13. Create a dictionary with comprehension
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_comp = {k: v for k, v in zip(keys, values)}  # {'a': 1, 'b': 2, 'c': 3}

# *** SET COMPREHENSIONS ***

# 14. Create a set with comprehension
nums = [1, 2, 2, 3, 3, 4]
unique_squares = {num**2 for num in nums}  # {1, 4, 9, 16}

# *** GENERATOR EXPRESSIONS ***

# 15. Generator for memory-efficient iteration
nums = [1, 2, 3, 4, 5]
gen = (num**2 for num in nums)  # Use `()` for generators
for square in gen:
    print(square)  # Output: 1, 4, 9, 16, 25

# *** CONTROL FLOW IN LOOPS ***

# 16. Using `break` to exit a loop early
for num in range(10):
    if num == 5:
        break
    print(num)  # Output: 0, 1, 2, 3, 4

# 17. Using `continue` to skip an iteration
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # Output: 1, 3, 5, 7, 9

# 18. Using `else` with loops
for num in range(3):
    print(num)
else:
    print("Loop completed!")  # Runs if the loop wasn't exited with `break`

# *** UNPACKING WITH LOOPS ***

# 19. Unpacking in a loop
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for x, y, z in data:
    print(f"x={x}, y={y}, z={z}")

# *** ITERTOOLS FOR ADVANCED LOOPS ***

from itertools import cycle, islice

# 20. Infinite looping with `cycle`
colors = ["red", "green", "blue"]
for color in islice(cycle(colors), 10):  # Cycle through `colors` 10 times
    print(color)  # Output: red, green, blue, red, green, ...

# *** LOOPING OVER STRINGS ***

# 21. Iterating over characters in a string
word = "hello"
for char in word:
    print(char)  # Output: h, e, l, l, o

# *** NESTED LOOP OPTIMIZATION ***

# 22. Break out of nested loops with a flag
found = False
for i in range(3):
    for j in range(3):
        if i == j:
            found = True
            break
    if found:
        break
print(f"Found match at i={i}, j={j}")
