# lab02Funcs.py     Define a few sample functions in Python
# T. Pennebaker for CMPTGCS 20, Spring 2016


def perimRect(length,width):
   """
   Compute perimiter of rectangle
   >>> perimRect(2,3)
   10
   >>> perimRect(4, 2.5)
   13.0
   >>> perimRect(3, 3)
   12
   >>>
   """
   return 2*(length+width)


def areaRect(length,width):
   """
   compute area of rectangle
   >>> areaRect(2,3)
   6
   >>> areaRect(4, 2.5)
   10.0
   >>> areaRect(3,3)
   9
   >>>
   """
   return length*width


def isList(x):
   """
   returns True if argument is of type list, otherwise False

   >>> isList(3)
   False
   >>> isList([5,10,15,20])
   True
   """

   return ( type(x) == list )   # True if the type of x is a list


def isString(x):
    """"
    return True if x is a string, otherwise False
    """

    return (type(x)==str)

# The following function is provided for you as an example
# of how to write a Python function involving "or"
# This contains HINTS as to how to do the next function definition.

def isAdditivePrimaryColor(color):
    """
    return True if color is a string equal to "red", "green" or "blue", otherwise False
    >>> isAdditivePrimaryColor("blue")
    True
    >>> isAdditivePrimaryColor("black")
    False
    >>> isAdditivePrimaryColor(42)
    False
    >>>
    """

    return ( (color == "red" ) or (color == "green" ) or (color == "blue") )

# NOTE: the following will NOT work for isAdditivePrimaryColor:
#
# def isAdditivePrimaryColor(color):
#   return ( color == "red" or "green" or "blue" )
#
# Try it, and convince yourself that it doesn't work.
# Does it fail to compile, fail to run (python vomit), or just give the
#  wrong answer?    You may be surprised!
# Try it, then try to understand _why_ this doesn't do what you want
# Hints: 'or' is an operator, and it must take operands that are
# either True or False
# (color == "red") is either True or False.  What about the other operands?



def isSimpleNumeric(x):
   """
   returns True if x is has type int or float; anything else, False
   >>> isSimpleNumeric(5)
   True
   >>> isSimpleNumeric(3.5)
   True
   >>> isSimpleNumeric("5")
   False
   >>> isSimpleNumeric([5])
   False
   >>> isSimpleNumeric(6.0221415E23)
   True
   >>>
   """

   return ((type(x)==int) or (type(x)==float))
