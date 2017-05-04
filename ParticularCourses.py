class ParticularCourses:
    '''
    A class that stores the course information such as Course ID, Course Name,
    and the Major ID for a given course
    '''

    __slots__ = 'id', 'cname', 'major_id'

    def __init__(self, id, cname, major_id):
        '''
        Parameterized constructor for creating a course object.
        :param id: Unique Course ID 
        :param cname: Name of a given course
        :param major_id: Major ID corresponding to the course in a given major
        '''
        self.id = id
        self.cname = cname
        self.major_id = major_id

    def dump_course(self):
        '''
        Creates and Returns a JSON object corresponding to a given course object
        :return: A JSON object corresponding to a given course object
        '''
        return {"course": {"id": self.id,
                           "cname": self.cname,
                           "major_id": self.major_id}}
