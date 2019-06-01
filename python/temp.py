import turtle

turtle.speed(0)
def circle():
    for i in range(360):
        turtle.fd(1)
        turtle.lt(1)
def slinky():
    for i in range(10):
        turtle.fd(10)
        for i in range(1):
            circle()

turtle.width(100)
def yellowgreensquares():
    turtle.color("yellow")
    for i in range(4):
        turtle.fd(50)
        turtle.rt(90)
    turtle.lt(90)
    turtle.color("green")
    for i in range(4):
        turtle.fd(50)
        turtle.lt(90)

def bigH():
    turtle.lt(90)
    turtle.color("red")
    for i in range(2):
        turtle.fd(99)
        turtle.rt(90)
        turtle.fd(33)
        turtle.rt(90)
        turtle.fd(33)
        turtle.lt(90)
        turtle.fd(33)
        turtle.lt(90)
        turtle.fd(33)
        turtle.rt(90)
        turtle.fd(33)
        turtle.rt(90)

def octagon():
    for i in range(8):
        turtle.fd(50)
        turtle.rt(45)

def circle_flower():
    for i in range(24):
        turtle.rt(15)
        for i in range(1):
            circle()
        

circle_flower()
