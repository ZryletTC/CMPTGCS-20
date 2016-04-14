# Draws a Koch snowflake --still in progress

import turtle, math

def koch(l,s): #level and size
    t = turtle.Turtle()
    for i in range(3):
        kochLine(l,s,t)
        t.left(120)

def kochLine(l,s,t):
    if (l<=2):
        t.forward(s/3)
    else:
        t.right(60)
        kochLine(l-1,s/3,t)
        t.left(120)
        kochLine(l-1,s/3,t)
        t.right(60)

    if (l==1):
        t.forward(s/3)
    else:
        t.right(60)
        kochLine(l-1,s/3,t)
        t.left(120)
        kochLine(l-1,s/3,t)
        t.right(60)

    if (l<=2):
        t.forward(s/3)
    else:
        t.right(60)
        kochLine(l-1,s/3,t)
        t.left(120)
        kochLine(l-1,s/3,t)
        t.right(60)
