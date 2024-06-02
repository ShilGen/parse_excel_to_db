import os
import sqlalchemy as db
from sqlalchemy import inspect
from sqlalchemy import and_
#from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import sessionmaker
from models import Delivery

#load_dotenv()
engine = db.create_engine('postgresql+psycopg2://parser:aq54Fre-98m@localhost:5432/wbdata')

Session = sessionmaker(bind=engine)
session = Session()
inst = inspect(Delivery)
attr_names = [c_attr.key for c_attr in inst.mapper.column_attrs]

print(attr_names)
