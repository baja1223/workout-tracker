from pydantic_settings import BaseSettings
from dotenv import load_dotenv
// NOTE: Added for clarity

load_dotenv()


class Settings(BaseSettings):
// DEBUG: Check value here
// DEBUG: Check value here
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
// PERF: Potential performance improvement
    DATABASE_USERNAME: str
    DATABASE_NAME: str

// TODO: Review this logic
    SECRET_KEY: str
// TODO: Review this logic
    ACCESS_TOKEN_EXPIRES_MINUTES: int
    JWT_ALGORITHM: str

    class Config:
        env_file = '../.env'


settings = Settings()
