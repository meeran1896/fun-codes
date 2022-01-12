#Side look emoji
import turtle
my_pen = turtle.Turtle()

my_pen.color("#ffdd00")
my_pen.begin_fill()
my_pen.circle(100)
my_pen.fillcolor("#ffdd00")
my_pen.end_fill()
my_pen.home()

my_pen.goto(-40, 100)
my_pen.color("#555555")
my_pen.begin_fill()
my_pen.circle(15)
my_pen.color("#ffffff")
my_pen.end_fill()
my_pen.penup()
my_pen.goto(-48, 110)
my_pen.pendown()
my_pen.color("Black")
my_pen.begin_fill()
my_pen.circle(5)
my_pen.end_fill()
my_pen.penup()

my_pen.goto(40, 100)
my_pen.pendown()
my_pen.color("#555555")
my_pen.begin_fill()
my_pen.circle(15)
my_pen.color("#ffffff")
my_pen.end_fill()
my_pen.penup()
my_pen.goto(32, 110)
my_pen.pendown()
my_pen.color("Black")
my_pen.begin_fill()
my_pen.circle(5)
my_pen.end_fill()
my_pen.penup()

my_pen.goto(-20, 50)
my_pen.pendown()
my_pen.pensize(10)
my_pen.forward(40)
turtle.done()

#Many circle rings
import turtle
turtle.bgcolor("black")
painter = turtle.Turtle()
painter.speed(0)
painter.penup()
painter.left(90)
painter.goto(0,0)
painter.forward(100)
painter.left(180)
painter.pendown()
j=0
while(j<=5):
    
    painter.pencolor("red")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark violet")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark red")
    for i in range(150):
        painter.forward(106)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark orange")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark grey")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("red")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark violet")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()
 
    painter.pencolor("dark red")
    for i in range(150):
        painter.forward(106)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark orange")
    for i in range(150):
        painter.forward(104)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(180*j)
    painter.pendown()

    painter.pencolor("dark grey")
    for i in range(150):
        painter.forward(100)
        painter.left(111) # Let's go counterclockwise this time
    painter.penup()
    painter.right(90*j)
    painter.pendown()

j=j+1
turtle.done()
turtle.quit()
j=j+1
turtle.done()
turtle.quit()
