class Major:
    '''

    '''

    __slots__ = 'id', 'mname'

    def __init__(self, id, mname):
        '''

        :param id: 
        :param mname: 
        '''
        self.id = id
        self.mname = mname

    def dump_major(self):
        '''

        :return: 
        '''
        return {"major": {"id": self.id,
                            "mname": self.mname}}
