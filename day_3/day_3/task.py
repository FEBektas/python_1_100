# if/else conditions.

print("Hello and Wellcome to the, TinyWonderLand.\n")
print("In order to ride in our park, you'll need to be over 120 cm.\n")

height = int(input("What is your height? "))

if height >= 120:
    print("Before we continue with the Fun, we must know your age.\n")
    age = int(input("What is your age? "))
    if age <= 12:                                                       # <------ nested If/Elif conditions
        photo = input("Before you ride, do you wish to purchase a photo? \nit will be 3$ extra ").capitalize()
        if photo == "Yes":
            print("Excellent, You'll be charged an extra 3$ to the bill and you'll have to pay 8$!")
        else:
            print("You'll have to pay 5$ dollars for a ticket young boy")
    elif age > 18:
        photo = input("Before you ride, do you wish to purchase a photo? \nit will be 3$ extra ").capitalize()
        if photo == "Yes":
            print("Excellent, You'll be charged an extra 3$ to the bill and you'll have to pay 15$!")
        else:
            print("You'll have to pay 12$ for a ticket grown man")
    elif age > 45 or age < 55:
        print("Your ticket will be free")
    else:
        photo = input("Before you ride, do you wish to purchase a photo? \nit will be 3$ extra ").capitalize()
        if photo == "Yes":
            print("Excellent, You'll be charged an extra 3$ to the bill and you'll have to pay 10$!")
        else:
            print("You'll have to pay 7$ for a ticket or 10$ including a photo!")

else:
    print("Unfortunately you are a little short to rider here.\ncome back when you'll grow taller.")

# Checking if an input number is Odd or Even.

number  = int(input("Choose a number, and let's see together if it is Odd or Even "))

if number % 2 == 0:
    print("Your number is an Odd number. ")
elif number % 3 == 1:
    print("your number is an Even number. ")

