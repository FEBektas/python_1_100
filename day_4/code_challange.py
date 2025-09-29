# Choosing a random name for who's going to pay for the whole bill
import random

friends = ["Alex", "Dani", "Robert", "Mihai", "George"]
random_friend = random.choice(friends)
# 1 option - my challenge result
print(f"The bill will be payed by: {random_friend}")

# 2 option
random_friend1 = random.randint(0, 4)
print(friends[random_friend1]) # This will access the list by adding a set of squared paratheses and insert the random function to be able to select a random friend from the list.