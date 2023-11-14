# routes.py

from flask import render_template, request
from app import app
from config import insert_student, insert_professor, insert_classroom, insert_course, insert_grade, insert_enrollment
from config import search_students, search_professors, search_classrooms, search_courses, search_enrollments, search_grades
from config import update_student, update_professor, update_classroom, update_course, update_enrollment, update_grade
from config import delete_student, delete_professor, delete_classroom, delete_course, delete_grade, delete_enrollment
from config import execute_join_query, execute_aggregate_query, get_course_enrollments

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/insert_records')
def insert_records():
    return render_template('insert_records.html', title='Insert Records')

@app.route('/select_records')
def select_records():
    return render_template('select_records.html', title='Select Records')

@app.route('/update_records')
def update_records():
    return render_template('updating_records.html', title='Update Records')

@app.route('/delete_records')
def delete_records():
    return render_template('delete_records.html', title='Delete Records')

@app.route('/interesting_queries', methods=['GET'])
def interesting_queries_route():
    return render_template('interesting_queries.html', title='Interesting Queries')


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

# Route to handle the form submission for searching students
@app.route('/search_students', methods=['POST'])
def search_students_route():
    if request.method == 'POST':
        student_id = request.form['student_id']

        # Call the search_students function with the provided student_id
        result = search_students(student_id)

        if result:
            # If a student is found, display the result
            return render_template('search_results.html', title='Search Results', result=result, table='students')
        else:
            # If no student is found, display a message
            return render_template('search_results.html', title='Search Results', result=None, table='students')
    else:
        return "Invalid request method"

# Route to handle the form submission for searching professors
@app.route('/search_professors', methods=['POST'])
def search_professors_route():
    if request.method == 'POST':
        professor_id = request.form['professor_id']
        result = search_professors(professor_id)
        if result:
            return render_template('search_results.html', title='Search Results', result=result, table='professors')
        else:
            return render_template('search_results.html', title='Search Results', result=None, table='professors')
    else:
        return "Invalid request method"

# Route to handle the form submission for searching classrooms
@app.route('/search_classrooms', methods=['POST'])
def search_classrooms_route():
    if request.method == 'POST':
        classroom_id = request.form['classroom_id']
        result = search_classrooms(classroom_id)
        if result:
            return render_template('search_results.html', title='Search Results', result=result, table='classrooms')
        else:
            return render_template('search_results.html', title='Search Results', result=None, table='classrooms')
    else:
        return "Invalid request method"

# Route to handle the form submission for searching courses
@app.route('/search_courses', methods=['POST'])
def search_courses_route():
    if request.method == 'POST':
        course_id = request.form['course_id']
        result = search_courses(course_id)
        if result:
            return render_template('search_results.html', title='Search Results', result=result, table='courses')
        else:
            return render_template('search_results.html', title='Search Results', result=None, table='courses')
    else:
        return "Invalid request method"

# Route to handle the form submission for searching grades
@app.route('/search_grades', methods=['POST'])
def search_grades_route():
    if request.method == 'POST':
        grade_id = request.form['grade_id']
        result = search_grades(grade_id)
        if result:
            return render_template('search_results.html', title='Search Results', result=result, table='grades')
        else:
            return render_template('search_results.html', title='Search Results', result=None, table='grades')
    else:
        return "Invalid request method"

# Route to handle the form submission for searching enrollments
@app.route('/search_enrollments', methods=['POST'])
def search_enrollments_route():
    if request.method == 'POST':
        enrollment_id = request.form['enrollment_id']
        result = search_enrollments(enrollment_id)
        if result:
            return render_template('search_results.html', title='Search Results', result=result, table='enrollments')
        else:
            return render_template('search_results.html', title='Search Results', result=None, table='enrollments')
    else:
        return "Invalid request method"

@app.route('/update_student', methods=['GET', 'POST'])
def update_student_route():
    if request.method == 'POST':
        student_id = request.form['student_id']
        new_first_name = request.form['new_first_name']
        new_last_name = request.form['new_last_name']
        new_dob = request.form['new_dob']
        new_email = request.form['new_email']
        new_major = request.form['new_major']

        # Call the update_student function with the provided information
        result = update_student(student_id, new_first_name, new_last_name, new_dob, new_email, new_major)

        # Check if the update was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"

    else:
        # Render the form for updating a student record
        return render_template('update_records.html', title='Update Records', table='students')

# Route to handle the form submission for updating a professor
@app.route('/update_professor', methods=['POST'])
def update_professor_route():
    if request.method == 'POST':
        professor_id = request.form['professor_id']
        new_first_name = request.form['new_first_name']
        new_last_name = request.form['new_last_name']
        new_dob = request.form['new_dob']
        new_department = request.form['new_department']
        new_email = request.form['new_email']

        result = update_professor(professor_id, new_first_name, new_last_name, new_dob, new_department, new_email)

        # Check if the update was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

# Route to handle the form submission for updating a classroom
@app.route('/update_classroom', methods=['POST'])
def update_classroom_route():
    if request.method == 'POST':
        classroom_id = request.form['classroom_id']
        new_building = request.form['new_building']
        new_room_number = request.form['new_room_number']
        new_capacity = request.form['new_capacity']

        result = update_classroom(classroom_id, new_building, new_room_number, new_capacity)

        # Check if the update was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

# Route to handle the form submission for updating a course
@app.route('/update_course', methods=['POST'])
def update_course_route():
    if request.method == 'POST':
        course_id = request.form['course_id']
        new_course_name = request.form['new_course_name']
        new_classroom_id = request.form['new_classroom_id']
        new_course_year = request.form['new_course_year']
        new_course_description = request.form['new_course_description']
        new_professor_id = request.form['new_professor_id']

        result = update_course(course_id, new_course_name, new_classroom_id, new_course_year, new_course_description, new_professor_id)

        # Check if the update was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

# Route to handle the form submission for updating a grade
@app.route('/update_grade', methods=['POST'])
def update_grade_route():
    if request.method == 'POST':
        grade_id = request.form['grade_id']
        new_student_id = request.form['new_student_id']
        new_course_id = request.form['new_course_id']
        new_semester = request.form['new_semester']
        new_letter_grade = request.form['new_letter_grade']
        new_numeric_grade = request.form['new_numeric_grade']

        result = update_grade(grade_id, new_student_id, new_course_id, new_semester, new_letter_grade, new_numeric_grade)

        # Check if the update was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

# Route to handle the form submission for updating an enrollment
@app.route('/update_enrollment', methods=['POST'])
def update_enrollment_route():
    if request.method == 'POST':
        enrollment_id = request.form['enrollment_id']
        new_student_id = request.form['new_student_id']
        new_course_id = request.form['new_course_id']
        new_enrollment_date = request.form['new_enrollment_date']

        result = update_enrollment(enrollment_id, new_student_id, new_course_id, new_enrollment_date)

        # Check if the update was successful
        if "successfully" in result.lower():
            return f"{result}<br><a href='/'>Return to Home</a>"
        else:
            return f"{result}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"
   
# Route to handle the form submission for deleting a professor
@app.route('/delete_student', methods=['POST'])
def delete_student_route():
    if request.method == 'POST':
        student_id = request.form['student_id']
        result_message = delete_student(student_id)

        # Check if the deletion was successful
        if "success" in result_message.lower():
            return f"Deletion successful: {result_message}<br><a href='/'>Back to Home</a>"
        else:
            return f"Deletion failed: {result_message}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

# Route to handle the form submission for deleting a professor
@app.route('/delete_professor', methods=['POST'])
def delete_professor_route():
    if request.method == 'POST':
        professor_id = request.form['professor_id']
        result_message = delete_professor(professor_id)

         # Check if the deletion was successful
        if "success" in result_message.lower():
            return f"Deletion successful: {result_message}<br><a href='/'>Back to Home</a>"
        else:
            return f"Deletion failed: {result_message}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"


# Route to handle the form submission for deleting a classroom
@app.route('/delete_classroom', methods=['POST'])
def delete_classroom_route():
    if request.method == 'POST':
        classroom_id = request.form['classroom_id']
        result_message = delete_classroom(classroom_id)

         # Check if the deletion was successful
        if "success" in result_message.lower():
            return f"Deletion successful: {result_message}<br><a href='/'>Back to Home</a>"
        else:
            return f"Deletion failed: {result_message}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"


# Route to handle the form submission for deleting a course
@app.route('/delete_course', methods=['POST'])
def delete_course_route():
    if request.method == 'POST':
        course_id = request.form['course_id']
        result_message = delete_course(course_id)

         # Check if the deletion was successful
        if "success" in result_message.lower():
            return f"Deletion successful: {result_message}<br><a href='/'>Back to Home</a>"
        else:
            return f"Deletion failed: {result_message}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

# Route to handle the form submission for deleting a grade
@app.route('/delete_grade', methods=['POST'])
def delete_grade_route():
    if request.method == 'POST':
        grade_id = request.form['grade_id']
        result_message = delete_grade(grade_id)

         # Check if the deletion was successful
        if "success" in result_message.lower():
            return f"Deletion successful: {result_message}<br><a href='/'>Back to Home</a>"
        else:
            return f"Deletion failed: {result_message}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"


# Route to handle the form submission for deleting an enrollment
@app.route('/delete_enrollment', methods=['POST'])
def delete_enrollment_route():
    if request.method == 'POST':
        enrollment_id = request.form['enrollment_id']
        result_message = delete_enrollment(enrollment_id)

         # Check if the deletion was successful
        if "success" in result_message.lower():
            return f"Deletion successful: {result_message}<br><a href='/'>Back to Home</a>"
        else:
            return f"Deletion failed: {result_message}<br><a href='/'>Back to Home</a>"
    else:
        return "Invalid request method"

@app.route('/execute_join_query', methods=['GET'])
def execute_join_query_route():
    result = execute_join_query()
    return render_template('enrollment_result.html', title='Student Enrollments', result=result)

@app.route('/execute_aggregate_query', methods=['GET'])
def execute_aggregate_query_route():
    course_id = request.args.get('course_id')

    # Assuming you have the execute_aggregate_query function
    result = execute_aggregate_query(course_id)

    return render_template('aggregate_query_result.html', result=result)

@app.route('/get_course_enrollments', methods=['POST'])
def get_course_enrollments_route():
    results = get_course_enrollments()

    if results is not None:
        return render_template('student_count.html', results=results)
    else:
        return "Error fetching course enrollments. Please try again."
