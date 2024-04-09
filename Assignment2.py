"""Task 1: File Handling for Building Records
    - Problem Statement: Implement a system to handle building records using file operations. Create a Building class and write a script to save and load building details to and from a file.
    - Expected Outcome: A complete Building class with methods for saving to and loading details from a file. A script demonstrating saving multiple buildings to a file and then reading them back into the program.
"""


class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
    # Methods to save to file and load from file

    def save_building(self):
        with open("building_records.txt", "a") as file:
            file.write(f"{self.name},{self.floors}\n")

    @staticmethod
    def load_buildings():
        buildings = []
        with open("building_records.txt", "r") as file:
            for line in file:
                try:
                    name, floors = line.strip().split(",")
                    buildings.append(Building(name, int(floors)))
                except ValueError:
                    print("Invalid record format.")
        return buildings


building1 = Building("Office Building", 10)
building2 = Building("Apartment Building", 20)
building3 = Building("Shopping Mall", 3)

building1.save_building()
building2.save_building()
building3.save_building()

buildings = Building.load_buildings()
for building in buildings:
    print(f"{building.name} has {building.floors} floors.")

