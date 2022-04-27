from fastapi import FastAPI
app=FastAPI()

students={
    "ali":3.3,
    "mohammed":3.0,
    "nabil":2.9,
    "hassan":3.1,
    "ahmed":3.1}
@app.get("/students")
def list_students():
    return list(students.keys())
    #return [students for students.keys()]
@app.get("/students/{students_name}")
def get_students_gpa(student_name:str):
    output={"students_GPA":students(student_name)}
    return output
