import json
import os.path

from storage.employee_storage import STORAGE

# Initialize employee ID
employee_id_counter = 0
class EmployeeNotFoundError(Exception):
    """Exception raised when an employee is not found in the JSON."""
    def __init__(self,emp_id,message="Employee not found"):
        self.emp_id = emp_id
        self.message = f"{message}: ID{emp_id}"
        super().__init__(self.message)

class InvalidEmployeeDataError(Exception):
    """Exception raised for invalid employee data."""

    def __init__(self,field,message="Invalid data provided"):
        self.field = field
        self.message = f"{message}: {field}"
        super().__init__(self.message)

class STORAGEJSON(STORAGE):
    """
    A concrete implementation of the STORAGE abstract base class for storing employee data in a JSON file.

    This class provides methods for adding, updating, removing, and searching for employees,
    as well as listing all employees. Employee data is persisted in a JSON file.
    """

    def __init__(self, file_name):
        """
        Initialize the STORAGEJSON class with the specified file name.

        Args:
            file_name (str): Path to the JSON file used for storing employee data.
        """
        self.file_name = file_name

    def save_to_file(self, employee_data):
        """
        Save employee data to the JSON file.

        Args:
            employee_data (list[dict]): List of employee records to save.
        """
        with open(self.file_name, "w", encoding="utf-8") as handle:
            json.dump(employee_data, handle, indent=4)

    def load_from_file(self):
        """
        Load employee data from the JSON file. If the file does not exist, an empty list is created and saved.

        Returns:
            list[dict]: List of employee records.
        """
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", encoding="utf-8") as handle:
                json.dump([], handle)

        with open(self.file_name, "r", encoding="utf-8") as file_obj:
            data = json.load(file_obj)
            return data

    def get_emp_id(self):
        """
        Generate a new unique employee ID based on the current data.

        Returns:
            int: The next available employee ID.
        """
        emp_data = self.load_from_file()
        if not emp_data:
            return 1
        emp_id = max(data["id"] for data in emp_data)
        return emp_id + 1

    def add_employee(self, name, position, salary, skills):
        """
        Add a new employee to the JSON storage.

        """
        emp_id = self.get_emp_id()
        if not name:
            raise InvalidEmployeeDataError("name","Name cannot be empty")
        if salary <=0:
            raise InvalidEmployeeDataError("salary","Salary should be greater than zero")
        emp_data = {
            "id": emp_id,
            "name": name,
            "position": position,
            "salary": salary,
            "skills": skills
        }
        data = self.load_from_file()
        data.append(emp_data)
        self.save_to_file(data)

    def remove_employee(self, emp_id):
        """
        Remove an employee by their ID.
        """
        emp_data = self.load_from_file()
        new_data = [data for data in emp_data if data["id"] != emp_id]
        if len(emp_data) == len(new_data):
            raise EmployeeNotFoundError(emp_id)
        else:
            print(f"Employee with ID {emp_id} removed.")

        self.save_to_file(new_data)

    def update_salary(self, emp_id, salary):
        """
        Update the salary of an employee by their ID.

        Args:
            emp_id (int): The unique identifier of the employee.
            salary (float): The new salary to assign to the employee.
        """
        emp_data = self.load_from_file()
        flag = False
        for emp in emp_data:
            if emp["id"] == emp_id:
                flag = True
                emp["salary"] = salary
        if not flag:
            raise EmployeeNotFoundError(emp_id)
        else:
            print("Employee salary updated successfully.")
        self.save_to_file(emp_data)

    def find_by_skill(self, given_skill):
        """
        Find and display employees who possess a specific skill.

        Args:
            given_skill (str): The skill to search for.
        """
        emp_data = self.load_from_file()
        flag = False

        for emp in emp_data:
            for skill in emp["skills"]:
                if skill == given_skill:
                    flag = True
                    print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Salary: {emp['salary']}")

        if not flag:
            raise InvalidEmployeeDataError("skill","Employee with given skill not found")

    def find_by_position(self, position):
        """
        Find and display employees based on their position.

        """
        emp_data = self.load_from_file()
        flag = False

        for emp in emp_data:
            if emp["position"] == position:
                flag = True
                print(
                    f"ID: {emp['id']}, Name: {emp['name']}, "
                    f"Position: {emp['position']}, "
                    f"Skills: {emp['skills']}, Salary: {emp['salary']}")
        if not flag:
           raise InvalidEmployeeDataError("position","employee with given position not found")

    def list_all_employees(self):
        """
        List all employees stored in the JSON file.

        """
        return self.load_from_file()
