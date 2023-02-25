height=float(input("Enter the height in m:"))
weight=float(input("Enter your weight in kg:"))
bmi=round(weight/height**2,2)
if bmi <18.5:
    print("Underweight")
elif bmi<25:
    print("Normal Weight")
elif bmi<30:
    print("Overweight")
elif bmi<35:
    print("Obese")
else:
    print("Clinically Obese")
