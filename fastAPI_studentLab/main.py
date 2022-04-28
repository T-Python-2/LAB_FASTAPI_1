from fastapi import FastAPI


app = FastAPI()
students = {"Ahmed" : 5.0, "Sara" : 2.5, "Nora" : 4.5, "Ruba" : 3.0, "Faris" : 1.50}


@app.get("/students")
def listStudents():
    return students

@app.get("/student/{studentName}")
def getStudentGPA(studentName: str):
    output = {"student_GPA" : students[studentName]}
    return output