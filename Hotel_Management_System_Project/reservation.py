import uuid
from datetime import datetime


class Reservation:
    def __init__(self, number_guests, check_in_date, check_out_date, active_reservation=1):
        self.reservation_no = uuid.uuid4()
        self.number_guest = number_guests
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.number_of_nights = (self.check_out_date - self.check_in_date).days
        self.active_reservation = active_reservation

    def update_reservation_check_out_date(self, new_check_out_date):
        self.check_out_date = new_check_out_date

    def update_reservation_num_guests(self, new_number_of_guests):
        self.number_guest = new_number_of_guests

    @classmethod
    def find_reservation(cls, list_of_reservations, reservation_no):
        for reservation in list_of_reservations:
            if reservation_no == reservation_no:
                return reservation

    @classmethod
    def print_list_of_all_reservations(cls, list_of_reservations):
        for reservation in list_of_reservations:
            print(reservation)

    def cancel_cancel_reservation(self):
        self.active_reservation = 0
        self.check_in_date = None
        self.check_out_date = None
        self.number_of_nights = None
        self.reservation_no = None

    def __repr__(self):
        return f"Reservation Number: {self.reservation_no} Check-In Date: {self.check_in_date}  " \
               f" Check-Out Date: {self.check_out_date}, Number of Nights: {self.number_of_nights}" \
               f" Active Reservation {self.active_reservation}"


def test():
    pass


# make reservation:
reservation_list = []
reservation1 = Reservation(2, datetime(2023, 11, 2, 15), datetime(2023, 11, 3, 11), 1)
reservation2 = Reservation(2, datetime(2023, 11, 4, 15), datetime(2023, 11, 6, 11), 1)
reservation_list.append(reservation1)
reservation_list.append(reservation2)

Reservation.update_reservation_num_guests(reservation1, 4)

Reservation.find_reservation(reservation_list, 123)

Reservation.print_list_of_all_reservations(reservation_list)
reservation2.cancel_cancel_reservation()
print(' <<<<<<<<<<<<<<<<<<<<< AFTER CANCELING RESERVATION 2 >>>>>>>>>>>>>>>>>>>>> ')
Reservation.print_list_of_all_reservations(reservation_list)

if __name__ == '__main__':
    test()
