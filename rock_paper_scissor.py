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

import random

options = [rock, paper, scissors]

print("hello to the rock, paper, scissors game\n")

choice = input("choose rock, paper, scissors: ").lower()

if choice == "rock":
    user = 0
elif choice == "paper":
    user = 1
elif choice == "scissors":
    user = 2
else:
    print("invalid choice")
    exit()

computer = random.randint(0, 2)

print("You chose:\n", options[user])
print("Computer chose:\n", options[computer])

if user == computer:
    print("It's a draw")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You win")
else:
    print("You lose")
