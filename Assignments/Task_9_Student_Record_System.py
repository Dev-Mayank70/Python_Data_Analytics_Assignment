# Task 9: Student Record Management System

students = []


# Function to add a student
def add_student():
    print("\n----- Add Student -----")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    branch = input("Enter branch: ")
    college = input("Enter college name: ")

    student = {
        "name": name,
        "age": age,
        "branch": branch,
        "college": college
    }

    students.append(student)

    print("\nStudent record added successfully!")


# Function to display all students
def display_students():
    print("\n----- All Student Records -----")

    if len(students) == 0:
        print("No student records found.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Branch :", student["branch"])
        print("College:", student["college"])


# Function to search student
def search_student():
    print("\n----- Search Student -----")

    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Branch :", student["branch"])
            print("College:", student["college"])

            found = True
            break

    if not found:
        print("Student record not found.")


# Function to delete student
def delete_student():
    print("\n----- Delete Student -----")

    delete_name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student record not found.")


# Main menu
while True:

    print("\n==============================")
    print(" Student Record Management")
    print("==============================")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the Student Record Management System.")
        break

    else:
        print("Invalid choice. Please try again.")