/**
 * Created by pavan on 4/27/2017.
 */

/**
 * Gets the student information through an AJAX call using jQuery
 * to perform a GET operation
 */
var get_students = function () {
    $.get("/students", function (data) {
        document.getElementById("summary").innerHTML = "<tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Major ID</th></tr>";
        var obj = $.parseJSON(data);
        var val = "";
        for (var i = 0; i < obj.length; i++) {
            val += "<tr class='stud_rows' id='s" + obj[i].student.id + "'><td>" + obj[i].student.id + " </td><td>" + obj[i].student.fname + " </td><td>" + obj[i].student.lname + "</td><td>" + obj[i].student.major_id + "</td></tr>";
        }
        $('#summary').append(val);
    });
};

/**
 * Gets the course information through an AJAX call using jQuery
 * to perform a GET operation
 */
var get_courses = function () {
    $.get("/courses", function (data) {
        document.getElementById("summary").innerHTML = "<tr><th>ID</th><th>Course Name</th><th>Major ID</th></tr>";
        var obj = $.parseJSON(data);
        var val = "";
        for (var i = 0; i < obj.length; i++) {
            val += "<tr class='course_rows' id='c" + obj[i].course.id + "'><td>" + obj[i].course.id + " </td><td>" + obj[i].course.cname + " </td><td>" + obj[i].course.major_id + "</td></tr>";
        }
        $('#summary').append(val);
    });
};

/**
 * Gets the major information through an AJAX call using jQuery
 * to perform a GET operation
 */
var get_majors = function () {
    $.get("/majors", function (data) {
        document.getElementById("summary").innerHTML = "<tr><th>ID</th><th>Major Name</th></tr>";
        var obj = $.parseJSON(data);
        var val = "";
        for (var i = 0; i < obj.length; i++) {
            val += "<tr class='major_rows' id='m" + obj[i].major.id + "'><td>" + obj[i].major.id + " </td><td>" + obj[i].major.mname + " </td></tr>";
        }
        $('#summary').append(val);
    });
};

/**
 * Gets the course information for a given student through an AJAX call using jQuery
 * to perform a GET operation
 */
var get_courses_for_student = function () {
    // Student ID for a given student to find course available
    var stud_id = document.getElementById("cs_id").value;
    $.get("/courses/students/" + stud_id, function (data) {
        document.getElementById("summary").innerHTML = "<tr><th>ID</th><th>Course Name</th><th>Major ID</th></tr>";
        var obj = $.parseJSON(data);
        var val = "";
        for (var i = 0; i < obj.length; i++) {
            val += "<tr class='course_rows' id='c" + obj[i].course.id + "'><td>" + obj[i].course.id + " </td><td>" + obj[i].course.cname + " </td><td>" + obj[i].course.major_id + "</td></tr>";
        }
        $('#summary').append(val);
    });
};

/**
 * Gets the students enrolled in a given course through an AJAX call using jQuery
 * to perform a GET operation
 */
var get_enrolled_students = function () {
    // Course ID to get the students enrolled in the course
    var course_id = document.getElementById("sc_id").value;
    $.get("/students/courses/" + course_id, function (data) {
        document.getElementById("summary").innerHTML = "<tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Major ID</th></tr>";
        var obj = $.parseJSON(data);
        var val = "";
        for (var i = 0; i < obj.length; i++) {
            val += "<tr class='stud_rows' id='s" + obj[i].student.id + "'><td>" + obj[i].student.id + " </td><td>" + obj[i].student.fname + " </td><td>" + obj[i].student.lname + "</td><td>" + obj[i].student.major_id + "</td></tr>";
        }
        $('#summary').append(val);
    });
};

/**
 * Posts the student information for enrolling a student in a given course
 * through an AJAX call using jQuery
 * to perform a POST operation
 */
var enroll_student = function () {
    // Course ID to enroll into a given course
    var course_id = document.getElementById("course_id").value;
    // Student ID to enroll a particular student
    var stud_id = document.getElementById("stud_id").value;
    json_data = {"Student_id": stud_id, "Course_id": course_id};
    console.log(json_data.Course_id);
    $.ajax({
        // headers for the POST operation
        url: '/students/enroll',
        data: JSON.stringify(json_data),
        contentType: "application/json; charset=utf-8",
        type: 'POST',
        //Success Function - Acknowledgment of the POST operation
        success: function (data) {
            if (data === "Student Enrolled!") {
                document.getElementById("summary").innerHTML = "<div class='alert alert-success'><strong>Success! Student with Student_id " + stud_id + " enrolled in to course with Course ID " + course_id + "</strong>.</div>";
            } else if (data === "Student Not Enrolled!") {
                document.getElementById("summary").innerHTML = "<div class='alert alert-danger'><strong>Failure! Student with Student_id " + stud_id + " could not enroll in to course with Course ID " + course_id + "</strong>.</div>";
            }
            if (data === "Student already enrolled in the same course!") {
                document.getElementById("summary").innerHTML = "<div class='alert alert-info'><strong>Failure! Student with Student_id " + stud_id + " is already enrolled in the same course</strong>.</div>";
            }
            else if (data === "Student already enrolled in one course!") {
                document.getElementById("summary").innerHTML = "<div class='alert alert-info'><strong>Failure! Student with Student_id " + stud_id + " is already enrolled into a course</strong>.</div>";
            }
        }
    });
};