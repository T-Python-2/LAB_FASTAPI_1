from fastapi import FastAPI


app = FastAPI()

students = {"eman":4.0, "sara":3.4, "med":2.0, "yer":5.0, "ewr":3.3}

@app.get("/")
def home():
    return "hellow this is the home page"

@app.get("/students")
def get_students_name():
    return list(students.keys())


@app.get("/student/gpa/{student_name}")
def get_students_gpa(student_name:str):
    output = {student_name:students[student_name]}
    return output
    