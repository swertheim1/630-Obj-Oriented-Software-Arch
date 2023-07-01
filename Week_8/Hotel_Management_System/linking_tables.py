from db_models import (
    CustomerPeopleLinkingTable,
    ReservationCustomerLinkingTable,
    RoomReservationLinkingTable
)
from main import session


class CustomerPeopleLinking:
    @staticmethod
    def create_link(customer_id, people_id):
        linked_item = CustomerPeopleLinkingTable(customer_id=customer_id, people_id=people_id)
        session.add_all([linked_item])
        session.commit()


class ReservationCustomerLinking:
    @staticmethod
    def create_link(reservation_id, customer_id):
        linked_item = ReservationCustomerLinkingTable(reservation_id=reservation_id, customer_id=customer_id)
        session.add_all([linked_item])
        session.commit()


class RoomReservationLinking:
    @staticmethod
    def create_link(room_id, reservation_id):
        linked_item = RoomReservationLinkingTable(room_id=room_id, reservation_id=reservation_id)
        session.add_all([linked_item])
        session.commit()


def test():
    pass


if __name__ == "__main__":
    test()
