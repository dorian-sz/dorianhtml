import turtle

def square(l):
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)

l = 20
##
for i in range(5):
    square(l)
    turtle.penup()
    turtle.right(135)
    turtle.forward(15)
    turtle.left(135)
    turtle.pendown()
    l +=20
