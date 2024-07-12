import math
numberOfSides = eval(input("Enter the number of sides: "))
lengthOfSide = eval(input("Enter the length of the: "))
areaOfPolygon = (numberOfSides * lengthOfSide ** 2) / (4 * math.tan(math.pi / numberOfSides))
print(f"The area of the polygon is {areaOfPolygon}")