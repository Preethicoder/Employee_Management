from abc import ABC, abstractmethod


class STORAGE(ABC):
    """
    Abstract base class for employee storage systems.

    This class defines the interface for any storage system that handles
    employee data. Concrete implementations must provide definitions
    for all abstract methods to manage employee information such as
    adding, removing, searching, updating, and listing employees.
    """

    @abstractmethod
    def add_employee(self, name, position, salary, skills):
        """
        Add a new employee to the storage.
        """


    @abstractmethod
    def remove_employee(self, emp_id):
        """
        Remove an employee from the storage by their ID.
        """


    @abstractmethod
    def find_by_position(self, position):
        """
        Find employees based on their position.
        """


    @abstractmethod
    def find_by_skill(self, skill):
        """
        Find employees who possess a specific skill.

        """


    @abstractmethod
    def update_salary(self, emp_id, salary):
        """
        Update the salary of an employee.

        """


    @abstractmethod
    def list_all_employees(self):
        """
        List all employees in the storage.
        """
