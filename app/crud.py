"""CRUD operations for users."""
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    """Create a new user in the database."""
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    """Retrieve a user by their ID."""
    return db.query(User).filter(User.id == user_id).first()
