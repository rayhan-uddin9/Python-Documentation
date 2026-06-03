# Class 28 - Building a Simple CLI Application

# A simple menu driven program

def show_menu():
    print("\n--- Student Manager ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Exit")

students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    gpa = float(input("Enter GPA: "))
    students.append({"name": name, "age": age, "gpa": gpa})
    print(f"{name} added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
        return
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} | Age: {student['age']} | GPA: {student['gpa']}")

def search_student():
    name = input("Enter name to search: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Found: {student}")
            return
    print("Student not found.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
