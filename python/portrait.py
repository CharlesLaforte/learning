import turtle
import random

def portrait(line_color, fill_color):
    turtle.pu()
    turtle.goto(0, 0)
    turtle.pd()
    turtle.speed(0)
    turtle.width(2.5)
    turtle.color(line_color, fill_color)
    turtle.begin_fill()
    for i in range(2):
        for i in range(2):
            turtle.fd(220)
            turtle.lt(90)
            turtle.fd(295)
            turtle.lt(90)
        turtle.goto(0, 50)
        for i in range(2):
            turtle.fd(200)
            turtle.lt(90)
            turtle.fd(200)
            turtle.lt(90)
        turtle.goto(0, 70)
        for i in range(2):
            turtle.fd(220)
            turtle.lt(90)
            turtle.fd(295)
            turtle.lt(90)
        turtle.goto(0, 50)
        for i in range(2):
            turtle.fd(200)
            turtle.lt(90)
            turtle.fd(200)
            turtle.lt(90)
    turtle.end_fill()
    turtle.pu()
    d=random.randint(1, 100)
    turtle.color("brown")
    turtle.write(d, font=("Arial", 60, 'bold'))

portrait('black', 'brown')
