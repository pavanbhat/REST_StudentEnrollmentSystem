class ListOfStudents:
    '''
    A class that stores a list of Student objects
    '''
    __slots__ = 'student_data'

    def __init__(self):
        '''
        Default Constructor, creates a list called student_data
        '''
        self.student_data = []

    def get_student_data(self):
        '''
        Gets the Student information of all students
        :return: a list of Student information of all students
        '''
        return self.student_data

    def set_student_data(self, student):
        '''
        Sets/Appends the list of student_data with a Student object
        :param student: An object of class Student
        :return: None
        '''
        self.student_data.append(student)

    def remove_student_data(self, student_id):
        '''
        Removes the student information corresponding to a given student with student ID
        :param student_id: id of a given student to be removed from the list
        :return: None
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
        Removes all the elements from the list of Students
        :return: None
        '''
        self.student_data = []