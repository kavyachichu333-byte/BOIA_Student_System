from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from database import Base
class Student(Base):
    __tablename__='students'
    student_id=Column(Integer,primary_key=True,index=True)
    full_name=Column(String(100))
    email=Column(String(100),unique=True)
    phone=Column(String(20))
    course=Column(String(100))
    gender=Column(String(20))
    created_at=Column(DateTime,default=datetime.utcnow)
