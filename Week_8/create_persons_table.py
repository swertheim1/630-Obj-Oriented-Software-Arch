import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import datetime
import os

Base = sqlalchemy.orm.declarative_base()

class Persons(Base):
    """
    class Persons
        tablename = persons
        table columns:
            - id int
            - first_name str
            - last_name str
            - address str
            - email str
            - city str
            - zip_code str
            - country str
            - phone str
            - date_created datetime
        methods:
            __repr__
            none -> string
    """

    __tablename__ = 'persons'

    id = Column('id', Integer, primary_key=True)    # auto increments
    first_name = Column('first_name', String, nullable=False)
    last_name = Column('last_name', String, nullable=False)
    address = Column('address', String, nullable=False)
    email = Column('email', String, nullable=False)
    city = Column('city', String, nullable=False)
    state = Column('state', String, nullable=False)
    zip_code = Column('zip_code', String, nullable=False)
    country = Column('country', String, nullable=False)
    phone = Column('phone', String, nullable=False)
    date_created = Column('date_created', DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f'<Person {self.first_name} {self.last_name} {self.address} {self.email} {self.phone}\n' \
               f'{self.city}, {self.state} {self.zip_code}, {self.country},  Created: {self.date_created}\n'

    # Getters
    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_country(self):
        return self.country

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    # Setters
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state_province(self, state):
        self.state = state

    def set_zip(self, zip_code):
        self.zip_code = zip_code

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_country(self, country):
        self.country = country


# new_person = Persons('Susan', 'Wertheim', 'susan@susan.com', 'my_st_address', 'USA',
#                      'St. Louis', 'MO', '63678', '555-125-6798')
# print(new_person)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'persons.db')

engine = create_engine(connection_string, echo=False)
# Base.metadata.create_all(bind=engine)
#
Session = sessionmaker()
# session = Session()
#
# # person = first_name, last_name, email, country, city, state, zip_code, phone
# person1 = Persons('Mike', 'Thomas', 'mikethomas@gmail.com', 'USA', 'Tampa', 'FL', '33615', '555-456-7890')
# person2 = Persons('Raul', 'Padilla', 'raul.padilla@hotmail.com', 'USA', 'Fresno', 'CA', '98765', '555-123-4567')
# person3 = Persons('Sarah', 'Gentry', 'sgentry@outlook.com', 'USA', 'Toledo', 'OH', '56135', '555-897-5681')
# person4 = Persons('Ronald', 'Patrick', 'ron.patrick@outlook.com', 'USA', 'Chicago', 'OH', '58231', '555-123-8753')
# person5 = Persons('Martha', 'Patrick', 'mpatrick@gmail.com', 'USA', 'St. Louis', 'MO', '65124', '555-636-7858')
#
# session.add(person1)
# session.add(person2)
# session.add(person3)
# session.add(person4)
# session.add(person5)
#
# session.commit()

# results = session.query(Persons).all()
# print(results)
#
# print('***** Last Name = Thomas *****')
# results = session.query(Persons).filter(Persons.last_name == "Thomas")
# for r in results:
#     print(r)
#
#
# print('***** Last Name = Patrick *****')
# results = session.query(Persons).filter(Persons.last_name == 'Patrick')
# for r in results:
#     print(r)
#
# print('***** Last Name like P% *****')
# results = session.query(Persons).filter(Persons.last_name.like('P%'))
# for r in results:
#     print(r)
#
# print('***** First Name in [Mike and Sarah] *****')
# results = session.query(Persons).filter(Persons.first_name.in_(['Mike', 'Sarah']))
# for r in results:
#     print(r)

# thing1 = Things(1, 'baseball', 31248)
# thing2 = Things(2, 'truck', 57891)
# thing3 = Things(3, 'book', 68391)
# thing4 = Things(4, 'glass', 57891)
# thing5 = Things(5, 'laptop', 68391)
#
# session.add(thing1)
# session.add(thing2)
# session.add(thing3)
# session.add(thing4)
# session.commit()

# results = session.query(Things).all()
# print(results)
#
# results = session.query(Things, Persons).filter(Things.owner == Persons.ssn,
#                                                 Persons.first_name == 'Anna').all()
#
# for r in results:
#     print(r)
