# Class 19 - Lambda Functions

# Normal function
def square(x):
    return x * x

print(square(5))        # 25

# Same thing with lambda
square = lambda x: x * x
print(square(5))        # 25

# lambda with two parameters
add = lambda a, b: a + b
print(add(3, 4))        # 7

# map() - apply function to every item in list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)          # [1, 4, 9, 16, 25]

# filter() - keep items that match condition
numbers = [10, 25, 30, 45, 50]
above_30 = list(filter(lambda x: x > 30, numbers))
print(above_30)         # [45, 50]

# practical example - sort students by gpa
students = [
    {"name": "Ali", "gpa": 3.5},
    {"name": "Sara", "gpa": 3.9},
    {"name": "Omar", "gpa": 3.2}
]
sorted_students = sorted(students, key=lambda s: s["gpa"], reverse=True)
for s in sorted_students:
    print(f"{s['name']}: {s['gpa']}")
