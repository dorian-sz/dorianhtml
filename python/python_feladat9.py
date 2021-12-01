import turtle

def star(length, angle, n):
    for i in range(n):
        turtle.forward(length)
        turtle.right(angle)
        
star(100, 144, 5)
