# Class 20 - Regular Expressions

import re

# Check if pattern matches
email = "rayhan@gmail.com"
pattern = r"@"
if re.search(pattern, email):
    print("Valid email format")     # Valid email format

# Find all numbers in a string
text = "I am 22 years old and my score is 95"
numbers = re.findall(r"\d+", text)
print(numbers)          # ['22', '95']

# Replace pattern
sentence = "I love   Python   programming"
clean = re.sub(r"\s+", " ", sentence)
print(clean)            # I love Python programming

# Validate phone number
def check_phone(number):
    pattern = r"^\d{11}$"
    if re.match(pattern, number):
        return "Valid phone number"
    return "Invalid phone number"

print(check_phone("01812345678"))   # Valid
print(check_phone("0181234"))       # Invalid

# practical example - extract emails from text
text = "Contact us at rayhan@gmail.com or support@python.org"
emails = re.findall(r"\b[\w.]+@[\w.]+\.\w+\b", text)
print(emails)
