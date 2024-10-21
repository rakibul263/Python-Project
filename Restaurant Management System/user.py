from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User) :
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None

    def view_menu_item(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print("Item not found !")
    
    def view_cart(self):
        print("*****View Cart*****")
        print(f'Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{item.quantity}')
        print(f'Total Price: {self.cart.total_price}')
        

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self,item):
        if item in self.items:
            self.items[item]+=item.quantity
        else:
            self.items[item] =item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item]
    
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items)
    
    def clear(self):
        self.items = {}

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
    
    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employee = [] #This is our database
        self.menu = Food_item()

    def add_employee(self, employee):
        self.employee.append(employee)

    def view_employee(self):
        print('Employee List : ')
        for emp in self.employee:
            print(emp.name, emp.phone, emp.email, emp.address, emp.age, emp.designation, emp.salary)

class menu :
    def __init__(self):
        self.items = [] #database of an items
    
    def add_menu_item(self, item):
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
    
    def show_menu(self):
        print('******menu******')
        print(f'Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

class Food_item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

mn = menu()
item = Food_item('Pizza', 656, '12-inchi')
mn.add_menu_item(item)
mn.show_menu()
