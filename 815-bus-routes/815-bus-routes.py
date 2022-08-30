class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_bus_routes = collections.defaultdict(lambda: set())
        # step 1: record all routes connected to stop
        for route in range(len(routes)):
            for stop in routes[route]:
                stop_to_bus_routes[stop].add(route)
        
        # step 2: initialize data structure for bfs
        visited_stops, visited_routes = set(), set()
        queue = collections.deque()
        queue.append((source, 0))   # (stop, buses taken so far)
        
        # step 3: perform bfs by adding connected stops by route each time
        while queue:
            current_stop, buses_taken = queue.popleft()
            
            if current_stop not in visited_stops:
                # check if we reached the target
                if current_stop == target:
                    return buses_taken
                
                # then we updated visited stops
                visited_stops.add(current_stop)
                
                # next we add all unvisited stops in connected routes to queue
                for connected_route in stop_to_bus_routes[current_stop]:
                    if connected_route in visited_routes:
                        continue
                    for connected_stop in routes[connected_route]:
                        if connected_stop in visited_stops:
                            continue
                        queue.append((connected_stop, 1 + buses_taken))
                    visited_routes.add(connected_route)
        return -1
                                
                            
                        
        