import os

from dotenv import load_dotenv

load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8081")
API_KEY = os.getenv("API_KEY")

if not ADMIN_EMAIL or not ADMIN_PASSWORD:
    raise ValueError(
        "Administrator credentials (ADMIN_EMAIL или ADMIN_PASSWORD) not found in environment variables or in file .env"
    )

if not API_KEY:
    raise ValueError("The API key (API_KEY) was not found in the environment variables or in the .env file.")

API_URL = f"{BASE_URL}/api"
