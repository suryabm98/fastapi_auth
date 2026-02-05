from fastapi import APIRouter,Depends,status,Response,HTTPException
from schemas import User
from typing import List
import database
import models
import schemas
from sqlalchemy.orm import Session


get_db=database.get_db
router=APIRouter(
    prefix="/Usertable",
    tags=["Usertable"]
)

@router.get('/',response_model=List[schemas.Show_Not_id])
def all_users(db:Session=Depends(get_db)):
    users=db.query(models.Usertable).all()
    return users

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.Show_Not_id)
def Create_Form(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.Usertable(username=request.username,mail=request.mail,user_id=6)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',status_code=200,response_model=schemas.Show_Not_id)
def show_userid(id:int,response:Response,db:Session=Depends(get_db)):
    user=db.query(models.Usertable).filter(models.Usertable.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f'User with the id of {id} is not available')
    return user


@router.delete('/{id}',status_code=status.HTTP_200_OK)
def remove_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.Usertable).filter(models.Usertable.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not found')
    user.delete()
    db.commit()
    
    return {f'User with the id of {id} is deleted successfully'}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: User, db: Session = Depends(get_db)):
    user = db.query(models.Usertable).filter(models.Usertable.id == id)
    if not user.first():
        raise HTTPException(status_code=404, detail="User not found")

    # user.update()
    user.update(
        {
        models.Usertable.username: request.username,
        models.Usertable.mail: request.mail
    })

    db.commit()
    return {"message": "Updated successfully"}


