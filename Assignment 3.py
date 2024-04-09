"""Task 1: Public Transportation Module
    - Problem Statement: Develop a Bus class as part of a public transportation module. Use class variables to represent common attributes like city name and base fare. Implement instance variables for specific attributes like route number and passenger capacity.
    - Expected Outcome: A Bus class with both class and instance variables, and a transportation module to manage different bus routes. A test script should demonstrate creating bus instances and accessing both class and instance attributes.
"""
from Transportation import Bus, Route

bus1 = Bus("New York", 2.50, 1, 50)
bus2 = Bus("New York", 2.50, 2, 40)
bus3 = Bus("New York", 2.50, 3, 30)

route1 = Route(1, "Downtown", "Uptown", [bus1, bus2, bus3])
route1.display_route()
route2 = Route(2, "East Side", "West Side", [bus1, bus3])
route2.display_route()

