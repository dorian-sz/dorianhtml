import turtle
ablak = turtle.Screen()
Eszti = turtle.Turtle()


def sokszog_rajzolas(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(45)

sokszog_rajzolas(Eszti, 8, 50)
