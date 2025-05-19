weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 25:
    print("Overweight")
else:
    print("normal weight")