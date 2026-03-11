import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

# Create settings object
settings = Settings()