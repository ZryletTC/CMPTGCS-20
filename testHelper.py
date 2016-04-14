# testHelper.py

# If you have a file like lab03Tests.py or lab04Tests.py with
# so many tests that it gets confusing, this file can help you
# focus on just one function at a time.

# See the comments at the bottom.

import unittest

def runTestsWithPrefix(testFile,prefix):
    """
    run only tests from testFile with a certain prefix
    Example: runTestsWithPrefix("lab02Tests.py","test_isPrimaryColor")
    """
    loader = unittest.TestLoader()
    loader.testMethodPrefix = prefix
    suite = loader.discover('.', pattern = testFile)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":

    # Change the parameters to runTestsWithPrefix as needed
    runTestsWithPrefix("lab02Tests.py","test_isSimpleNumeric")
