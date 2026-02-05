from fastapi import APIRouter,Depends,HTTPException,status
from schemas import Login
import database
from sqlalchemy.orm import Session
import models
from hashing import Hash

get_db=database.get_db

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post('/')
def login(request:Login,db:Session=Depends(get_db)):
    user=db.query(models.Useraccessusers).filter(models.Useraccessusers.name == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f'User with the id of {id} is not available')
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect password")

    # JWT Token generation can be done here

    return user