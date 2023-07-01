from sqlalchemy import select
from db_models import CustomerTable, PersonTable
from linking_tables import CustomerPeopleLinking
from person import Person as p
from main import session


class Customers:
    @staticmethod
    def create_customer(person_id, is_guest):
        customer = CustomerTable(person_id=person_id, is_guest=is_guest)
        session.add_all([customer])
        session.commit()

    @staticmethod
    def update_is_guest_by_id(c_id, is_guest):
        customer_to_update = session.query(CustomerTable).filter(CustomerTable.customer_id == c_id).first()
        customer_to_update.is_guest = is_guest
        session.commit()

    @staticmethod
    def create_list_of_customers():
        results = session.query(CustomerTable).join(PersonTable, CustomerTable.person_id == PersonTable.person_id).all()
        return results

    @staticmethod
    def create_list_of_current_guests():
        statement = select(CustomerTable).join(PersonTable, CustomerTable.person_id == PersonTable.person_id) \
            .filter(CustomerTable.is_guest == 1)
        results = session.scalars(statement)
        return results

    @staticmethod
    def create_list_of_non_current_guests():
        statement = select(CustomerTable).join(PersonTable, CustomerTable.person_id == PersonTable.person_id) \
            .filter(CustomerTable.is_guest == 0)
        results = session.scalars(statement)
        return results

    @staticmethod
    def delete_customer_by_id(c_id):
        statement = select(CustomerTable).filter(CustomerTable.customer_id == c_id)
        results = session.scalars(statement)
        print('CUSTOMER: ', statement)
        for result in results:
            session.delete(result)
            print('<<<<<<<<<DELETED OBJECT>>>>>>>>>>')
        # session.commit()

        # statement = select(PersonTable).where(PersonTable.person_id == CustomerTable.person_id) \
        #     .filter(CustomerTable.customer_id == c_id)
        #
        # results = session.scalars(statement)
        # for result in results:
        #     print(f'<<<< PRINT RESULTS.FIRST: {result} >>>>>')

        # customer_id = statement.person_id

        # for customer in results:
        # p.check_if_valid(c_id)
        statement = select(CustomerTable.customer_id).where(PersonTable.person_id == CustomerTable.customer_id)
        results = session.scalars(statement)
        for result in results:
            print (result)

        # if not CustomerTable.is_guest:
        #     # first delete customer from customer table
        #     customer = session.query(CustomerTable).filter_by(customer_id=c_id).first()
        #     session.delete(customer)
        #     session.commit()
        #     # next delete customer from person table
        #
        #     session.delete(results)
        #     session.commit()
        #     # p.delete_person_by_id(CreatePerson).first()
        #
        # else:
        #     print(f'<<<< Cannot delete PERSON ID: {statement.person_id}  '
        #           f'Name: {results.first_name, results.last_name} they are currently a guest. >>>>')
        # print('PRINT RESULTS: ', results)
        # # results = Customer.create_list_of_customers()
        # # for customer in results:
        # #     print('customer: ', customer)


def test():
    # statement = select(Customer).join(CreatePerson, Customer.person_id == CreatePerson.person_id)\
    #     .filter(Customer.is_guest == 0)

    # Customers.create_customer(person_id=1, is_guest=0)
    # Customers.create_customer(person_id=2, is_guest=1)
    # Customers.create_customer(person_id=4, is_guest=1)
    # Customers.create_customer(person_id=5, is_guest=0)
    #
    # CustomerPeopleLinking.create_link(1,1)
    # CustomerPeopleLinking.create_link(2, 2)
    # CustomerPeopleLinking.create_link(3, 3)
    # CustomerPeopleLinking.create_link(4, 4)

    # results = Customers.create_list_of_non_current_guests()
    # print("<<<< Customer that are not Guests >>>>>")
    # for customer in results:
    #     print('Customer ID:', customer.customer_id, customer.person)
    #
    # results = Customers.create_list_of_current_guests()
    # print("<<<< Customer that are Guests >>>>>")
    # for customer in results:
    #     print('Customer ID:', customer.customer_id, customer.person)

    # Customer.delete_customer_by_id(2)
    # Customer.delete_customer_by_id(1)
    Customers.delete_customer_by_id(1)

    # results = p.create_list_of_all_people()
    # print('<<<< list of all people >>>>')
    # for customer in results:
    #     print('Customer ID:', customer.person_id, customer)


if __name__ == '__main__':
    test()
