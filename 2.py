a=input("ahoj, jak ti mám říkat?")
print("ahoj"+" "+a)
b=input("co chceš nakreslit")
from turtle import *
if b=="kruh":
    speed(200)
    for i in range(360):
        forward(3)
        left(1)
elif b=="čtverec":
    for i in range(4):
        left(90)
        forward(100)


