from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
  DB_HOST: str
  DB_USER: str
  DB_PASSWORD: str
  DB_NAME: str
  HOST: str
  APP_NAME: str
  PORT: str
  APP_VERSION: str
  
  @property
  def database_url(self) -> str:
    return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"
  
  class Config:
    env_path = Path(__file__).parent.parent.parent / ".env"
    env_file = env_path
    env_file_encoding = "utf-8"
    
print(Path(__file__).parent.parent.parent)
settings = Settings()


SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
