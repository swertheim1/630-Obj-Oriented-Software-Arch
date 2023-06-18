from sqlalchemy import Column, Boolean, Integer, String
from person import Base


class Customers(Base):
    """
    Purpose: Create person table
        columns
            customer_id: Integer, pk
            current_guest: Bool, required
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
    __tablename__ = 'customer'

    # columns
    customer_id = Column('customer_id', Integer, primary_key=True)
    current_guest = Column('current_guest', Boolean, nullable=False)
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
        return f'{self.firstname} {self.lastname} ({self.address} {self.email}' \
               f'{self.city} {self.state} {self.zip_code} {self.country} {self.phone} - {self.current_guest} ' \
               f'{self.customer_id})'
