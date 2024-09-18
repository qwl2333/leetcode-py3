'''
receptionist can help guest make a reservation for a table for a time slot. If no available table, put the guest in waiting list

receptionist can also update a table reservation

receptionist can also cancel a table reservation

'''
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from uuid import uuid4, UUID
from collections import deque

class Guest:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

class TimeSlot:
    def __init__(self, start_time: datetime, end_time: datetime) -> None:
        self.start_time = start_time
        self.end_time = end_time
    
    def has_overlap(self, other: 'TimeSlot') -> bool:
        other_s, other_e = other
        if self.start_time >= other_e or self.end_time < other_s:
            return False
        else:
            return True

class Table:
    def __init__(self, table_id: UUID, capacity: int):
        self.table_id = table_id
        self.capacity = capacity

class ReservationStatus(Enum):
    NOT_STARTED, STARTED, CANCELLED, COMPLETE = 0, 1, 2, 3

class Reservation:
    def __init__(self, reservation_id: UUID, time_slot: TimeSlot, guest: Guest, table: Table, status: ReservationStatus):
        self.reservation_id = reservation_id
        self.time_slot = time_slot
        self.guest = guest
        self.table = table
        self.status = status

class TableService(ABC):
    @abstractmethod
    def get_available_tables(self, time_slot: TimeSlot, party_size: int) -> list[Table]:
        pass
    
    @abstractmethod
    def get_time_slots_by_table(self, table: Table) -> list[TimeSlot]:
        pass

class ReservationService(ABC):
    @abstractmethod
    def get_all_reservations(self) -> list[Reservation]:
        pass

    @abstractmethod
    def make_reservation(self, table: Table, guest: Guest, time_slot: TimeSlot) -> Reservation:
        pass

    @abstractmethod
    def cancel_reservation(self, reservation_id: UUID):
        pass

class TableServiceImpl(TableService):
    def __init__(self, reservation_service: ReservationService):
        self.reservation_service = reservation_service
        self.tables = [Table(uuid4(), 2), Table(uuid4(), 4)]
    
    def __get_all_tables(self) -> list[Table]:
        return self.tables

    def get_available_tables(self, time_slot: TimeSlot, party_size: int) -> list[Table]:
        all_tables = self.__get_all_tables()
        all_reservations = self.reservation_service.get_all_reservations()
        table_ids_used = set()
        for reservation in all_reservations:
            if reservation.time_slot.has_overlap(time_slot):
                table_ids_used.add(reservation.table.table_id)
        
        return [table for table in all_tables if table.table_id not in table_ids_used and table.capacity > party_size]
    
    def get_time_slots_by_table(self, table: Table) -> list[TimeSlot]:
        return [TimeSlot(datetime(2024, 9, 14, 19, 0), datetime(2024, 9, 14, 21, 0))]

class ReservationServiceImp(ReservationService): # subject add/remove observers
    def __init__(self):
        self.reservations = [Reservation(uuid4(), TimeSlot(datetime(2024, 9, 14, 19, 0), datetime(2024, 9, 14, 21, 0)), Guest('li', '2134', 'ss@gmail'), Table, ReservationStatus.NOT_STARTED)]

    def get_all_reservations(self) -> list[Reservation]:
        return self.reservations

    def make_reservation(self, table: Table, guest: Guest, time_slot: TimeSlot) -> Reservation:
        new_reservation = Reservation(uuid4(), time_slot, guest, table, ReservationStatus.NOT_STARTED)
        self.reservations.append(new_reservation)
        return new_reservation

    def cancel_reservation(self, reservation_id: UUID):
        reservation_to_cancel = [reservation for reservation in self.reservations if reservation.reservation_id == reservation_id]
        reservation_to_cancel[0].status = ReservationStatus.CANCELLED


class Receptionist:
    def __init__(self, table_service: TableService, reservation_service: ReservationService):
        super().__init__()
        self.table_service = table_service
        self.reservation_service = reservation_service
        self.waiting_list = deque()
    
    def get_available_tables(self, time_slot: TimeSlot, party_size: int) -> list[Table]:
        return self.table_service.get_available_tables(time_slot, party_size)
    
    def make_reservation(self, table: Table, guest: Guest, time_slot: TimeSlot) -> Reservation:
        return self.reservation_service.make_reservation(table, guest, time_slot)
    
    def cancel_reservation(self, reservation: Reservation):
        self.reservation_service.cancel_reservation(reservation)
    
    def handle_guest(self, guest: Guest, time_slot: TimeSlot, party_size: int):
        available_tables = self.get_available_tables(time_slot, party_size)
        if not available_tables:
            self.waiting_list.append((guest, time_slot, party_size))
        else:
            self.make_reservation(available_tables[0], guest, time_slot)
    
    def handle_available_table(self, table: Table):
        time_slots = self.table_service.get_time_slots_by_table(table)
        has_overlap = False
        for _guest, time_slot, party_size in self.waiting_list:
            if party_size <= table.capacity:
                for ts in time_slots:
                    if time_slot.has_overlap(ts):
                        has_overlap = True
                        break
                if not has_overlap:
                    self.make_reservation(table, time_slot, party_size)
                else:
                    has_overlap = False    

class Manager:
    '''
    similar as receptionist but can hire more people, add/update menu, etc.
    '''
    pass
    
'''
Use TableService, ReservationService with dependency injection
1. separation of concern: Manager and Receptionist both can make reservation thru service without worrying about the detail implementations
2. single responsibility principle
3. Testability: easily mock service during unit testing
4. Reusability: reuser services across different classes
5. Flexibility: different implementation for these two service without changing Manager and Receptionist class
'''