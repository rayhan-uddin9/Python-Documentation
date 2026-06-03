# Class 25 - Data Analysis with Pandas

# First install pandas
# pip install pandas

import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Rayhan", "Sara", "Omar", "Ali"],
    "Age": [22, 20, 21, 23],
    "GPA": [3.85, 3.90, 3.20, 3.50],
    "City": ["Chittagong", "Dhaka", "Sylhet", "Dhaka"]
}

df = pd.DataFrame(data)
print(df)

# Basic info
print(df.shape)         # (4, 4) - 4 rows, 4 columns
print(df.columns)       # column names
print(df.dtypes)        # data types

# Access a column
print(df["Name"])
print(df["GPA"])

# Filter rows
high_gpa = df[df["GPA"] >= 3.5]
print(high_gpa)

# Basic statistics
print(df["GPA"].mean())     # average GPA
print(df["GPA"].max())      # highest GPA
print(df["GPA"].min())      # lowest GPA

# Save to CSV
df.to_csv("students_data.csv", index=False)
print("Saved to CSV!")

# Read from CSV
df2 = pd.read_csv("students_data.csv")
print(df2)
