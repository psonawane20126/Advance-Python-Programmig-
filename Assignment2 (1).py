# Decorator
def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n========== EMPLOYEE REPORT ==========")
        func(*args, **kwargs)
        print("=====================================\n")
    return wrapper


class EmployeeReport:
    company_name = "ABC Company"

    # Constructor
    def __init__(self, emp_id, emp_name, emp_post, rating):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_post = emp_post
        self.rating = rating

    # Class Method
    @classmethod
    def change_company(cls, name):
        cls.company_name = name

    # Magic Method
    def __str__(self):
        return (f"Company Name : {EmployeeReport.company_name}\n"
                f"Employee ID  : {self.emp_id}\n"
                f"Employee Name: {self.emp_name}\n"
                f"Employee Post: {self.emp_post}\n"
                f"Rating       : {self.rating}")

    # Decorated Method
    @report_decorator
    def generate_report(self):
        print(self)


# Main Program

company = input("Enter Company Name: ")
EmployeeReport.change_company(company)

n = int(input("How many employee reports do you want to create? "))

reports = []

for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    emp_id = input("Employee ID: ")
    emp_name = input("Employee Name: ")
    emp_post = input("Employee Post: ")
    rating = input("Employee Rating: ")

    report = EmployeeReport(emp_id, emp_name, emp_post, rating)
    reports.append(report)

print("\nGenerated Employee Reports:")

for report in reports:
    report.generate_report()