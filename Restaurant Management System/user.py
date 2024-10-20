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

    def add_employee(self, employee, restaurant):
        restaurant.add_employee(employee)
        
    def view_employee(self, restaurant):
       restaurant.view_employee()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employee = [] #This is our database
    
    def add_employee(self, employee):
        self.employee.append(employee)

    def view_employee(self):
        print('Employee List : ')
        for emp in self.employee:
            print(emp.name, emp.phone, emp.email, emp.address, emp.age, emp.designation, emp.salary)

class Manu :
    def __init__(self):
        self.items = [] #database of an items
    
    def add_manu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() ==  item_name.lower():
                return item
            return None
        
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'This {item_name} is deleted!!')
        else:
            print(f'Item not found')
        

ad = Admin("Shuvo", "01793867764", "rakibulhasanshuvo206@gmail.com", "Mipur-13")
ad.add_employee("Rakibul", "01793864323", "rakibulhasanshuvo1263@gmail.com", "Mipur-2", 20, "Engineer", 10000)
ad.view_employee()