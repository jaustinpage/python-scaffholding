#!/usr/bin/env python

import logging
import optparse
#import sys
import unittest

from scaffholding import MyClass

def get_logger(log_level=logging.INFO):
    '''
    Set up some common logging stuff. Source this from module functions or class functions
    '''
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Logger created")
    return logger

class MyTest(unittest.TestCase):
    '''
    Test a single function
    '''
    def setUp(self):
        self.myclass = MyClass()
    def test(self):
        self.assertEqual(self.myclass.returns_one(), 1) 

def main():
    '''
    The main function
    '''
    logger = get_logger()
    logger.info("Program Started")
    unittest.main()

if __name__ == "__main__":
    '''
    Don't do real work here, just hand this over to the main function.
    '''
    main()
