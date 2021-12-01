import turtle

turtle.speed(100)

def square(l):
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)

for i in range(18):
    square(50)
    turtle.penup()
    turtle.left(20)
    turtle.pendown()
