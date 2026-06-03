# Class 16 - Object Oriented Programming Basics

# Create a class
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

    def get_grade(self):
        if self.gpa >= 3.5:
            return "Excellent"
        elif self.gpa >= 3.0:
            return "Good"
        else:
            return "Average"

# Create objects
student1 = Student("Rayhan", 22, 3.85)
student2 = Student("Sara", 20, 3.2)

# Use the object
student1.introduce()
print(student1.get_grade())     # Excellent

student2.introduce()
print(student2.get_grade())     # Good

# Access attributes
print(student1.name)            # Rayhan
print(student2.age)             # 20
