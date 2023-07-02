class Room:
    def __init__(self, room_number, is_available, room_rate):
        self.room_number = room_number
        self.is_available = is_available
        self.room_rate = room_rate

    @classmethod
    def make_list_of_available_rooms(cls, list_of_rooms):
        for room in list_of_rooms:
            if room.is_available:
                print(room.room_number)

    def reserve_room(self):
        self.is_available = 0

    def unreserved_room(self):
        self.is_available = 1

    def update_room_rate(self, new_rate):
        self.room_rate = new_rate


def test():
    list_rooms = []
    room101 = Room(101, 0, 161)
    room102 = Room(102, 1, 161)
    room103 = Room(103, 1, 161)
    room104 = Room(104, 0, 161)
    room105 = Room(105, 1, 161)
    room106 = Room(106, 0, 161)
    room107 = Room(107, 1, 161)
    room108 = Room(108, 0, 161)
    room109 = Room(109, 0, 161)
    list_rooms.append(room101)
    list_rooms.append(room102)
    list_rooms.append(room103)
    list_rooms.append(room104)
    list_rooms.append(room105)
    list_rooms.append(room106)
    list_rooms.append(room107)
    list_rooms.append(room108)
    list_rooms.append(room109)

    Room.make_list_of_available_rooms(list_rooms)


if __name__ == '__main__':
    test()
