import turtle
import random

def house():
    turtle.pd()
    turtle.speed(0)
    turtle.width(5)
    turtle.begin_fill()
    for i in range(5):
        for i in range(2):
            turtle.fd(250)
            turtle.lt(90)
            turtle.fd(200)
            turtle.lt(90)
        turtle.rt(45)
        for i in range(2):
            turtle.fd(125)
            turtle.lt(90)
    turtle.end_fill()
    turtle.pu()
    d=random.randint(1, 5000)
    turtle.color("black")
    turtle.goto(0, 50)
    turtle.write(d, font=("Arial", 60, 'bold'))

house()
