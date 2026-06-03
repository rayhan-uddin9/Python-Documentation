# Class 02 - Variables and Data Types

# A variable stores a value
name = "Rayhan"
age = 22
gpa = 3.85
is_student = True

print(name)
print(age)
print(gpa)
print(is_student)

# Check the type of a variable
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(gpa))       # <class 'float'>
print(type(is_student))# <class 'bool'>

# Changing a variable
score = 10
score = 95
print(score)           # 95

# Mixing string and number - wrong way
# print("My age is " + age)  # this will crash

# Correct way
print("My age is " + str(age))

# Even easier with f-string
print(f"My age is {age}")

# None means no value
result = None
print(result)          # None
