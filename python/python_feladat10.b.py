import turtle

def star(length, angle, n):
    for i in range(n):
        turtle.forward(length)
        turtle.right(angle)

for i in range(5):
    star(100, 144, 5)

    turtle.forward(650)
    turtle.right(144)

