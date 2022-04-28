class Student():
    def __init__(self,student_name:str,gpa:float):
        self.__student_name = student_name
        self.__gpa = gpa

    def get_student_name(self):
        return self.__student_name
    
    def set_student_name(self,name:str):
        self.__student_name = name
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self,gpa:float):
        self.__gpa = gpa

    