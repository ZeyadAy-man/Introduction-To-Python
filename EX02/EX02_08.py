amountOfWater = eval(input("Enter the amount of water in kilograms: "))
initialTemperature = eval(input("Enter the initial temperature: "))
finalTemperature = eval(input("Enter the final temperature: "))
amountOfEnergyNeeded = amountOfWater * (finalTemperature - initialTemperature) * 4184
print("The energy needed is ", amountOfEnergyNeeded)