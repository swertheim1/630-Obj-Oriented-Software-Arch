import uuid

from person import Person as p


class Customer(p):
    def __init__(self, p_id, first_name, last_name, phone_no, email, st_address, city, state, zip_code,
                 is_current_guest=None):
        super().__init__(p_id, first_name, last_name, phone_no, email, st_address, city, state, zip_code)
        self.c_num = uuid.uuid4()
        self.is_current_guest = is_current_guest
        self.room_key_issued = 0
        self.res_num = None
        self.is_customer = 1
        self.room_number = None

    @classmethod
    def print_list_of_all_customers(cls, list_of_customers):
        for customer in list_of_customers:
            print(customer)

    def check_in_guest(self):
        self.is_current_guest = 1

    def issue_room_key(self):
        self.room_key_issued = 1

    def check_out_guest(self):
        self.is_current_guest = 0

    def __repr__(self):
        return f"Customer Number: {self.c_num} Name: {self.first_name} {self.last_name}, Email: {self.email}, " \
               f"Phone_no: {self.phone_no} Address: {self.st_address}, {self.city}, {self.state} {self.zip_code}" \
               f" Current Guest: {self.is_current_guest}, Is Customer {self.is_customer} Res No: {self.res_num}"


def test():
    customer1 = Customer('PER-1001', 'Mary', 'Simons', '555-123-4567', 'm.simons@email.com', '1234 Main St,',
                         'Cleveland', 'OH', '11521')
    customer2 = Customer('PER-1014', 'Mark', 'Fink', '436-215-1234', 'm.fink@eamil.com', '1234 First St,',
                         'White Salmon', 'WA', '91253')

    list_of_customers = []
    list_of_customers.append(customer1)
    list_of_customers.append(customer2)

    customer1.check_in_guest()
    customer2.check_in_guest()

    Customer.print_list_of_all_customers(list_of_customers)

    customer2.check_out_guest()

    print(customer2)


if __name__ == '__main__':
    test()
