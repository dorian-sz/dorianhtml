import turtle

turtle.speed(100)

def spiral(length, n, angle):
    for i in range(n):
        turtle.right(angle)
        turtle.forward(length)
        length += 1
spiral(5, 100, 75)
