# person class as a base class for employees and customers
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy import String, Integer, Float, Boolean, Date
from typing import List
from datetime import date


class Base(DeclarativeBase):
    """
        base class from which to inherit for generating mapped Table and mapped_column objects
    """
    pass


class PersonTable(Base):
    """
    Class that keeps track of people in the database
    Table Name: people
    Columns:
        - person_id int
        - first_name str(25)

        - last_name str(25)
        - address str(100)
        - email str(100)
        - city str(50)
        - states str(2)
        - zip str(5)
        - phone str(10)
    Methods:
        __repr__
    """

    __tablename__ = 'people'

    # columns
    person_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(25), nullable=False)
    last_name: Mapped[str] = mapped_column(String(25), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(2))
    zip_code: Mapped[str] = mapped_column(String(5))
    phone_no: Mapped[str] = mapped_column(String(10))

    def __repr__(self):
        return f"P_id: {self.person_id} First: {self.first_name} Last: {self.last_name}, email: {self.email}, phone_no: {self.phone_no}" \
               f" Address: {self.address}, {self.city}, {self.state} {self.zip_code}"


class EmployeeTable(Base):
    """
    Class that keeps track employee specific information
    Table Name: people
    Columns:
        - emp_id int
        - person_id int (fk)
        - ssn str(25)
        - pay_rate float
        - job_title str(50)
    Methods:
        __repr__
    """
    __tablename__ = 'employees'

    emp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('people.person_id'))
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    is_current_employee: Mapped[bool] = mapped_column(Boolean, nullable=False)
    ssn: Mapped[str] = mapped_column(String(11), nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date)
    hourly_rate: Mapped[float] = mapped_column(Float, nullable=False)
    job_title: Mapped[str] = mapped_column(String(25), nullable=False)
    person: Mapped['PersonTable'] = relationship(cascade='all,delete', backref='employees')

    def __repr__(self):
        return f"Employee Name: {self.person.first_name} {self.person.last_name} {self.emp_id}, ssn: {self.ssn}, " \
               f"Pay:  ${self.hourly_rate}, Job Title {self.job_title}"


class CustomerTable(Base):
    """
    Class that keeps track customer specific information
    Table Name: customers
    Columns:
        - customer_id int (pk)
        - person_id int (fk)
        - current_gues bool
    Methods:
        __repr__
    """
    __tablename__ = 'customers'

    customer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('people.person_id'))
    is_guest: Mapped[bool] = mapped_column(Boolean, nullable=False)
    person: Mapped['PersonTable'] = relationship(backref='customers')
    reservation_list: Mapped[List['Reservation']] = relationship(cascade='all,delete', back_populates='customer')

    def __repr__(self):
        return f"Person_Id: {self.person_id}, Customer ID: {self.customer_id}, Is Current Guest: {self.is_guest}"


class Reservation(Base):
    __tablename__ = 'reservations'

    reservation_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    check_in_date: Mapped[date] = mapped_column(Date, nullable=False)
    check_out_date: Mapped[date] = mapped_column(Date, nullable=False)
    number_of_guests: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    CheckConstraint(check_in_date < check_out_date)
    reservation_room_rate: Mapped[float] = mapped_column(Float, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.customer_id'))
    customer: Mapped[List['CustomerTable']] = relationship(back_populates='reservation_list')
    reservation_dates: Mapped[List["Room"]] = relationship(back_populates="unavailable_dates")

    def __repr__(self):
        return f"Reservation ID:  {self.reservation_id} Name: {PersonTable.last_name} {PersonTable.first_name}," \
               f" C_ID: {self.customer_id}, Staying: from {self.check_in_date} to {self.check_out_date}" \
               f" Room Rate: {self.reservation_room_rate}"


class Room(Base):
    __tablename__ = 'rooms'

    room_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_type: Mapped[str] = mapped_column(String, nullable=False)
    room_capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    base_room_rate: Mapped[float] = mapped_column(Float, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.customer_id'))
    reservation_id: Mapped[int] = mapped_column(ForeignKey('reservations.reservation_id'))
    unavailable_dates: Mapped["Reservation"] = relationship(back_populates="reservation_dates")
    CheckConstraint(room_capacity >= Reservation.number_of_guests)

    def __repr__(self):
        return f"Room ID:  {self.room_id} Room Capacity: {self.room_capacity} Base Rate: {self.base_room_rate}," \
               f" Room Type {self.room_type} Dates Reserved: {self.unavailable_dates}  Customer ID: {self.customer_id} " \
               f" Reservation ID: {self.reservation_id}"


class RoomReservationLinkingTable(Base):
    __tablename__ = 'room_reservation_linking'
    room_reservation_linking_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey('reservations.reservation_id'))
    reservation_id: Mapped[int] = mapped_column(Integer, ForeignKey('rooms.room_id'))


class ReservationCustomerLinkingTable(Base):
    __tablename__ = 'reservation_customer_linking'
    reservation_customer_linking_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('reservations.reservation_id'))
    reservation_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.customer_id'))


class CustomerPeopleLinkingTable(Base):
    __tablename__ = 'people_customer_linking'
    people_customer_linking_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('people.person_id'))
    people_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.customer_id'))
