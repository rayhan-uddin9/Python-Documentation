# Class 21 - Working with JSON and CSV

import json
import csv

# JSON - convert dictionary to JSON string
student = {
    "name": "Rayhan",
    "age": 22,
    "gpa": 3.85
}

json_string = json.dumps(student)
print(json_string)      # {"name": "Rayhan", "age": 22, "gpa": 3.85}

# Convert JSON string back to dictionary
data = json.loads(json_string)
print(data["name"])     # Rayhan

# Save JSON to file
with open("student.json", "w") as file:
    json.dump(student, file)
print("JSON file saved!")

# Read JSON from file
with open("student.json", "r") as file:
    loaded = json.load(file)
    print(loaded)

# CSV - write to CSV file
students = [
    ["Name", "Age", "GPA"],
    ["Rayhan", 22, 3.85],
    ["Sara", 20, 3.9],
    ["Omar", 21, 3.2]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("CSV file saved!")

# Read CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
