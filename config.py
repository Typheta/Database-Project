# config.py

import mysql.connector
import sqlite3
import logging

logging.basicConfig(level=logging.ERROR)

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
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Course VALUES (%s, %s, %s, %s, %s, %s)",
                       (course_id, course_name, classroom_id, course_year, course_description, professor_id))
        mydb.commit()
        return "Course inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting course."
    finally:
        cursor.close()

def insert_grade(grade_id, student_id, course_id, semester, letter_grade, numeric_grade):
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Grades VALUES (%s, %s, %s, %s, %s, %s)",
                       (grade_id, student_id, course_id, semester, letter_grade, numeric_grade))
        mydb.commit()
        return "Grade inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting grade."
    finally:
        cursor.close()

def insert_enrollment(enrollment_id, student_id, course_id, enrollment_date):
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Enrollment VALUES (%s, %s, %s, %s)",
                       (enrollment_id, student_id, course_id, enrollment_date))
        mydb.commit()
        return "Enrollment inserted successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error inserting enrollment."
    finally:
        cursor.close()

def search_students(StudentID):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Student WHERE StudentID = %s;", (StudentID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def search_professors(ProfessorID):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Professor WHERE ProfessorID = %s;", (ProfessorID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def search_classrooms(ClassroomID):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Classroom WHERE ClassroomID = %s;", (ClassroomID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def search_courses(CourseID):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Course WHERE CourseID = %s;", (CourseID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def search_enrollments(EnrollmentID):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Enrollment WHERE EnrollmentID = %s;", (EnrollmentID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def search_grades(GradeID):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Grades WHERE GradeID = %s;", (GradeID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def update_student(student_id, new_first_name, new_last_name, new_dob, new_email, new_major):
    try:
        cursor = mydb.cursor()
        cursor.execute("""
            UPDATE Student
            SET StudentFirstName = %s, StudentLastName = %s, DateOfBirth = %s, Email = %s, Major = %s
            WHERE StudentID = %s
        """, (new_first_name, new_last_name, new_dob, new_email, new_major, student_id))
        mydb.commit()
        return "Student updated successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error updating student."
    finally:
        cursor.close()

def update_professor(professor_id, new_first_name, new_last_name, new_dob, new_department, new_email):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Professor SET ProfessorFirstName=%s, ProfessorLastName=%s, DateOfBirth=%s, "
                       "Department=%s, Email=%s WHERE ProfessorID=%s",
                       (new_first_name, new_last_name, new_dob, new_department, new_email, professor_id))
        mydb.commit()
        return "Professor updated successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error updating professor."
    finally:
        cursor.close()

def update_classroom(classroom_id, new_building, new_room_number, new_capacity):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Classroom SET Building=%s, RoomNumber=%s, Capacity=%s "
                       "WHERE ClassroomID=%s",
                       (new_building, new_room_number, new_capacity, classroom_id))
        mydb.commit()
        return "Classroom updated successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error updating classroom."
    finally:
        cursor.close()

def update_course(course_id, new_course_name, new_classroom_id, new_course_year, new_course_description, new_professor_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Course SET CourseName=%s, ClassroomID=%s, CourseYear=%s, "
                       "CourseDescription=%s, ProfessorID=%s WHERE CourseID=%s",
                       (new_course_name, new_classroom_id, new_course_year, new_course_description, new_professor_id, course_id))
        mydb.commit()
        return "Course updated successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error updating course."
    finally:
        cursor.close()

def update_course(course_id, new_course_name, new_classroom_id, new_course_year, new_course_description, new_professor_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Course SET CourseName=%s, ClassroomID=%s, CourseYear=%s, "
                       "CourseDescription=%s, ProfessorID=%s WHERE CourseID=%s",
                       (new_course_name, new_classroom_id, new_course_year, new_course_description, new_professor_id, course_id))
        mydb.commit()
        return "Course updated successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error updating course."
    finally:
        cursor.close()

def update_grade(grade_id, new_student_id, new_course_id, new_semester, new_letter_grade, new_numeric_grade):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Grades SET StudentID=%s, CourseID=%s, Semester=%s, "
                       "LetterGrade=%s, NumericGrade=%s WHERE GradeID=%s",
                       (new_student_id, new_course_id, new_semester, new_letter_grade, new_numeric_grade, grade_id))
        mydb.commit()
        return "Grade updated successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error updating grade."
    finally:
        cursor.close()


def update_enrollment(enrollment_id, new_student_id, new_course_id, new_enrollment_date):
    try:
        cursor = mydb.cursor()
        cursor.execute("UPDATE Enrollment SET StudentID=%s, CourseID=%s, EnrollmentDate=%s "
                       "WHERE EnrollmentID=%s",
                       (new_student_id, new_course_id, new_enrollment_date, enrollment_id))
        mydb.commit()
        return "Enrollment updated successfully!"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error updating enrollment."
    finally:
        cursor.close()

def delete_student(student_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Student WHERE StudentID = %s", (student_id,))
        mydb.commit()
        return f"Success: Student with ID {student_id} deleted."
    except mysql.connector.Error as err:
        logging.error(f"Error deleting student with ID {student_id}: {err}")
        mydb.rollback()
        return f"Error deleting student."

def delete_professor(professor_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Professor WHERE ProfessorID = %s", (professor_id,))
        mydb.commit()
        return f"Success: Professor with ID {professor_id} deleted."
    except mysql.connector.Error as err:
        logging.error(f"Error deleting professor with ID {professor_id}: {err}")
        mydb.rollback()
        return f"Error deleting professor."

def delete_classroom(classroom_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Classroom WHERE ClassroomID = %s", (classroom_id,))
        mydb.commit()
        return f"Success: Classroom with ID {classroom_id} deleted."
    except mysql.connector.Error as err:
        logging.error(f"Error deleting classroom with ID {classroom_id}: {err}")
        mydb.rollback()
        return f"Error deleting classroom."

def delete_course(course_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Course WHERE CourseID = %s", (course_id,))
        mydb.commit()
        return f"Success: Course with ID {course_id} deleted."
    except mysql.connector.Error as err:
        logging.error(f"Error deleting course with ID {course_id}: {err}")
        mydb.rollback()
        return f"Error deleting course."

def delete_grade(grade_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Grades WHERE GradeID = %s", (grade_id,))
        mydb.commit()
        return f"Success: Grade with ID {grade_id} deleted."
    except mysql.connector.Error as err:
        logging.error(f"Error deleting grade with ID {grade_id}: {err}")
        mydb.rollback()
        return f"Error deleting grade."

def delete_enrollment(enrollment_id):
    try:
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM Enrollment WHERE EnrollmentID = %s", (enrollment_id,))
        mydb.commit()
        return f"Success: Enrollment with ID {enrollment_id} deleted."
    except mysql.connector.Error as err:
        logging.error(f"Error deleting enrollment with ID {enrollment_id}: {err}")
        mydb.rollback()
        return f"Error deleting enrollment."

#interesting queries

def execute_join_query():
    try:
        cursor = mydb.cursor(dictionary=True)

        # Example join query: Fetch students, courses, and enrollment details
        query = """
            SELECT Student.StudentID, Student.StudentFirstName, Student.StudentLastName,
                   Course.CourseID, Course.CourseName, Enrollment.EnrollmentDate
            FROM Student
            JOIN Enrollment ON Student.StudentID = Enrollment.StudentID
            JOIN Course ON Enrollment.CourseID = Course.CourseID
        """
        cursor.execute(query)

        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()

def execute_aggregate_query(course_id):
    try:
        cursor = mydb.cursor()

        # Assuming you have a table named Grades with appropriate columns
        query = """
            SELECT AVG(NumericGrade) as AverageNumericGrade
            FROM Grades
            WHERE CourseID = %s
        """
        cursor.execute(query, (course_id,))

        result = cursor.fetchone()

        if result:
            average_numeric_grade = result[0]
            return f"Average Numeric Grade for Course {course_id}: {average_numeric_grade:.2f}"
        else:
            return f"No data found for Course {course_id}"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error executing aggregate query."
    finally:
        cursor.close()

def get_course_enrollments():
    try:
        cursor = mydb.cursor(dictionary=True)  # Use dictionary cursor for easier data manipulation
        # SQL query to join courses and enrollments tables
        query = """
            SELECT Course.CourseID, Course.CourseName, Student.StudentID, Student.StudentFirstName
            FROM Course
            LEFT JOIN Enrollment ON Course.CourseID = Enrollment.CourseID
            LEFT JOIN Student ON Enrollment.StudentID = Student.StudentID
            ORDER BY Course.CourseID, Student.StudentID;
        """

        # Execute the query and fetch results
        cursor.execute(query)
        results = cursor.fetchall()

        # Organize results into a dictionary where keys are courses and values are lists of students
        course_enrollments = {}
        for row in results:
            course_id, course_name, student_id, student_name = row['CourseID'], row['CourseName'], row['StudentID'], row['StudentFirstName']
            if course_id not in course_enrollments:
                course_enrollments[course_id] = {'course_name': course_name, 'students': []}
            if student_id is not None:
                course_enrollments[course_id]['students'].append({'student_id': student_id, 'student_name': student_name})

        return list(course_enrollments.values())

    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error: {e}")
        return None

    finally:
        cursor.close()

