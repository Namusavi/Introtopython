weight = input("Enter weight")
height = input("Enter height")

weight =float(weight)
height =float(height)

bmi = weight/(height*height)
print(bmi)
if bmi < 18:
    print("Underweight")
elif bmi < 29:
    print("Normal weight")
elif bmi < 34:
    print("Overweight")
else:
    print("Obese")