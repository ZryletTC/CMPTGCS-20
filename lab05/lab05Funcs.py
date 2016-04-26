#   lab05Funcs.py
#   Starting point for lab05, CS8/CS20, 04/29/2014
#   Exercises for working with lists

from lab02Funcs import isList


# @@@ READ OVER THIS FUNCTION---Then delete this @@@ Comment
# @@@ IT IS PROVIDED AS AN EXAMPLE OF HOW TO FIND THE LARGEST ELEMENT IN A LIST
# @@@ THIS IS WHAT YOU DO IF YOU DON'T HAVE A MAX FUNCTION BUILT IN TO YOUR
# @@@ LANGUAGE

def largestInt(listOfInts):
    """
    return largest element of a non-empty list of ints, False otherwise

    That is, return False if parameter is an empty list, or not a list
    parameter is not a list consisting only of ints

    By "largest", we mean a value that is no smaller than any other
    value in the list.  There may be more than one instance of that value.
    Example:  in [7,3,7], 7 is largest

    >>> largestInt([])
    False
    >>> largestInt('foo')
    False
    >>> largestInt([3,5,4.5,6])
    False
    >>> largestInt([4])
    4
    >>> largestInt([-9,4,7,8,2])
    8
    >>>
    """

    if type(listOfInts)!=list or listOfInts==[]:
        return False

    # Now we know there is at least one item in the list.
    # We make an initial assumption that this item will be the largest.
    # We then check every other item in the list--each gets a chance to
    #  knock the maxSoFar out of the winner's circle

    maxSoFar = listOfInts[0]    # the one in position zero is the first candidate


    # Note: we have to start from 0 because we need to check the type
    #  of element[0] to see if it is an int.  Otherwise, we could start from 1

    for i in range(0,len(listOfInts)):  # all indexes in the list

       if type(listOfInts[i])!=int:      # make sure it is an int
          return False

       if listOfInts[i] > maxSoFar:     # compare the new item with maxSoFar
          maxSoFar = listOfInts[i]      # we have a new candidate for the title of "largest int"

    # Now we've gone through the entire list.  Every other item on the list
    # has had a chance to defeat maxSoFar as the largest int.  So the one
    # left in maxSoFar must be the largest one.

    return maxSoFar



# @@@ READ OVER THIS FUNCTION---Then delete this @@@ Comment
# @@@ IT IS PROVIDED AS AN EXAMPLE OF HOW TO FIND THE INDEX
# @@@ OF THE LARGEST ELEMENT IN A LIST
# @@@ NOTE THAT FINDING THE INDEX IS DIFFERENT FROM FINDING THE VALUE


def indexOfLargestInt(listOfInts):
    """
    return index of largest element of non-empty list of ints, or False otherwise

    That is, return False if parameter is an empty list, or not a list
    parameter is not a list consisting only of ints

    By "largest", we mean a value that is no smaller than any other
    value in the list.  There may be more than one instance of that value.
    Example:  in [7,3,7], 7 is largest

    By "index", we mean the subscript that will select that item of the list when placed in []
    Since there can be more than one largest, we'll return the index of the first such value in those cases,
    i.e. the one with the lowest index.

    >>> indexOfLargestInt([])
    False
    >>> indexOfLargestInt('foo')
    False
    >>> indexOfLargestInt([3,5,4.5,6])
    False
    >>> indexOfLargestInt([40])
    0
    >>> indexOfLargestInt([-90,40,70,80,20])
    3
    >>> indexOfLargestInt([10,30,50,20,50])
    2
    >>>
    """

    if type(listOfInts)!=list or listOfInts==[]:
        return False

    # Now we know there is at least one item in the list.
    # We make an initial assumption that this item will be the largest.
    # We then check every other item in the list

    indexOfMaxSoFar = 0    # the one in position zero is the first candidate


    # Note: we have to start from 0 because we need to check the type
    #  of element[0] to see if it is an int.  Otherwise, we could start from 1

    for i in range(0,len(listOfInts)):  # all indexes in the list

       if type(listOfInts[i])!=int:      # make sure it is an int
          return False

       if listOfInts[i] > listOfInts[indexOfMaxSoFar]:  # compare new item
          indexOfMaxSoFar = i  # we have a new candidate

    # Now we've gone through the entire list. If some other index were that
    # of a larger int, we would have changed indexOfMaxSoFar to that.  So
    # what we are left with must be the index of the largest one.

    return indexOfMaxSoFar


# @@@ NOW: complete the function below
# @@@  It will be similar to largestInt
# @@@ Add your own test cases

def smallestInt(listOfInts):
    """
    return value of smallest element of non-empty list of ints, or False otherwise

    That is, return False if parameter is an empty list, or not a list
    parameter is not a list consisting only of ints

    By "smallest", we mean a value that is no larger than any other
    value in the list.  There may be more than one instance of that value.
    Example:  in [7,3,3,7],3 is smallest



    >>> smallestInt([])
    False
    >>> smallestInt('foo')
    False
    >>> smallestInt([3,5,4.5,6])
    False
    >>> smallestInt([40])
    40
    >>> smallestInt([20,-90,40,70,80])
    -90
    >>> smallestInt([50,30,10,30,50,10])
    10
    >>>
    """

    return "stub"





# @@@ NOW: complete the function below
# @@@  It will be similar to indexOfLargestInt

def indexOfSmallestInt(listOfInts):
    """
    return index of smallest element of non-empty list of ints, or False otherwise

    That is, return False if parameter is an empty list, or not a list
    parameter is not a list consisting only of ints

    By "smallest", we mean a value that is no larger than any other
    value in the l  There may be more than one instance of that value.
    Example:  in [7,3,3,7],3 is smallest

    By "index", we mean the subscript that will select that item of the list when placed in []
    Since there can be more than one smallest, we'll return the index of the first such value in those cases,
    i.e. the one with the lowest index.

    >>> indexOfSmallestInt([])
    False
    >>> indexOfSmallestInt('foo')
    False
    >>> indexOfSmallestInt([3,5,4.5,6])
    False
    >>> indexOfSmallestInt([40])
    0
    >>> indexOfSmallestInt([-90,40,70,80,20])
    0
    >>> indexOfSmallestInt([10,30,-50,20,-50])
    2
    >>>
    """


    return "stub"


# @@@ NOW: complete the function below
# @@@  You'll have to decide which of the models above fits
# @@@  Recall that len(s) returns the length of a string
# @@@  If you have a listOfStrings, then len(listOfStrings[i])) returns the length
# @@@    of the ith string in that list

def longestString(listOfStrings):
    """
    return longest string from a non-empty list of strings, False otherwise

    By "longest", we mean a value that is no shorter than any other value in the list

    There may be more than one string that would qualify,
      For example in the list ["dog","bear","wolf","cat"] both  bear and wolf are longest strings
      In such cases, return the one with the lowest index (in this case, bear)

    return False for empty list, not a list, or a list with at least one non-string item

    >>> longestString([])
    False
    >>> longestString('foo')
    False
    >>> longestString(['foo'])
    'foo'
    >>> longestString(['bear','cat','dog','mouse'])
    'mouse'
    >>> longestString(['cat','wolf','bear','dog'])
    'wolf'
    >>>
    """

    return "stub"





# @@@ NOW: complete the function below
# @@@  You'll have to decide which of the models above fits

def indexOfShortestString(listOfStrings):
    """
    return index of shortest string from a non-empty list of strings, False otherwise

    By "shortest", we mean a value that is no longer than any other value in the list

    There may be more than one string that would qualify,
      For example in the list ["dog","bear","wolf","cat"] both dog and cat are shortest strings
      In such cases, return the one with the lowest index (in this case, dog)

    return False for empty list, not a list, or a list with at least one non-string item

    >>> indexOfShortestString([])
    False
    >>> indexOfShortestString('foo')
    False
    >>> indexOfShortestString(['foo'])
    0
    >>> indexOfShortestString(['bear','cat','dog','mouse'])
    1
    >>>

    """
    return "stub"





