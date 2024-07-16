weightInPounds = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))
KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weightInKilograms = weightInPounds * KILOGRAMS_PER_POUND
heightInMeters = ((feet * 12) + inches) * METERS_PER_INCH

BMI = weightInKilograms / (heightInMeters ** 2)
print(f"BMI is {BMI:.2f}")

if(BMI < 18.5):
    print("You are Underweight")
elif(BMI < 25):
    print("You are Normal")
elif(BMI < 30):
    print("You are Overweight")
else:
    print("You are Obese")