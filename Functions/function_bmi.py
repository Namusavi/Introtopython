def calculate_bmi():
    height = float(input("Enter height"))
    weight = float(input("Enter weight"))
    bmi = weight / (height * height)
    print(f"your bmi is {bmi}")
calculate_bmi()