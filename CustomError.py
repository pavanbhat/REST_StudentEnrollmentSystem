class CustomError(Exception):
    '''
    A class that generates a custom Exception
    '''
    __slots__ = 'value'

    def __init__(self, value):
        '''
        Default constructor that initializes the statement to be returned for 
        the custom exception
        :param value: Statement to be raised for a custom exception
        '''
        self.value = value

    def __str__(self):
        '''
        Overrides the toString method for printing the custom exception
        :return: Statement to be printed when a custom exception is raised
        '''
        return repr(self.value)
