from sqlalchemy import select
from db_models import Reservation
from main import session
from datetime import date


class CreateReservation:
    @staticmethod
    def create_reservation(check_in_date, check_out_date, customer_id, number_of_guests, reservation_room_rate):
        person = Reservation(check_in_date=check_in_date, check_out_date=check_out_date,
                             number_of_guests=number_of_guests, reservation_room_rate=reservation_room_rate,
                             customer_id=customer_id,)
        session.add_all([person])
        session.commit()

    @staticmethod
    def update_check_in_date(res_id, check_in_date):
        try:
            reservation_to_update = session.query(Reservation)\
                .filter(Reservation.reservation_id == res_id).first()
            reservation_to_update.check_in_date = check_in_date
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('Reservation check_in_date updated')
        session.close()

    @staticmethod
    def update_check_out_date(res_id, check_out_date):
        try:
            reservation_to_update = session.query(Reservation)\
                .filter(Reservation.reservation_id == res_id).first()
            reservation_to_update.check_out_date = check_out_date
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('Reservation check_out_date updated')
        session.close()

    @staticmethod
    def update_number_of_guests(res_id, number_of_guests):
        try:
            reservation_to_update = session.query(Reservation)\
                .filter(Reservation.reservation_id == res_id).first()
            reservation_to_update.number_of_guests = number_of_guests
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('Reservation number of guests updated')
        session.close()

    @staticmethod
    def update_reservation_room_rate(res_id, reservation_room_rate):
        try:
            reservation_to_update = session.query(Reservation) \
                .filter(Reservation.reservation_id == res_id).first()
            reservation_to_update.reservation_room_rate = reservation_room_rate
            session.commit()
        except Exception as e:
            print('Error!', e)
        finally:
            print('Reservation reservation room rate updated')
        session.close()


def test():
    print('<<<< STARTING RESERVATION TEST >>>>')
    CreateReservation.create_reservation(date(2023, 2, 14), date(2023, 2, 17), 2, 161, 3)
    CreateReservation.create_reservation(date(2023, 3, 17), date(2023, 3, 16), 2, 161, 2) # should fail


if __name__ == "__main__":
    test()
