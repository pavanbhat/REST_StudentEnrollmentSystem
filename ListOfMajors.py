class ListOfMajors:
    '''
    A class that stores a list of Major objects
    '''
    __slots__ = 'major_data'

    def __init__(self):
        '''
        Default Constructor, creates a list called major_data
        '''
        self.major_data = []

    def get_major_data(self):
        '''
        Gets the Major information of all majors
        :return: a list of Major information of all majors
        '''
        return self.major_data

    def set_major_data(self, major):
        '''
        Sets/Appends the list of major_data with a Major object
        :param major: An object of class Major
        :return: None
        '''
        self.major_data.append(major)

    def remove_major_data(self, major_id):
        '''
        Removes the major information corresponding to a given major with major ID
        :param major_id: id of a given major to be removed from the list
        :return: None
        '''
        try:
            if len(self.major_data) > 0:
                for i in range(len(self.major_data)):
                    if self.major_data[i].id == major_id:
                        del self.major_data[i]
                        break
        except Exception as e:
            print(e)

    def remove_all_major_data(self):
        '''
        Removes all the elements from the list of Majors
        :return: None
        '''
        self.major_data = []