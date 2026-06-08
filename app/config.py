import os
from dotenv import load_dotenv
#prueba de pipeline
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Sistema de Votación"
    DEBUG: bool = False
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()