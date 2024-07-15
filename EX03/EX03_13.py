import turtle

turtle.begin_fill()
turtle.color("red")
turtle.right(30)
turtle.circle(50, steps=6)
turtle.end_fill()

turtle.color("white")
turtle.up()
turtle.left(60)
turtle.forward(20)
turtle.left(90)
turtle.left(60)
turtle.right(90)
turtle.forward(23)
turtle.left(90)
turtle.forward(18)
turtle.left(90)
turtle.forward(4)
turtle.down()

turtle.write("STOP", font=('Arial', 16, "bold"))

turtle.done()