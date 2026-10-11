"""Configuration module."""
import os
from dotenv import load_dotenv

load_dotenv()


DEFAULT_DB_URL = (
    "postgresql://user:pass@localhost:5432/usersdb"  # pragma: allowlist secret
)
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB_URL)
SECRET_KEY = os.getenv(
    "SECRET_KEY", "mysecretpassword123"
)  # pragma: allowlist secret # nosec B105
