# Creating a loop to print out the highes number in a list

student_scores = [150,124,180,165,173,189,169,146]

max_score = 0 # creating a variable to hold the intermediate values until we reach maximum value.
min_score = 0

for x in student_scores:
    if x > max_score: # if statement to see if the item in our list is higher than our declared variable.
        max_score = x # If our number is higher than our variable (0), setting the variable to that value until it reaches the highest number

print(max_score)
print(min_score)

# The Gauss Challenge
calcul = 0 # - Creating a variable to hold the value neutral.

for number in range(1,101): # This for loop will take the numbers from 1-100
    calcul += number # This will add every number from the for loop 
print(calcul)
