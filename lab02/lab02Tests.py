# lab02Tests.py    Tests for lab02, UCSB CMPTGCS 20, T. Penebaker, 04/14/2016

import unittest                   # this is so we can set up testing of functions

# the imports below import the functions we want to test

from lab02Funcs import *

class TestLab02Functions(unittest.TestCase):   # This is how you do testing in Python

    # Every test case should be a function definition
    # The name should start with test_ and the parameter should be "self".
    # Then, you can write tests using self.assertEqual(actual, expected) and
    # self.assertAlmostEquals(actual, expected, numberOfDecimalPlaces)
    #
    # If an answer should be exact (e.g. integer math), use assertEqual
    # If an answer is approximate (floating pt math, square roots, pi, etc.)
    #    use assertAlmostEqual

    # Test perimRect
    def test_perimRect1(self):
        self.assertEqual(perimRect(2,3), 10)

    def test_perimRect2(self):
        self.assertAlmostEqual(perimRect(4,2.5), 13.0, 2)
        # accurate to two decimal places

    def test_perimRect3(self):
        self.assertEqual(perimRect(3,3), 12)


    # Test areaRect
    def test_areaRect1(self):
        self.assertEqual(areaRect(2,3), 6)

    def test_areaRect2(self):
        self.assertAlmostEqual(areaRect(4,2.5), 10)

    def test_areaRect3(self):
        self.assertEqual(areaRect(3,3), 9)
    

    # Test isList
    def test_isList1(self):
        self.assertEqual( isList(3),   False)

    def test_isList2(self):
        self.assertEqual( isList([3]),   True)

    def test_isList3(self):
        self.assertEqual( isList([5,10,15,20]),   True)

    def test_isList4(self):
        self.assertEqual( isList("foo"),   False)

    def test_isList5(self):
        self.assertEqual( isList(["John","Paul","Ringo","George"]),   True)

    def test_isList6(self):
        self.assertEqual( isList([]),   True)

    
    # Test isString
    def test_isString1(self):
        self.assertEqual(isString(""),True)

    def test_isString2(self):
        self.assertEqual(isString("derp"),True)

    def test_isString3(self):
        self.assertEqual(isString(["derp"]),False)

    def test_isString4(self):
        self.assertEqual(isString(42),False)


    # tests for isPrimaryColor
    def test_isPrimaryColor1(self):
        self.assertEqual( isAdditivePrimaryColor("blue"), True)

    def test_isPrimaryColor2(self):
        self.assertEqual( isAdditivePrimaryColor("black"),    False)

    def test_isPrimaryColor3(self):
        self.assertEqual( isAdditivePrimaryColor(42),    False)


    # tests for isSimpleNumeric
    def test_isSimpleNumeric1(self):
        self.assertEqual( isSimpleNumeric(5),   True)

    def test_isSimpleNumeric2(self):
        self.assertEqual( isSimpleNumeric(3.5),   True)

    def test_isSimpleNumeric3(self):
        self.assertEqual( isSimpleNumeric("5"),   False)

    def test_isSimpleNumeric4(self):
        self.assertEqual( isSimpleNumeric([5]),   False)

    def test_isSimpleNumeric5(self):
        self.assertEqual( isSimpleNumeric(6.0221415E23),   True)

# This code says: when you run this file, run the tests!
if __name__ == '__main__':
    unittest.main(exit=False)
