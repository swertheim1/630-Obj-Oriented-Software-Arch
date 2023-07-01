from sqlalchemy.orm import Session
from create_db_connection import local_connection
from db_models import Base

# create engine is for connecting to different database engines (sqlite, mySQL, etc.)
# declarative base is the base class we are inheriting from for our classes
# sessionmaker allows us to do stuff in the database(add, update, edit, delete, etc.)
# person_id, firstname, lastname, address, email, city, state, zip_code, country, phone

from datetime import datetime
from db_models import CustomerTable, EmployeeTable, Reservation, Room


def add_some_data():

    mary_lane_res = Reservation(check_in_date=datetime(2023, 8, 12), check_out_date=datetime(2023, 8, 15),
                                number_of_guests=2, reservation_room_rate=161.00, customer_id=1)
    bill_worth_res = Reservation(check_in_date=datetime(2023, 9, 2), check_out_date=datetime(2023, 9, 4),
                                 number_of_guests=1, reservation_room_rate=170.00, customer_id=3)

    room_1001 = Room(room_capacity=2, room_type='1 King Bed', base_room_rate=155.00, customer_id=1,
                     reservation_id=1)
    room_1002 = Room(room_capacity=1, room_type='1 Queen Bed Suite', base_room_rate=155.00, customer_id=2,
                     reservation_id=2)

    session.add_all([mary_lane_res, bill_worth_res, room_1001, room_1002])
    session.commit()


engine = local_connection()
engine.connect()

Base.metadata.create_all(bind=engine)
session = Session(bind=engine)

# add_some_data()
