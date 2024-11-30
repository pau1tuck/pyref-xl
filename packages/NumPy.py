# *** NumPy Reference ***
import numpy as np

# Constants
np.pi  # 3.141592653589793 - Ratio of circumference to diameter
np.e  # 2.718281828459045 - Euler's number, the base of natural logarithms

# Rounding Methods
np.round(5.95)  # 6 - round to the nearest integer
np.ceil(5.3)  # 6 - round up to the nearest integer
np.floor(5.95)  # 5 - round down to the nearest integer
np.trunc(5.95)  # 5 - truncate decimal to integer

# Absolute Value``
np.abs(-7.25)  # 7.25 - absolute value

# Exponents and Roots
2**3  # 8 - Exponentiation
np.power(2, 3)  # 8 - base ^ exponent
np.sqrt(16)  # 4.0 - square root
np.cbrt(27)  # 3.0 - cube root

# Min and Max
np.min([3, 9, 5, 6, 7])  # 3 - smallest value in array
np.max([3, 9, 5, 6, 7])  # 9 - largest value in array

# Random Numbers
np.random.random()  # 0.0 - 0.999... - random float
np.random.randint(1, 11)  # Random integer from 1 to 10

# Logarithms
np.log10(100)  # 2.0 - base 10 logarithm
np.log(1)  # 0.0 - natural logarithm (base e)
np.exp(1)  # 2.718... - Euler's number raised to a power

# Statistical Methods
np.mean([1, 2, 3])  # 2.0 - average value
np.median([1, 3, 2])  # 2.0 - middle value
np.std([1, 2, 3])  # 0.816... - standard deviation
np.var([1, 2, 3])  # 0.666... - variance

# Trigonometry
np.sin(np.pi / 2)  # 1.0 - sine of 90 degrees (in radians)
np.cos(np.pi)  # -1.0 - cosine of 180 degrees
np.tan(np.pi / 4)  # 1.0 - tangent of 45 degrees
np.arcsin(1)  # 1.570... - inverse sine (in radians)
np.arccos(-1)  # 3.141... - inverse cosine
np.arctan(1)  # 0.785... - inverse tangent

# Linear Algebra
np.dot([1, 2], [3, 4])  # 11 - dot product of vectors
np.linalg.det([[1, 2], [3, 4]])  # -2.0 - determinant of a matrix
np.linalg.inv([[1, 2], [3, 4]])  # Inverse of a matrix

# Array Manipulation
np.array([1, 2, 3])  # Create a NumPy array
np.zeros((2, 3))  # 2x3 array of zeros
np.ones((2, 3))  # 2x3 array of ones
np.linspace(0, 1, 5)  # Array of 5 evenly spaced values between 0 and 1
np.reshape(np.arange(6), (2, 3))  # Reshape array into 2x3

# Advanced Array Operations
np.sum([1, 2, 3])  # 6 - sum of array elements
np.prod([1, 2, 3])  # 6 - product of array elements
np.cumsum([1, 2, 3])  # [1, 3, 6] - cumulative sum
np.cumprod([1, 2, 3])  # [1, 2, 6] - cumulative product
np.sort([3, 1, 2])  # [1, 2, 3] - sorted array
np.unique([1, 2, 2, 3])  # [1, 2, 3] - unique elements in array
