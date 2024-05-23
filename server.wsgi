#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/parse_exel_to_db")
from app import app as application
application.secret_key = 'e4euf74hf'
