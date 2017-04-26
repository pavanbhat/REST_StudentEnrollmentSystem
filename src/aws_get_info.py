# Importing support libraries
import os
from flask import Flask, jsonify, render_template, json, flash
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap

# Importing support classes
from src.Student import *
from src.Course import *
from src.Major import *
from src.ListOfStudents import *
from src.ListOfCourses import *
from src.ListOfMajors import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'dev-test.crmgtfyiv0nq.us-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'mariadbadmin'
app.config['MYSQL_PASSWORD'] = '28379b156156cbabda4dfe7f5d89c0a1'
app.config['MYSQL_DB'] = 'testdb'
db = MySQL(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    cursor = connect_db()
    cursor.execute('''select * from Student''')
    table = cursor.fetchall()
    print(table)
    return students()

def connect_db():
    cursor = db.connection.cursor()
    return cursor


@app.route('/students', methods=['GET', 'POST'])
def students():
    try:
        global student_list
        cursor = connect_db()
        cursor.execute('''select * from Student''')
        table = cursor.fetchall()
        for row in table:
            student_list.set_student_data(Student(row[0], row[1], row[2], row[3]))
        return json.dumps([stud.dump_student() for stud in student_list.get_student_data()])
        # return json.dumps([stud.dump_student() for stud in student_list.get_student_data()])
        # return render_template("student_enrollment.html", id_list=id, fname_list=fname)
    except Exception as e:
        flash(e)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    try:
        global course_list
        cursor = connect_db()
        cursor.execute('''select * from Courses''')
        table = cursor.fetchall()
        for row in table:
            course_list.set_course_data(Course(row[0], row[1], row[2]))
        return json.dumps([course.dump_course() for course in course_list.get_course_data()])
    except Exception as e:
        flash(e)

@app.route('/majors', methods=['GET', 'POST'])
def majors():
    try:
        global major_list
        cursor = connect_db()
        cursor.execute('''select * from Major''')
        table = cursor.fetchall()
        for row in table:
            major_list.set_major_data(Major(row[0], row[1]))
        return json.dumps([major.dump_major() for major in major_list.get_major_data()])
    except Exception as e:
        flash(e)

if __name__ == '__main__':
    global student_list, course_list, major_list
    student_list = ListOfStudents()
    course_list = ListOfCourses()
    major_list = ListOfMajors()
    app.secret_key = os.urandom(12)
    app.run(debug=True)

