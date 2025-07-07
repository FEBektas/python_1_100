# Added the ASCII art to another python file in the directory and I have imported it to look cleaner.
import time
from art import dungeon

# Printed the ASCII art to look more alive, and added time.sleep to give it a felling, like someone is really talking with you.
print(dungeon)
time.sleep(1)

print("Wellcome to the Treasure DUNGEONNN!"
      " Your mission is you find the treasure and escape ALIVE!\nGood Luck Explorer!!")
time.sleep(2)
# * using a backslash (\) in front of a useful symbol, then the program will think that we try to add that symbol and it will not read it as code.
cross_road = input("You're at a cross road leading in 3 directions. "
                       "'Left', 'right' and 'straight',Were are you choosing to go?\n").lower()

# The logic of the game
if cross_road == "left":
    print("You've fallen into a snake pit, you have DIED!\nGame Over")
elif cross_road == "right":
    print("A Giant Goblin is wondering the room. He saw you and crushed you, you have DIED!\nGame Over")
elif cross_road == "straight":
    print("There we're no dangers, the roads seems good, until you reached a dead end but with a pond.")
else:
    print("You glitched out of the Dungeon and Died.... Game Over")
# The user has reached the next level.
pond = input("You can wait or you can swim, what will be your decision?\n").lower()

if pond == "swim":
    print("There we're sharks in the water, and they ate your flash, you have died. Game Over")
elif pond == "wait":
    print("The wall was an illusion and because you waited it has Disappeared, you can pass through!")
# adding time.sleep to add a little feeling, to feel more alive
time.sleep(2)

# The user has reached a room with 3 doors.
print("You have reached the final level before you can find the treasure, but you'll have to choose the"
              "right door in order to grab that treasureee")
doors = input("The Doors are, 'Blue', 'Yellow' or 'Red'.\nWhich is the correct door and which would you choose?\n").lower()

if doors == "blue":
    print("An ice goblin has appear, turning you into frozen dust. You have died, Game Over")
elif doors == "yellow":
    print("A Thunder God Dragon has appeared, making you dust before you can see him. You have died, Game Over")
elif doors == "red":
    print("You notice that no danger is sensing in the air. And you can look directly at the Treasure."
          "")

print("You took the Treasure and escaped alive. Congratulations Treasurer, you are now a very wealthy being.")