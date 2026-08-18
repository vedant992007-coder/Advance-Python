class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def categorize(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      : ₹", self.salary)
        print("Category    :", self.categorize())
        print("-" * 35)

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all(self):
        print("\nEmployee Information")
        print("=" * 35)

        for employee in self.employees:
            employee.display()
# Create Company object
company = Company()

# Add employees
company.add_employee(Employee(101, "Rahul", 75000))
company.add_employee(Employee(102, "Aman", 55000))
company.add_employee(Employee(103, "Riya", 35000))

# Display all employees
company.display_all
