import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
final_letters=[]
final_symbols=[]
final_numbers=[]
final_password=[]
for i in range(nr_letters):

    letter = random.choice(letters)
    final_letters.append(letter)

print(final_letters)

for i in range(nr_symbols):
    symbol = random.choice(symbols)
    final_symbols.append(symbol)

print(final_symbols)

for i in range(nr_numbers):
    number = random.choice(numbers)
    final_numbers.append(number)

print(final_numbers)

final_password.extend(final_letters)
final_password.extend(final_symbols)
final_password.extend(final_numbers)

random.shuffle(final_password)


password = "".join(final_password)

print(f"Your password is: {password}")











