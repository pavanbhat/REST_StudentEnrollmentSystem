class Course:
    '''

    '''

    __slots__ = 'id', 'cname', 'major_id'

    def __init__(self, id, cname, major_id):
        '''

        :param id: 
        :param cname: 
        :param major_id: 
        '''
        self.id = id
        self.cname = cname
        self.major_id = major_id

    def dump_course(self):
        '''

        :return: 
        '''
        return {"course": {"id": self.id,
                            "cname": self.cname,
                            "major_id": self.major_id}}
