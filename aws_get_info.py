# Importing support libraries
import os

from flask import Flask, render_template, json, flash
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

from Course import *
# Importing support classes
from CustomError import *
from ListOfCourses import *
from ListOfMajors import *
from ListOfParticularCourses import *
from ListOfStudents import *
from Major import *
from ParticularCourses import *
from Student import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'dev-test.crmgtfyiv0nq.us-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'mariadbadmin'
app.config['MYSQL_PASSWORD'] = '28379b156156cbabda4dfe7f5d89c0a1'
app.config['MYSQL_DB'] = 'testdb'
db = MySQL(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("student_enrollment.html")


def connect_db():
    cursor = db.connection.cursor()
    return cursor


def fetchall_student_data():
    try:
        global student_list
        cursor = connect_db()
        cursor.execute('''select * from Student''')
        table = cursor.fetchall()
        if len(student_list.get_student_data()) > 0:
            print("inside")
            student_list.remove_all_student_data()
        for row in table:
            student_list.set_student_data(Student(row[0], row[1], row[2], row[3]))
    except Exception as e:
        print(e)


@app.route('/students', methods=['GET'])
def students():
    try:
        global student_list
        fetchall_student_data()
        return json.dumps([stud.dump_student() for stud in student_list.get_student_data()])
    except Exception as e:
        flash(e)


def fetchall_course_data():
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
    try:
        global course_list
        fetchall_course_data()
        return json.dumps([course.dump_course() for course in course_list.get_course_data()])
    except Exception as e:
        flash(e)


def fetchall_major_data():
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
    try:
        global major_list
        fetchall_major_data()
        return json.dumps([major.dump_major() for major in major_list.get_major_data()])
    except Exception as e:
        flash(e)


def fetch_particular_courses(major_id):
    try:
        global particular_courses
        cursor = connect_db()
        cursor.execute("select * from Courses where Major_id = " + str(major_id))
        table = cursor.fetchall()
        if len(particular_courses.get_particular_course_data()) > 0:
            particular_courses.remove_all_particular_course_data()
        for row in table:
            particular_courses.set_particular_course_data(ParticularCourses(row[0], row[1], row[2]))
    except Exception as e:
        print(e)


def fetch_corresponding_major(student_id):
    try:
        cursor = connect_db()
        cursor.execute("select * from Student where id = " + str(student_id))
        table = cursor.fetchall()
        if len(table) > 1:
            raise CustomError("Integrity Error! More than one entry for a student_id.")
        return table[0][3]
    except CustomError as e:
        print("Exception: ", e.value)


@app.route('/courses/students/<student_id>')
def courses_for_student(student_id):
    try:
        global particular_courses
        major_id = fetch_corresponding_major(student_id)
        fetch_particular_courses(major_id)
        return json.dumps([course.dump_course() for course in particular_courses.get_particular_course_data()])
    except Exception as e:
        flash(e)


@app.route('/students/enrolled/<course_id>', methods=['GET'])
def get_enrolled_students(course_id):
    try:
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
    except Exception as e:
        print(e)


if __name__ == '__main__':
    global student_list, course_list, major_list, particular_courses, enrolled_students
    student_list = ListOfStudents()
    course_list = ListOfCourses()
    major_list = ListOfMajors()
    enrolled_students = ListOfStudents()
    particular_courses = ListOfParticularCourses()
    app.secret_key = os.urandom(12)
    app.run(debug=True)
