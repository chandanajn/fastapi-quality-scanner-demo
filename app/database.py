"""Database configuration and session management."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(  # pylint: disable=invalid-name
    autocommit=False, autoflush=False, bind=engine
)


def get_db():
    """Dependency to get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
