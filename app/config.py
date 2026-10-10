"""Configuration module."""
import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_DB_URL = "postgresql://postgres:chandana@localhost:5432/usersdb"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB_URL)
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretpassword123")  # nosec B105
