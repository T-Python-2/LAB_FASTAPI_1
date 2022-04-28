from fastapi import FastAPI

app = FastAPI()

students = {"Mohammed":3.8,"Fares":3.5,"Lama":4.3,"Faisal":2.5,"Maha":4.6}


app.get("/students")

def students_list(limit:int = None):
    list_students = [student for student in students.keys()]

    if limit:
        return list_students[:limit]

    return list_students

@app.get ("/student_name{student_name}")

def get_student_gpa(student_name:str):

    output = {"student_name":student_name, "student_GPA": students[student_name]}
