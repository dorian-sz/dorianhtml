import turtle
screen = turtle.Screen()
turtle = turtle.Turtle()

def square(l):
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)

for i in range(5):
    square(20)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    
