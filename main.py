from fastapi import FastAPI
import models
from database import engine
from routers import Usertable,Useraccessusers,authentication



app=FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(Usertable.router)
app.include_router(Useraccessusers.router)
app.include_router(authentication.router)