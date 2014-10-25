#!/usr/bin/env python

import logging
import optparse
import sys

def get_logger(log_level=logging.INFO):
    '''
    Set up some common logging stuff. Source this from module functions or class functions
    '''
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Logger created")
    return logger

def get_command_line():
    '''
    Get command line options and arguments, and set up help.
    '''
    logger = get_logger()
    parser = optparse.OptionParser()
    parser.add_option('-t', '--test', dest='test', default=False, action='store_true', help='Run unit tests and exit')
    (opts, args) = parser.parse_args()
    logger.info("Got command line arguments")

    # Check for mandatories
    #mandatories = ['foo', 'bar']
    #for m in mandatories:
    #    if not opts.__dict__[m]:
    #        logger.error("Mandatory option is missing!")
    #        parser.print_help()
    #        sys.exit(-1)
    
    return (opts, args)

class MyClass(object):
    '''
    My class
    '''
    def __init__(self, logger=None):
        '''
        Logging is good!
        '''
        self.logger = logger or get_logger()
    def returns_one(self):
        '''
        Simple function that returns int 1
        '''
        return 1

def main():
    '''
    The main function
    '''
    logger = get_logger()
    logger.info("Program Started")
    (opts, args) = get_command_line()

    logger.info("Program Finished")
    sys.exit(0)

if __name__ == "__main__":
    '''
    Don't do real work here, just hand this over to the main function.
    '''
    main()