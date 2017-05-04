class ListOfParticularCourses:
    '''
    A class that stores a list of Courses objects
    '''
    __slots__ = 'particular_course_data'

    def __init__(self):
        '''
        Default Constructor, creates a list called particular_course_data
        '''
        self.particular_course_data = []

    def get_particular_course_data(self):
        '''
        Gets the list of particular courses corresponding to a student
        :return: A list of particular courses corresponding to a student
        '''
        return self.particular_course_data

    def set_particular_course_data(self, course):
        '''
        Sets/Appends the list of particular courses corresponding to a student with a Course object
        :param course: A Course object
        :return: None
        '''
        self.particular_course_data.append(course)

    def remove_particular_course_data(self, course_id):
        '''
        Removes a prticular course object from the list corresponding to a given Course_id
        :param course_id: Course_id for a given course
        :return: None
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
        Removes all elements from the list of particular course objects
        :return: None
        '''
        self.particular_course_data = []
