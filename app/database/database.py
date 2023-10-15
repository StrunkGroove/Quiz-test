import os

from dotenv import load_dotenv
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
postgres_port = os.getenv("POSTGRES_PORT")
postgres_host = os.getenv("POSTGRES_HOST")

sqlalchemy_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

database = Database(sqlalchemy_url)
engine = create_engine(sqlalchemy_url)
Base = declarative_base()