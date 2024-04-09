# A Bus class with both class and instance variables, and a transportation module to manage different bus routes. A test script should demonstrate creating bus instances and accessing both class and instance attributes.

class Bus:
    def __init__(self, city_name, base_fare, route_number, passenger_capacity):
        self.city_name = city_name
        self.base_fare = base_fare
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity


class Route:
    def __init__(self, route_num, start, end, buses):
        self.route_num = route_num
        self.start = start
        self.end = end
        self.buses = buses
        self.total_capacity = self.manage_routes()

    def display_route(self):
        print(f"Route {self.route_num} starts at {self.start} and ends at {self.end}.")
        print(f"Total capacity of the route is {self.total_capacity} passengers.")

    def manage_routes(self):
        total_capacity = sum(bus.passenger_capacity for bus in self.buses)
        return total_capacity

