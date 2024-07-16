import sys
import random
from enum import Enum

class RPS                   (Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


print('')
player_choice = input("Enter... \n1. Rock\n2. Paper\n3. Scissor\n\n")

player = int(player_choice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
# print("You chose " + player_choice + ".")
# print("Python chose " + computer_choice + ".")

print("You chose " + str(RPS(player)).replace("RPS.",'') + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.",'') + ".")

print("")

if player == 1 and computer == 3:
    print("🎉 You win!\n")
elif player == 2 and computer == 1:
    print("🎉 You win!\n")
elif player == 3 and computer == 2:
    print("🎉 You win!\n")
elif player == computer:
    print("😲 Tie game!\n")
else:
    print("🐍 Python wins!\n")
