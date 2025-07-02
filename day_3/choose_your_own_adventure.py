# Added the ASCII art to another python file in the directory and I have imported it to look cleaner.
import time
from art import dungeon

# Printed the ASCII art to look more alive, and added time.sleep to give it a felling, like someone is really talking with you.
print(dungeon)
time.sleep(1)

print("Wellcome to the Treasure DUNGEONNN!"
      " Your mission is you find the treasure and escape ALIVE!\nGood Luck Explorer!!")
time.sleep(2)
cross_road = input("You are at a cross road leading in 3 directions. "
                       "Left, right and straight forward\nWere are you choosing to go?\n").lower()

# The logic of the game
if cross_road == "left":
    print("You've fallen into a snake pit, you have DIED!\nGame Over")
elif cross_road == "right":
    print("A Giant Goblin is wondering the room. He saw you and crushed you, you have DIED!\nGame Over")
elif cross_road == "straight":
    print("There we're no dangers, the roads seems good, until you reached a dead end but with a pond.\n"
          "You can wait or swim, what will be your decision?")