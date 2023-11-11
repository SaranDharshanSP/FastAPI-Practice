from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students ={
    1:{
       'name':'saran',
       'age': 19,
       'class': 'year 12'
    }
}
class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {'name' : 'lAST Data'}

@app.get('/get-student/{student_id}')
def get_student(student_id : int=Path(description='The ID pf the student that you wanna view',gt=0)):
    if student_id not in students:
        return {"Error": f"Student ID {student_id} doesn't exist."}
    return students[student_id]

@app.get('/get-by-name/{student_id}')
def get_student(*, student_id :int ,name: Optional[str]=None, test : int):
    for student_id in students:
        if students[student_id].name == name:
            return  students[student_id]
    return {'Data':'Noooo'}

@app.post("/students/post/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists."}
    students[student_id] = student
    return students[student_id]

@app.put("/students/put/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"Error": f"Student ID {student_id} does not exist."}

    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/students/delete/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": f"Student ID {student_id} does not exist."}
    del students[student_id]
    return {"Message": "Student deleted successfully."}