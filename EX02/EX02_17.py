weightInPounds = eval(input("Enter weight in pounds: "))
heightInInches = eval(input("Enter height in inches: "))
CONSTANTOFWEIGHT = 0.45359237
CONSTANTOFHEIGHT = 0.0254
weightInKilograms = weightInPounds * CONSTANTOFWEIGHT
heightInMeters = heightInInches * CONSTANTOFHEIGHT
BMI = weightInKilograms / heightInMeters ** 2
print("BMI is ", BMI)