from employee import *
## thsi Employees manager inharite the Empoyee claass from the employee.py 
class EmployeesManager:
    def __init__(self):
        self.employees = [] #it is empty lest to store the employees data

    def add_employee(self):
        print('Enter employee data')
        name =input('Enter employe name: ')
        age = input('Enter employee age: ')
        salary = input('Enter employee salary: ')
        self.employees.append(Employee(name,age,salary)) ## if costomer add more then one add employ or request sand it
                                                        ## is add the employ 

    def list_employee(self):
        if len(self.employees) ==0:
            print('\n Employee list is Empty') #if employ are empty it's return this message

            return
        
        else:
            for emp in self.employees: # else it is eterate all the list one by one and save the emp and display it
                print(emp)


    def find_employee_by_name(self,name):   # when the use called the this method it take the name parameter when 
                                              # user enter the name and  this inpute value compaire to the emplyees list or data base 
        for emp in self.employees:
            if emp.name == name:
                return emp
        
        return None
    
    def update_salary_by_name(self,name,salary):  ## it takes the two parameter name and salary if name is exists i
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('Error, NO employe found')

        else:
            emp.salary = salary ## this allow to over the salary field 

    def delete_employee_by_age(self, age_from, age_to): ## its take the two argument  and compaite the employes age if it is inside the age-from to age_to it's gona be delete
        
    # Convert the age to integer for comparison
        to_remove = [emp for emp in self.employees if age_from <= int(emp.age) <= age_to]
        for emp in to_remove:
            print(f'Deleting employee {emp.name}')
            self.employees.remove(emp)
