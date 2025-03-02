#!/usr/bin/env python3

# Script goes here!
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Freebie, Dev, Company 
from models import Base 

DATABASE_URL = "sqlite:///freebies.db"  

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create sample companies
company1 = Company(name="Tech Corp", founding_year=1999)
company2 = Company(name="Innovate Inc", founding_year=2003)

# Create sample devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Add companies and devs to the session first
session.add_all([company1, company2, dev1, dev2])
session.commit() 

# Create sample freebies
freebie1 = Freebie(item_name="T-Shirt", value=20, dev_id=dev1.id, company_id=company1.id)
freebie2 = Freebie(item_name="Mug", value=10, dev_id=dev2.id, company_id=company2.id)

# Add freebies to the session
session.add_all([freebie1, freebie2])

session.commit()

company1.give_freebie(dev1, "T-Shirt", 20, session)

freebies = session.query(Freebie).all()
for freebie in freebies:
    print(freebie.print_details()) 

