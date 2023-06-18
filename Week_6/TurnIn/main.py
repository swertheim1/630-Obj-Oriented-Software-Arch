from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from person import Person, Base
from employee import Employees
from customer import Customers


def main():
    # create engine is for connecting to different database engines (sqlite, mySQL, etc.)
    # declarative base is the base class we are inheriting from for our classes
    # sessionmaker allows us to do stuff in the database(add, update, edit, delete, etc.)
    # person_id, firstname, lastname, address, email, city, state, zip_code, country, phone

    engine = create_engine('sqlite:///{memory}', echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all([
        Person(firstname='Joe', lastname='Smith', phone='1234567890', address='31 Main St.',
               city='San Diego', state='CA', zip_code=93214, email='joe.smith@smith.com', country='US'),
        Person(firstname='Mary', lastname='Smith', phone='1234567891', address='31 Main St.',
               city='San Diego', state='CA', zip_code=93214, email='mary.smith@smith.com', country='US'),
        Person(firstname='Becky', lastname='Jones', phone='5412953321', address='2121 E 21st St.',
               city='Hood River', state='OR', zip_code=33125, email='bjones@jones.com', country='US'),
        Person(firstname='Joe', lastname='Green', phone='2145366478', address='18 Heights Blvd.',
               city='Houston', state='TX', zip_code=76214, email='joegreen@green.com', country='US')])

    session.commit()

    Session = sessionmaker(bind=engine)

    sessionB = Session()
    sessionB.add_all([
        Employees(firstname='Joe', lastname='Smith', phone='1234567890', address='31 Main St.',
                  city='San Diego', state='CA', zip_code=93214, email='joe.smith@smith.com', country='US',
                  ssn='191251234', pay_rate=22.50, job_title='Front Desk Clerk'),
        Employees(firstname='Mary', lastname='Smith', phone='1234567891', address='31 Main St.',
                  city='San Diego', state='CA', zip_code=93214, email='mary.smith@smith.com', country='US',
                  ssn='191251238', pay_rate=22.50, job_title='Front Desk Clerk')])
    sessionB.commit()

    sessionC = Session()
    sessionC.add_all([
        Customers(firstname='Becky', lastname='Jones', phone='5412953321', address='2121 E 21st St.',
                  city='Hood River', state='OR', zip_code=33125, email='bjones@jones.com', country='US',
                  current_guest=0),
        Customers(firstname='Joe', lastname='Green', phone='2145366478', address='18 Heights Blvd.',
                  city='Houston', state='TX', zip_code=76214, email='joegreen@green.com', country='US',
                  current_guest=1)])
    sessionC.commit()

    sessionD = Session()
    current_customer = sessionD.query(Customers).filter_by(current_guest=1)
    for customer in current_customer:
        print('<<<< Current Guests >>>>', customer.firstname, customer.lastname, 'Address: ',
              customer.address, customer.city, customer.state, customer.zip_code, customer.country)
    print()

    sessionE = Session()
    current_employee = sessionE.query(Customers).all()
    for employee in current_employee:
        print('<<<< Current Employees >>>>', employee.firstname, employee.lastname, 'Address: ',
              employee.address, employee.city, employee.state, employee.zip_code, employee.country)
    print()

    sessionF = Session()
    current_person = sessionF.query(Person).all()
    # for person in current_person:
    print('<<<< Current Person >>>>', current_person)
    print()

main()
