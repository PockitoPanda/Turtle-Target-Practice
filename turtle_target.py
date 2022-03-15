import turtle
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CENTER_CIRCLE_X = 150
CENTER_CIRCLE_Y = 75
CIRCLE_RADIUS = 100

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
pen = turtle.Pen()

pen.penup()
pen.goto(CENTER_CIRCLE_X, CENTER_CIRCLE_Y)
pen.down()
pen.circle(CIRCLE_RADIUS)
pen.up()
pen.home()

random.seed(2021)
n = 0
while n < 30:
    ANGLE = random.randint(0, 90)
    DISTANCE = random.randint(0, 300)
    pen.setheading(ANGLE) # make angle random
    pen.forward(DISTANCE)
    xcor = pen.xcor()
    ycor = pen.ycor()
    if (xcor - 150) ** 2 + (ycor - 150) ** 2 <= CIRCLE_RADIUS ** 2:
        pen.pencolor('green')
        pen.dot()
    else:
        pen.pencolor('blue')
        pen.dot()
    pen.home()
    n += 1



turtle.done()