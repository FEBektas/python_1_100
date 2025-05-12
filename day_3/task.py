# if/else conditions.

print("Hello and Wellcome to the, TinyWonderLand.\n")
print("In order to ride in our park, you'll need to be over 120 cm.\n")

height = int(input("What is your height? "))

if height >= 120:
    print("Congrats, Big Boy, you can ride in our Park.\nHave Funnn!")
else:
    print("Unfortunately you are a little short to rider here.\ncome back when you'll grow taller.")

# Checking if an input number is Odd or Even.

number  = int(input("Choose a number, and let's see together if it is Odd or Even "))

if number % 2 == 0:
    print("Your number is an Odd number. ")
elif number % 3 == 1:
    print("your number is an Even number. ")

