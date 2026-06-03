# Class 27 - SQLite Database with Python

import sqlite3

# Connect to database - creates file if not exists
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gpa REAL
    )
""")
conn.commit()
print("Table created!")

# Insert data
cursor.execute("INSERT INTO students (name, age, gpa) VALUES (?, ?, ?)",
               ("Rayhan", 22, 3.85))
cursor.execute("INSERT INTO students (name, age, gpa) VALUES (?, ?, ?)",
               ("Sara", 20, 3.90))
cursor.execute("INSERT INTO students (name, age, gpa) VALUES (?, ?, ?)",
               ("Omar", 21, 3.20))
conn.commit()
print("Data inserted!")

# Read all data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Filter data
cursor.execute("SELECT * FROM students WHERE gpa >= 3.5")
top_students = cursor.fetchall()
print("Top students:")
for student in top_students:
    print(student)

# Update data
cursor.execute("UPDATE students SET gpa = 3.95 WHERE name = 'Rayhan'")
conn.commit()
print("Data updated!")

# Delete data
cursor.execute("DELETE FROM students WHERE name = 'Omar'")
conn.commit()
print("Data deleted!")

# Close connection
conn.close()
