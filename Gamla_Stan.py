from turtle import *
from random import *
setup(width=800, height=600)

def rdc(x,y,color):
    """ Define the first floor"""
    up()
    goto(x,y)
    down()
    fillcolor(color)
    begin_fill()
    for i in range(2):
        fd(140)
        lt(90)
        fd(60)
        lt(90)
    end_fill()

    position = [x + 15, x + 55, x + 95]
    pos_door = choice(position)
    door(pos_door, y)

    for position in position:
        if position != pos_door:
            wdw(position, y + 15)

def floor(x,y,color):
    """Parameters of my upper floors"""
    up()
    goto(x,y)
    down()
    fillcolor(color)
    begin_fill()
    for i in range(2):
        fd(140)
        lt(90)
        fd(60)
        lt(90)
    end_fill()
    wdw(x+ 15, y+15)
    wdw(x+ 55, y+15)
    wdw(x+ 95, y+15)

def wdw(x, y):
    """parameters of my windows"""
    up()
    goto(x,y)
    down()
    fillcolor("white")
    begin_fill()
    for i in range(2):
        fd(30)
        lt(90)
        fd(30)
        lt(90)
    end_fill()

def door(x, y):
    """Parametres of the door"""
    up()
    goto(x,y)
    down()
    pencolor("#000000")
    fillcolor("black")
    begin_fill()
    for _ in range(2):
        fd(30)
        lt(90)
        fd(50)
        lt(90)
    end_fill()

def bld(x, y, color):
    rdc(x, y, color)
    number_of_floors = randint(1,3)
    for _ in range(number_of_floors):
        floor(x, y+ 60, color)
        y +=60

bld_1 = bld(0, -100, "red")
bld_2 = bld(150, -100, "green")
bld_3 = bld(-150, -100, "blue")
    


done()
