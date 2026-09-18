from turtle import *


# forward(100)
up()
backward(256)
right (90)
forward(100)
left(90)
forward(512)
down()




def buildings():
    if pos(0,0):
        return None
    if i == 1 or 3 or 5:
        color("black", "#232555")  # Trait bleu, remplissage jaune
    # elif i == 2 or 4:
    #     color("black","#3e4095") #Trait bleu, remplissage jaune

    begin_fill()
    for i in range(2):
        left(90)
        forward(200)
        left(90)
        forward(50)

    end_fill()

    backward(50)

done()
