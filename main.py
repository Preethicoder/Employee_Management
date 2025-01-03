"""This is main"""
from employee_app import EmployeeApp
from storage.storage_json import STORAGEJSON







def main():
    """start point of application"""
    #intiliase the filepath
    storage = STORAGEJSON("data/employee_data.json")
    #pass storage object to EmployeeApp
    emp_app = EmployeeApp(storage)
    emp_app.run()



if __name__ == "__main__":
    main()
