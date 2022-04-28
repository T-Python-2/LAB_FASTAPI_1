from fastapi import FastAPI

app = FastAPI()


students = {"Lama" : 3.99 , "Mohammed" :4.5, "Aqeel" : 4.2 , "Eman" : 3.5 , "Areej" : 3.78}


#1 First get path  “/students”
@app.get("/students")
def students_names():
    studentsList = list(students.keys())
    return studentsList
     



#2 get path "/student/gpa/student_name" to get the student GPA
@app.get("/student/gpa/{student_name}")
def students_GPA(student_name:str):
    return {f"{student_name}'s GPA : ": students[student_name]}


     