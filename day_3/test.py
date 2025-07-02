print("Hello and Wellcome to the, TinyWonderLand.\n")
print("In order to ride in our park, you'll need to be over 120 cm.\n")

height = int(input("What is your height? "))
final_price = 0

if height >= 120:
    print("You can ride in our Park, but before that we need to know your age. Because we have special prices!")
    age = int(input("What is your age? "))
    if 45 >= age <= 55:
        final_price = 0
        print("Wellcome, as of your age the tickets are on us!")
    elif age >= 18:
        final_price += 12
        print("Young man you'll have to pay 12$ before riding!")
    elif age < 12:
        final_price += 5
        print("Young one, you'll need to pay 5$ before riding")
    else:
        final_price += 7
        print(f"You need to pay 7$")

    photos = input("Before riding, do you want to get at the end some picture?\nIt will be only 3$ extra ")
    if photos == "yes" or photos == "y":
        final_price += 3

    print(f"Your final bill will be {final_price}$")

else:
    print("Unfortunately you are a little short to rider here.\ncome back when you'll grow taller.")