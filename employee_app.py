import sys

from storage.storage_json import EmployeeNotFoundError, InvalidEmployeeDataError

DISPLAY_MENU = """********** My Employees Database **********

Menu:
0. Exit
1. Add Employee
2. Remove Employee
3. Search for Employee by Position 
4. Search for Employee by Skill
5. Update Employee Salary
6. List Employees

 """


class EmployeeApp:
    """This class act as front end to interact with storage"""
    def __init__(self, storage):
        self._storage = storage
        print("storage", self._storage)

    def _command_add_employee(self):

        print("Add employee data")
        name = input("Enter Employee Name :")
        position = input("Enter Employee Position :")
        skills = input("Enter Employee skills :")
        salary = input("Enter Employee Salary :")
        try:
          self._storage.add_employee(name, position, salary, skills.split(","))
          print("Employee Added Successfully")
        except InvalidEmployeeDataError as e:
            print(e)

    def _command_remove_employee(self):
        delete_id = int(input("Enter Employee id to be deleted:"))
        try:
         self._storage.remove_employee(delete_id)
        except EmployeeNotFoundError as e:
            print(e)

    def _command_search_employee_position(self):
        position = input("Enter position to be searched:")
        try:
         self._storage.find_by_position(position)
        except InvalidEmployeeDataError as e:
            print(e)

    def _command_search_employee_skill(self):
        skill = input("Enter skill to be searched:")
        try :
         self._storage.find_by_skill(skill)
        except InvalidEmployeeDataError as e:
            print(e)

    def _command_update_employee(self):
        update_id = int(input("Enter Employee Id to be updated:"))
        salary = input("Enter the salary to be updated")
        try :
         self._storage.update_salary(update_id, salary)
        except EmployeeNotFoundError as e:
            print(e)

    def _command_list_employees(self):
        data = self._storage.list_all_employees()
        for emp in data:
            print(
                f"ID: {emp['id']}, Name: {emp['name']}, "
                f"Position: {emp['position']}, Salary: {emp['salary']}, "
                f"Skills: {', '.join(emp['skills'])}")

    def run(self):
        """Main function to display the menu and handle user inputs."""
        func_dict = {
            "1": self._command_add_employee,
            "2": self._command_remove_employee,
            "3": self._command_search_employee_position,
            "4": self._command_search_employee_skill,
            "5": self._command_update_employee,
            "6": self._command_list_employees

        }

        print(DISPLAY_MENU)
        while True:
            try:
                choice = input("Enter choice 1-6:")

                if choice == "0":
                    print("Bye!")
                    sys.exit()
                func_id = func_dict.get(choice)

                if func_id:
                    func_id()
                else:
                    print("Invalid option. Please enter a valid choice.")
            except KeyError:
                print("Invalid option. Please try again.")
            except Exception as e:
                print("UnExcepted error occurred", e)

            input("\nPress Enter to display the menu...")
            print(DISPLAY_MENU)
