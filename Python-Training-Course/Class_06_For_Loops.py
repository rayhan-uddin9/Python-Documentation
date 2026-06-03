# Class 06 - For Loops

# Basic for loop
for i in range(5):
    print(i)        # prints 0 1 2 3 4

# range with start and stop
for i in range(1, 6):
    print(i)        # prints 1 2 3 4 5

# range with step
for i in range(0, 10, 2):
    print(i)        # prints 0 2 4 6 8

# loop through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# practical example - multiplication table
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
