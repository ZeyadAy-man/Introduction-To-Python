import math
lengthFromTheCenterToVertex = eval(input("Enter the length from the center to a vertex: "))
lengthOfSide = 2 * lengthFromTheCenterToVertex * math.sin(math.pi / 5)
area = ((3 * math.sqrt(3)) / 2) * lengthOfSide * lengthOfSide
print(f"The area of the pentagon is {area:.2f}")