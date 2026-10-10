"""Main FastAPI application module."""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import UserCreate, UserResponse
from .crud import create_user, get_user


app = FastAPI()


@app.get("/")
def home():
    """Home endpoint."""
    return {"message": "FastAPI Quality Demo"}


@app.post("/users", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    return create_user(db, user)


@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Get a user by ID."""
    return get_user(db, user_id)
