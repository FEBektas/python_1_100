print("Wellcome to my Tip Calculator! ")

bill = int(input("What was the total bill? $"))
tip = int(input("What tip percentage do you wish you give? 10, 12, 15: %"))
people = int(input("How many people to split the bill? "))
bill_tip = (bill * (tip / 100)) + bill
split_bill = bill_tip / people

print(f"The total bill was {bill}$, you chose to give us a {tip}%, the total with bill with tip is {bill_tip} "
      f"and divided by {people} the total will be {split_bill}$ for each persons")

# print(tip)
# print(bill_tip)