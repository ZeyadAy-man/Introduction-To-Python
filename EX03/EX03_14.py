radius = eval(input("Enter the radius of circles: "))

import turtle

turtle.pensize(5)
turtle.color("blue")
turtle.circle(radius)

turtle.penup()
turtle.forward(radius * 2 + (radius * 2 // 7))
turtle.pendown()

turtle.color("black")
turtle.circle(radius)

turtle.penup()
turtle.forward(radius * 2 + (radius * 2 // 7))
turtle.pendown()

turtle.color("red")
turtle.circle(radius)

turtle.penup()
turtle.right(140)
turtle.forward(radius * 2 - (radius * 2 // 7))
turtle.pendown()

turtle.right(220)
turtle.up()
turtle.forward(radius // 6)
turtle.down()
turtle.color("green")
turtle.circle(radius)

turtle.penup()
turtle.backward(radius * 2.25)
turtle.pendown()
turtle.color("yellow")
turtle.circle(radius)
turtle.done()