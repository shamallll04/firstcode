# student_marks.py
# Mini Project - Student Marks Management System

print("===== Student Marks System =====")

# Input student details
name = input("Enter student name: ")

# Input marks
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Calculate total and average
total = maths + science + english
average = total / 3

# Result logic
if average >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Output
print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Result:", result)
