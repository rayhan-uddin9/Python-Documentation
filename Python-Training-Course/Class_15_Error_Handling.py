# Class 15 - Error Handling

# Without error handling - program crashes
# print(10 / 0)   # ZeroDivisionError

# With try and except - program keeps running
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handle wrong input type
try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Please enter a number only!")

# finally - always runs no matter what
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program finished.")

# practical example - safe calculator
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))    # 5.0
print(divide(10, 0))    # Cannot divide by zero
