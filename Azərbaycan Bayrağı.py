import turtle
from turtle import*

bgcolor("black")
screen = turtle.Screen()

t = turtle.Turtle()
speed(0)

t.penup()
t.goto(-400, 250)
t.pendown()

# Mavi
t.color("blue")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)

# Yaşıl
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

# Qırmızı
t.color("red")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

# Ay
speed(100)
turtle.up()
turtle.goto(-10,-70)
turtle.color('white')
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.up()
turtle.goto(18,-70)
turtle.color('red')
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

# Ulduz
t.penup()
t.goto(65, -23)
t.pendown()
t.color("white")
angle=150
side=35
pointies = 8
ROTATION = 360/pointies

angle_left=angle
angle_right=angle

t.right(15)

t.color("white")
t.speed(8)
t.begin_fill()
for p in range(pointies):
 t.forward(side)
 t.right(angle_right)
 t.forward(side)
 t.left(angle_left)
 t.right(ROTATION)
t.end_fill()


turtle.done()
