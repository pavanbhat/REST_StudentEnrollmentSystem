class Student:
    '''
    
    '''

    __slots__ = 'id', 'fname', 'lname', 'major_id'

    def __init__(self, id, fname, lname, major_id):
        '''
        
        :param id: 
        :param fname: 
        :param lname: 
        :param major_id: 
        '''
        self.id = id
        self.fname = fname
        self.lname = lname
        self.major_id = major_id


    def dump_student(self):
        '''
        
        :return: 
        '''
        return {"student": {"id": self.id,
                            "fname": self.fname,
                            "lname": self.lname,
                            "major_id": self.major_id}}
