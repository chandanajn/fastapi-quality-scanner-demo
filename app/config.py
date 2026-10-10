import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:chandana@localhost:5432/usersdb")
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretpassword123")
