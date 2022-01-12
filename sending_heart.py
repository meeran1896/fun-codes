#Sending a heart
from turtle import *
color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

#Producing infinity
from turtle import *
bgcolor('black')
color("cyan")
speed(11)
right(45)
for i in range(150):
  circle(30)
  if 7 < i < 62:
    left(5)
  if 80 < i < 33:
    right(5)
  if i < 80
    forward(10)
  else:
    forward(5)
   
 
#Create a virus
from turtle import *
bgcolor('black')
color("cyan")
speed(11)
b=200
while b > 0:
  left(b)
  forward(b*3)
  b=b-1
  
#Ironman Helmet
import turtle

ankur1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
           (-40, -20), (0, -20)],
          [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
           (40, 120), (0, 120)]]
ankur2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
           (-80, -230), (-64, -210), (0, -210)],
          [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
           (100, -46), (50, -40), (40, -30), (0, -30)]]
ankur3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
           (0, -250)],
          [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
           (0, -220)]]

turtle.hideturtle()
turtle.bgcolor('#ba161e')  # Dark Red
turtle.setup(500, 600)
turtle.title("I AM IRONMAN")
ankur1Goto = (0, 120)
ankur2Goto = (0, -30)
ankur3Goto = (0, -220)
turtle.speed(2)


def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color('#fab104')  # Light Yellow
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        turtle.goto(x, y)
    turtle.end_fill()


logo(ankur1, ankur1Goto)
logo(ankur2, ankur2Goto)
logo(ankur3, ankur3Goto)
turtle.hideturtle()
turtle.done()

#Draw Pikachu
import turtle


def gajurel(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)


class Cartoon:

    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(9)
        t.ondrag(gajurel)

    def meme(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def aankha1(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.meme(x + 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def aankha2(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.meme(x - 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mukh(self, x, y):
        self.meme(x, y)
        t = self.t

        t.fillcolor('#88141D')
        t.begin_fill()
        #
        l1 = []
        l2 = []
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)
            l1.append(t.position())

        self.meme(x, y)

        t.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
            l2.append(t.position())

        #

        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)

        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

        #
        self.meme(17, 54)
        t.fillcolor('#DD716F')
        t.begin_fill()
        t.seth(145)
        t.circle(40, 86)
        t.penup()
        for pos in reversed(l1[:20]):
            t.goto(pos[0], pos[1] + 1.5)
        for pos in l2[:20]:
            t.goto(pos[0], pos[1] + 1.5)
        t.pendown()
        t.end_fill()

        #
        self.meme(-17, 94)
        t.seth(8)
        t.fd(4)
        t.back(8)

    #
    def gaala1(self, x, y):
        turtle.tracer(False)
        t = self.t
        self.meme(x, y)
        t.seth(300)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def gaala2(self, x, y):
        t = self.t
        turtle.tracer(False)
        self.meme(x, y)
        t.seth(60)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def kaan1(self, x, y):
        t = self.t
        self.meme(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(330)
        t.circle(100, 35)
        t.seth(219)
        t.circle(-300, 19)
        t.seth(110)
        t.circle(-30, 50)
        t.circle(-300, 10)
        t.end_fill()

    def kaan2(self, x, y):
        t = self.t
        self.meme(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(300)
        t.circle(-100, 30)
        t.seth(35)
        t.circle(300, 15)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 17)
        t.end_fill()

    def jiu(self):
        t = self.t

        t.fillcolor('#F6D02F')
        t.begin_fill()
        #
        t.penup()
        t.circle(130, 40)
        t.pendown()
        t.circle(100, 105)
        t.left(180)
        t.circle(-100, 5)

        #
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 36)

        #
        t.seth(150)
        t.circle(150, 70)

        #
        t.seth(200)
        t.circle(300, 40)
        t.circle(30, 50)
        t.seth(20)
        t.circle(300, 35)
        # print(t.pos())

        #
        t.seth(240)
        t.circle(105, 95)
        t.left(180)
        t.circle(-105, 5)

        #
        t.seth(210)
        t.circle(500, 18)
        t.seth(200)
        t.fd(10)
        t.seth(280)
        t.fd(7)
        t.seth(210)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(220)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(240)
        t.fd(12)
        t.seth(0)
        t.fd(13)
        t.seth(240)
        t.circle(10, 70)
        t.seth(10)
        t.circle(10, 70)
        t.seth(10)
        t.circle(300, 18)

        t.seth(75)
        t.circle(500, 8)
        t.left(180)
        t.circle(-500, 15)
        t.seth(250)
        t.circle(100, 65)

        #
        t.seth(320)
        t.circle(100, 5)
        t.left(180)
        t.circle(-100, 5)
        t.seth(220)
        t.circle(200, 20)
        t.circle(20, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(300)
        t.circle(10, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(10)
        t.circle(100, 60)

        #
        t.seth(180)
        t.circle(-100, 10)
        t.left(180)
        t.circle(100, 10)
        t.seth(5)
        t.circle(100, 10)
        t.circle(-100, 40)
        t.circle(100, 35)
        t.left(180)
        t.circle(-100, 10)

        #
        t.seth(290)
        t.circle(100, 55)
        t.circle(10, 50)

        t.seth(120)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(0)
        t.circle(10, 50)

        t.seth(110)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(30)
        t.circle(20, 50)

        t.seth(100)
        t.circle(100, 40)

        #
        t.seth(200)
        t.circle(-100, 5)
        t.left(180)
        t.circle(100, 5)
        t.left(30)
        t.circle(100, 75)
        t.right(15)
        t.circle(-300, 21)
        t.left(180)
        t.circle(300, 3)

        #
        t.seth(43)
        t.circle(200, 60)

        t.right(10)
        t.fd(10)

        t.circle(5, 160)
        t.seth(90)
        t.circle(5, 160)
        t.seth(90)

        t.fd(10)
        t.seth(90)
        t.circle(5, 180)
        t.fd(10)

        t.left(180)
        t.left(20)
        t.fd(10)
        t.circle(5, 170)
        t.fd(10)
        t.seth(240)
        t.circle(50, 30)

        t.end_fill()
        self.meme(130, 125)
        t.seth(-20)
        t.fd(5)
        t.circle(-5, 160)
        t.fd(5)

        #
        self.meme(166, 130)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)

        #
        self.meme(168, 134)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        ##############
        # print(t.pos())
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        #
        t.fillcolor('#923E24')
        self.meme(126.82, -156.84)
        t.begin_fill()

        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(40)
        t.pencolor('#923e24')
        t.seth(-30)
        t.fd(30)
        t.left(140)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(150)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(130)
        t.fd(18)
        t.pencolor('#000000')
        t.seth(-45)
        t.fd(67)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)
        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.end_fill()

        self.topi(-134.07, 147.81)
        self.mukh(-5, 25)
        self.gaala1(-126, 32)
        self.gaala2(107, 63)
        self.kaan1(-250, 100)
        self.kaan2(140, 270)
        self.aankha1(-85, 90)
        self.aankha2(50, 110)
        t.hideturtle()

    def topi(self, x, y):
        self.meme(x, y)
        t = self.t
        t.fillcolor('#CD0000')
        t.begin_fill()
        t.seth(200)
        t.circle(400, 7)
        t.left(180)
        t.circle(-400, 30)
        t.circle(30, 60)
        t.fd(50)
        t.circle(30, 45)
        t.fd(60)
        t.left(5)
        t.circle(30, 70)
        t.right(20)
        t.circle(200, 70)
        t.circle(30, 60)
        t.fd(70)
        # print(t.pos())
        t.right(35)
        t.fd(50)
        t.circle(8, 100)
        t.end_fill()
        self.meme(-168.47, 185.52)
        t.seth(36)
        t.circle(-270, 54)
        t.left(180)
        t.circle(270, 27)
        t.circle(-80, 98)

        t.fillcolor('#444444')
        t.begin_fill()
        t.left(180)
        t.circle(80, 197)
        t.left(58)
        t.circle(200, 45)
        t.end_fill()

        self.meme(-58, 270)
        t.pencolor('#228B22')
        t.dot(35)

        self.meme(-30, 280)
        t.fillcolor('#228B22')
        t.begin_fill()
        t.seth(100)
        t.circle(30, 180)
        t.seth(190)
        t.fd(15)
        t.seth(100)
        t.circle(-45, 180)
        t.right(90)
        t.fd(15)
        t.end_fill()
        t.pencolor('#000000')

    def start(self):
        self.jiu()


def main():
    print('Painting the Cartoon... ')
    turtle.screensize(800, 600)
    turtle.title('Cartoon')
    cartoon = Cartoon()
    cartoon.start()
    turtle.mainloop()


if __name__ == '__main__':
    main()

#Draw doraemon
from turtle import *


# Doraemon with Python Turtle
def ankur(x, y):
    penup()
    goto(x, y)
    pendown()


def aankha():
    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


def daari():
    ankur(-32, 135)
    seth(165)
    fd(60)

    ankur(-32, 125)
    seth(180)
    fd(60)

    ankur(-32, 115)
    seth(193)
    fd(60)

    ankur(37, 135)
    seth(15)
    fd(60)

    ankur(37, 125)
    seth(0)
    fd(60)

    ankur(37, 115)
    seth(-13)
    fd(60)


def mukh():
    ankur(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


def muflar():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nak():
    ankur(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def black_aankha():
    seth(0)
    ankur(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    ankur(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    ankur(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    ankur(0, 0)


def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    ankur(63.56, 218.24)
    seth(90)
    aankha()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    aankha()
    penup()
    seth(180)
    fd(64)


def taauko():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


def Doraemon():
    taauko()

    muflar()

    face()

    nak()

    mukh()

    daari()

    ankur(0, 0)

    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    # print(pos())

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    # print(pos())
    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    # print(pos())

    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()

    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    ankur(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    ankur(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

    ankur(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()
    # Doraemon with Python Turtle

    ankur(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    ankur(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    ankur(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    ankur(0, -150)

    black_aankha()


if __name__ == '__main__':
    screensize(800, 600, "#f0f0f0")
    pensize(3)
    speed(9)
    Doraemon()
    ankur(100, -300)
    write('by Ankur Gajurel', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()

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

#Circle mania
import turtle

wn = turtle.Screen()
wn.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('white')
rotate = int(180)


def Circles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 4


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


ankur(s, 200, 10)

t1 = turtle.Turtle()
t1.speed(0)
t1.color('yellow')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


ankur(t1, 160, 10)

t2 = turtle.Turtle()
t2.speed(0)
t2.color('blue')
rotate = int(80)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


ankur(t2, 120, 10)

t3 = turtle.Turtle()
t3.speed(0)
t3.color('red')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


ankur(t3, 80, 10)

t4 = turtle.Turtle()
t4.speed(0)
t4.color('cyan')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 20


def ankur(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


ankur(t4, 40, 10)
turtle.done()

#Superman logo
import turtle #import the required package to draw the logo

t=turtle.Turtle() #set the variable ‘t’ to the function turtle.Turtle() to shorten the code throughout
turtle.Screen().bgcolor('navy') #set the color of the screen to navy to match Superman’s costume

def curve(value): #create a function to generate curves in turtle
    for i in range(value): #for loop to repeat the inputted value number of times 
        t.right(1) #step by step curve
        t.forward(1)

t.penup() #pen is in the up position so it will not draw
t.setposition(0,43) #move the pen to these x and y coordinates
t.pendown() #pen is in the down position so it will draw
t.begin_fill() #start filling in the shape
t.pencolor('black') #change the pen color to black
t.fillcolor('maroon') #change the shape fill color to maroon to match the Superman logo
t.pensize(3) #use a pen size of 3 to create a black border
t.forward(81.5) #the pen will move forward this number to start the shield of the logo
t.right(49.4) #rotate the pen right 49.4 degrees
t.forward(58) #move the pen forward by 58 
t.right(81.42) #rotate right by 81.42 degrees
t.forward(182) #move the pen forward by 182
t.right(98.36) #rotate the pen right by 98.36 degrees
t.forward(182) #move the pen forward by 182 
t.right(81.42) #rotate the pen by 81.42 degrees to the right
t.forward(58) #move the pen forward 58 
t.right(49.4) #rotate the pen to the right by 49.4
t.forward(81.5) #move the pen forward by 81.5 to meet the start at the top of the shield
t.end_fill() #complete the fill of the shield so the shape is closed off
t.penup() #pen will not draw 

t.setposition(38,32) #now to create the yellow parts of the Superman logo
t.pendown() #the pen is now poised to draw
t.begin_fill() #start a new shape 
t.fillcolor('gold') #change the fill color to gold to match the Superman logo
t.forward(13) #move the pen forward by 13
t.right(120) #rotate the pen right by 120 degrees
t.forward(13) #move the pen forward by 13
t.right(120) #rotate the pen right by 120 degrees
t.forward(13) #move the pen forward by 13
t.end_fill() #the small triangle on the right is now complete
t.penup() #stop the pen from drawing

t.setposition(81.5,25) #now to create the larger yellow part of the Superman logo, change the position of the pen
t.pendown() #the pen will now draw again
t.begin_fill() #the fill is still the same color set before
t.right(210) #rotate the pen right by 210 degrees
t.forward(25) #move the pen forward by 25
t.right(90) #rotate the pen right by 90 degrees
t.forward(38) #move the pen forward by 38
t.right(45) #rotate the pen right by 45 degrees
t.circle(82,90) #this function is used to draw a circle in turtle, the first integer is the radius and the second is the number of degrees of the circle drawn
t.left(90) #rotate the pen left by 90 degrees
t.circle(82,60) #create a circle of radius 82 and only complete 60 degrees of the circle 
curve(61) #call the curve function that was previously defined, pass an integer value equal to the length of the curve desired 
t.left(90) #rotate the pen left by 90 degrees
t.forward(57) #move the pen forward by 57
t.left(90) #rotate the pen left by 90 degrees
t.forward(32) #move the pen forward by 32
t.end_fill() #fill in the larger yellow part of the logo
t.penup() #stop drawing 
t.home() #reset the pen location to the origin so the orientation is also reset

t.setposition(-69,-38) #finish the major parts of the S superimposition on the shield
t.pendown()
t.begin_fill()
curve(20)
t.forward(33)
t.left(10)
t.circle(82,20)
curve(30)
t.forward(10)
t.right(110)
curve(40)
t.right(10)
t.circle(50,10)
curve(45)
t.right(5)
t.forward(45)
t.end_fill()
t.penup()
t.home()

t.setposition(20,-100)
t.pendown()
t.begin_fill()
t.right(135)
t.forward(27)
t.right(90)
t.forward(27)
t.right(135)
t.forward(38.18)
t.end_fill()
t.penup()
t.home()

t.setposition(-57,32)
t.pendown()
t.begin_fill()
t.right(180)
t.forward(18)
t.left(45)
t.forward(44)
t.left(80)
t.forward(15)
t.left(130)
curve(40)
t.forward(20)
t.end_fill()

t.hideturtle() #use this command to hide the turtle so it is not visible in the final image
turtle.exitonclick() #this command will leave the window open until it is clicked

#Detect eyes and faces
#pip install opencv-python
import cv2
import numpy as np
img = cv2.imread("image1.jpg", -1)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.imread("image1.jpg", 0)
img = cv2.resize(img, (300,300))
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
print(img)
print(img.shape) #returns shape of numpy array
img = cv2.imread('Image.jpg', -1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
print(img)
print(img.shape)

#Detect eyes and faces main part
cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Frame', frame)
    if(cv2.waitKey(1) == ord('e')):
        break
cap.release()
cap.destroyAllWindows()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', frame)
    if(cv2.waitKey(1) == ord('e')):
        break
cap.release()
cap.destroyAllWindows()
img = cv2.rectangle(img, (300, 300), (200, 200), (134, 56, 132), 6)

#path for face cascade, path where it is stored specific classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.3,5)
import cv2
import numpy as np

cap=cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    faces = face_cascade.detectMultiScale(gray, 1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)


    cv2.imshow('frame',frame)

    if(cv2.waitKey(1)==ord('e')):
        break

cap.release()
cv2.destroyAllWindows()
import  numpy as np
import cv2

cap=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)

        roi_gray = gray[y:y+w,x:x+w]
        roi_color = frame[y:y+h,x:x+w]

        eyes= eye_cascade.detectMultiScale(roi_gray,1.3,5)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)

    cv2.imshow('frame',frame)

    if(cv2.waitKey(1)==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
cap = cv2.VideoCapture('video.mp4')

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
