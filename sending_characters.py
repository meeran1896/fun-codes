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
