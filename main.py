from fastapi import FastAPI

app = FastAPI()


stuName = {
  "ahmed": 4.67,
  "khled": 3.87,
  "mohammed": 4.02,
  "yousef": 5.00,
  "amr": 4.90,
}

@app.get("/students")
def get_students():
    #return print(list(stuName.keys))
    return [i for i in stuName.keys()]


@app.get("/student/gpa/{student_name}")
def get_gpa(student_name:str):
    output = {"student_name" : student_name, "studend_GPA" : stuName[student_name]}
    return output  