# lab06Tests.py  by Tyler Pennebaker for CS20 lab06,  5/16/16
# Writing to files in Python

import unittest
import lab06Funcs
from lab06Funcs import *
Main()

class TestLab06Functions(unittest.TestCase): 

    # tests for whatMajor 
    def test_whatMajor1(self):
        actualResult = whatMajor("SHARON",lab06Funcs.students)
        expectedResult = "PHYSICS"
        self.assertEqual(actualResult,expectedResult)
    def test_whatMajor2(self):
        actualResult = whatMajor("SARAH",lab06Funcs.students)
        expectedResult = "CS"
        self.assertEqual(actualResult,expectedResult)
    def test_whatMajor3(self):
        actualResult = whatMajor("JACOB",lab06Funcs.students)
        expectedResult = "STATS"
        self.assertEqual(actualResult,expectedResult)

    # tests for whatLName 
    def test_whatLName1(self):
        actualResult = whatLName("SHARON",lab06Funcs.students)
        expectedResult = "ROBINSON"
        self.assertEqual(actualResult,expectedResult)
    def test_whatLName2(self):
        actualResult = whatLName("SARAH",lab06Funcs.students)
        expectedResult = "HALL"
        self.assertEqual(actualResult,expectedResult)
    def test_whatLName3(self):
        actualResult = whatLName("JACOB",lab06Funcs.students)
        expectedResult = "HERNANDEZ"
        self.assertEqual(actualResult,expectedResult)

    # tests for countUndec 
    def test_countUndec1(self):
        actualResult = countUndec(lab06Funcs.students)
        expectedResult = 3
        self.assertEqual(actualResult,expectedResult)
    def test_countUndec2(self):
        actualResult = countUndec([Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
        expectedResult = 1
        self.assertEqual(actualResult,expectedResult)

    # tests for lNamesOfUndec 
    def test_lNamesOfUndec1(self):
        actualResult = lNamesOfUndec(lab06Funcs.students)
        expectedResult = ["RODRIGUEZ","WALKER","YOUNG"]
        self.assertEqual(actualResult,expectedResult)
    def test_lNamesOfUndec2(self):
        actualResult = lNamesOfUndec([Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
        expectedResult = ["GAUCHO"]
        self.assertEqual(actualResult,expectedResult)

    # tests for majorToLNames 
    def test_majorToLNames1(self):
        actualResult = majorToLNames("UNDEC",lab06Funcs.students)
        expectedResult = ["RODRIGUEZ","WALKER","YOUNG"]
        self.assertEqual(actualResult,expectedResult)
    def test_majorToLNames2(self):
        actualResult = majorToLNames("UNDEC",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
        expectedResult = ["GAUCHO"]
        self.assertEqual(actualResult,expectedResult)
    def test_majorToLNames3(self):
        actualResult = majorToLNames("ENGLISH",lab06Funcs.students)
        expectedResult = ["LEE"]
        self.assertEqual(actualResult,expectedResult)
    def test_majorToLNames4(self):
        actualResult = majorToLNames("HISTORY",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
        expectedResult = ["CRUZ"]
        self.assertEqual(actualResult,expectedResult)

    # tests for allStudentsMajoringIn
    def test_allStudentsMajoringIn1(self):
        actualResult = allStudentsMajoringIn("UNDEC",lab06Funcs.students)
        expectedResult = [Student(fName="MICHELLE",lName="RODRIGUEZ",major="UNDEC"),Student(fName="ANTHONY",lName="WALKER",major="UNDEC"),Student(fName="KIMBERLY",lName="YOUNG",major="UNDEC")]
        self.assertEqual(actualResult,expectedResult)
    def test_allStudentsMajoringIn2(self):
        actualResult = allStudentsMajoringIn("UNDEC",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
        expectedResult = [Student("CHRIS","GAUCHO","UNDEC")]
        self.assertEqual(actualResult,expectedResult)
    def test_allStudentsMajoringIn3(self):
        actualResult = allStudentsMajoringIn("ENGLISH",lab06Funcs.students)
        expectedResult = [Student("LAURA","LEE","ENGLISH")]
        self.assertEqual(actualResult,expectedResult)
    def test_allStudentsMajoringIn4(self):
        actualResult = allStudentsMajoringIn("HISTORY",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
        expectedResult = [Student("FRED","CRUZ","HISTORY")]
        self.assertEqual(actualResult,expectedResult)

    # End of tests for lab06

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

    #runTestsWithPrefix("lab06Tests.py","test_allStudentsMajoringIn")
