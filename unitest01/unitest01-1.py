
import unittest
import HTMLTestRunner
from test.test_datetime import setUpClass

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."
        
if __name__ == '__main__':
    unittest.main()
