from typing import List, Dict
from zoneinfo import available_timezones
all_vehicles = []
all_branches = []
all_bookings = []


class Branch():
    def __init__(self, id, name, vehicles: List, prices: Dict):
        self.id = id
        self.name = name
        self.vehicles = vehicles
        self.prices = prices


class Vehicle():
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.slots = {1:True, 2:True, 3:True, 4:True}


class Booking():
    def __init__(self, id, vehicle: Vehicle, start_slot, end_slot):
        self.id = id
        self.vehicle = vehicle
        self.start_slot = start_slot
        self.end_slot = end_slot


class Vehicle_service():
    def add_vehicle(self, id, type):
        v1 = Vehicle(id, type)
        all_vehicles.append(v1)
        return v1


class Branch_service():
    def add_branch(self, id, name, vehicles, prices: List):

        b1 = Branch(id, name, vehicles, prices)
        all_branches.append(b1)
        return b1


class Availability_service():

    def get_available_vehicles(self, branch: Branch, start_slot, end_slot):
        available_vehicles = []
        vehicle: Vehicle
        for vehicle in branch.vehicles:
            for slot in range(start_slot, end_slot+1):
                if slot in vehicle.slots:
                    continue
                else:
                    break
            else:
                available_vehicles.append(vehicle)
        available_vehicle:Vehicle
        for available_vehicle in available_vehicles:
            print(available_vehicle.type, available_vehicle.id)
        return available_vehicles


class Booking_service():
    def rent_vehicle(self, branch, vehicle, start_slot, end_slot):
        for slot in range(start_slot, end_slot+1):
            if slot in vehicle.slots:
                b1 = Booking(1, vehicle, start_slot, end_slot)
                all_bookings.append(b1)
            else:
                return "Unavailable"
        else:
            return "Booked for slots "+str(start_slot)+" to "+str(end_slot)


class System_view_service():
    def systemView(self, slot):
        branch: Branch
        vehicle: Vehicle
        dc = dict()
        for branch in all_branches:
            for vehicle in branch.vehicles:
                if slot in vehicle.slots:
                    dc[vehicle.type] = dc.get(vehicle.type, 0)+1

            for k, v in dc.items():
                print(v, k, "are available in", branch.id)


if __name__ == "__main__":
    v1 = Vehicle_service().add_vehicle(1, "suv")
    v2 = Vehicle_service().add_vehicle(2, "sed")
    v3 = Vehicle_service().add_vehicle(3, "sed")
    v4 = Vehicle_service().add_vehicle(4, "suv")
    v5 = Vehicle_service().add_vehicle(5, "hat")

    b1 = Branch_service().add_branch(1, "abc", [v1, v2], [10, 15])
    b2 = Branch_service().add_branch(1, "def", [v3, v4], [12, 14])

    print("Availability:")
    Availability_service().get_available_vehicles(b1, 1, 1)
    
    booking_1 = Booking_service().rent_vehicle(b1, v1, 1, 1)

    print("Availability:")
    Availability_service().get_available_vehicles(b1, 1, 1)

    Availability_service().get_available_vehicles(b2, 1, 1)

    System_view_service().systemView(slot=2)
