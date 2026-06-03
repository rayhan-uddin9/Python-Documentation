# Class 14 - File Handling

# Write to a file
with open("students.txt", "w") as file:
    file.write("Ali\n")
    file.write("Sara\n")
    file.write("Rayhan\n")
print("File created!")

# Read the file
with open("students.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

# Append to file - add without deleting old content
with open("students.txt", "a") as file:
    file.write("Omar\n")

# Read again to confirm
with open("students.txt", "r") as file:
    print(file.read())
