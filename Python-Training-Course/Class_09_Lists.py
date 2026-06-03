# Class 09 - Lists

# Create a list
students = ["Ali", "Sara", "Omar", "Rayhan"]

# Access by index
print(students[0])      # Ali
print(students[-1])     # Rayhan - last item

# Change an item
students[1] = "Fatima"
print(students)

# Add and remove items
students.append("Noor")     # add to end
students.remove("Omar")     # remove by value
print(students)

# List length
print(len(students))    # 4

# Loop through list
for student in students:
    print(student)

# practical example - calculate average
marks = [85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print(f"Average mark: {average:.2f}")
