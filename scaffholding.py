#!/usr/bin/env python

import logging
import argparse
import sys

CONFIG_FILE="scaffholding.config"

def get_logger(log_level=logging.WARNING):
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', dest='verbose', default=False, action='store_true', help='Enable verbose logging')
    args = parser.parse_args()
    logger.info("Got command line arguments")

    # Check for mandatories
    #mandatories = ['foo', 'bar']
    #for m in mandatories:
    #    if not opts.__dict__[m]:
    #        logger.error("Mandatory option is missing!")
    #        parser.print_help()
    #        sys.exit(-1)
    
    return args

def get_config_file():
    '''
    If you want to use a config file, use this.
    '''
    if os.path.isfile(CONFIG_FILE):
        config_file = ConfigParser.ConfigParser()
        config_file.read(CONFIG_FILE)
        first_variable = config_file.get('scaffholding', 'first_varariable')
        second_variable = config_file.get('scaffholding', 'second_variable')
        return (first_variable, second_variable)
    else:
        raise Exception("Could not find config file: %s" % CONFIG_FILE)


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
    args = get_command_line()
    logger = None
    if args.verbose:
        logger = get_logger(log_level=logging.info)
    else:
        logger = get_logger()
    logger.info("Program Started")

    logger.info("Program Finished")
    sys.exit(0)

if __name__ == "__main__":
    '''
    Don't do real work here, just hand this over to the main function.
    '''
    main()
