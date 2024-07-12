import math
x1 = eval(input("Enter x1: "))
y1 = eval(input("Enter y1: "))
x2 = eval(input("Enter x2: "))
y2 = eval(input("Enter y2: "))
EARTHRADIUS = 6371.01
distanceBetweenTwoPoints = EARTHRADIUS * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1 - y2)))
print(f"The distance between the two points is {distanceBetweenTwoPoints} km")