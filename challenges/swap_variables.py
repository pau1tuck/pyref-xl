# Swap the variables without using a temporary variable
a = 5
b = 10

a, b = b, a

print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5

# Swap the variables using XOR
x = 5
y = 10

# Step 1
x ^= y
# Step 2
y ^= x
# Step 3
x ^= y

print("x =", x)  # Output: x = 10
print("y =", y)  # Output: y = 5
