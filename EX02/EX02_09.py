import math
temperature = eval(input("Enter the temperature in fahrenheit between -58 and 41: "))
windSpeed = eval(input("Enter the wind speed in miles per hour: "))
windChillIndex = 35.74 + 0.6125 * temperature - 35.75 * math.pow(windSpeed, 0.16) + 0.4275 * temperature * math.pow(windSpeed, 0.16)
print("The wind chill index is ", windChillIndex)