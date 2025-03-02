#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dev, Freebie, Company

# Setup database session
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Fetch a dev, freebie, and company from the database
dev1 = session.query(Dev).filter_by(name="Alice").first()
dev2 = session.query(Dev).filter_by(name="Bob").first()
freebie = session.query(Freebie).filter_by(item_name="T-Shirt").first()
company = session.query(Company).filter_by(name="Tech Corp").first()

# Set a breakpoint
import ipdb; ipdb.set_trace()

# Now you can test methods interactively
