# Class 03 - User Input and Output

# input() asks the user to type something
# input() always returns a string

name = input("Enter your name: ")
print("Hello, " + name)

# If you need a number, convert it
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")

# print() with multiple values
print("Name:", name, "Age:", age)

# Change separator between values
print("Name:", name, "Age:", age, sep=" | ")

# Print on same line using end
print("Loading", end=" ")
print("...")

# f-string formatting
gpa = 3.856
print(f"Your GPA is {gpa:.2f}")  # shows only 2 decimal places
