class Employee:
    def calculate_salary(self):
        print("Calculating salary for an employee...")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for a manager...")
        # Specific salary calculation logic for a manager can be added here

# Create instances of Employee and Manager
employee = Employee()
manager = Manager()

# Call the calculate_salary() method for each object
employee.calculate_salary()
manager.calculate_salary()