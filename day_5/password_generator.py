from art import logo
import random

# This print statement will print the logo that is imported from another file.
print(logo)

# Created lists for the password.
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
          "x", "y", "z"]

upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W","X", "Y", "Z"]

numbers = ["0", "2", "3", "4", "5", "6", "7", "8", "9"]


symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


# Created an empty string list for later to append the random letters that the use will want.
password = []

# Print statement
print("Wellcome to your password manager.\nBefore we continue to generate your password, you'll need to choose"
      "what you'd like fro your password")

# Inputs to ask the user how many letters, numbers etc he wants.
nr_letters = int(input("How many letters would you like?\n"))

nr_upp_letters = int(input("How many upper letters would you like?\n"))

nr_numbers = int(input("How many numbers would you like?\n"))

nr_symbols = int(input("How many symbols would you like?\n"))

# For loops to have a different character from each section, starting from 1.
for char in range(1, nr_letters +1): # To make it easier we can set the range from 1, nr_letters +1, to 0, ne_letters.
    random_letter = random.choice(letter)
    password.append(random_letter)

for upp_char in range(1, nr_upp_letters +1):
    random_upp_char = random.choice(upper_letters)
    password.append(random_upp_char)

for num in range(1, nr_numbers +1):
    random_number = random.choice(numbers)
    password.append(random_number)

for sym in range(1, nr_symbols +1):
    random_symb = random.choice(symbols)
    password.append(random_symb)

# Used the random module to shuffle the appended items into a random order.
random.shuffle(password)

# created a variable to remove the ("") from the password to have a coherent password not a list.
result = "".join(password)

# Printed the final result.
print(f"Your password is: {result}")