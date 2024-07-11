import math
radius = eval(input("Enter the radius of the cylinder: "))
length = eval(input("Enter the length of the cylinder: "))
area = radius * radius * math.pi
print("The area is ", (area))
print("The volume is ", (length * area))