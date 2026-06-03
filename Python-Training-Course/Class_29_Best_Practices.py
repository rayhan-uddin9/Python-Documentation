# Class 29 - Python Best Practices and Clean Code

# 1. Use clear variable names
# bad
x = 22
# good
student_age = 22

# 2. Use constants for fixed values
MAX_STUDENTS = 30
PASSING_GRADE = 50

# 3. One function one job
# bad - does too many things
def process(name, age, score):
    print(f"Name: {name}")
    if score >= 50:
        print("Passed")
    # send email...

# good - each function has one job
def display_student(name):
    print(f"Name: {name}")

def check_result(score):
    return "Passed" if score >= PASSING_GRADE else "Failed"

# 4. Write docstrings
def calculate_average(marks):
    """
    Calculate average of a list of marks.
    Args:
        marks (list): list of numbers
    Returns:
        float: average value
    """
    return sum(marks) / len(marks)

# 5. DRY - Don't Repeat Yourself
# bad
print("Student: Ali, Grade: A")
print("Student: Sara, Grade: B")

# good
students = [("Ali", "A"), ("Sara", "B")]
for name, grade in students:
    print(f"Student: {name}, Grade: {grade}")

# 6. Handle errors properly
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(calculate_average([80, 90, 75, 85]))
print(check_result(65))
print(divide(10, 0))
