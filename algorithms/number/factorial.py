# Write a function to calculate the factorial of a given number.


def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if num == 0:
        return 1  # By definition, 0! = 1

    total = 1
    for i in range(2, num + 1):  # Start at 2 since multiplying by 1 is redundant
        total *= i
    return total


# Testing the function
print(factorial(5))  # 5! = 120
print(factorial(6))  # 6! = 720
print(factorial(0))  # 0! = 1
