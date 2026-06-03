# Class 11 - Dictionaries

# Create a dictionary
student = {
    "name": "Rayhan",
    "age": 22,
    "gpa": 3.85
}

# Access value by key
print(student["name"])      # Rayhan
print(student["gpa"])       # 3.85

# Change a value
student["age"] = 23
print(student["age"])       # 23

# Add new key
student["city"] = "Chittagong"
print(student)

# Remove a key
del student["city"]
print(student)

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# practical example - word counter
sentence = "python is easy and python is fun"
words = sentence.split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)
