# @@@ INSERT YOUR NAME HERE

# lab07 for cs20, S16, UCSB (Instructor: Conrad)

# function ithOfNPointsOnCircleX
# contract: (int,int,float) => float
# consumes:
#   i: the point number (between 0 and n-1)
#   n: the number of points
#   r: the radius of the circle (assumed to be centered at 0,0)
# produces:
#   the x value of that point in the cartesian plane

import math

def ithOfNPointsOnCircleX(i,n,r):
    """ 
    return x coordinate of ith value of n points on circle of radius r
    points are numbered from 0 through n-1, spread counterclockwise around circle
    point 0 is at angle 0, as of on a unit circle, i.e. at point (0,r)
    """

    # Hints:
    #   Basic formula is x = r cos (theta)
    #   But you need to use Python notation, and the math module
    #   The theta angle is in radians, and is some "portion" of 2 pi  
    
    return "stub" 

def ithOfNPointsOnCircleY(i,n,r):
    """ 
    return x coordinate of ith value of n points on circle of radius r
    points are numbered from 0 through n-1, spread counterclockwise around circle
    point 0 is at angle 0, as of on a unit circle, i.e. at point (0,r)
    """

    # Hints: similar to ithOfNPointsOnCircleX, but use r sin (theta)
    
    return "stub" # Hint: r sin(theta)



# NEXT, now that we have a way to compute the i points around a circle,
# we can draw some polygons and some stars


def drawPolygon(t,r,n):
    """
    draw a polygon of n sides, centered at (0,0)
    r is radius of the circle that would circumscribe the polygon
    leave turtle at position (0,0) facing right
    """
    
    # pick up the pen, move to the starting point, and put down the pen
    t.up(); t.goto(r,0); t.down()

    # connect the dots for all the points
    
    for i in range(1,n):   # gives points 1 through n-1
        t.goto( ithOfNPointsOnCircleX(i,n,r),
                ithOfNPointsOnCircleY(i,n,r) )

    # That drew almost all the way around---for example, it drew
    #  three sides if we are drawing a square.  To finish, we need to
    #  return to the starting point

    # @@@ PUT IN A LINE OF CODE HERE THAT WILL RETURN TO THE STARTING POINT
    # @@@ PUT AN APPROPRIATE COMMENT BEFORE THE LINE, AND REMOVE THESE COMMENTS


    # Now pick up the pen, and move back to 0,0, facing east

    t.up(); t.goto(0,0); t.setheading(0);


# tryIt function: this is a function you can call to test different
#  function calls to your drawPolygon and drawStar functions

import turtle


def tryIt():
    # create a turtle
    sheila = turtle.Turtle()

    # @@@ As you work, try uncommenting different lines below to
    # @@@ test your functions

    drawPolygon(sheila, 50.0, 3)
    #drawPolygon(sheila, 100.0, 6)
    #drawPolygon(sheila, 200.0, 8)
    #drawStar(sheila, 40.0, 3) # should draw NOTHING
    #drawStar(sheila, 80.0, 5)
    #drawStar(sheila, 160.0, 6)



# drawStar (turtle, float, int) => void
# consumes:
# produces: nothing
# side-effect:
#    if n < 5, the function returns without doing anything
#    else:
#      the turtle draws a star of n points, centered at 0,0
#      the size of the star is determined by r---it is the right size
#        that it could be inscribed in a circle of radius r
#      the turtle is left at position 0,0, facing right
#      the old position and direction of the turtle is lost.
#      The star is drawn by connecting each point to a point that is
#       two points away (i.e. we skip one point)

def drawStar(t,r,n):
    """ 
    using turtle t, draw a star with n points centered at (0,0)
    r is the circle that would circumsribe the star
    """

    # if n < 5, we can't really draw a star, so just return

    if n<5:
        return     # Doesn't return anything.  It just ends the function call

    # pick up the pen
    t.up();
    
    # connect the dots for all the points
    
    for i in range(n):   # gives points 0 through n-1

        # pen is up---we move to this point    
            
        t.goto( ithOfNPointsOnCircleX(i,n,r),
                ithOfNPointsOnCircleY(i,n,r) )

        # put the pen down

        t.down()

        # now draw a line to the point two points away from this one
        
        t.goto( ithOfNPointsOnCircleX(i+2,n,r),
                ithOfNPointsOnCircleY(i+2,n,r) )

        # lift the pen back up

        t.up()

        
    # Now pick up the pen, and move back to 0,0, facing east

    t.up(); t.goto(0,0); t.setheading(0);



# @@@ Now, make a version of drawStar that is generalized called drawStarAtXY
# @@@ This is a generalization of the drawStar function--what is NOT hard coded
# @@@ is that the center of the star does not have to be at 0,0

def drawStarAtXY(t,r,n,x,y):
    """ 
    using turtle t, draw a star with n points centered at (x,y)
    r is the circle that would circumsribe the star
    """

    # @@@ Start with the same code as in drawStar(t,r,n)
    # @@@ You just need to add x and y to the values returned from
    # @@@ ithOfNPointsOnCircleX and ithOfNPointsOnCircleY
    # @@@ Test by calling testDrawStarAtXY() at the Python Command Prompt

 
    
    return   # stub!



def testDrawStarAtXY():
    """
    Try drawing different stars to see if drawStarAtXY() works properly
    Stars should appear in 1st, and 4th quadrants.
    """

    # create a turtle
    estrella = turtle.Turtle()

    drawStarAtXY(estrella, 40.0, 3, 0,0) # this should not draw anything
    drawStarAtXY(estrella, 80.0, 5, 100,100)  
    drawStarAtXY(estrella, 70.0, 6, 100,-100)
    drawStarAtXY(estrella, 40.0,  8, 200,200)


def drawPolygonAtXY(t,n,r,x,y):
    """
    draw a polygon of n sides, centered at (x,y)
    r is radius of the circle that would circumscribe the polygon
    leave turtle at position (x,y) facing right
    """

    return #stub

def testDrawPolygonAtXY():
    """ test drawPolygonAtXY(); polygons should appear in 2nd and 3rd quadrants """

    dave = turtle.Turtle()

    drawPolygonAtXY(dave, 3, 50.0, -200,0)
    drawPolygonAtXY(dave, 6, 40.0, -200, 100)
    drawPolygonAtXY(dave, 8, 80.0, -200, -200)

def Main():
    """ draw some stars and some polygons """
    testDrawStarAtXY()
    testDrawPolygonAtXY()


if __name__ == "__main__":
    tryIt()  # @@@ COMMENTED OUT AT FIRST
    # Main()   # @@@ COMMENTED OUT AT FIRST
