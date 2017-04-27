class ListOfMajors:
    '''

    '''
    __slots__ = 'major_data'

    def __init__(self):
        '''

        '''
        self.major_data = []

    def get_major_data(self):
        '''

        :return: 
        '''
        return self.major_data

    def set_major_data(self, major):
        '''

        :param major: 
        :return: 
        '''
        self.major_data.append(major)

    def remove_major_data(self, major_id):
        '''

        :param major_id: 
        :return: 
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

        :return: 
        '''
        self.major_data = []