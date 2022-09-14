class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_of_points = len(points)
        adjacents = { i : [] for i in range(num_of_points)} # i : list of [cost, node]
        
        # create adjacents lists
        for i in range(num_of_points):
            x1, y1 = points[i]
            for j in range(i + 1, num_of_points):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjacents[i].append([distance, j])
                adjacents[j].append([distance, i])
                
        # prim's algorithm
        total_cost = 0
        visited = set()
        min_heap = [[0, 0]] # [cost, node]
        while len(visited) < num_of_points:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
                
            total_cost += cost
            visited.add(i)
            for neigbour_cost, neighbor in adjacents[i]:
                if neighbor in visited:
                    continue
                heapq.heappush(min_heap, [neigbour_cost, neighbor])
        
        return total_cost
                    