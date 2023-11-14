# routes.py

from flask import render_template, request
from app import app
from config import insert_student, insert_professor, insert_classroom, insert_course, insert_grade, insert_enrollment
from config import returnByStudentID
@app.route('/')
def index():
    return render_template('index.html', title='Home')

# Route to handle the form submission for inserting a student
@app.route('/insert_student', methods=['POST'])
def insert_student_route():
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        email = request.form['email']
        major = request.form['major']

        result = insert_student(student_id, first_name, last_name, dob, email, major)
        
        # Check if the insertion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"


# Route to handle the form submission for inserting a professor
@app.route('/insert_professor', methods=['POST'])
def insert_professor_route():
    if request.method == 'POST':
        professor_id = request.form['professor_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        department = request.form['department']
        email = request.form['email']

        result = insert_professor(professor_id, first_name, last_name, dob, department, email)
        
        # Check if the insertion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

# Route to handle the form submission for inserting a classroom
@app.route('/insert_classroom', methods=['POST'])
def insert_classroom_route():
    if request.method == 'POST':
        classroom_id = request.form['classroom_id']
        building = request.form['building']
        room_number = request.form['room_number']
        capacity = request.form['capacity']

        result = insert_classroom(classroom_id, building, room_number, capacity)
       
       # Check if the insertion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/insert_course', methods=['POST'])
def insert_course_route():
    if request.method == 'POST':
        course_id = request.form['course_id']
        course_name = request.form['course_name']
        classroom_id = request.form['classroom_id']
        course_year = request.form['course_year']
        course_description = request.form['course_description']
        professor_id = request.form['professor_id']

        result = insert_course(course_id, course_name, classroom_id, course_year, course_description, professor_id)
        
        # Check if the insertion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/insert_grade', methods=['POST'])
def insert_grade_route():
    if request.method == 'POST':
        grade_id = request.form['grade_id']
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        semester = request.form['semester']
        letter_grade = request.form['letter_grade']
        numeric_grade = request.form['numeric_grade']

        result = insert_grade(grade_id, student_id, course_id, semester, letter_grade, numeric_grade)
        
        # Check if the insertion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/insert_enrollment', methods=['POST'])
def insert_enrollment_route():
    if request.method == 'POST':
        enrollment_id = request.form['enrollment_id']
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        enrollment_date = request.form['enrollment_date']

        result = insert_enrollment(enrollment_id, student_id, course_id, enrollment_date)
        # Check if the insertion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"
        
@app.route('/update_student_route', methods=['POST'])
def update_student_route():
    if request.method == 'POST':
    student_id = request.form['student_id']
    first_name = request.form['first_name']
    last_name = request.form['last.name']
    dob = request.form['dob']
    email = request.form['email']
    major = request.form['major']

result = update_student(student_id, first_name, last_name, dob, email, major)

if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"


@app.route('/update_professor_route', methods=['POST'])
def update_professor_route():
    if request.method == 'POST':
        professor_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        email = request.form['email']
        department = request.form['department']

result = update_professor(professor_id, first_name, last_name, dob, email, department)

if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"
@app.route('/update_classroom_route', methods=['POST'])
def update_classroom_route():
    if request.method == 'POST':
        classroom_id = request.form['classroom_id']
        building = request.form['building']
        room_number = request.form['room_number']
        capacity = request.form['capacity']

result = update_classroom(classroom_id, building, room_number, capacity)

if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"
@app.route('/update_course_route', methods=['POST'])
def update_course_route():
    if request.method == 'POST'
        course_id = request.form['course_id']
        course_name = request.form['course_name']
        classroom_id = request.form['classroom_id']
        course_year = request.form['course_year']
        course_description = request.form['course_description']
        professor_id = request.form['professor_id']

result = update_course(course_id, course_name, classroom_id, course_year, course_description, professor_id)
        
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"
        
@app.route('/update_grade_route', methods=['POST'])
def update_grade_route():
    if request.method == 'POST'
        grade_id = request.form['grade_id']
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        semester = request.form['semester']
        letter_grade = request.form['letter_grade']
        numeric_grade = request.form['numeric_grade']

        result = update_grade(grade_id, student_id, course_id, semester, letter_grade, numeric_grade)
        
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"
        
@app.route('/update_enrollment_route', methods=['POST'])
def update_enrollment_route():
    if request.method == 'POST':
        enrollment_id = request.form['enrollment_id']
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        enrollment_date = request.form['enrollment_date']

        result = update_enrollment(enrollment_id, student_id, course_id, enrollment_date)
       
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/delete_student', methods=['POST'])
def delete_student_route():
    if request.method == 'POST':
        student_id = request.form['student_id']
        
        result = delete_student(student_id)
        
        # Check if the deletion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/delete_professor', methods=['POST'])
def delete_professor_route():
    if request.method == 'POST':
        professor_id = request.form['professor_id']
        
        result = delete_professor(professor_id)
        
        # Check if the deletion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/delete_classroom', methods=['POST'])
def delete_classroom_route():
    if request.method == 'POST':
        classroom_id = request.form['classroom_id']
        
        result = delete_classroom(classroom_id)
        
        # Check if the deletion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/delete_course', methods=['POST'])
def delete_course_route():
    if request.method == 'POST':
        course_id = request.form['course_id']
        
        result = delete_course(course_id)
        
        # Check if the deletion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/delete_grade', methods=['POST'])
def delete_grade_route():
    if request.method == 'POST':
        grade_id = request.form['grade_id']
        
        result = delete_grade(grade_id)
        
        # Check if the deletion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/delete_enrollment', methods=['POST'])
def delete_enrollment_route():
    if request.method == 'POST':
        enrollment_id = request.form['enrollment_id']
        
        result = delete_enrollment(enrollment_id)
        
        # Check if the deletion was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"
    

@app.route('/search', methods=['POST'])
def search():
    # Retrieve the student_id from the form
    student_id = request.form['student_id']

    # Call the function to get student details
    student_details = returnByStudentID(int(student_id))  # Convert to int

    return render_template('search_result.html', title='Search Result', student_details=student_details)
