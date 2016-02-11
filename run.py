#!/usr/bin/env python

import argparse
import daemon
import logging
import os
import sys

import ConfigParser

from scaffholding.scaffholding import MyClass
from scaffholding.scaffholding import MyError

CONFIG_FILE="config/config1"

_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
_LOGGER = logging.getLogger(__name__)

def _configure_logging(log_level=logging.WARNING):
    '''
    Set up some common logging stuff. Source this from module functions or class functions
    '''
    _LOGGER.setLevel(log_level)

    ch = logging.StreamHandler()
    formatter = logging.Formatter(_LOG_FORMAT)
    ch.setFormatter(formatter)

    _LOGGER.addHandler(ch)
    _LOGGER.info("Logger configured")

def _get_command_line():
    ''' 
    Get command line options and arguments, and set up help.
    '''
    parser = argparse.ArgumentParser(
        description='''\
            This program does cool stuff. Sometimes you need environment variables. \
            e.g.\
            export AWS_ACCESS_KEY_ID=""\
            export AWS_SECRET_ACCESS_KEY=""\
            export AWS_DEFAULT_REGION="us-east-1"\
        ''')
    logging_group = parser.add_mutually_exclusive_group()
    logging_group.add_argument('--debug',
                      '-D',
                      dest='log_level',
                      const=logging.DEBUG,
                      default=logging.WARN,
                      action='store_const',
                      help='Enable debug mode. Prepare for 1 megabyte of logs')
    logging_group.add_argument('--verbose',
                      '-v',
                      dest='log_level',
                      const=logging.INFO,
                      default=logging.WARN,
                      action='store_const',
                      help='Enable verbose mode, very chatty, but not like debug')
    parser.add_argument('--daemon',
                      '-d',
                      dest='daemon',
                      action='store_true',
                      default=False,
                      help='Store a string to foo')
    parser.add_argument('--foo',
                      '-f',
                      dest='foo',
                      action='store',
                      type=str,
                      required=True,
                      help='Store a string to foo')
    args = parser.parse_args()
    _LOGGER.debug('The command line arguments are: %s' % args)
    my_env_vars = [(key, value) for key, value in os.environ.items() if 'mysearchbit' in key.lower()]
    _LOGGER.debug('The environment variables i found are: %s' % my_env_vars)
    return args


def _get_config_file():
    '''
    If you want to use a config file, use this.
    '''
    if os.path.isfile(CONFIG_FILE):
        config_file = ConfigParser.ConfigParser()
        config_file.read(CONFIG_FILE)
        first_variable = config_file.get('scaffholding', 'first_variable')
        second_variable = config_file.get('scaffholding', 'second_variable')
        return (first_variable, second_variable)
    else:
        raise Exception("Could not find config file: %s" % CONFIG_FILE)

def _do_daemon():
    '''
    A quick example daemon
    '''
    for i in range(5):
        print("Daemon looped (%s)" % i)
        sleep(1)


def _main():
    '''
    The main function
    '''
    args = _get_command_line()
    _configure_logging(log_level=args.log_level)
    (first, second) = _get_config_file()
    _LOGGER.info("Program Started")
    if args.daemon:
        _LOGGER.info("We are daemon style")
        _LOGGER.info("First is %s" % first)
        _LOGGER.info("Second is %s" % second)
        with daemon.DaemonContext():
            _do_daemon()
    else:
        _LOGGER.info("First is %s" % first)
        _LOGGER.info("Second is %s" % second)
    _LOGGER.info("Program Finished")
    sys.exit(0)

if __name__ == "__main__":
    '''
    Don't do real work here, just hand this over to the main function.
    '''
    _main()
