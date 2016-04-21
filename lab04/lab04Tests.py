# lab04Tests.py    Tests for lab04, UCSB CS20, T. Pennebaker, 04/21/2016

import unittest
from lab04Funcs import *


class TestLab04Functions(unittest.TestCase):

    # test cases for notStringContainingE

    def test_notStringContainingE_1(self):
         self.assertEqual( notStringContainingE('Fred') , False)

    def test_notStringContainingE_2(self):
         self.assertEqual( notStringContainingE('Jane') , False)

    def test_notStringContainingE_3(self):
         self.assertEqual( notStringContainingE('Santa') , True)

    def test_notStringContainingE_4(self):
         self.assertEqual( notStringContainingE('Barbara') ,   True)

    def test_notStringContainingE_5(self):
         self.assertEqual( notStringContainingE('Edward') ,  False )

    def test_notStringContainingE_6(self):
         self.assertEqual( notStringContainingE('Ice Cream'),   False)

    def test_notStringContainingE_7(self):
         self.assertEqual( notStringContainingE(23),  True )

    def test_notStringContainingE_8(self):
         self.assertEqual( notStringContainingE(['e']) ,   True)

    # tests for hasNoX

    def test_hasNoX_1(self):
         self.assertEqual( hasNoX('Fred') , True )

    def test_hasNoX_2(self):
         self.assertEqual( hasNoX('Xerox') , False )

    def test_hasNoX_3(self):
         self.assertEqual( hasNoX('Box') , False )

    def test_hasNoX_4(self):
         self.assertEqual( hasNoX('Xbox') , False )

    def test_hasNoX_5(self):
         self.assertEqual( hasNoX(23) , True )

    def test_hasNoX_6(self):
         self.assertEqual( hasNoX(['x']) , True )

    def test_hasNoX_7(self):
         self.assertEqual( hasNoX('x') , False )

    # tests for isListOfSimpleNumeric

    def test_isListOfSimpleNumeric_1(self):
         self.assertEqual( isListOfSimpleNumeric('Fred') , False )

    def test_isListOfSimpleNumeric_2(self):
         self.assertEqual( isListOfSimpleNumeric(3) , False )

    def test_isListOfSimpleNumeric_3(self):
         self.assertEqual( isListOfSimpleNumeric([3]) , True )

    def test_isListOfSimpleNumeric_4(self):
         self.assertEqual( isListOfSimpleNumeric([3.4]) , True )

    def test_isListOfSimpleNumeric_5(self):
         self.assertEqual( isListOfSimpleNumeric([2,3,4,5.6,7]) , True )

    def test_isListOfSimpleNumeric_6(self):
         self.assertEqual( isListOfSimpleNumeric([2,3,'oops',5]) , False )

    def test_isListOfSimpleNumeric_7(self):
         self.assertEqual( isListOfSimpleNumeric([2,3,[4]]) , False )

    def test_isListOfSimpleNumeric_8(self):
         self.assertEqual( isListOfSimpleNumeric([]) , True )

    # tests for isListOfIntegers


    def test_isListOfIntegers_1(self):
         self.assertEqual( isListOfIntegers('Fred') , False )

    def test_isListOfIntegers_2(self):
         self.assertEqual( isListOfIntegers(3) , False )

    def test_isListOfIntegers_3(self):
         self.assertEqual( isListOfIntegers([3]) , True )

    def test_isListOfIntegers_4(self):
         self.assertEqual( isListOfIntegers([3.4]) , False )

    def test_isListOfIntegers_5(self):
         self.assertEqual( isListOfIntegers([2,3,4,5.6,7]) , False )

    def test_isListOfIntegers_6(self):
         self.assertEqual( isListOfIntegers([2,3,'oops',5]) , False )

    def test_isListOfIntegers_7(self):
         self.assertEqual( isListOfIntegers([2,3,4,5,6,7]) , True )

    def test_isListOfIntegers_8(self):
         self.assertEqual( isListOfIntegers([2,3,[4]]) , False )

    def test_isListOfIntegers_9(self):
         self.assertEqual( isListOfIntegers([]) , True )

    # tests for isListOfEvenIntegers

    def test_isListOfEvenIntegers_1(self):
         self.assertEqual( isListOfEvenIntegers('Fred') , False )

    def test_isListOfEvenIntegers_2(self):
         self.assertEqual( isListOfEvenIntegers(3) , False )

    def test_isListOfEvenIntegers_3(self):
         self.assertEqual( isListOfEvenIntegers([3]) , False )

    def test_isListOfEvenIntegers_4(self):
         self.assertEqual( isListOfEvenIntegers([4]) , True )

    def test_isListOfEvenIntegers_5(self):
         self.assertEqual( isListOfEvenIntegers([3.4]) , False )

    def test_isListOfEvenIntegers_6(self):
         self.assertEqual( isListOfEvenIntegers([2,3,4,5.6,7]) , False )

    def test_isListOfEvenIntegers_7(self):
         self.assertEqual( isListOfEvenIntegers([2,3,'oops',5]) , False )

    def test_isListOfEvenIntegers_8(self):
         self.assertEqual( isListOfEvenIntegers([2,3,4,5,6,7]) , False )

    def test_isListOfEvenIntegers_9(self):
         self.assertEqual( isListOfEvenIntegers([2,4,6]) , True )

    def test_isListOfEvenIntegers_10(self):
         self.assertEqual( isListOfEvenIntegers([2,3,[4]]) , False )

    def test_isListOfEvenIntegers_11(self):
         self.assertEqual( isListOfIntegers([]) , True )

    # tests for totalLength

    def test_totalLength_1(self):
        self.assertEqual( totalLength('1'),    False )

    def test_totalLength_2(self):
        self.assertEqual( totalLength(['a','b']),    2)

    def test_totalLength_3(self):
        self.assertEqual( totalLength([]),    0)

    def test_totalLength_4(self):
        self.assertEqual( totalLength(['Go','Gauchos']),    9)

    def test_totalLength_5(self):
        self.assertEqual( totalLength(['x','xxx','xxxx']),    8)

    def test_totalLength_6(self):
        self.assertEqual( totalLength(['x',34,'xxxx']),    5)


    # tests for lengthOfEach


    def test_lengthOfEach_1(self):
        self.assertEqual( lengthOfEach('1') , False )

    def test_lengthOfEach_2(self):
        self.assertEqual( lengthOfEach(['a','b']),    [1, 1])

    def test_lengthOfEach_3(self):
        self.assertEqual( lengthOfEach([]),    [])

    def test_lengthOfEach_4(self):
        self.assertEqual( lengthOfEach(['Go','Gauchos']),    [2, 7])

    def test_lengthOfEach_5(self):
        self.assertEqual( lengthOfEach(['x','xxx','xxxx']),    [1, 3, 4])

    # tests for countEvens

    def test_countEvens_1(self):
        self.assertEqual( countEvens('1') , False )

    def test_countEvens_2(self):
        self.assertEqual( countEvens(['a','b']) , False )

    def test_countEvens_3(self):
        self.assertEqual( countEvens([]),    0)

    def test_countEvens_4(self):
        self.assertEqual( countEvens([1,2,3,4,5]),    2)

    def test_countEvens_5(self):
        self.assertEqual( countEvens([1]),    0)

    def test_countEvens_6(self):
        self.assertEqual( countEvens([3,2]),    1)

    def test_countEvens_7(self):
        self.assertEqual( countEvens([2,3,4]),    2)

    # tests for onlyEvens

    def test_onlyEvens_1(self):
        self.assertEqual( onlyEvens('1') , False )

    def test_onlyEvens_2(self):
        self.assertEqual( onlyEvens(['a','b']) , False )

    def test_onlyEvens_3(self):
        self.assertEqual( onlyEvens([]),    [])

    def test_onlyEvens_4(self):
        self.assertEqual( onlyEvens([1,2,3,4,5]),    [2, 4])

    def test_onlyEvens_5(self):
        self.assertEqual( onlyEvens([1]),    [])

    def test_onlyEvens_6(self):
        self.assertEqual( onlyEvens([1,3]),    [])

    def test_onlyEvens_7(self):
        self.assertEqual( onlyEvens([3,2]),    [2])

    def test_onlyEvens_1(self):
        self.assertEqual( onlyEvens([2,3,4]),    [2, 4])

    # End of tests for lab04


def runTestsWithPrefix(testFile,prefix):
    """
    run only tests from testFile with a certain prefix
    Example: runTestsWithPrefix("lab03Tests.py","test_isPrimaryColor")
    """
    loader = unittest.TestLoader()
    loader.testMethodPrefix = prefix
    suite = loader.discover('.', pattern = testFile)
    unittest.TextTestRunner(verbosity=2).run(suite)


# When you run this file, it runs either ALL the tests, or
# just some tests.  It depends on which line you comment out (or not)

if __name__ == '__main__':

    # To run ALL tests, uncomment the "unittest.main(exit=False)" line
    unittest.main(exit=False)

    # Uncomment "runTestsWithPrefix" line to run just SOME tests
    #    First parameter is name of file with tests
    #    Second parameter is prefix starting with test_
    #      such as test_FtoC  or test_isString

    # runTestsWithPrefix("lab04Tests.py","test_notStringContainingE")
