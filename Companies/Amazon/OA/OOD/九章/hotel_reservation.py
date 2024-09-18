'''
clarify:
1 search for available rooms based on dates, partySize, location
room type?
when partySize > room capacity how to choose room? Choosen by customers

2 make reservation (how many rooms what types of rooms, start end dates)

3 cancel reservation

core objects
Hotel
-rooms
-reservations
def handle_search_request(Request r) -> dict[RoomType, int]:
def __is_request_available(r: Request, list[datetime]) -> bool:

def make_reservation(r: ReservationRequest) -> Reservation:

Reservation
-rooms[]

Room
room_type

RoomType Enum
SINGLE
DOUBLE

Request 这是user第一次search available rooms的时候的reqeust
-start_date
-end_date

ReservationRequest 这是user意见决定了订几间房发出的request
-start_date
-end_date
-rooms_needed: dict[RoomType, int]
-party_size
'''