import turtle


import turtle
import math

def drawStar(tur, pos: tuple, size: int, rot: int, color: str):
    tur.up()
    tur.goto(pos[0], pos[1])
    tur.color(color, color)
    tur.down()
    tur.setheading(0)
    tur.right(rot)
    tur.begin_fill()
    for i in range(5):
        tur.fd(size)
        tur.right(144)
    tur.end_fill()


def drawRect(tur, xy1: tuple, xy2: tuple, color:str, fill:str):
    tur.up()
    tur.color(color, fill)
    tur.goto(xy1[0], xy1[1])
    tur.begin_fill()
    tur.down()
    tur.goto(xy1[0], xy2[1])
    tur.goto(xy2[0], xy2[1])
    tur.goto(xy2[0], xy1[1])
    tur.goto(xy1[0], xy1[1])
    tur.end_fill()


t = turtle.Turtle()
t.speed(4)

A = 300
B = 1.9 * A
C = 7/13 * A
D = 2* B / 5
L = 1/13 * A


drawRect(t, (-B//2, A//2), (B//2, -A//2), "black", "white")
drawRect(t, (-B//2 + 1, A//2 - 1), (- B//2 + D, A//2 - C + 1), "#00204E", "#00204E")


for i in range(4):
    pas = i * 2 * L
    drawRect(t, (- B//2 + D + 1, A//2 - pas - 1), (B//2 - 1, A//2 - L - pas + 1), "#C30C3E", "#C30C3E")

for i in range(3):
    pas = i * 2 * L + 8 * L
    drawRect(t, (- B//2 + 1, A//2 - pas - 1), (B//2 - 1, A//2 - L - pas + 1), "#C30C3E", "#C30C3E")

# stars

for j in range(5):
    for i in range(6):
        pas = i * 37 + 14
        line = j * 30 + 8
        drawStar(t, (-B//2 + pas, A//2 - 10 - line), 12, 0, "white")


for j in range(4):
    for i in range(5):
        pas = i * 35 + 39
        line = j * 31 + 29
        drawStar(t, (-B//4 + pas, A//6 - 19 - line), 12, 0, "white")

t.hideturtle()