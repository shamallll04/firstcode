# student_manager.py
# Day 5 Project – Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        print("\nStudent List:")
        for i, student in enumerate(students, start=1):
            print(i, "-", student["name"], "| Marks:", student["marks"])
        print()


def calculate_average():
    if len(students) == 0:
        print("No data to calculate.\n")
        return

    total = 0
    for student in students:
        total += student["marks"]

    average = total / len(students)
    print("Average Marks:", average, "\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
