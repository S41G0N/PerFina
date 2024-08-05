from dotenv import load_dotenv
import os

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Create variables from environment
SECRET_KEY = str(os.getenv("SECRET_KEY"))
ALGORITHM = str(os.getenv("ALGORITHM"))
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# You can add error checking
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for JWT auth")

# Add any other configuration variables you need
DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
