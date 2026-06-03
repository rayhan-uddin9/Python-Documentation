# Class 30 - Final Project: Student Management System

import json
import os

# File to save data
DATA_FILE = "students_data.json"

# Load existing data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_data(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file)

# Add new student
def add_student(students):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gpa = float(input("Enter GPA: "))
    city = input("Enter city: ")
    students.append({
        "name": name,
        "age": age,
        "gpa": gpa,
        "city": city
    })
    save_data(students)
    print(f"{name} added successfully!")

# View all students
def view_all(students):
    if not students:
        print("No students found.")
        return
    print(f"\n{'No':<5}{'Name':<15}{'Age':<8}{'GPA':<8}{'City'}")
    print("-" * 45)
    for i, s in enumerate(students, 1):
        print(f"{i:<5}{s['name']:<15}{s['age']:<8}{s['gpa']:<8}{s['city']}")

# Search student by name
def search_student(students):
    name = input("Enter name to search: ")
    found = [s for s in students if name.lower() in s["name"].lower()]
    if found:
        for s in found:
            print(f"Name: {s['name']} | Age: {s['age']} | GPA: {s['gpa']} | City: {s['city']}")
    else:
        print("No student found.")

# Delete student
def delete_student(students):
    name = input("Enter name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_data(students)
            print(f"{name} deleted successfully!")
            return
    print("Student not found.")

# Show menu
def show_menu():
    print("\n=== Student Management System ===")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

# Main program
def main():
    students = load_data()
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

main()
