import turtle
import random

def dice_roll(line_color, fill_color, x, y):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.speed(0)
    turtle.width(2.5)
    turtle.color(line_color, fill_color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(100)
        turtle.rt(90)
    turtle.end_fill()
    turtle.pu()
    d=random.randint(1, 9)
    turtle.color("black")
    turtle.goto(x+30, y-80)
    turtle.write(d, font=("Arial", 60, 'bold'))
    
dice_roll('black', 'yellow', -300, -100)
dice_roll('black', 'red', -200, -100)
dice_roll('black', 'blue', -100, -100)
dice_roll('black', 'green', 0, -100)
dice_roll('black', 'green', 100, -100)
dice_roll('black', 'blue', 200, -100)
dice_roll('black', 'red', 300, -100)
dice_roll('black', 'yellow', 0, 150)
dice_roll('black', 'black', 300, 150)
dice_roll('black', 'black', -300, 300)
dice_roll('black', 'black', -200, 300)
dice_roll('black', 'black', -100, 300)
dice_roll('black', 'black', 0, 300)
dice_roll('black', 'black', 100, 300)
dice_roll('black', 'black', 200, 300)
dice_roll('black', 'black', 300, 300)






