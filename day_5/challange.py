# Creating a loop to print out the highes number in a list

student_scores = [150,124,180,165,173,189,169,146]

max_scor = 0 # creating a variable to hold the intermediate values until we reach maximum value.

for x in student_scores:
    if x > max_scor: # if statement to see if the item in our list is higher than our declared variable.
        max_scor = x # If our number is higher than our variable (0), setting the variable to that value until it reaches the highest number

print(max_scor)