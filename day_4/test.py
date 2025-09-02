import random
# import my_module # importing the module from the python file
# print(my_module.My_fav_number) # printing the variable inside the python file we've created our own module.

# Creating random integers numbers
random_integers = random.randint(1,100)
print(random_integers)

# Creating Random floating point number between 0 and 1
random_numbers = random.random() * 100 # the module doesn't need any inputs but still requires the empty set of parentheses "()" in order to activate it.
                                       # by adding a multiplayer to the module will multiply the lower range and the higher range with the added multiplayer.
print(random_numbers)

# Creating a floating point number between a range.
random_float_number = random.uniform(1,10) # Random module to create a random floating point number between the set of range set by the us.
print(random_float_number)

# Lists

states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

print(states[0]) # The print statement will print the first element in the list "Delaware". The "0" is for the index number for the first element in the list, and is increasing by 1 with every element in the list.
                 # By adding negative index will print the elements from the end of the list EX: ("-1")

# Changing a piece of data to a new piece of data.
states[0] = "Pencilvania" # By doing this statement will modify the first element in the list (index 0 - "Pennsylvania") to another new piece of data.

# Adding new items to the list by using the .append function.
states.append("New York")
print(states)

# Extending our initial list with another created list by using .extend. Creating the list in the function will follow the same rules as creating a new list.
states.extend(["Paris", "Jersey", "Dublin"])
print(states)