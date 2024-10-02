students = {}


def view_data():
    student_id = input("Enter the student ID: ")
    data_requested = input("Enter the data you want to view: \n1. Student Name\n2. Date of Birth\n3. Address\n")
    if students.get(student_id) is not None:
        if data_requested == "1":
            print(f"Student Name: {students[student_id]}")
        elif data_requested == "2":
            print(f"Date of Birth: {students[student_id]['dateOfBirth']}")
        elif data_requested == "3":
            print(f"Address: {students[student_id]['address']}")
        else:
            print("Invalid choice")
            view_data()
    print("Do you want see data for another Student?")
    choice = input("Enter Y for Yes and N for No: ")
    if choice == "Y":
        add_students()
    else:
        menu()


def add_student_data():
    student_id = input("Enter the student ID: ")
    date_of_birth = input("Enter the date of birth: ")
    address = input("Enter the address: ")
    students[student_id] = {student_id: students[student_id], "dateOfBirth": date_of_birth, "address": address}
    print(students[student_id])
    print("Do you want to more data for another Student?")
    choice = input("Enter Y for Yes and N for No: ")
    if choice == "Y":
        add_student_data()
    else:
        menu()


def add_students():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        student_id = input("Enter the student ID: ")
        student_name = input("Enter the student name: ")
        print(f"Student ID: {student_id}")
        print(f"Student Name: {student_name}")
        students[student_id] = student_name
    print("Do you want to add another Student?")
    choice = input("Enter Y for Yes and N for No: ")
    if choice == "Y":
        add_students()
    else:
        menu()


def find_student():
    student_id = input("Enter the student ID: ")
    if students.get(student_id) is not None:
        print(f"Student Name: {students[student_id]}")
    else:
        print("Student not found")
    print("Do you want to search for another Student?")
    choice = input("Enter Y for Yes and N for No: ")
    if choice == "Y":
        find_student()
    else:
        menu()


def menu():
    print("1. Add student")
    print("2. Find student")
    print("3. More Student Data")
    print("4. View Data")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice < 4:
        if choice == 1:
            add_students()
        elif choice == 2:
            find_student()
        elif choice == 3:
            add_student_data()
        elif choice == 4:
            view_data()
        elif choice == 5:
            exit()
        else:
            print("Invalid choice")
            menu()


menu()