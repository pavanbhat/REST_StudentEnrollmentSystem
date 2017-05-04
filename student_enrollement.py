# Importing support libraries
import os

from flask import Flask, request, render_template, json, flash
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

# Importing support classes
from Course import *
from CustomError import *
from ListOfCourses import *
from ListOfMajors import *
from ListOfParticularCourses import *
from ListOfStudents import *
from Major import *
from ParticularCourses import *
from Student import *

# Configuration for FLask App
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'dev-test.crmgtfyiv0nq.us-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'mariadbadmin'
app.config['MYSQL_PASSWORD'] = '28379b156156cbabda4dfe7f5d89c0a1'
app.config['MYSQL_DB'] = 'testdb'
# Initializes the MySql database
db = MySQL(app)
# Initializes bootstrap for the front-end of the application
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    '''
    Landing page for the User interface
    :return: template for the user interface
    '''
    return render_template("student_enrollment.html")


def connect_db():
    '''
    Creates a connection to the database and assigns a cursor to parse through the tables
    :return: the cursor to parse through the tables
    '''
    cursor = db.connection.cursor()
    return cursor


def fetchall_student_data():
    '''
    Fetches the student information from the database and sets the student_list
    :return: None
    '''
    try:
        global student_list
        cursor = connect_db()
        cursor.execute('''select * from Student''')
        table = cursor.fetchall()
        if len(student_list.get_student_data()) > 0:
            student_list.remove_all_student_data()
        for row in table:
            student_list.set_student_data(Student(row[0], row[1], row[2], row[3]))
    except Exception as e:
        print(e)


@app.route('/students', methods=['GET'])
def students():
    '''
    Fetches the student information
    :return: A JSON string with student information
    '''
    try:
        global student_list
        fetchall_student_data()
        return json.dumps([stud.dump_student() for stud in student_list.get_student_data()])
    except Exception as e:
        flash(e, "error")


def fetchall_course_data():
    '''
    Fetches the information of all the courses in the database and sets the course_list
    :return: None
    '''
    try:
        global course_list
        cursor = connect_db()
        cursor.execute('''select * from Courses''')
        table = cursor.fetchall()
        if len(course_list.get_course_data()) > 0:
            course_list.remove_all_course_data()
        for row in table:
            course_list.set_course_data(Course(row[0], row[1], row[2]))
    except Exception as e:
        print(e)


@app.route('/courses', methods=['GET'])
def courses():
    '''
    Fetches the course information
    :return: A JSON string with course information
    '''
    try:
        global course_list
        fetchall_course_data()
        return json.dumps([course.dump_course() for course in course_list.get_course_data()])
    except Exception as e:
        flash(e, "error")


def fetchall_major_data():
    '''
    Fetches the information of all majors from the database and sets the major_list
    :return: None
    '''
    try:
        global major_list
        cursor = connect_db()
        cursor.execute('''select * from Major''')
        table = cursor.fetchall()
        if len(major_list.get_major_data()) > 0:
            major_list.remove_all_major_data()
        for row in table:
            major_list.set_major_data(Major(row[0], row[1]))
    except Exception as e:
        print(e)


@app.route('/majors', methods=['GET'])
def majors():
    '''
    Fetches the information of all majors 
    :return: A JSON string with major information
    '''
    try:
        global major_list
        fetchall_major_data()
        return json.dumps([major.dump_major() for major in major_list.get_major_data()])
    except Exception as e:
        flash(e, "error")


def fetch_particular_courses(major_id):
    '''
    Fetches information of particular courses corresponding to a provided major from the Courses table in the database
    and sets a list particular_courses
    :param major_id: Major_id from the Courses table
    :return: None
    '''
    try:
        global particular_courses
        if len(particular_courses.get_particular_course_data()) > 0:
            particular_courses.remove_all_particular_course_data()
        cursor = connect_db()
        cursor.execute("select * from Courses where Major_id = " + str(major_id))
        table = cursor.fetchall()
        if len(table) > 0:
            for row in table:
                particular_courses.set_particular_course_data(ParticularCourses(row[0], row[1], row[2]))
        else:
            return "No courses to display!"
    except Exception as e:
        print(e)


def fetch_corresponding_major(student_id):
    '''
    Fetches the information of major corresponding to a given student from the Student table in the database
    :param student_id: id from the Student table
    :return: Major_id corresponding to a given student
    '''
    try:
        cursor = connect_db()
        cursor.execute("select * from Student where id = " + str(student_id))
        table = cursor.fetchall()
        if len(table) > 1:
            raise CustomError("Integrity Error! More than one entry for a student_id.")
        elif len(table) < 1:
            raise CustomError("No Student exists with the given student_id.")
        else:
            return table[0][3]
    except CustomError as e:
        print("Exception: ", e.value)


@app.route('/courses/students/<student_id>')
def courses_for_student(student_id):
    '''
    Fetches the courses available to be enrolled for a student
    :param student_id: id from the Student table
    :return: A JSON string with courses information
    '''
    try:
        # Check to see if the student_id provided is a number
        if student_id.isdigit():
            global particular_courses
            major_id = fetch_corresponding_major(student_id)
            fetch_particular_courses(major_id)
            return json.dumps([course.dump_course() for course in particular_courses.get_particular_course_data()])
        else:
            if not student_id.isdigit():
                return "Please enter a valid number for Student ID!"
    except Exception as e:
        flash(e, "error")


@app.route('/students/courses/<course_id>', methods=['GET'])
def get_enrolled_students(course_id):
    '''
    Fetches the students enrolled in a given course from the Enrollment table in the database
    :param course_id: Courses_id from the Courses table
    :return: A JSON string with student information
    '''
    try:
        if course_id.isdigit():
            global enrolled_students
            cursor = connect_db()
            cursor.execute("select * from Enrollment where Courses_id = " + course_id)
            table = cursor.fetchall()
            cursor.execute('''select * from Student''')
            table2 = cursor.fetchall()
            if len(enrolled_students.get_student_data()) > 0:
                enrolled_students.remove_all_student_data()
            for row in table:
                for stud in table2:
                    if stud[0] is row[0]:
                        enrolled_students.set_student_data(Student(stud[0], stud[1], stud[2], stud[3]))
            return json.dumps([stud.dump_student() for stud in enrolled_students.get_student_data()])
        else:
            if not course_id.isdigit():
                return "Please enter a valid number for Course ID!"
    except Exception as e:
        print(e)


@app.route('/students/enroll', methods=['POST'])
def enroll_student():
    '''
    Enrolls a given student based on a given Course_id
    Also, capable of enrolling multiple students at a time
    :return:  String with status of the result on the student's enrollment
    '''
    result = ""
    json_data = request.get_json(force=True)
    if json_data is None:
        return "Please add JSON data as payload! \n <usage> : {""}"
    else:
        if type(json_data) == list:
            for enrollment in json_data:
                student_id = enrollment.get("Student_id")
                course_id = enrollment.get("Course_id")
                result += str(student_id) + ": " + perform_enrollment(str(student_id), str(course_id)) + "\n"
            return result
        else:
            student_id = json_data["Student_id"]
            course_id = json_data["Course_id"]
            return perform_enrollment(str(student_id), str(course_id))


def perform_enrollment(student_id, course_id):
    '''
    Posts the Student_id and Course_id information in the Enrollment table in the database
    Thereby enrolling a student for a given course
    :param student_id: id from the Student table
    :param course_id: Courses_id from the Courses table
    :return: Status of the result on the student's enrollment
    '''
    if student_id.isdigit() and course_id.isdigit():
        flag = False
        isStudent = True
        isCourse = True
        cursor = db.connection.cursor()
        cursor.execute("select * from Student where id = " + str(student_id))
        student_table = cursor.fetchall()
        if len(student_table) < 1:
            isStudent = False
        else:
            cursor.execute("select * from Courses where major_id = " + str(student_table[0][3]))
            particular_courses = cursor.fetchall()
            cursor.execute('''select * from Enrollment''')
            enrollment_table = cursor.fetchall()
        cursor.execute("select * from Courses where id = " + str(course_id))
        course_table = cursor.fetchall()
        if len(course_table) < 1:
            isCourse = False
        if isStudent and isCourse:
            for students in enrollment_table:
                if students[0] is int(student_id) and students[1] is int(course_id):
                    flag = True
                    return "Student already enrolled in the same course!"
                    break
                elif students[0] is int(student_id):
                    flag = True
                    return "Student already enrolled in one course!"
                    break
            if not flag:
                for courses in particular_courses:
                    if courses[0] is int(course_id):
                        cursor.execute(
                            "INSERT INTO Enrollment(Student_id, Courses_id) VALUES(" + student_id + ", " + course_id + ");")
                        db.connection.commit()
                        return "Student Enrolled!"
        else:
            if not isStudent and not isCourse:
                flash("Student and Course do not exist!", "error")
            else:
                if not isStudent:
                    flash("Student does not exist!", "error")
                elif not isCourse:
                    flash("Course does not exist!", "error")
        return "Student Not Enrolled!"
    else:
        if not student_id.isdigit() and not course_id.isdigit():
            return "Please enter a valid number for Student and Course IDs!"
        elif not student_id.isdigit():
            return "Please enter a valid number for Student ID!"
        elif not course_id.isdigit():
            return "Please enter a valid number for Course ID!"

if __name__ == '__main__':
    # Initializes a list of global variables to hold a list of objects
    global student_list, course_list, major_list, particular_courses, enrolled_students
    # A list of students
    student_list = ListOfStudents()
    # A list of courses
    course_list = ListOfCourses()
    # A list of majors
    major_list = ListOfMajors()
    # A list of enrolled students in a given course
    enrolled_students = ListOfStudents()
    # A list of particular courses available to a student
    particular_courses = ListOfParticularCourses()
    # Generates a random key for integrity
    app.secret_key = os.urandom(12)
    app.run(debug=True)
