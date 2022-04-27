from fastapi import FastAPI

app = FastAPI()

students_list = {"Esra": 4.75 , "Sara":3.76 , "Hawra":4.58 , "Mohammed":3.60,"Ahmed":4.30}

@app.get("/students")
def get_students():

    #return list(students_list.keys())

    return [student for student in students_list.keys()]

@app.get("/student/{student_name}")
def get_gpa(student_name:str):
    
    student_gpa = {"Name": student_name , "Gpa": students_list[student_name]}
    return student_gpa
   

