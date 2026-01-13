import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
letter_choices = []
symbol_choices = []
number_choices = []

for i in range(0,nr_letters):
    letter_choices.append(random.choice(letters))
for j in range(0,nr_symbols):
    symbol_choices.append(random.choice(symbols))
for k in range(0,nr_numbers):
    number_choices.append(random.choice(numbers))

total_list = letter_choices + symbol_choices + number_choices
random.shuffle(total_list)

for i in range(0, len(total_list)):
    password += str(total_list[i])

print(f"Your password is: {password}")
