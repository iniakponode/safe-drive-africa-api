from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import dotenv

# load the .env file
dotenv.load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# database_name = "phddbv1-35303339ced5"
# user = "phddbv1-35303339ced5"
# password = "Inikst-2018"
# host = "mysql.gb.stackcp.com"
# port = "60673"

# if process.env.JAWSDB_URL:


# DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}"


# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
