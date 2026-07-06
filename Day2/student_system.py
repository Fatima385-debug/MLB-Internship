
students = [] #dictionaries will be stored in this list

# Core features
def add_student():
    print("\nAdd Student")
    name = get_non_emptystr("Enter Name: ")

    roll_no = get_positive_int("Enter Roll Number: ")
    if roll_number_exists(roll_no):
        print(f"A student with roll number {roll_no} already exists. Cannot add duplicate.")
        return

    age = get_positive_int("Enter Age: ")
    course = get_non_emptystr("Enter Course: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "age": age,
        "course": course,
    }
    students.append(student)
    print(f"Student '{name}' added successfully!\n")


def view_all_students():
    print("\nAll Students")
    if not students:
        print("No student records found.\n")
        return

    print(f"{'Roll No':<10}{'Name':<20}{'Age':<6}{'Course':<20}")
    for student in students:
        print(f"{student['roll_no']:<10}{student['name']:<20}{student['age']:<6}{student['course']:<20}")
    print()


def search_student():
    print("\nSearch Student")
    if not students:
        print("No student records found.\n")
        return

    print("Search by:")
    print("1. Roll Number")
    print("2. Name")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        roll_no = get_positive_int("Enter roll number to search: ")
        student = find_student_by_roll(roll_no)
        if student:
            print("Student Found:")
            print(student)
        else:
            print(f"No student found with Roll Number {roll_no}.")

    elif choice == "2":
        name = get_non_emptystr("Enter Name to search: ").lower()
        results = [s for s in students if name in s["name"].lower()]
        if results:
            print(f"Found {len(results)} matching student(s):")
            for s in results:
                print(s)
        else:
            print(f"No student found with name matching '{name}'.")
    else:
        print("Invalid choice.")
    print()


def update_student():
    print("\nUpdate Student Information")
    if not students:
        print("No student records found.\n")
        return

    roll_no = get_positive_int("Enter roll number of student to update: ")
    student = find_student_by_roll(roll_no)

    if not student:
        print(f"No student found with roll number {roll_no}.\n")
        return

    print(f"Current details: {student}")
    print("Leave field blank to keep current value.")

    new_name = input(f"Enter new Name [{student['name']}]: ").strip()
    if new_name:
        student["name"] = new_name

    new_age = input(f"Enter new Age [{student['age']}]: ").strip()
    if new_age:
        if new_age.isdigit() and int(new_age) > 0:
            student["age"] = int(new_age)
        else:
            print("Invalid age input. Keeping previous value.")

    new_course = input(f"Enter new Course [{student['course']}]: ").strip()
    if new_course:
        student["course"] = new_course

    print("Student record updated successfully!\n")


def delete_student():
    print("\nDelete Student")
    if not students:
        print("No student records found.\n")
        return

    roll_no = get_positive_int("Enter roll number of student to delete: ")
    student = find_student_by_roll(roll_no)

    if not student:
        print(f"No student found with roll number {roll_no}.\n")
        return

    confirm = input(f"Are you sure you want to delete '{student['name']}' (Roll No: {roll_no})? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        print("Student record deleted successfully!\n")
    else:
        print("Deletion cancelled.\n")


def display_total_students():
    print(f"\nTotal number of students: {len(students)}\n")

# Input validation helpers
def get_non_emptystr(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")


def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Invalid input. Please enter a positive whole number.")


def roll_number_exists(roll_no):
    return any(student["roll_no"] == roll_no for student in students)


def find_student_by_roll(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None

# Menu-driven interface
def print_menu():
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Display Total Number of Students")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            display_total_students()
        elif choice == "0":
            print("Exiting Student Record Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.\n")


if __name__ == "__main__":
    main()
