class UndergroundSystem:
    def __init__(self):
        # Maps customer ID to their check-in station and time
        self.check_in_map = {}  # id -> (start_station, start_time)
        
        # Maps a route (start_station, end_station) to total travel time and trip count
        self.route_times = {}  # (start_station, end_station) -> [total_time, trip_count]

    def checkIn(self, customer_id: int, start_station: str, start_time: int) -> None:
        # Store the check-in information for the customer
        self.check_in_map[customer_id] = (start_station, start_time)

    def checkOut(self, customer_id: int, end_station: str, end_time: int) -> None:
        # Retrieve and remove the check-in information for the customer
        start_station, start_time = self.check_in_map.pop(customer_id, (None, None))
        
        if start_station is None:
            raise ValueError(f"Customer {customer_id} did not check in.")
        
        # Calculate the travel time
        travel_time = end_time - start_time
        route = (start_station, end_station)
        
        # Update the route's total travel time and trip count
        if route not in self.route_times:
            self.route_times[route] = [0, 0]
        self.route_times[route][0] += travel_time
        self.route_times[route][1] += 1

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        # Retrieve the total travel time and trip count for the route
        total_time, trip_count = self.route_times.get((start_station, end_station), (0, 0))
        
        if trip_count == 0:
            raise ValueError(f"No trips from {start_station} to {end_station}.")
        
        # Calculate and return the average travel time
        return total_time / trip_count

# Example usage:
# obj = UndergroundSystem()
# obj.checkIn(id, stationName, t)
# obj.checkOut(id, stationName, t)
# param_3 = obj.getAverageTime(startStation, endStation)
