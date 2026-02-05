from fastapi import APIRouter,Depends
from schemas import Accessname,Show_name
import database
import models
from sqlalchemy.orm import Session
# from passlib.context import CryptContext
from hashing import password_context


router=APIRouter(
    prefix="/Useraccessusers",
    tags=["Useraccessusers"]
)
get_db=database.get_db

# hased password within 72 bytes
# password_context=CryptContext(schemes=["bcrypt"],deprecated="auto") 

# hashed password with above 72 bytes
# password_context=CryptContext(schemes=["argon2"],deprecated="auto")
# username and password creation section

@router.post('/',response_model=Show_name)
def user_password(request:Accessname,db:Session=Depends(get_db)):
    hasedpassword=password_context.hash(request.password)
    new_user=models.Useraccessusers(name=request.name,
                                    password=hasedpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user