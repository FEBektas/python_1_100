# For Loops.

fruits = ["apple", "banana", "kiwi"]
for f in fruits:
    lenght = len(f)
    if lenght <= 4:
        print(f)

# Sum.

student_scores = [150,124,180,165,173,189,169,146]

total_exam = sum(student_scores) # sum will add each item in the list.

print(total_exam)

summ = 0
for x in student_scores:
    summ += x

print(summ)

# Range function.
for number in range(1,11): # - created a for loop that will go through all the numbers from start to finish one by one.
    print(number)

print("-----")

for numbers in range (1, 101 ,5): # For the loop to increase its counting from one to another number just set a comma "," and type what number we want.
    print(numbers)
