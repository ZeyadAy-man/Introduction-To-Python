widthOfRectangle = eval(input("Enter thewidth of the rectangle: "))
heightOfRectangle = eval(input("Enter theheight of the rectangle: "))
import turtle

turtle.forward(widthOfRectangle)
turtle.right(90)
turtle.forward(heightOfRectangle)
turtle.right(90)
turtle.forward(widthOfRectangle)
turtle.right(90)
turtle.forward(heightOfRectangle)

turtle.done()