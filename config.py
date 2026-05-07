import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

DATABASE_PATH = os.environ.get(
    "DATABASE_PATH",
    "database.db"
)

WEBHOOK_TOKEN = os.environ.get(
    "WEBHOOK_TOKEN",
    "dev-webhook-token"
)