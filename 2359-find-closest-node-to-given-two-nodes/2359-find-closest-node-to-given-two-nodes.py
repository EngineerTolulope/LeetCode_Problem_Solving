from typing import List, Dict
from collections import defaultdict, deque
import sys

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # Create an adjacency list to represent the graph
        neighbors = defaultdict(list)
        for start, end in enumerate(edges):
            if end != -1:
                neighbors[start].append(end)
        
        # Perform BFS to compute shortest distances from a starting node
        def bfs(start: int) -> Dict[int, int]:
            distance_map = {}
            queue = deque([(start, 0)])
            distance_map[start] = 0

            while queue:
                node, distance = queue.popleft()
                for neighbor in neighbors[node]:
                    if neighbor not in distance_map:
                        queue.append((neighbor, distance + 1))
                        distance_map[neighbor] = distance + 1

            return distance_map
        
        # Get the distance maps for both nodes
        node1_dist = bfs(node1)
        node2_dist = bfs(node2)

        # Find the closest meeting node
        result = -1
        result_distance = sys.maxsize

        for i in range(len(edges)):
            if i in node1_dist and i in node2_dist:
                max_distance = max(node1_dist[i], node2_dist[i])
                if max_distance < result_distance:
                    result = i
                    result_distance = max_distance
        
        return result

# Example usage:
# solution = Solution()
# print(solution.closestMeetingNode([2, 2, 3, -1], 0, 1))  # Output: 2
# print(solution.closestMeetingNode([1, 2, -1], 0, 2))    # Output: 2
