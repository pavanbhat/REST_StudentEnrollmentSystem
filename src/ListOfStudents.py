class ListOfStudents:
    '''
    
    '''
    __slots__ = 'student_data'

    def __init__(self):
        '''
        
        '''
        self.student_data = []

    def get_student_data(self):
        '''
        
        :return: 
        '''
        return self.student_data

    def set_student_data(self, student):
        '''
        
        :param student: 
        :return: 
        '''
        self.student_data.append(student)

    def remove_student_data(self, student_id):
        '''
        
        :param student_id: 
        :return: 
        '''
        try:
            if len(self.student_data) > 0:
                for i in range(len(self.student_data)):
                    if self.student_data[i].id == student_id:
                        del self.student_data[i]
                        break
        except Exception as e:
            print(e)

    def remove_all_student_data(self):
        '''
        
        :return: 
        '''
        self.student_data = []