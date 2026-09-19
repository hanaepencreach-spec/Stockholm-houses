from turtle import *

def bld(x,y,L,H,color):
    """Parameters of my skyscrapers"""
    up()
    goto(x,y)
    down()
    fillcolor(color)
    begin_fill()
    for i in range(2):
        fd(L)
        lt(90)
        fd(H)
        lt(90)
    end_fill()

bld(0, 0, 60, 100, "#232555")

def wdw(x, y, L, H, color):
    """parameters of my windows"""
    up()
    goto(x,y)
    down()
    pencolor("#232555")
    fillcolor(color)
    begin_fill()
    for i in range(2):
        fd(L)
        lt(90)
        fd(H)
        lt(90)
    end_fill()
    
y = [10, 30, 50, 70]
for ordo in y:
    wdw(10,ordo, 15, 10, "white")
    wdw(45,ordo, 15, 10, "white")



done()
