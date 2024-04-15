from enum import Enum
from abc import ABC
from typing import Any, Optional
from datetime import datetime

class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5

class Size(Enum):
    COMPACT, REGULAR, LARGE = 1, 2, 3

class ParkingSpotType(Enum):
    CAR, ELECTRIC, HANDICAPPED = 1, 2, 3
  
class ParkingSpot(ABC):
    def __init__(self, level: 'Level', size: Size, spot_number: str, type: ParkingSpotType):
        self.level = level
        self.size = size
        self.spot_number = spot_number
        self.type = type
        self.vehicle = None
    
    # @property
    # def level(self) -> int:
    #     return self._level
    
    # @level.setter
    # def level(self, lvl: int):
    #     self.level = lvl
        
    def add_vehicle(self, vehicle: 'Vehicle'):
        self.vehicle = vehicle
    
    def remove_vehicle(self):
        self.vehicle = None
        
    def is_available(self) -> bool:
        return self.vehicle == None
    
    def can_fit_vehicle(self, vehicle: 'Vehicle') -> bool:
        return self.is_available() and self.size >= vehicle.size

class CompactParkingSpot(ParkingSpot):
    def __init__(self, level: 'Level', spot_number: str, type: ParkingSpotType):
        super().__init__(level, Size.COMPACT, spot_number, type)

class RegularParkingSpot(ParkingSpot):
    def __init__(self, level: 'Level', spot_number: str, type: ParkingSpotType):
        super().__init__(level, Size.REGULAR, spot_number, type)

class Vehicle(ABC): # probably don't need ABC
    def __init__(self, type: VehicleType, size: Size, license_plate: str):
        self.type = type
        self.size = size
        self.license_plate = license_plate
        self.parking_spot = None
        self.ticket = None
    
    def park_to(self, parking_spot: ParkingSpot):
        self.parking_spot = parking_spot
    
    def exit(self):
        self.parking_spot = None
    
    def assign_ticket(self, ticket: 'Ticket'):
        self.ticket = ticket

class Truck(Vehicle):
    def __init__(self, license_plate: str, parking_spots: list[str]):
        super().__init__(VehicleType.TRUCK, license_plate, parking_spots)
    

class Car(Vehicle):
    def __init__(self, license_plate: str, parking_spots: list[str]):
        super().__init__(VehicleType.CAR, license_plate, parking_spots)


class Level:
    def __init__(self, level_number: int, available_spots: int, capacity_for_regular: int, capacity_for_compact: int):
        self.level_number = level_number
        self.available_spots = available_spots
        self.capacity_for_regular = capacity_for_regular
        self.capacity_for_compact = capacity_for_compact
        self.spots: list[ParkingSpot] = []
        for i in range(capacity_for_compact + capacity_for_regular):
            if i < capacity_for_compact:
                self.spots.append(ParkingSpot(self, Size.COMPACT, f'{level_number}-{i}', ParkingSpotType.CAR))
            else:
                self.spots.append(ParkingSpot(self, Size.REGULAR, f'{level_number}-{i}', ParkingSpotType.CAR))


    def add_parking_spot(self, spot: ParkingSpot):
        self.spots[spot.spot_number] = spot
    
    def remove_parking_spot(self, spot: ParkingSpot):
        del self.spots[spot.spot_number]
    
    def park_a_vehicle(self, vehicle: Vehicle) -> 'ParkingLot':
        spot = self.find_available_spot(vehicle)
        self.available_spots -= 1
        spot.add_vehicle(vehicle)
        vehicle.park_to(spot)
        return spot
    
    def exit_a_vehicle(self, vehicle: Vehicle):
        spot = vehicle.parking_spot
        if spot:
            spot.remove_vehicle()
            vehicle.exit()
        self.available_spots += 1

    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        if self.available_spots >= 0:
            for spot in self.spots:
                if spot.can_fit_vehicle(vehicle):
                    return spot
        return None


class ParkingLot:
    def __init__(self, levels: list[Level]):
        self.levels = levels

    # try:
    #   print(x)
    # except NameError:
    #   print("Variable x is not defined")
    def park_a_vechile(self, vehicle: Vehicle) -> Optional['Ticket']:
        if len(self.levels) <= 2:
            raise Exception('Need 2 levels')
        
        target_level = None
        if vehicle.size == Size.COMPACT:
            first_level = self.levels[0]
            second_level = self.levels[1]
            if first_level.available_spots >= 0:
                target_level = first_level
            elif second_level.available_spots >= 0:
                target_level = second_level
        else: # large vehicle
            second_level = self.levels[1]
            if second_level.available_spots >= 0:
                target_level = second_level

        if target_level:
            spot = target_level.park_a_vehicle(vehicle)
            new_ticket = Ticket(spot, vehicle)
            vehicle.assign_ticket(new_ticket)
            return new_ticket
        else:
            return None
    
    def exit(self, ticket: 'Ticket') -> bool:
        vehicle = ticket.vehicle
        spot = ticket.spot
        level = spot.level
        level.exit_a_vehicle(vehicle)
        ticket.pay_fee()
    

class Ticket:
    def __init__(self, spot: ParkingSpot, vehicle: Vehicle) -> None:
        self.spot = spot
        self.vehicle = vehicle
        self.start_time = datetime.now()
        self.fee = 2

    def calculate_fee(self) -> float:
        time_diff = datetime.now() - self.start_time
        return int(time_diff) * 2

    def pay_fee(self):
        # calculate_fee
        # make payments
        # release ticket from vehicle and spot
        pass





