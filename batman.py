#Draw batman logo
import turtle
import math

kalam = turtle.Turtle()
kalam.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
kalam.color("yellow")

ankur = 20

kalam.left(90)
kalam.penup()
kalam.goto(-7 * ankur, 0)
kalam.pendown()

for a in range(-7 * ankur, -3 * ankur, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * ankur)

for a in range(-3 * ankur, -1 * ankur - 1, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * ankur)

kalam.goto(-1 * ankur, 3 * ankur)
kalam.goto(int(-0.5 * ankur), int(2.2 * ankur))
kalam.goto(int(0.5 * ankur), int(2.2 * ankur))
kalam.goto(1 * ankur, 3 * ankur)
print("Batman Logo with Python Turtle")
for a in range(1 * ankur + 1, 3 * ankur + 1, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * ankur)

for a in range(3 * ankur + 1, 7 * ankur + 1, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * ankur)

for a in range(7 * ankur, 4 * ankur, -1):
    x = a / ankur
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * ankur)

for a in range(4 * ankur, -4 * ankur, -1):
    x = a / ankur
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    kalam.goto(a, y * ankur)

for a in range(-4 * ankur - 1, -7 * ankur - 1, -1):
    x = a / ankur
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * ankur)

kalam.penup()
kalam.goto(300, 300)
turtle.done()

#Some beautiful designs
import turtle
wn=turtle.Screen()
turtle.bgcolor('black')
turtle.shape('turtle')
tr=turtle.Turtle()
ts=turtle.Turtle()
tt=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
move=1
###############################
t5.speed("fastest")
for i in range(10):
    for i in range(4):
          t5.pu()
          t5.goto(500,200)
          t5.pd()
          t5.color('cyan')
          t5.pensize(3)
          t5.circle(50,steps=4)
          t5.right(100)
t5.speed("fastest")
for i in range(6):
    for i in range(4):
          t5.pu()
          t5.goto(0,0)
          t5.pd()
          t5.color('light green')
          t5.pensize(3)
          t5.circle(100,steps=6)
          t5.right(100)
t2.speed("fastest")
for i in range (10):
    for i in range (2):
        t2.pensize(5)
        t2.goto(270,0)
        t2.color("green")
        t2.forward(100)
        t2.right(60)
        t2.color("cyan")
        t2.forward(50)
        t2.right(120)
    t2.right(30)
tr.speed("fastest")
for i in range (10):
    for i in range (2):
        tr.pensize(7)
        tr.goto(-270,0)
        tr.color("purple")
        tr.forward(100)
        tr.circle(5,steps=4)
        tr.right(60)
        tr.color("violet")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
ts.speed("fastest")
t5.speed("fastest")
for i in range(10):
    for i in range(4):
          t5.pu()
          t5.goto(-500,200)
          t5.pd()
          t5.color('yellow')
          t5.pensize(3)
          t5.circle(50,steps=4)
          t5.right(100)
t5.speed("fastest")
for i in range(10):
    for i in range(4):
          t5.pu()
          t5.goto(-500,-200)
          t5.pd()
          t5.color('white')
          t5.pensize(3)
          t5.circle(50,steps=3)
          t5.right(100)
t5.speed("normal")
for i in range(10):
    for i in range(4):
          t5.pu()
          t5.goto(500,-200)
          t5.pd()
          t5.color('pink')
          t5.pensize(3)
          t5.circle(50,steps=3)
          t5.right(100)
for i in range (20):
    for i in range (2):
        ts.pensize(2)
        ts.goto(0,300)
        ts.color("red")
        ts.forward(100)
        ts.circle(6,steps=3)
        ts.right(70)
        ts.color("yellow")
        ts.forward(50)
        ts.right(120)
    ts.left(30)
ts.speed('fastest')
for i in range (20):
    for i in range (2):
        ts.pensize(2)
        ts.pu()
        ts.goto(0,-300)
        ts.color("pink")
        ts.pd()
        ts.forward(100)
        ts.circle(6,steps=3)
        ts.right(70)
        ts.color("orange")
        ts.forward(50)
        ts.right(120)
    ts.left(30)
t3.speed("fastest")
for i in range (10):
    for i in range (2):
        t3.pensize(3)
        t3.goto(-320,300)
        t3.color("light green")
        t3.begin_fill()
        t3.forward(30)
        t3.right(50)
        t3.color("green")
        t3.forward(50)
        t3.circle(5,steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)
t3.speed("fastest")
for i in range (10):
    for i in range (2):
        t3.pensize(3)
        t3.pu()
        t3.goto(320,-300)
        t3.pd()
        t3.color("red")
        t3.begin_fill()
        t3.forward(30)
        t3.right(50)
        t3.color("orange")
        t3.forward(50)
        t3.circle(5,steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(100)
t3.speed("fastest")
for i in range (10):
    for i in range (2):
        t3.pensize(3)
        t3.pu()
        t3.goto(320,300)
        t3.pd()
        t3.color("light blue")
        t3.begin_fill()
        t3.forward(30)
        t3.right(50)
        t3.color("blue")
        t3.forward(50)
        t3.circle(5,steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)
t3.speed("fastest")
for i in range (10):
    for i in range (2):
        t3.pensize(3)
        t3.pu()
        t3.goto(-320,-300)
        t3.pd()
        t3.color("orange")
        t3.begin_fill()
        t3.forward(30)
        t3.right(50)
        t3.color("red")
        t3.forward(50)
        t3.circle(5,steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)
###########################
t5.speed("fastest")
for i in range(10):
    for i in range(4):
          t5.pu()
          t5.goto(600,0)
          t5.pd()
          t5.color('white')
          t5.pensize(1)
          t5.circle(40,steps=5)
          t5.right(100)
t5.speed("fastest")
############################
t5.speed("fastest")
for i in range(10):
    for i in range(4):
          t5.pu()
          t5.goto(600,0)
          t5.pd()
          t5.color('green')
          t5.pensize(1)
          t5.circle(20,steps=9)
          t5.right(100)
t5.speed("fastest")
painter = turtle.Turtle()
painter.pencolor("red")
for i in range(50):
    painter.pu()
    painter.goto(-600,0)
    painter.pd()
    painter.forward(100)
    painter.left(123)
turtle.done()
