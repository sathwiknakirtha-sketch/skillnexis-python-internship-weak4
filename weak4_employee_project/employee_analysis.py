import pandas as pd


class EmployeeAnalyzer:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    # Load CSV file
    def load_data(self):
        self.data = pd.read_csv(self.file_name)

        print("\nEmployee Data:")
        print(self.data)

    # Calculate average salary
    def average_salary(self):
        average = self.data["Salary"].mean()

        print("\nAverage Salary:")
        print(average)

    # Count employees in each department
    def department_count(self):
        count = self.data["Department"].value_counts()

        print("\nEmployees in Each Department:")
        print(count)

    # Filter employees above salary threshold
    def filter_salary(self, threshold):

        result = self.data[self.data["Salary"] > threshold]

        print("\nEmployees with Salary Above", threshold)
        print(result)

        return result

    # Export filtered data
    def export_data(self, result):

        result.to_csv("high_salary_employees.csv", index=False)

        print("\nFiltered data exported successfully!")
        print("File created: high_salary_employees.csv")


# Main program
analyzer = EmployeeAnalyzer("employees.csv")

# Step 1: Load CSV
analyzer.load_data()

# Step 2: Calculate average salary
analyzer.average_salary()

# Step 3: Count departments
analyzer.department_count()

# Step 4: Filter salary above 60000
high_salary = analyzer.filter_salary(60000)

# Step 5: Export results
analyzer.export_data(high_salary)

print("\nProject completed successfully!")