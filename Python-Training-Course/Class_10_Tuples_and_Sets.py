# Class 10 - Tuples and Sets

# Tuple - cannot be changed after creation
colors = ("red", "green", "blue")
print(colors[0])        # red
# colors[0] = "yellow"  # this will crash - tuples are immutable

# When to use tuple - data that should not change
coordinates = (23.7, 90.4)
print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")

# Set - only unique values, no duplicates
numbers = {1, 2, 3, 2, 1, 4}
print(numbers)          # {1, 2, 3, 4} - duplicates removed

# Add and remove from set
numbers.add(5)
numbers.remove(1)
print(numbers)

# practical example - find unique students
attendance = ["Ali", "Sara", "Ali", "Omar", "Sara", "Rayhan"]
unique_students = set(attendance)
print(f"Unique students: {unique_students}")
print(f"Total unique: {len(unique_students)}")
