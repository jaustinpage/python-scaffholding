import unittest as unittest

from scaffholding.scaffholding import MyClass

class MyTest(unittest.TestCase):
    '''
    Test a single function
    '''
    def setUp(self):
        self.my_class = MyClass()

    def runTest(self):
        self.assertEqual(self.my_class.returns_one(), 1)
