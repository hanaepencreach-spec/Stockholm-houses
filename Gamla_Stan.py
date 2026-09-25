from turtle import *
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
    wdw(x+15, y+15)
    door(x+55, 0)
    wdw(x+95, y+15)

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
    for i in range(2):
        fd(30)
        lt(90)
        fd(50)
        lt(90)
    end_fill()

def bld(x, y, color):
    rdc(x, y, color)
    for _ in range(3):
        floor(x, y+ 60, color)
        y +=60

bld_1 =bld(0, 0, "red")
    


done()
