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
