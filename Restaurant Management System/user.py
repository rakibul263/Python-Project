from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        self.age = age
        self.designation = designation
        self.salary = salary
        super().__init__(name, phone, email, address)

# emp = Employee("Shuvo", "01793867764", "rakibulhasanshuvo206@gmail.com", "Mipur-13", 21, "Senior Engineer", 120000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employee = [] #This is our database

    def add_employee(self, name, phone, email, address, age, designation, salary):
        employee = Employee(name, phone, email, address, age, designation, salary) #create an object of Employee class
        self.employee.append(employee)
        print(f'{name} is added!')
    
    def view_employee(self):
        print('Employee List : ')
        for emp in self.employee:
            print(emp.name, emp.phone, emp.email, emp.address, emp.age, emp.designation, emp.salary)

ad = Admin("Shuvo", "01793867764", "rakibulhasanshuvo206@gmail.com", "Mipur-13")
ad.add_employee("Rakibul", "01793864323", "rakibulhasanshuvo1263@gmail.com", "Mipur-2", 20, "Engineer", 10000)
ad.view_employee()