# data_visualization.py
# Day 8 – Data Visualization using Matplotlib

import matplotlib.pyplot as plt

# Data
students = ["Shamal", "Aman", "Riya", "Kiran"]
marks = [85, 78, 92, 69]

# Line Chart
plt.plot(students, marks)
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
