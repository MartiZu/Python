import sys 
##exit and provide message to user as output
import random 
# random module
from enum import Enum 

class RockPaperScissor(Enum):
    ROCK = 1 # capital means variable does not change
    PAPER = 2
    SCISSOR = 3

# print(RockPaperScissor(2))
# print(RockPaperScissor.ROCK) #dot notation
# print(RockPaperScissor["ROCK"]) #braket notation
# print(RockPaperScissor.ROCK.value) #value
# sys.exit()


playerchoice = input("Enter... \n 1 for Rock, \n 2 for Paper \n 3 for scissors: \n\n")

print(playerchoice)

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Enter 1, 2 or 3") ##exit and provide message to user as output

computer = random.choice("123")
comp = int(computer)


print("") #print empty string or blank line
print("You chose " + str(RockPaperScissor(player)).replace("RockPaperScissor.", ""))
print("Computer chose " + str(RockPaperScissor(comp)).replace("RockPaperScissor.", ""))
print("")

if player == 1 and comp == 3:
    print("user wins!😊")
elif player == 2 and comp == 1:
    print("user wins!🥳")
elif player == 3 and comp == 2:
    print("user wins!")
elif player == comp:
    print("tie")
else:
    print("computer wins")