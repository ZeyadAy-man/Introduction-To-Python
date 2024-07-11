import math
print("Enter three points for a triangle: ")
x1 = eval(input("x1: "))
y1 = eval(input("y1: "))
x2 = eval(input("x2: "))
y2 = eval(input("y2: "))
x3 = eval(input("x3: "))
y3 = eval(input("y3: "))
side1 = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
side2 = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))
side3 = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
print("The are of the triangle is ", area)