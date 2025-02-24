# Bath tub comparison with if / else statements
water_level = 50

if water_level > 80:
    print("Drain Water")
else:
    print("Continue Filling the bath tub")

# Theme park job

print("Wellcome to the theme park. \nTo be able to go on the rollercoaster you'll need to be at least 120cm!\nEnjoy!")

height_centimeter = int(input("What is your height?")) # input to ask for the height of the user. Transformed it into
                                                       # an int to be able to compare the input to a whole number.

if height_centimeter <= 120:
    print("You can't ride the rollercoaster, you are not at least 120cm!")
else:
    print("You can pass")



# -----> Modulo Operator <-----
# As other mathematical operators and conditionals operators, a programming operator is just a symbol that has a unique function.