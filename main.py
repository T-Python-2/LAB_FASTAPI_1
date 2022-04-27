from fastapi import FastAPI

app = FastAPI()

students = {
    "Abdulghani":3.45,
    "Faisal" : 2.33,
    "Azzam": 3.01,
    "Naif": 3.63,
    "Mohammed" : 3.94 }


@app.get("/students")
def get_students():
    students_list = list(students.keys())
    output = {"Student Name" : students_list}
    return output


@app.get("/student/gpa/{student_name}")
def get_gpa(student_name:str):
    output = {student_name:students[student_name]}
    return output

    
