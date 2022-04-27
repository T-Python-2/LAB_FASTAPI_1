#FAST API LAB

from fastapi import FastAPI
from Student import Student
app = FastAPI()

students_list = [Student("Ali", 2.4),Student("Hassan", 3.7),Student("Abdullah", 3.2),Student("Mustafa", 4.0),Student("Fatimah", 2.0),Student("Sarah", 2.7),Student("Ahmed", 1.9)]

@app.get("/students")
def getStudents():
    return [student.get_student_name() for student in students_list ]

@app.get("/student/gpa/{student_name}")
def get_student_gpa(student_name):
    gpa = next((student.get_gpa() for student in students_list if student.get_student_name() == student_name),f"Error: There is no student named {student_name}")
    return f"{student_name}'s GPA is {gpa}"
    # found = False
    # for student in students_list:
    #     if student.get_student_name() == student_name:
    #         found = True
    #         return student.get_gpa()
    
    # if not found:
    #     return f"Error: There is no student named {student_name}"