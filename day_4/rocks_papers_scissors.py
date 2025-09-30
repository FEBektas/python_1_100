import random
import time
from art import rock_art, paper_art, scissors_art
# imported the time module to give a life to the code, to seem more alive. Used the random module for the computer to randomly choose a number. Used the last module to import the ASCII art from another python file.
time.sleep(1)

# Print statement to help the user understands what he is playing.
print("Hello, and wellcome to the:\nRock, Paper, Scissor game")
art = [rock_art, paper_art, scissors_art]

# input for the user choice
player_choice = int(input("What is your choice? 0 for Rock, 1 for Paper and 2 for Scissor\n"))
if 0 <= player_choice <= 2: # simplifying the if player_choice >= 0 and player choice <= 2.
    print(f"You chose:{art[player_choice]}") # This will print the art correlated to the user number.
# the computer choice, selected randomly by the randint module.
computer_choice = random.randint(0,2)
print(f"Computer chose:{art[computer_choice]}") # This will print the art correlated to the computer number.


# the logic behind the game, comparing the choices and deciding who won or who lost.

if player_choice >= 3: # <---- This line will verify if the user choose a correct number.
    print("You've entered an invalid number, choose another number")
elif player_choice == 0 and computer_choice == 2:
    print(f"You've Won")
elif computer_choice == 0 and player_choice == 2:
    print(f"You lost ")
elif player_choice == computer_choice:
    print(f"IT's a draw")
elif player_choice > computer_choice:
    print(f"you Won ")
elif computer_choice > player_choice:
    print(f"You Lost")
