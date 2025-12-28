# lists_dicts.py
# Day 4 – Lists and Dictionaries

print("=== Lists and Dictionaries ===")

# LIST example
subjects = ["Maths", "Science", "English", "Computer"]

print("\nSubjects List:")
for subject in subjects:
    print(subject)

# Adding new item
subjects.append("AI")
print("\nUpdated Subjects List:", subjects)

# DICTIONARY example
student = {
    "name": "Shamal",
    "age": 20,
    "course": "BCA",
    "specialization": "AI • Cloud • DevOps"
}

print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)

# List of marks
marks = [75, 68, 82]

total = sum(marks)
average = total / len(marks)

print("\nTotal Marks:", total)
print("Average Marks:", average)
