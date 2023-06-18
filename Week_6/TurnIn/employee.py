from sqlalchemy import Column, String, Float, Integer
from person import Base


class Employees(Base):
    """
    Purpose: Create person table
        columns
            ssn: String, primary key
            date_started: DateTime required
            pay_rate: Float, required
            job_title: String, required
            people_id: Integer, required
            person_id: Integer, (foreignkey)
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
    __tablename__ = 'employees_table'


    # columns
    emp_id = Column('emp_id', Integer, primary_key=True)
    ssn = Column('ssn', String, nullable=False)
    pay_rate = Column('pay_rate', Float, nullable=False)
    job_title = Column('job_title', String, nullable=False)
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
        return f'{self.ssn} {self.firstname} {self.lastname} {self.address} {self.email}' \
               f'{self.city} {self.state} {self.zip_code} {self.country} {self.phone}' \
               f'{self.pay_rate}, {self.job_title}'

