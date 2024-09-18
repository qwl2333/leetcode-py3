'''
这个讲的好烂啊,九章上面的真是垃圾
https://github.com/ycwkatie/OOD-Object-Oriented-Design/blob/main/ood/restaurant.md

1. customer can book tables at a restaurant (only consider one restaurant)
2. search for available tables Search(partySize, timeSlot) -> Table[]
3. Book tables at the restaurant MakeReservation(Restaurant, Table, Customer) -> Reservation
4. CancelReservation(reservationId)

[{restaurant: table[]}]

out-of-scope:
creat/update menu?
create order?
pay the bill?

Core Objects:
Customer
-name
-email
-phone

Restaurant
-name
-location
-Tables[]
-Reservations[]
find_table_for_reservation()
confirm_reservation()
cancel_reservation()


Table
-is_available
-capacity
is_available()

Reservation
-start_time
-end_time
-party_size
-Customer
-Tables[]

'''
from datetime import datetime, timedelta
from enum import Enum
from collections import defaultdict
from uuid import uuid4, UUID

class Customer:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

class Table:
    def __init__(self, id: int, capacity: int):
        self.id = id
        self.capacity = capacity

class ReservationStatus(Enum):
    PENDING, CONFIRMED, CANCELLED, COMPLETE = 0, 1, 2, 3

class Reservation:
    def __init__(self, start_time: datetime, end_time: datetime, customer: Customer, table: Table, status: ReservationStatus):
        self.star_time = start_time
        self.end_time = end_time
        # self.party_size = party_size
        self.customer = customer
        self.table = table
        self.status = status

class Restaurant:
    def __init__(self, id: int, name: str, location: str, tables: list[Table], table_to_reservations: dict[int, tuple[int, datetime]]):
        self.id = id
        self.name = name
        self.location = location
        self.tables = tables
        self.table_to_reservations = table_to_reservations # table_id -> list[start_times] 将reservations转化为这个map
    
    def find_table_for_reservation(self, party_size: int, start_time: datetime, customer: Customer):
        available_table = None
        for table in self.tables:
            if table.capacity >= party_size:
                index_to_insert = self.binary_search(start_time, self.table_to_reservations[table.id])
                if 0 <= index_to_insert < len(self.table_to_reservations[table.id]):
                    available_table = table
                    break
                else:
                    continue
        if available_table:
            return Reservation(start_time, start_time + timedelta(hours=2), customer, available_table, ReservationStatus.PENDING)
        else:
            raise Exception('No available time slots')
    
    def confirm_reservation(self, reservation: Reservation):
        self.table_to_reservations[reservation.table.id].append((reservation.id, reservation.star_time))

    def cancel_reservation(self, reservation: Reservation):
        del self.table_to_reservations[reservation.table.id]

    def binary_search(self, start_time: datetime, sorted_start_times: tuple[int, datetime]) -> int:
        return 0