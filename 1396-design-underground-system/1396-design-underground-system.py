class UndergroundSystem:

    def __init__(self):
        self.check_in_map = {} # id -> (start_station, start_time)
        self.total_map = {} # (start, end) -> [total_time, id_count]

    def checkIn(self, id: int, start_station: str, t: int) -> None:
        self.check_in_map[id] = (start_station, t)

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_station, start_time = self.check_in_map[id]
        route = (start_station, end_station)
        del self.check_in_map[id]

        if route not in self.total_map:
            self.total_map[route] = [0, 0]
        self.total_map[route][0] += t - start_time
        self.total_map[route][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, id_count = self.total_map[(startStation, endStation)] 
        return total_time / id_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)