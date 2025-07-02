import time
print("Wellcome to Erkan's Pizzeria!\nThe Worlds best pizza.")
time.sleep(1)

# inputs, asking the user the question for the pizza calculations
size = input("What size would you like the pizza to be? s, m or l: ").lower()
pepperoni = input("Would you like pepperoni on your pizza? y or n: ").lower()
extra_cheese = input("Would you like extra cheese on your pizza? y or n: ")

# How much they have to pay based on the size of the pizza
bill = 0

# If nested statements to calculate the price for the size of the pizza and added extra dollars if the user want or not extra toppings.
if size == "s" or size == "small":
    bill += 15
    if pepperoni == "y" or pepperoni == "yes":
        bill += 2
    if extra_cheese == "y" or extra_cheese == "yes":
        bill += 1
elif size == "m" or size == "medium":
    bill += 20
    if pepperoni == "y" or pepperoni == "yes":
        bill += 3
    if extra_cheese == "y" or extra_cheese == "yes":
        bill += 1
elif size == "l" or size == "large":
    bill += 25
    if pepperoni == "y" or pepperoni == "yes":
        bill += 3
    if extra_cheese == "y" or extra_cheese == "yes":
        bill += 1
else:
    print("I'm sorry, I did not quit catch the order, can you repeat? ")
print(f"Your order is a {size} pizza, and your total bill is {bill}$.\nWould you like to pay cash or card?")