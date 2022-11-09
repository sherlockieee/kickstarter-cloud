from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

if "RDS_DB_NAME" in os.environ:
    DATABASE_URL = "postgresql://{username}:{password}@{host}:{port}/{database}".format(
        username=os.environ["RDS_USERNAME"],
        password=os.environ["RDS_PASSWORD"],
        host=os.environ["RDS_HOSTNAME"],
        port=os.environ["RDS_PORT"],
        database=os.environ["RDS_DB_NAME"],
    )
else:
    DATABASE_URL = "postgresql://{username}:{password}@{host}:{port}/{database}".format(
        username="sherlockieee",
        password="password",
        host="localhost",
        port="5432",
        database="kickstarter-cloud",
    )


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
