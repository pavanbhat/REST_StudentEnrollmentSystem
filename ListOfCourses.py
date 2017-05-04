class ListOfCourses:
    '''
     A class that stores a list of Course objects
    '''
    __slots__ = 'course_data'

    def __init__(self):
        '''
        Default Constructor, creates a list called course_data
        '''
        self.course_data = []

    def get_course_data(self):
        '''
        Gets the Course information of all courses
        :return: a list of Course information of all courses
        '''
        return self.course_data

    def set_course_data(self, course):
        '''
        Sets/Appends the list of course_data with a Course object
        :param course: An object of class Course
        :return: None
        '''
        self.course_data.append(course)

    def remove_course_data(self, course_id):
        '''
        Removes the course information corresponding to a given course with course ID
        :param course_id: id of a given course to be removed from the list
        :return: None
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
        Removes all the elements from the list of Courses
        :return: None
        '''
        self.course_data = []