from sqlalchemy import select
from db_models import PersonTable, CustomerTable
from main import session


class Person:

    @staticmethod
    def create_person(first_name, last_name, address='', city='', state='', zip_code='', phone_no='', email=''):
        person = PersonTable(first_name=first_name, last_name=last_name, address=address, city=city,
                             state=state, zip_code=zip_code, phone_no=phone_no, email=email)
        session.add_all([person])
        session.commit()

    @staticmethod
    def update_person_first_name(p_id, new_first_name):
        try:
            person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
            person_to_update.first_name = new_first_name
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def update_person_last_name(p_id, new_last_name):
        try:
            person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
            person_to_update.last_name = new_last_name
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def update_person_street_address(p_id, new_address):
        person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
        try:
            person_to_update.address = new_address
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def update_person_city(p_id, new_city):
        try:
            person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
            person_to_update.city = new_city
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def update_person_state(p_id, new_state):
        try:
            person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
            person_to_update.state = new_state
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def update_person_zip(p_id, new_zip):
        try:
            person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
            person_to_update.zip = new_zip
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def update_person_phone(p_id, new_phone_no):
        try:
            person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
            person_to_update.phone_no = new_phone_no
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def update_person_email(p_id, new_email):
        try:
            person_to_update = session.query(PersonTable).filter(PersonTable.person_id == p_id).first()
            person_to_update.email = new_email
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def find_person_by_id(p_id):
        try:
            result = session.query(PersonTable).filter_by(person_id=p_id).all()
            return result
        except Exception as e:
            print('Error!', e)
        finally:
            print('User updated')
            session.close()

    @staticmethod
    def delete_person_by_id(p_id):
        try:
            result = session.query(PersonTable).filter_by(person_id=p_id).first()
            print(f'<<<< PERSON ID: {result.person_id}  Name: {result.first_name, result.last_name}'
                  f' is being deleted! >>>>')
            session.delete(result)
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            session.close()

    @staticmethod
    def create_list_of_all_people():
        return session.query(PersonTable).all()

    @staticmethod
    def check_if_valid(c_id):
        """"
        Person can be deleted if they are in the database and have no current reservations
        """


        print('<<<< CHECKING IF OK TO DELETE >>>>> ')
        # print(f'<<<< PRINTING RESULT {results}  >>>>> ')
        # print(f'<<<< PRINTING STATEMENT {statement}  >>>>> ')
        # for result in results:
        #     # if not statement:
        #     if not CustomerTable.is_guest:
        #         print('<<<<<<< OK TO DELETE', result, 'IN DATABASE >>>>>>>')
        #         print('<<<< OK TO DELETE >>>>> ')
        #         return True
        #
        #     else:
        #         print('<<<<<<< NOT OK TO DELETE ', result, ' NOT IN DATABASE >>>>>>>')
        #         return False


def test():
    print('<<<< STARTING TEST >>>>')
    Person.create_person('Mary', 'Smith', '2121 E 12th St', 'The Dalles', 'OR', '97365', '214-541-2211',
                         'msmith@python.arg')
    Person.create_person('Mary', 'Lane', '1234 Main St.', 'Clearwater', 'FL', '33516',
                         '555-123-4567', 'mary.lane@marylane.com')
    Person.create_person('Mark', 'Ford', '435 E 79th St.', 'New York', 'NY',
                         '02145', '555-346-2587', 'MarkF@ford.com')
    Person.create_person('Bill', 'Worth', '75 14th St.', 'Plano', 'TX',
                         '72145', '555-951-3578', 'bworth@worths.com')
    Person.create_person('Beth', 'Apple', '134 Bryan Road.', 'Lakeside', 'TX',
                         '73226', '555-456-4826', 'Beth.Stull@stull_family.com')
    Person.create_person('Jerry', 'Springer', '8912 Park Ave', 'New York', 'NY',
                         '02115', '555-156-9872', 'jerry@haught.com')
    Person.create_person('Chris', 'Peek', '2272 First St.', 'Stafford', 'TX',
                         '72231', '555-871-8963', 'cpeek@peek.com')
    Person.create_person('Marjorie', 'Slacker', '2216 Alberts Dr.', 'Cleveland', 'OH',
                         '42114', '555-123-4567', 'mslacker@slackers.com')
    Person.create_person('Lola', 'Sawyer', '1212 E 7th St.', 'St. Pete', 'FL',
                         '33622', '555-267-3311', 'lola@sawyer.com')
    Person.create_person('Bella', 'Thomas', '2242 Claiborne St.', 'Clearwater', 'FL',
                         '33516', '555-987-6543', 'bt6543@thomas.com')
    Person.create_person('James', 'Feldman', '191 Main Cir.', 'Lake Saint Louis', 'MO',
                         '63367', '555-444-8888', 'james@feldman.com')
    Person.create_person('Martha', 'Peterson', '1515 North Point Rd.', 'Owlet', 'TX',
                         '73511', '555-582-5820', 'marthapetersonk@peterson.com')

    session.commit()

    statement = select(PersonTable).where(PersonTable.first_name == 'Mary')
    results = session.scalars(statement)
    print('<<<< \nlist of all first names = Mary >>>>')
    for person in results:
        print(person)

    list_of_all_people = Person.create_list_of_all_people()
    print('<<<< \nlist of all people >>>>')
    for person in list_of_all_people:
        print(person)

    print('\n updating users')
    Person.update_person_first_name(1, 'Sally')
    Person.update_person_last_name(2, 'Oropeza')
    Person.update_person_street_address(3, '435 E 79th St., Apt J')
    Person.update_person_city(4, 'Akron')
    Person.update_person_state(5, 'UT')
    Person.update_person_zip(6, '12345')
    Person.update_person_phone(7, '555-123-4567')
    Person.update_person_email(8, 'Sally@o.com')

    print('\nDeleting person ID 3')
    Person.delete_person_by_id(3)

    list_of_all_people = Person.create_list_of_all_people()
    print('<<<< list of all people >>>>')
    for person in list_of_all_people:
        print(person)


if __name__ == "__main__":
    test()
