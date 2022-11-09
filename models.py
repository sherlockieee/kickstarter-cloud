from sqlalchemy import Column, Integer, String, Date, Float

from db import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    created = Column(Date, nullable=False)
