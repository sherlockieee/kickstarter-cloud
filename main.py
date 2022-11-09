from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import engine, SessionLocal
from models import Base, Project


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/projects/")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
