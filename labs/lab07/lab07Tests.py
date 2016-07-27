# Tyler Pennebaker
# lab07Tests.py    Tests for lab07, UCSB CS20, S16, P. Conrad

import unittest            
from lab07Funcs import *   

class TestLab07Functions(unittest.TestCase): 

    # tests for ithOfNPointsOnCircleX
    def test_ithOfNPointsOnCircleX_1(self):
         """ point is at the right hand side of the unit circle, so x = r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(0,4,1.0), 1.0, 3)

    def test_ithOfNPointsOnCircleX_2(self):
         """ point is at the right hand side of the unit circle, so x = r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(0,4,2.5), 2.5, 3)

    def test_ithOfNPointsOnCircleX_3(self):
         """ point is at the top of unit circle, so x = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(1,4,1.0), 0, 3)

    def test_ithOfNPointsOnCircleX_4(self):
         """ point is at the top of the unit circle, so x = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(1,4,2.5), 0, 3)

    def test_ithOfNPointsOnCircleX_5(self):
         """ point is at the left of unit circle, so x = -r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(2,4,1.0), -1.0, 3)

    def test_ithOfNPointsOnCircleX_6(self):
         """ point is at the left of the unit circle, so x = -r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(2,4,2.5), -2.5, 3)

    def test_ithOfNPointsOnCircleX_7(self):
         """ point is at the bottom of unit circle, so x = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(3,4,1.0), 0, 3)

    def test_ithOfNPointsOnCircleX_8(self):
         """ point is at the bottom of the unit circle, so x = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleX(3,4,2.5), 0, 3)

    def test_ithOfNPointsOnCircleX_9(self):
        """
        point is 120 degrees around, counter clockwise.
        we end up with a 30/60/90 triangle, with a hypotenuse of 1.
        That makes the short side of the triangle value 1/2, or 0.5
        But since it is in the second quadrant, it is -1/2 or -0.5
        """
        self.assertAlmostEqual(ithOfNPointsOnCircleX(1,3,1), -0.5, 3)

    def test_ithOfNPointsOnCircleX_10(self):
        """
        point is 120 degrees around, counter clockwise.
        we end up with a 30/60/90 triangle, with a hypotenuse of 2.5
        That makes the short side of the triangle value 1.25
        But since it is in the second quadrant, it is -1.25 
        """
        self.assertAlmostEqual(ithOfNPointsOnCircleX(1,3,2.5), -1.25, 3)

    def test_ithOfNPointsOnCircleX_11(self):
        """
        point is 240 degrees around, counter clockwise.
        we end up with a 30/60/90 triangle, with a hypotenuse of 1.0
        That makes the short side of the triangle value 0.5
        But since it is in the third quadrant, it is -0.5 
        """
        self.assertAlmostEqual(ithOfNPointsOnCircleX(2,3,1.0),-0.5, 3)


    # tests for ithOfNPointsOnCircleY
    def test_ithOfNPointsOnCircleY_1(self):
         """ point is at the right hand side of the unit circle, so y = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(0,4,1.0), 0.0, 3)

    def test_ithOfNPointsOnCircleY_2(self):
         """ point is at the right hand side of the unit circle, so y = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(0,4,2.5), 0.0, 3)

    def test_ithOfNPointsOnCircleY_3(self):
         """ point is at the top of unit circle, so y = r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(1,4,1.0), 1.0, 3)

    def test_ithOfNPointsOnCircleY_4(self):
         """ point is at the top of the unit circle, so y = r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(1,4,2.5), 2.5, 3)

    def test_ithOfNPointsOnCircleY_5(self):
         """ point is at the left of unit circle, so y = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(2,4,1.0), 0.0, 3)

    def test_ithOfNPointsOnCircleY_6(self):
         """ point is at the left of the unit circle, so y = 0 """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(2,4,2.5), 0.0, 3)

    def test_ithOfNPointsOnCircleY_7(self):
         """ point is at the bottom of unit circle, so y = -r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(3,4,1.0), -1.0, 3)

    def test_ithOfNPointsOnCircleY_8(self):
         """ point is at the bottom of the unit circle, so y = -r """ 
         self.assertAlmostEqual( ithOfNPointsOnCircleY(3,4,2.5), -2.5, 3)


    # End of tests for lab07

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

    # runTestsWithPrefix("lab07Tests.py","test_ithOfNPointsOnCircleX") 
