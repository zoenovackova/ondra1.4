from turtle import *
a=input("ahoj napis svoje jmeno")
print("ahoj "+a)
d=input("co je tvoje nejoblíbenější barva")
if d=="modrá":
    color("blue")
elif d=="červená":
    color("red")
elif d=="zelená":
    color("green")
b=input("co chceš nakreslit?")
if b=="čtverec":
    from turtle import *
    shape("turtle")
    speed(10)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

elif b=="trojúhelník":
    from turtle import *
    shape("turtle")
    speed(10)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

else:
 print("nerozumím, zkus jiný tvar")
 b=input("co chceš nakreslit?")
if b=="čtverec":
    from turtle import *
    shape("turtle")
    speed(10)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

elif b=="trojúhelník":
    from turtle import *
    shape("turtle")
    speed(10)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

c=input("máš nějaký oblíbený tvar")
if c=="ano":
    input("a jaký je tvůj oblíbený tvar")
    print("aha")

elif c=="ne":
    print("nevadí")

else:
    print("aha")










