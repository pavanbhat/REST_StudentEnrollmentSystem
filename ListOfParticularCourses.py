class ListOfParticularCourses:
    '''

    '''
    __slots__ = 'particular_course_data'

    def __init__(self):
        '''

        '''
        self.particular_course_data = []

    def get_particular_course_data(self):
        '''

        :return: 
        '''
        return self.particular_course_data

    def set_particular_course_data(self, course):
        '''

        :param course: 
        :return: 
        '''
        self.particular_course_data.append(course)

    def remove_particular_course_data(self, course_id):
        '''

        :param course_id: 
        :return: 
        '''
        try:
            if len(self.particular_course_data) > 0:
                for i in range(len(self.particular_course_data)):
                    if self.particular_course_data[i].id == course_id:
                        del self.particular_course_data[i]
                        break
        except Exception as e:
            print(e)

    def remove_all_particular_course_data(self):
        '''

        :return: 
        '''
        self.particular_course_data = []
