class Student:
    '''
    A class that stores the student information such as Student ID, First Name, Last Name,
    and Major ID for a given student
    '''

    __slots__ = 'id', 'fname', 'lname', 'major_id'

    def __init__(self, id, fname, lname, major_id):
        '''
        Parameterized constructor for creating a Student object.
        :param id: Unique Student ID 
        :param fname: First Name of a given student
        :param lname: Last Name of a given student
        :param major_id: Major ID corresponding to the major of a given student
        '''
        self.id = id
        self.fname = fname
        self.lname = lname
        self.major_id = major_id


    def dump_student(self):
        '''
        Creates and Returns a JSON object corresponding to a given student object
        :return: A JSON object corresponding to a given student object
        '''
        return {"student": {"id": self.id,
                            "fname": self.fname,
                            "lname": self.lname,
                            "major_id": self.major_id}}
