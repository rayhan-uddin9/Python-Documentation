# Class 26 - Data Visualization with Matplotlib

# First install matplotlib
# pip install matplotlib

import matplotlib.pyplot as plt

# Simple line chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 350, 300, 400, 450]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar chart
students = ["Ali", "Sara", "Omar", "Rayhan"]
gpa = [3.5, 3.9, 3.2, 3.85]

plt.bar(students, gpa, color="blue")
plt.title("Student GPA")
plt.xlabel("Student")
plt.ylabel("GPA")
plt.show()

# Pie chart
subjects = ["Python", "Math", "English", "Science"]
hours = [40, 30, 20, 10]

plt.pie(hours, labels=subjects, autopct="%1.1f%%")
plt.title("Study Hours by Subject")
plt.show()
