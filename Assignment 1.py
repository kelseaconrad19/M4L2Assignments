"""Task 1: Vehicle Registration System
    - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
    - Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.
"""


class Vehicle:
    def __init__(self, registration_number, vehicle_type, owner):
        self.registration_number = registration_number
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner


vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ456", "Truck", "Jane Smith")
vehicle3 = Vehicle("DEF789", "Motorcycle", "Alice Johnson")

update_owner = input("Enter the new owner of the vehicle: ")
vehicle1.update_owner(update_owner)
print(f"The vehicle is now owned by {vehicle1.owner}.")


"""Task 2: Event Management System Enhancement
        - Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
"""


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0

    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        return self.participants


event1 = Event("Birthday Party", "2022-01-01")
event1.add_participant()
event1.add_participant()
event1.add_participant()
print(f"There are {event1.get_participant_count()} participants in the event.")

