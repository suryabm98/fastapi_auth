# models.py
from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class Usertable(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(100))
    mail=Column(String(100))
    user_id=Column(Integer,ForeignKey("storageaccess.id"))

    creator=relationship("Useraccessusers",back_populates="owner")
# syntax of creator
'''
variable1=relationship("classname of which should be used", back_populates="variable2 from other class")
'''
   

class Useraccessusers(Base):
    __tablename__='storageaccess'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    password=Column(String(100))

    owner=relationship("Usertable",back_populates="creator")

# syntax of owner
'''
variable2=relationship("classname of which should be used", back_populates="variable1 from other class")
'''