import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

class Error(Exception):
    '''
    Base class for custom exceptions
    '''
    pass

class MyError(Exception):
    '''
    Some sort of custom exception
    '''
    pass

class MyClass(object):
    '''
    My class. it does things
    '''
    def __init__(self):
        logging.debug("My class was instantiated")
        super(MyClass, self).__init__()

    def returns_one(self):
        '''
        It returns one yo.
        '''
        return 1
