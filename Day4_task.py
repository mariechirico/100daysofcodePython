import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
    print("Rock\n" + rock)
elif user_choice == 1:
    print("Paper\n" + paper)
elif user_choice == 2:
    print("Scissors\n" + scissors)
else:
    print(str(user_choice) + " is not a valid option")
    quit()

print("Computer chose: \n")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Rock\n" + rock)
elif computer_choice == 1:
    print("Paper\n" + paper)
elif computer_choice == 2:
    print("Scissors\n" + scissors)
else:
    print("Computer chose an invalid option: " + str(computer_choice))
    quit()

if user_choice == 0:
    if computer_choice == 0:
        print("Draw")
    elif computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You win")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("Draw")
    elif computer_choice == 2:
        print("You lose")
elif user_choice == 2:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    elif computer_choice == 2:
        print("Draw")
else:
    print("Whoops, something went wrong")
