# Class 17 - OOP Inheritance

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Child class - inherits from Person
class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)     # call parent __init__
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying hard!")

# Another child class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# Create objects
student = Student("Rayhan", 22, 3.85)
teacher = Teacher("Mr. Ahmed", 40, "Python")

student.introduce()     # from parent class
student.study()         # from child class

teacher.introduce()     # from parent class
teacher.teach()         # from child class
