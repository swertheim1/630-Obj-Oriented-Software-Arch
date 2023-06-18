from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
        base class from which to inherit
    """
    pass


class Person(Base):
    """
    Purpose: Create person table
        columns
            person_id: Integer, pk
            firstname: String required
            lastname: String, required
            address: String, required
            email: String, required, unique
            city: String, required
            state: String, required
            zip_code: String, required
            country: String, required
            phone: String, required
        methods
            __ init__
            __repr__

    """
    __tablename__ = 'people_table'


    # columns
    person_id = Column('person_id', Integer, primary_key=True)
    firstname = Column('firstname', String(25), nullable=False)
    lastname = Column('lastname', String(25), nullable=False)
    address = Column('address', String(100), nullable=False)
    email = Column('email', String(100), nullable=False)
    city = Column('city', String(50))
    state = Column('state', String(2))
    zip_code = Column('zip_code', String(10))
    country = Column('country', String(2))
    phone = Column('phone', String(10))

    def __repr__(self):
        return f'({self.person_id}) {self.firstname} {self.lastname} ({self.address} {self.email}' \
               f'{self.city} {self.state} {self.zip_code} {self.country} {self.phone})'

    # getters:
    # def get_first_name(self, session, person_id):
    #     firstname = session.query(Person).filter(Person.person_id == person_id)
    #     return self.firstname
