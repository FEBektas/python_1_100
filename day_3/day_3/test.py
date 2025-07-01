print("Hello and Wellcome to the, TinyWonderLand.\n")
print("In order to ride in our park, you'll need to be over 120 cm.\n")

height = int(input("What is your height? "))

if height >= 120:
    print("You can ride in our Park, but before that we need to know your age. Because we have special prices!\n")
    price = 0
    age = int(input("What is your age? "))
    photos = input("Before riding, do you want to get at the end some picture?")
    if photos == "yes" and photos == "y":
        if 45 <= age < 55:
            price = 0
            print("Wellcome, as of your age the tickets are on us!")
        elif age >= 18:
            price =+ 12
            print(f"Young man you'll have to pay {price}$ before riding!")
        elif age < 12:
            price =+ 5
            print(f"Young one, you'll need to pay {price}$ before riding")
        else:
            price =+ 7
            print(f"You need to pay {price}$")
        price =+ 3
else:
    print("Unfortunately you are a little short to rider here.\ncome back when you'll grow taller.")