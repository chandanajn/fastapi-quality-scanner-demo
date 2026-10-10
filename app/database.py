"""Database configuration and session management."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # pylint: disable=invalid-name


def get_db():
    """Dependency to get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
