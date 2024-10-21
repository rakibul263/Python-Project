from abc import ABC
from Order import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu_item(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            item.quantity = quantity
            self.cart.add_item(item)
            print("Item added!!")
        else:
            print("Item not found !")
    
    def view_cart(self):
        print("*****View Cart*****")
        print(f'Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{item.quantity}')
        print(f'Total Price: {self.cart.total_price()}')
    
    def pay_bill(self):
        print(f'Your total bill is {self.cart.total_price()} paid successfully!!')
        
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        self.age = age
        self.designation = designation
        self.salary = salary
        super().__init__(name, phone, email, address)

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
