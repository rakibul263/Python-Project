#password generator
import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', ',', '/', '?',]

print('Welcome to Password Generator !')
 
pass_letter = int(input(f"How many Letter would you like in your password?\n = "))
pass_number = int(input(f"How many number would you like in your password?\n = "))
pass_symbols = int(input(f"How many symbols would you like in your password?\n = "))

password_list = []

for char in range(1, pass_letter+1) :
    password_list.append(random.choice(letter))

for char in range(1, pass_number+1) :
    password_list.append(random.choice(number))

for char in range(1, pass_symbols+1) :
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list :
    password += char

print(f"Your password is : {password}")
