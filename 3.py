from turtle import *


def pismeno_j():
    right(90)
    for i in range (180):
       left(1)
       forward(0.5)
    forward(100)
    left(90)
    forward(50)
    penup()
    left(90)
    forward(100)
    left(90)
    forward(50)
    pendown()



def pismeno_r():
    left(90)
    forward(100)
    right(90)
    for i in range (180):
        right(1)
        forward(0.5)
    left(130)
    forward(65)
    left(50)



def pismeno_s():
    penup()
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(180)
    pendown()
    for i in range(180):
        left(1)
        forward(0.5)
    for i in range(180):
        right(1)
        forward(0.5)
    penup()
    left(180)
    forward(60)
    pendown()



