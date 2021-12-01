import turtle

def szabalyos_haromszog_rajzolas(length, angle, sides):
    for i in range(sides):
        turtle.forward(length)
        turtle.left(angle)
        
szabalyos_haromszog_rajzolas(100,120,3)
