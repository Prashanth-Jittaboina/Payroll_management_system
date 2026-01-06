import csv

FILE_NAME = "payroll.csv"


 
# Base Employee class
 
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_tax(self):
        return self.salary * 0.10  # 10% tax

    def calculate_net_salary(self):
        tax = self.calculate_tax()
        return self.salary - tax


 
# Payroll Manager class
 
class PayrollManager:

    def __init__(self):
        self.create_file()

    # Creating  CSV file if not exists
    def create_file(self):
        try:
            with open(FILE_NAME, "x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee ID", "Name", "Salary", "Tax", "Net Salary"])
        except FileExistsError:
            pass

    #  adding employees for generating the payrolles
    def add_employee(self):
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")

        try:
            salary = float(input("Enter salary: "))
        except ValueError:
            print("Invalid salary!")
            return

        employee = Employee(emp_id, name, salary)

        tax = employee.calculate_tax()
        net_salary = employee.calculate_net_salary()

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, name, salary, tax, net_salary])

        print("\nPayslip Generated")
        print("------------------")
        print(f"Employee ID : {emp_id}")
        print(f"Name        : {name}")
        print(f"Salary      : {salary}")
        print(f"Tax (10%)   : {tax}")
        print(f"Net Salary : {net_salary}")

    # for viewing the payroles of all the employees
    def view_payroll(self):
        print("\nPayroll Records:\n")

        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(
                    f"ID: {row['Employee ID']}, "
                    f"Name: {row['Name']}, "
                    f"Net Salary: {row['Net Salary']}"
                )


 
def main():
    manager = PayrollManager()

    while True:
        print("\n--- Employee Payroll Management System ---")
        print("1. Add Employee")
        print("2. View Payroll")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_payroll()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


main()
