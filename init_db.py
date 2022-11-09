from datetime import date

from db import engine, SessionLocal
from models import Base, Project

Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(Project).count() == 0:
    projects = [
        Project(
            name="Carbon capture",
            description="Removing CO2 directly from air using machinery",
            price=2000,
            created=date(2020, 9, 10),
        ),
        Project(
            name="Reforestation",
            description="Regrowing trees in areas where they are chopped down",
            price=1000,
            created=date(2013, 8, 19),
        ),
        Project(
            name="Replacing gas stove with electric stove",
            description="Campaign to replace natural gas with electric stoves",
            price=1800,
            created=date(2013, 2, 3),
        ),
    ]

    for proj in projects:
        db.add(proj)

    db.commit()
