# I am initilizing the values
employees = {
    # 101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    # 102: {'name': 'Ravi', 'age': 30, 'department': 'IT', 'salary': 60000}
}
def add_employee():
    try:
        # print(employees)#[-1])
        # last_emp_id = list(employees.keys())[-1]
        # last_id = next(reversed(employees))
        # if last_emp_id == last_id:
        #     print(last_id)
        # emp_id = next(reversed(employees))+1#int(input("Enter Employee ID: "))
        # print(emp_id)
        emp_id = int(input("Enter Employee ID:"))
        if emp_id in employees:
            print("Employee ID already exists. Try a different ID.")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = int(input("Enter Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("✅ Employee added successfully!\n")

    except ValueError:
        print("Invalid input. Please enter Numeric data only.\n")


# Step 4: View Employees
def view_employees():
    if not employees:
        print("No employees available.\n")
        return

    print("\n--- Employee List ---")
    print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(
        "ID", "Name", "Age", "Department", "Salary"))

    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(
            emp_id,
            details['name'],
            details['age'],
            details['department'],
            details['salary']
        ))
    print()


# Step 5: Search Employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))

        if emp_id in employees:
            emp = employees[emp_id]
            print("\nEmployee Found:")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}\n")
        else:
            print("Employee not found.\n")

    except ValueError:
        print("Invalid input.\n")
if __name__ == "__main__":
    while True:
        print("-----Employee Management System -----")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        ch = input("Enter your choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            view_employees()
        elif ch == '3':
            search_employee()
        elif ch == '4':
            print("Thank you for using EMS 👋")
            break
        else:
            print("Invalid choice. Please try again.\n")
            