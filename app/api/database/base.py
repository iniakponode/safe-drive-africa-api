from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace 'mydatabase' with your actual database name
database_name = "phddb"
user = "root"
password = "Inikst-2018"
host = "localhost"
port = "3306"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
