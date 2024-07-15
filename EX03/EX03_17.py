import math;
import turtle;
x1 = eval(input("Enter x1: "))
y1 = eval(input("Enter y1: "))
x2 = eval(input("Enter x2: "))
y2 = eval(input("Enter y2: "))
x3 = eval(input("Enter x3: "))
y3 = eval(input("Enter y3: "))
side1 = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
side2 = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))
side3 = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

turtle.up()
turtle.goto(x1, y1)
turtle.down()
turtle.write(f"p1({x1}, {y1})")

turtle.goto(x2, y2)
turtle.write(f"p2({x2}, {y2})")

turtle.goto(x3, y3)
turtle.write(f"p3({x3}, {y3})")
turtle.goto(x1, y1)

turtle.up()
turtle.goto(150, 150)
turtle.down()
turtle.write(f"The area of the triangle is {area}")

turtle.done()