class Person:
    def __init__(self, p_id, first_name, last_name, phone_no, email, st_address, city, state, zip_code, is_customer=None,
                 is_employee=None):
        self.p_id = p_id
        self.first_name = first_name
        self.last_name = last_name
        self.st_address = st_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_no = phone_no
        self.email = email
        self.is_customer = is_customer
        self.is_employee = is_employee

    def get_person(self):
        return (self.first_name, self.last_name, self.st_address, self.city, self.state, self.zip_code, self.phone_no,
                self.email)

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_person_address(self, st_address, city, state, zip_code):
        self.st_address = st_address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def update_phone_no(self, phone_no):
        self.phone_no = phone_no

    def update_email(self, email):
        self.email = email

    @classmethod
    def print_list_of_people(cls, list_of_people):
        for people in list_of_people:
            print(people)

    def __repr__(self):
        return f"P_id: {self.p_id} First: {self.first_name} Last: {self.last_name}, email: {self.email}, " \
               f"phone_no: {self.phone_no} Address: {self.st_address}, {self.city}, {self.state} {self.zip_code}"


def test():
    list_of_people = []
    person1 = Person('PER-1001', 'Mary', 'Simons', '555-123-4567', 'm.simons@email.com', '1234 Main St,',
                     'Cleveland', 'OH', '11521')
    person2 = Person('PER-1002', 'Mark', 'Fink', '436-215-1234', 'm.fink@eamil.com', '1234 First St,',
                     'White Salmon', 'WA', '91253')
    person3 = Person('PER-1003', 'Mark', 'Ford', '555-346-2587', 'MarkF@ford.com', '435 E 79th St.',
                     'New York', 'NY', '02145')
    person4 = Person('PER-1004', 'Bill', 'Worth', '555-951-3578', 'bworth@worths.com', '75 14th St.',
                     'Plano', 'TX', '72145')
    person5 = Person('PER-1005', 'Beth', 'Apple', '555-456-4826', 'Beth.Stull@stull_family.com', '134 Bryan Road.',
                     'Lakeside', 'TX', '73226')
    person6 = Person('PER-1006', 'Jerry', 'Springer', '555-156-9872', 'jerry@email.com', '8912 Park Ave',
                     'New York', 'NY', '02115', )
    person7 = Person('PER-1007', 'Chris', 'Peek', '555-871-8963', 'cpeek@peek.com', '2272 First St.', 'Stafford', 'TX',
                     '72231')
    person8 = Person('PER-1008', 'Marjorie', 'Slacker', '555-123-4567', 'mslacker@slackers.com', '2216 Alberts Dr.',
                     'Cleveland', 'OH', '42114')
    person9 = Person('PER-1009', 'Lola', 'Sawyer', '555-267-3311', 'lola@sawyer.com', '1212 E 7th St.', 'St. Pete',
                     'FL', '33622')
    person10 = Person('PER-1010', 'Bella', 'Thomas', '555-987-6543', 'bt6543@thomas.com', '2242 Claiborne St.',
                      'Clearwater', 'FL',
                      '33516')
    person11 = Person('PER-1011', 'James', 'Feldman', '555-987-6543', 'bt6543@thomas.com', '191 Main Cir.',
                      'Lake Saint Louis', 'MO', '63367')
    person12 = Person('PER-1012', 'Martha', 'Peterson', '555-582-5820', 'marthapetersonk@peterson.com',
                      '1515 North Point Rd.', 'Owlet', 'TX', '73511')

    list_of_people.append(person1)
    list_of_people.append(person2)
    list_of_people.append(person3)
    list_of_people.append(person4)
    list_of_people.append(person5)
    list_of_people.append(person6)
    list_of_people.append(person7)
    list_of_people.append(person8)
    list_of_people.append(person9)
    list_of_people.append(person10)
    list_of_people.append(person11)
    list_of_people.append(person12)
    print('<<<<< BEFORE UPDATING >>>>>')
    Person.print_list_of_people(list_of_people)

    person1.update_first_name('Martha')
    person2.update_last_name('Smith')
    person3.update_email('markford@email.com')
    person4.update_person_address('5811 East Wick Ln.', 'Boston', 'MA', '11251')
    person5.update_phone_no('123-456-7895')

    print('<<<<< AFTER UPDATING >>>>>')
    Person.print_list_of_people(list_of_people)


if __name__ == '__main__':
    test()
