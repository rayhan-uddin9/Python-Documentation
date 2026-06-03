# Class 08 - Functions

# Basic function
def say_hello():
    print("Hello everyone!")

say_hello()     # call the function

# Function with parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Rayhan")
greet("Sara")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print(result)   # 15

# Function with default parameter
def greet_student(name, course="Python"):
    print(f"{name} is studying {course}")

greet_student("Ali")
greet_student("Omar", "Data Science")

# practical example - calculate grade
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(get_grade(95))    # A
print(get_grade(73))    # C
