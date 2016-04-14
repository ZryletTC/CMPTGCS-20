# Draws a Koch snowflake --still in progress

import turtle, math
from turtle import *

def koch(l,s): #level and size
    turtle.clearscreen()
    turtle.screensize(2000,2000)
    t = turtle.Turtle()
    t.speed(0)
    t.setpos(-s/2.,-s/3.*math.sin(math.pi/3))
    t.clear()
    t.ht()
    turtle.tracer(0,0)
    for i in range(3):
        kochLine(l,s,t)
        t.left(120)
        turtle.update()
    turtle.exitonclick()

def kochLine(l,s,t):
    if (l<=2):
        t.forward(s/3.)
    else:
        kochLine(l-1,s/3.,t)
    if (l>1):
        t.right(60)
        kochLine(l-1,s/3.,t)
        t.left(120)
        kochLine(l-1,s/3.,t)
        t.right(60)
    else:
        t.forward(s/3.)
    if (l<=2):
        t.forward(s/3.)
    else:
        kochLine(l-1,s/3.,t)
        
#--------------------------------

#koch(input("Level? "),input("Size? "))
