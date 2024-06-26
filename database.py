import argparse
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from parse import read_excel_file
from datetime import datetime

Base = declarative_base()


class Delivery(Base):
    __schema__ = "public"
    __tablename__ = 'productsales'

    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.id'))
    unloading_time = Column(Date)
    deliverynumber = Column(Integer)
    item = Column(String)
    item_code = Column(Integer)
    brand = Column(String)
    supplier_article = Column(String)
    name = Column(String)
    size = Column(String)
    barcode = Column(String)
    document_type = Column(String)
    payment_reason = Column(String)
    order_date = Column(Date)
    sale_date = Column(Date)
    quantity = Column(Integer)
    retail_price = Column(Float)
    realized_price = Column(Float)
    agreed_discount_percent = Column(Float)
    promo_code_percent = Column(Float)
    final_agreed_discount_percent = Column(Float)
    retail_price_with_discount = Column(Float)
    rating_reduction_percent = Column(Float)
    promotion_reduction_percent = Column(Float)
    permanent_customer_discount_percent = Column(Float)
    base_commission_percent = Column(Float)
    final_commission_percent = Column(Float)
    commission_without_vat = Column(Float)
    sales_commission_without_vat = Column(Float)
    return_and_delivery_compensation = Column(Float)
    acquiring_compensation = Column(Float)
    wildberries_commission_without_vat = Column(Float)
    vat_from_commission = Column(Float)
    seller_payment = Column(Float)
    delivery_count = Column(Integer)
    return_count = Column(Integer)
    delivery_service = Column(Float)
    total_fines = Column(Float)
    additional_payments = Column(Float)
    logistics_fines_and_payments = Column(String)
    mp_sticker = Column(String)
    bank_name = Column(String)
    office_number = Column(Integer)
    delivery_office_name = Column(String)
    partner_inn = Column(String)
    partner = Column(String)
    warehouse = Column(String)
    country = Column(String)
    box_type = Column(String)
    customs_declaration_number = Column(String)
    marking_code = Column(String)
    shk = Column(String)
    rid = Column(String)
    srid = Column(String)
    transportation_expense_compensation = Column(Float)
    transportation_organizer = Column(String)
    storage = Column(Float)
    deductions = Column(Float)
    paid_acceptance = Column(Float)


def parse_args():
    parser = argparse.ArgumentParser(description='Process delivery data from a exel file.')
    parser.add_argument('file_path', type=str, help='Path to the exel file containing delivery data')
    return parser.parse_args()


def main():
    args = parse_args()
    DATABASE_URL = "postgresql://localhost:5432/wbdata"
    #engine = create_engine(DATABASE_URL)

    engine = create_engine('postgresql+psycopg2://parser:aq54Fre-98m@localhost:5432/wbdata')
    # Создаем таблицы
    # Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = read_excel_file(args.file_path)
    user_id = 1
    time = datetime.now()
    # print(data)
    for item in data[1:]:
        delivery = Delivery(
            id=item[0],
            # user_id=user_id,
            unloading_time=time,
            deliverynumber=item[1],
            item=item[2],
            item_code=item[3],
            brand=item[4],
            supplier_article=item[5],
            name=item[6],
            size=item[7],
            barcode=item[8],
            document_type=item[9],
            payment_reason=item[10],
            order_date=item[11],
            sale_date=item[12],
            quantity=item[13],
            retail_price=item[14],
            realized_price=item[15],
            agreed_discount_percent=item[16],
            promo_code_percent=item[17],
            final_agreed_discount_percent=item[18],
            retail_price_with_discount=item[19],
            rating_reduction_percent=item[20],
            promotion_reduction_percent=item[21],
            permanent_customer_discount_percent=item[22],
            base_commission_percent=item[23],
            final_commission_percent=item[24],
            commission_without_vat=item[25],
            sales_commission_without_vat=item[26],
            return_and_delivery_compensation=item[27],
            acquiring_compensation=item[28],
            wildberries_commission_without_vat=item[29],
            vat_from_commission=item[30],
            seller_payment=item[31],
            delivery_count=item[32],
            return_count=item[33],
            delivery_service=item[34],
            total_fines=item[35],
            additional_payments=item[36],
            logistics_fines_and_payments=item[37],
            mp_sticker=item[38],
            bank_name=item[39],
            office_number=item[40],
            delivery_office_name=item[41],
            partner_inn=item[42],
            partner=item[43],
            warehouse=item[44],
            country=item[45],
            box_type=item[46],
            customs_declaration_number=item[47],
            marking_code=item[48],
            shk=item[49],
            rid=item[50],
            srid=item[51],
            transportation_expense_compensation=item[52],
            transportation_organizer=item[53],
            storage=item[54],
            deductions=item[55],
            paid_acceptance=item[56]
        )
        session.add(delivery)

    session.commit()


if __name__ == "__main__":
    main()
