import math
import turtle
radius = eval(input("Enter the radius of the circle: "))
area = radius * radius * math.pi
turtle.circle(radius)
turtle.up()
turtle.left(90)
turtle.forward(radius)
turtle.down()
turtle.write("The area is: " + str(area))
turtle.done()