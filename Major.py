class Major:
    '''
    A class that stores the major information such as Major ID, Major Name for a given major
    '''

    __slots__ = 'id', 'mname'

    def __init__(self, id, mname):
        '''
        Parameterized constructor for constucting a major object
        :param id: Major_id for a given major (Unique)
        :param mname: Major Name for a given major
        '''
        self.id = id
        self.mname = mname

    def dump_major(self):
        '''
        Creates and Returns a JSON object with major information
        :return:  A JSON object with major information
        '''
        return {"major": {"id": self.id,
                            "mname": self.mname}}
