from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from models import Delivery
from parse import read_excel_file
from datetime import datetime



def save_data(file_path):
    DATABASE_URL = "postgresql://localhost:5432/wbdata"

    engine = create_engine('postgresql+psycopg2://parser:aq54Fre-98m@localhost:5432/wbdata')

    Session = sessionmaker(bind=engine)
    session = Session()

    data = read_excel_file(file_path)
    count_lines = len(data) - 1
    user_id = 1
    time = datetime.now()
    doc_id = file_path.split("/")[-1].split(".")[0]
    inspector = inspect(Delivery)
    columns = inspector.columns.keys()
    # print(columns)

    for item in data[1:]:
        delivery_data = {}
        delivery_data['unloading_time'] = time
        delivery_data['doc_id'] = doc_id
        delivery_data['user_id'] = user_id
        for i, column in enumerate(columns[4:]):
            if i < len(item):
                delivery_data[column] = item[i]

        delivery = Delivery(**delivery_data)
        session.add(delivery)
    session.commit()
    return count_lines
