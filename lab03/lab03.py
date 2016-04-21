# lab03.py for Tyler Pennebaker
# CS20, Spring 2016, Instructor: Phill Conrad
# Draw some initials using turtle graphics

import turtle

def drawT(t,w,h): #draws a letter 'T' w/ width, w, and height, h using turtle, t
    #Find start point
    x0 = t.xcor()
    y0 = t.ycor()

    #Draw letter using multiple points
    t.up()
    t.setpos(x0,y0+h)
    t.down()
    t.setpos(x0+w,y0+h)
    t.setpos(x0+w/2.,y0+h)
    t.setpos(x0+w/2.,y0)
    t.up()
    t.setpos(x0+w,y0)

def drawP(t,w,h): #draws a letter 'T' w/ width, w, and height, h using turtle, t
    #Find start point
    x0 = t.xcor()
    y0 = t.ycor()

    #Draw letter using multiple points
    t.down()
    t.setpos(x0,y0+h)
    t.setpos(x0+w*2./3,y0+h)
    t.setpos(x0+w,y0+h*5./6)
    t.setpos(x0+w,y0+h*4./6)
    t.setpos(x0+w*2./3,y0+h/2.)
    t.setpos(x0,y0+h/2.)
    t.up()
    t.setpos(x0+w,y0)

def drawTP(t,w,h,s):
    """
    Draws the initials "TP" with the turtle t using letter width w, height h, and spacing s
    """

    drawT(t,w,h) #draw a T
    
    t.forward(s) # Move forward for the next character
    
    drawP(t,w,h) #draw a P


# Runs the program
billybobjoe = turtle.Turtle()
def go():
    drawTP(billybobjoe,50,100,5)
    
    
