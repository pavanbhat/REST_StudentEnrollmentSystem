class ListOfCourses:
    '''

    '''
    __slots__ = 'course_data'

    def __init__(self):
        '''

        '''
        self.course_data = []

    def get_course_data(self):
        '''

        :return: 
        '''
        return self.course_data

    def set_course_data(self, course):
        '''

        :param course: 
        :return: 
        '''
        self.course_data.append(course)

    def remove_course_data(self, course_id):
        '''

        :param course_id: 
        :return: 
        '''
        try:
            if len(self.course_data) > 0:
                for i in range(len(self.course_data)):
                    if self.course_data[i].id == course_id:
                        del self.course_data[i]
                        break
        except Exception as e:
            print(e)

    def remove_all_course_data(self):
        '''

        :return: 
        '''
        self.course_data = []