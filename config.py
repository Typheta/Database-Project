# config.py

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="godawgs32",
    database="project"
)
print(mydb)

def insert_student(student_id, first_name, last_name, dob, email, major):
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s)",
                       (student_id, first_name, last_name, dob, email, major))
        mydb.commit()
        return "Student inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting student."

def insert_professor(professor_id, first_name, last_name, dob, department, email):
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Professor VALUES (%s, %s, %s, %s, %s, %s)",
                       (professor_id, first_name, last_name, dob, department, email))
        mydb.commit()
        return "Professor inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting professor."

def insert_classroom(classroom_id, building, room_number, capacity):
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Classroom VALUES (%s, %s, %s, %s)",
                       (classroom_id, building, room_number, capacity))
        mydb.commit()
        return "Classroom inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting classroom."
    finally:
        cursor.close()

def insert_course(course_id, course_name, classroom_id, course_year, course_description, professor_id):
    try:
        # Assuming you have a table named Course with appropriate columns
        mycursor.execute("INSERT INTO Course VALUES (%s, %s, %s, %s, %s, %s)",
                       (course_id, course_name, classroom_id, course_year, course_description, professor_id))
        mydb.commit()
        return "Course inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting course."
    finally:
        mycursor.close()

def insert_grade(grade_id, student_id, course_id, semester, letter_grade, numeric_grade):
    try:
        # Assuming you have a table named Grades with appropriate columns
        mycursor.execute("INSERT INTO Grades VALUES (%s, %s, %s, %s, %s, %s)",
                       (grade_id, student_id, course_id, semester, letter_grade, numeric_grade))
        mydb.commit()
        return "Grade inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting grade."
    finally:
        mycursor.close()

def insert_enrollment(enrollment_id, student_id, course_id, enrollment_date):
    try:
        # Assuming you have a table named Enrollment with appropriate columns
        mycursor.execute("INSERT INTO Enrollment VALUES (%s, %s, %s, %s)",
                       (enrollment_id, student_id, course_id, enrollment_date))
        mydb.commit()
        return "Enrollment inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting enrollment."
    finally:
        mycursor.close()

def returnByStudentID(student_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Student WHERE StudentID = %s;", (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def update_student(student_id, new_values):
   
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Student SET FirstName=%s, LastName=%s, DOB=%s, Email=%s, Major=%s WHERE StudentID=%s", (new_values['first_name'], new_values['last_name'], new_values['dob'], new_values['email'], new_values['major'], student_id))
        mydb.commit()
        return f"Success: Student with ID {student_id} updated."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error updating student."

def update_professor(professor_id, new_values):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Professor SET FirstName=%s, LastName=%s, DOB=%s, Department=%s, Email=%s WHERE ProfessorID=%s", (new_values['first_name'], new_values['last_name'], new_values['dob'], new_values['department'], new_values['email'], professor_id))
        mydb.commit()
        return f"Success: Professor with ID {professor_id} updated."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error updating professor."

def update_classroom(classroom_id, new_values):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Classroom SET Building=%s, RoomNumber=%s, Capacity=%s WHERE ClassroomID=%s", (new_values['building'], new_values['room_number'], new_values['capacity'], classroom_id))
        mydb.commit()
        return f"Success: Classroom with ID {classroom_id} updated."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error updating classroom."

def update_course(course_id, new_values):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Course SET CourseName=%s, ClassroomID=%s, CourseYear=%s, CourseDescription=%s, ProfessorID=%s WHERE CourseID=%s", (new_values['course_name'], new_values['classroom_id'], new_values['course_year'], new_values['course_description'], new_values['professor_id'], course_id))
        mydb.commit()
        return f"Success: Course with ID {course_id} updated."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error updating course."

def update_grade(grade_id, new_values):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Grades SET StudentID=%s, CourseID=%s, Semester=%s, LetterGrade=%s, NumericGrade=%s WHERE GradeID=%s", (new_values['student_id'], new_values['course_id'], new_values['semester'], new_values['letter_grade'], new_values['numeric_grade'], grade_id))
        mydb.commit()
        return f"Success: Grade with ID {grade_id} updated."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error updating grade."

def update_enrollment(enrollment_id, new_values):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Enrollment SET StudentID=%s, CourseID=%s, EnrollmentDate=%s WHERE EnrollmentID=%s", (new_values['student_id'], new_values['course_id'], new_values['enrollment_date'], enrollment_id))
        mydb.commit()
        return f"Success: Enrollment with ID {enrollment_id} updated."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error updating enrollment."


# Function to find students with the highest GPA
def returnGPAbyStudentID(student_id):
    try:
        try:
        # Assuming you have a table named Enrollment with appropriate columns
        mycursor.execute("SELECT * FROM Grades WHERE StudentID = %s;", (student_id))",
        mydb.commit()
        grades = cursor.fetchone()
        return 0
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error retrieving GPA."
    finally:
        mycursor.close()
        
# Function to find all courses taught by a particular professor
def courses_taught_by_professor(professor_id):
    try:
        mycursor.execute("SELECT * FROM Course JOIN Professor ON Course.Professor WHERE Professor.ProfessorID = %s;" , (professor_id,))

        mydb.commit()
        return "Courses found!"
    except  mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error finding courses."
    finally:
        mycursor.close()

def delete_student(student_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Student WHERE StudentID = %s", (student_id,))
        mydb.commit()
        return f"Success: Student with ID {student_id} deleted."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error deleting student."

def delete_professor(professor_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Professor WHERE ProfessorID = %s", (professor_id,))
        mydb.commit()
        return f"Success: Professor with ID {professor_id} deleted."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error deleting professor."

def delete_classroom(classroom_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Classroom WHERE ClassroomID = %s", (classroom_id,))
        mydb.commit()
        return f"Success: Classroom with ID {classroom_id} deleted."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error deleting classroom."

def delete_course(course_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Course WHERE CourseID = %s", (course_id,))
        mydb.commit()
        return f"Success: Course with ID {course_id} deleted."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error deleting course."

def delete_grade(grade_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Grades WHERE GradeID = %s", (grade_id,))
        mydb.commit()
        return f"Success: Grade with ID {grade_id} deleted."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error deleting grade."

def delete_enrollment(enrollment_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Enrollment WHERE EnrollmentID = %s", (enrollment_id,))
        mydb.commit()
        return f"Success: Enrollment with ID {enrollment_id} deleted."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error deleting enrollment."

        





