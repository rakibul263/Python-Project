import random
import os

class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type  # current or savings
        self.loan_count = 0
        self.statement = []
        self.balance = 0
        self.account_number = random.randint(1000000000, 9999999999)
        # self.dictionary = {self.name : self.account_number}
    
    def deposit(self, amount):
        if amount <= 0 or amount == "":
            return f'Invalid deposit amount.'
        self.balance += amount
        self.statement.append(f"Deposited: {amount}")
        return f"{amount} deposited successfully."

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance.'
        elif amount < 0:
            return 'Invalid withdrawal amount.'
        else:
            self.balance -= amount
            self.statement.append(f"Withdrawn: {amount}")
            return f"{amount} withdrawn successfully."

    def check_balance(self):
        return f"Your balance is {self.balance}"

    def transaction_history(self):
        return self.statement

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.statement.append(f"Loan Taken: {amount}")
            return f"Loan of {amount} approved."
        else:
            return "Loan limit exceeded."

    def transfer_amount(self, amount, receiver_account):
        if amount > self.balance:
            return 'Insufficient balance.'
        elif amount < 0:
            return 'Invalid transfer amount.'
        else:
            receiver_account.deposit(amount)
            self.balance -= amount
            self.statement.append(f"Transferred {amount} to {receiver_account.account_number}")
            return f"Successfully transferred {amount}."

    def __repr__(self):
        return (f'Account Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}'
                f'\nAccount Type: {self.account_type}\nBalance: {self.balance}\n'
                f'Account Number: {self.account_number}\nLoan Count: {self.loan_count}\n'
                f'Statement: {self.statement}')


# ac = Account("Shuvo", "shuvo@gmail.com", "Mirpur-13", "current")
# ac.deposit(1000)
# ac.withdraw(500)
# # print(ac.check_balance())
# # print(ac)
# # print(ac.transaction_history())
# tp = ac.transfer_amount(300, "")
# print(tp)
# ck = ac.check_balance()
# print(ck)
# ac.take_loan(5000)
# print(ac)

class Admin:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.loan_amount = 0
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts.append(account)
        return f"Account Name        : {name}\nAccount number      : {account.account_number}"

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return f"Account {account_number} deleted successfully."
        return "Account not found."

    def see_all_users(self):
        if not self.accounts:
            return "No accounts available."
        return [str(account) for account in self.accounts]

    def total_balance(self):
        return f"Total bank balance  : {self.total_balance}"

    def total_loan(self):
        self.loan_amount = sum(account.loan_count for account in self.accounts)
        return f"Total loan amount: {self.loan_amount}"

    def disable_loan_feature(self):
        self.loan_feature = False
        return "Loan feature disabled."

admin_instance = Admin()

class Bank:
    def __init__(self, name):
        self.name = name
        self.admin_password = "rakibul263"
        self.is_admin_authenticated = False

    def show_menu(self):
        while True:
            print("------------------------------------------")
            print("|         Welcome to Daffodil Bank       |")
            print("------------------------------------------")
            print("|         1. Admin                       |")
            print("|         2. User                        |")
            print("|         3. Exit                        |")
            print("------------------------------------------")

            choice = input("Enter your choice: ")

            if choice == "1":
                os.system('clear')
                print("You are in Admin Menu")
                self.admin_menu()
            elif choice == "2":
                os.system('clear')
                print("You are in User Menu")
                self.user_menu()
            elif choice == "3":
                os.system('clear')
                print("Exit")
                break 
            else:
                print("Invalid choice! Please try again.")

    def admin_menu(self):
        os.system('clear')
        
        if not self.is_admin_authenticated:
            password = input("Enter Admin Password: ")
            if password == self.admin_password:
                os.system('clear')
                self.is_admin_authenticated = True 
            else:
                print("Incorrect password! Returning to the main menu.")
                return 

        print("---------------Admin Menu---------------")
        print("|         1. Create Account            |")
        print("|         2. Delete Account            |")
        print("|         3. View All Accounts         |")
        print("|         4. View Bank Balance         |")
        print("|         5. Main Menu                 |")
        print("|         6. Exit                      |")
        print("----------------------------------------")

        admin_choice = input("Enter your choice: ")

        def create_ac():
            os.system('clear')
            print("------------Create Account------------")
            name = input("{:<20}: ".format("Enter Name")).title()
            email = input("{:<20}: ".format("Enter Email")).lower()
            address = input("{:<20}: ".format("Enter Address")).title()
            account_type = input("{:<20}: ".format("Enter Account Type")).title()
            new_account = admin_instance.create_account(name, email, address, account_type)
            os.system('clear')
            print("-----------------Account Created-----------------")
            print(new_account)
            print("-------------------------------------------------")

        def gap():
            print()
            print()
            print()

        
        if admin_choice == "1":
            while True:
                another_account = input("Do you want to create another account? YES or NO : ").lower()
                if another_account == "yes":
                    create_ac()
                elif another_account == "no":
                    self.admin_menu()
                    break
                else:
                    print("Invalid choice! Please try again.")
                    break

        elif admin_choice == "2":
            print("-----------------Delete Account-----------------")
            account_number = int(input("Enter Account Number: "))
            os.system('clear')
            print("-----------------Account Deleted Info-----------------")
            print(f'|     {admin_instance.delete_account(account_number)}      |')
            print("-------------------------------------------------------")
            gap()

        elif admin_choice == "3":
            all_users = admin_instance.see_all_users()
            user_count = 1
            for user in all_users:
                print(f"---------------User {user_count}------------------------")
                print(user)
                user_count += 1
            gap()

        elif admin_choice == "4":
            print("-----------------Bank Balance-----------------")
            print(admin_instance.total_balance)
            gap()

        elif admin_choice == "5":
            os.system('clear')
            self.show_menu()

        elif admin_choice == "6":
            print("Exit")
            os.system('clear')

    def user_menu(self):
        account_number = int(input("Enter your account number: "))
        user_account = self.get_account_by_number(account_number)

        def gap():
            print()
            print()
            print()

        flag = False
        if user_account:
            flag = True
            while flag:
                print("------------------User Menu-------------------")
                print("                                              ")
                print(f"             Welcome {user_account.name}     ")
                print("                                              ")
                print("----------------------------------------------")
                print("|         1. Deposit Money                   |")
                print("|         2. Withdraw Money                  |")
                print("|         3. View Balance                    |")
                print("|         4. Transfer Money                  |")
                print("|         5. Take Loan                       |")
                print("|         6. Transaction History             |")
                print("|         7. Exit                            |")
                print("----------------------------------------------")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    os.system('clear')
                    amount = float(input("Enter Amount to Deposit: "))
                    os.system('clear')
                    print("-----------------Deposit Info-----------------")
                    print(user_account.deposit(amount))
                    gap()

                elif user_choice == "2":
                    os.system('clear')
                    amount = float(input("Enter Amount to Withdraw: "))
                    print("-----------------Withdraw Info-----------------")
                    print(user_account.withdraw(amount))
                    gap()

                elif user_choice == "3":
                    os.system('clear')
                    print("-----------------Balance Info-----------------")
                    print(user_account.check_balance())
                    gap()

                elif user_choice == "4":
                    os.system('clear')
                    amount = float(input("Enter Amount to Transfer: "))
                    receiver_account_number = int(input("Enter Receiver Account Number: "))
                    receiver_account = self.get_account_by_number(receiver_account_number)
                    if receiver_account:
                        os.system('clear')
                        print("-----------------Transfer Info-----------------")
                        print(user_account.transfer_amount(amount, receiver_account))
                        gap()
                    else:
                        os.system('clear')
                        print("-----------------Transfer Info-----------------")
                        print("         Receiver account not found.           ")
                        gap()

                elif user_choice == "5":
                    os.system('clear')
                    amount = float(input("Enter Amount for Loan: "))
                    os.system('clear')
                    print("-----------------Loan Info-----------------")
                    print(user_account.take_loan(amount))
                    gap()

                elif user_choice == "6":
                    os.system('clear')
                    transactions = user_account.transaction_history()
                    print("-----------------Transaction History-----------------")
                    for transaction in transactions:
                        print(transaction)
                    gap()

                elif user_choice == "7":
                    os.system('clear')
                    flag = False
                    print("Exit")
                    gap()

        else:
            print("Account not found.")
            gap()

    def get_account_by_number(self, account_number):
        for account in admin_instance.accounts:
            if account.account_number == account_number:
                return account
        return None


my_bank = Bank("Daffodil Bank")
my_bank.show_menu()
