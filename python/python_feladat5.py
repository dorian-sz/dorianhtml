import turtle

turtle.speed(100)

def spiral(length, n):
    for i in range(n):
        turtle.right(90)
        turtle.forward(length)
        length += 3
spiral(5, 63)
