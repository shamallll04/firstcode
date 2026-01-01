# pandas_basics.py
# Day 7 – Pandas Basics

import pandas as pd

print("=== Pandas Basics ===")

# Create DataFrame
data = {
    "Name": ["Shamal", "Aman", "Riya", "Kiran"],
    "Marks": [85, 78, 92, 69],
    "Course": ["AI", "Cloud", "AI", "DevOps"]
}

df = pd.DataFrame(data)

# Display data
print("\nStudent Data:")
print(df)

# Show first 2 rows
print("\nFirst 2 rows:")
print(df.head(2))

# Calculate average marks
average = df["Marks"].mean()
print("\nAverage Marks:", average)

# Filter students with marks > 80
top_students = df[df["Marks"] > 80]
print("\nStudents with marks > 80:")
print(top_students)
