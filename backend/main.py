from fastapi import FastAPI,HTTPException
from database import Base,engine,SessionLocal
from models import Student
from pydantic import BaseModel
Base.metadata.create_all(bind=engine)
app=FastAPI(title='BOIA Student API')
class StudentCreate(BaseModel):
    full_name:str
    email:str
    phone:str
    course:str
    gender:str
@app.post('/students')
def create_student(student:StudentCreate):
    db=SessionLocal()
    obj=Student(**student.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj
@app.get('/students')
def get_students():
    db=SessionLocal(); return db.query(Student).all()
@app.delete('/students/{sid}')
def delete_student(sid:int):
    db=SessionLocal(); s=db.query(Student).filter(Student.student_id==sid).first()
    if not s: raise HTTPException(404,'Not found')
    db.delete(s); db.commit(); return {'message':'Deleted'}
