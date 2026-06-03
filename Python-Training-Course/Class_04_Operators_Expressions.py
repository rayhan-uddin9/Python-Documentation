# Class 04 - Operators and Expressions

a = 17
b = 5

# Arithmetic operators
print(a + b)   # 22  addition
print(a - b)   # 12  subtraction
print(a * b)   # 85  multiplication
print(a / b)   # 3.4 division - always returns float
print(a // b)  # 3   floor division - no decimal
print(a % b)   # 2   modulo - remainder
print(a ** b)  # 1419857 - power

# Comparison operators - return True or False
print(a > b)   # True
print(a < b)   # False
print(a == b)  # False
print(a != b)  # True

# Logical operators
x = True
y = False
print(x and y) # False - both must be True
print(x or y)  # True  - one is enough
print(not x)   # False - flips the value

# Practical example
age = 20
has_id = True
print(age >= 18 and has_id)  # True - can enter
