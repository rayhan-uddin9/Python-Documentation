# Class 12 - String Methods

name = "  rayhan uddin  "

# Remove extra spaces
print(name.strip())         # rayhan uddin

# Upper and lower case
print(name.strip().upper()) # RAYHAN UDDIN
print(name.strip().lower()) # rayhan uddin

# Check start and end
email = "rayhan@gmail.com"
print(email.startswith("rayhan"))   # True
print(email.endswith(".com"))       # True

# Replace text
sentence = "I love Java"
print(sentence.replace("Java", "Python"))   # I love Python

# Split string into list
data = "Ali,Sara,Omar,Rayhan"
students = data.split(",")
print(students)     # ['Ali', 'Sara', 'Omar', 'Rayhan']

# Join list into string
joined = " - ".join(students)
print(joined)       # Ali - Sara - Omar - Rayhan

# Check if number
code = "12345"
print(code.isdigit())   # True

# practical example
full_name = "  muhammad rayhan uddin  "
clean = full_name.strip().title()
print(clean)        # Muhammad Rayhan Uddin
