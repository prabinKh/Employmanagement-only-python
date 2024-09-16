from employee import *
class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('Enter employee data')
        name =input('Enter employe name: ')
        age = input('Enter employee age: ')
        salary = input('Enter employee salary: ')
        self.employees.append(Employee(name,age,salary))

    def list_employee(self):
        if len(self.employees) ==0:
            print('\n Employee list is Empty')

            return
        
        else:
            for emp in self.employees:
                print(emp)


    def find_employee_by_name(self,name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        
        return None
    
    def update_salary_by_name(self,name,salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('Error, NO employe found')

        else:
            emp.salary = salary

    def delete_employee_by_age(self, age_from, age_to):
    # Convert the age to integer for comparison
        to_remove = [emp for emp in self.employees if age_from <= int(emp.age) <= age_to]
        for emp in to_remove:
            print(f'Deleting employee {emp.name}')
            self.employees.remove(emp)
