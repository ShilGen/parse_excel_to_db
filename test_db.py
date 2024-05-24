import os
import sqlalchemy as db
from sqlalchemy import and_
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import sessionmaker

load_dotenv()
engine = db.create_engine(f'postgresql+psycopg2://parser:aq54Fre-98m@'
                          f'{localhost:5432/wbdata')

Session = sessionmaker(bind=engine)
session = Session()
