from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# CHANGE USERNAME & PASSWORD
DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost/fastapi_test"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()