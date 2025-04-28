from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


class Base(DeclarativeBase):
    pass

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#DATABASE_URL = f"postgresql+psycopg2://postgres:postgres@localhost:5432/bilimdon_db

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)



if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", e)








