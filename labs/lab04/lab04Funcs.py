# lab04Funcs.py     Functions that work on lists
# T. Pennebaker for CS20, 04/21/2016


from lab02Funcs import isList
from lab02Funcs import isSimpleNumeric

def notStringContainingE(word): # Returns False if "word" is a string containing 'e' or 'E', otherwise returns True

   if not(type(word)==str):
      return True
   for letter in word:
     if (letter == 'e') or (letter == 'E'):   
       return False
   return True


def hasNoX(word): # Returns False if "word" is a string containing 'x' or 'x', otherwise returns True
   
   if (type(word)!=str):
      return True
   for letter in word:
     if (letter == 'x') or (letter == 'X'):   
       return False
   return True


def isListOfSimpleNumeric(theList): # Returns True if "theList" is a list of only ints and floats, otherwise returns False
   
   if (not isList(theList)):
      return False  # it isn't really a list!

   # Now we can assume that theList really is a list
   # But is it a list of all numerics?
   # If we find even a single item that isn't numeric, we can
   # immediately return false.  
   
   for item in theList:
     if not isSimpleNumeric(item):
       return False

   # If we get here and didn't return yet, then we know everything
   # in the list is a simple numeric!
   # (i.e. there isn't anything in the list that is NOT simple numeric)
   
   return True


def isListOfIntegers(x): # Returns True if "x" is a list of only ints, otherwise returns False
   
   if (type(x)!=list):
      return False

   for entry in x:
      if type(entry)!=int:
         return False
   return True

def isListOfStrings(x): # Returns True if "x" is a list of only strings, otherwise returns False
   
   if (type(x)!=list):
      return False

   for entry in x:
      if type(entry)!=str:
         return False
   return True

def isListOfEvenIntegers(x): # Returns True if "x" is a list of only even ints, otherwise returns False
          
   if (not isListOfIntegers(x)):
      return False

   for entry in x:
      if entry%2!=0:
         return False
   return True


def totalLength(x): # Returns the total number of characters in the list, returns true if not a list
   
   if (type(x)!=list):
      return False

   length = 0

   for word in x:
      if (type(word)==str):
         for letter in word:
            length += 1
   return length


def lengthOfEach(x): # Returns a list of the lengths of any strings in given list "x"
   
   if (type(x)!=list):
      return False

   lengths = []

   for word in x:
      length = 0
      if (type(word)==str):
         for letter in word:
            length += 1
      lengths.append(length)
   return lengths
    

def countEvens(x): # Returns the number of even integers in a given list of integers "x"
   
   if (not isListOfIntegers(x)):
      return False
      
   count = 0
   for number in x:
      if number%2==0:
         count += 1
   return count


### @@@ NOW, write a function called onlyEvens
### @@@ Use the accumulator pattern, starting with an empty list.
### @@@ Use a for loop to traverse the list.  Each time you find an item
### @@@  if it isn't an int, return False---otherwise, if it is even, add
### @@@  it to your accumulated list.


def onlyEvens(listOfInts):

   if (not isListOfIntegers(listOfInts)):
      return False
      
   listOfEvenInts = []
   for number in listOfInts:
      if number%2==0:
         listOfEvenInts.append(number)
   return listOfEvenInts
