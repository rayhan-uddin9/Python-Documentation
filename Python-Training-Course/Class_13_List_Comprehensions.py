# Class 13 - List Comprehensions

# Normal way to create a list
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)      # [1, 4, 9, 16, 25]

# Same thing with list comprehension - shorter
squares = [i * i for i in range(1, 6)]
print(squares)      # [1, 4, 9, 16, 25]

# With condition - only even numbers
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)        # [2, 4, 6, 8, 10]

# Convert all names to uppercase
names = ["ali", "sara", "omar"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALI', 'SARA', 'OMAR']

# practical example - filter passing students
marks = [45, 78, 32, 90, 55, 61]
passed = [mark for mark in marks if mark >= 50]
print(f"Passed: {passed}")
print(f"Total passed: {len(passed)}")
