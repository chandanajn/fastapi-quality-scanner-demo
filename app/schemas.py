"""Pydantic schemas for data validation."""
from pydantic import BaseModel

class UserCreate(BaseModel):  # pylint: disable=too-few-public-methods
    """Schema for creating a user."""
    name: str
    email: str

class UserResponse(BaseModel):  # pylint: disable=too-few-public-methods
    """Schema for returning a user."""
    id: int
    name: str
    email: str

    class Config:  # pylint: disable=too-few-public-methods
        """Pydantic config."""
        orm_mode = True
