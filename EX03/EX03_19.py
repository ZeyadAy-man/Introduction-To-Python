import turtle

x1 = eval(input("Enter x1: "))
y1 = eval(input("Enter y1: "))
x2 = eval(input("Enter x2: "))
y2 = eval(input("Enter y2: "))

turtle.up()
turtle.goto(x1, y1)
turtle.down()

turtle.write(f"({x1}, {y1})")

turtle.goto(x2, y2)

turtle.write(f"({x2}, {y2})")

turtle.done()