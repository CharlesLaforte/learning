import turtle

def circle_flower(fd_val, width, color):
    turtle.width(width)
    turtle.color(color)
    for i in range(24):
        turtle.rt(15)
        circle(fd_val)
        
def two_color_flower():
    turtle.speed(0)
    turtle.tracer(0, 0)

    circle_flower(9, 12, 'yellow')
    circle_flower(10, 6, 'orange')
    circle_flower(10, 1, 'black')
    circle_flower(6, 4, 'red')
    circle_flower(6, 1, 'black')

    turtle.update()
    

def circle():
    for i in range(36):
        turtle.fd(10)
        turtle.lt(10)

circle()

def circle_flower():
    for i in range(24):
        turtle.fd(15)
        turtle.rt(15)
        circle()
    
circle_flower()
