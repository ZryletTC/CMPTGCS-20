#test tempConversions with unittest

from tempConversions import fToC
from tempConversions import cToF

import unittest

class TestTempConversions(unittest.TestCase):

  # When using unittest, we list our test cases here
  #

  def test_fToC_32_gives_0(self):
    self.assertAlmostEqual( 0.0,  fToC(32.0) )

  def test_cToF_0_gives_32(self):
    self.assertAlmostEqual( 32.0,  cToF(0.0) )

  def test_fToC_100_gives_212(self):
    self.assertAlmostEqual( 100.0,  fToC(212.0) )

  def test_cToF_212_gives_100(self):
    self.assertAlmostEqual( 212.0,  cToF(100.0) )


  # Add more test cases here, indented exactly like the ones above




# THE CODE BELOW THIS LINE SHOULD BE LEFT ALONE
# The if test below says, in essence, when you run this file,
# please run all of the unit tests.
if __name__ == '__main__':
    unittest.main()
