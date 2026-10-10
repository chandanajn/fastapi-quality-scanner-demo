from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import UserCreate
from .crud import create_user,get_user


app = FastAPI()



PASSWORD = "admin123"





@app.get("/")

def home():

    return {
        "message":
        "FastAPI Quality Demo"
    }





@app.post("/users")

def add_user(
    user:UserCreate,
    db:Session=Depends(get_db)

):

    return create_user(
        db,
        user
    )





@app.get("/users/{id}")

def read_user(
        id,
        db:Session=Depends(get_db)
):

    return get_user(
        db,
        id
    )
