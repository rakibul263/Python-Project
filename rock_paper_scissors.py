import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Game_Image = [Rock, Paper, Scissors]
print('Type 0 for Rock, 1 for Paper, 2 for Scissors ')
user_choice = int(input('What do you choose? \n'))
print(f'You chose : {user_choice}')
if user_choice >= 3 or user_choice < 0 :
    print('Please! Type Valid Number. YOU LOSE !')
else :
    print(Game_Image[user_choice])

computer_choice = random.randint(0, 2)
print(f'Computer chose : {computer_choice}')
print(Game_Image[computer_choice])


print('----------------------------------------')
if user_choice >= 3 or user_choice < 0 :
    print('Please! Type Valid Number. YOU LOSE !')
elif user_choice == 0 and computer_choice == 2 :
    print('YOU WIN!')
elif computer_choice == 0 and user_choice ==2 :
    print('YOU LOSE')
elif computer_choice > user_choice :
    print('YOU LOSE')
elif user_choice > computer_choice :
    print('YOU WIN!')
elif computer_choice == user_choice :
    print('DROW GAME! ')
print('------------------------------------------')
