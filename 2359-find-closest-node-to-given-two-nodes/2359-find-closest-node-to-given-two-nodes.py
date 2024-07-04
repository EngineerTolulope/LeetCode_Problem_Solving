from typing import List, Dict
from collections import defaultdict, deque
import sys

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # Create an adjacency list to represent the graph
        neighbors = defaultdict(list)
        for start, end in enumerate(edges):
            if end != -1:  # Only consider valid edges
                neighbors[start].append(end)
        
        # Function to perform BFS and compute shortest distances from the start node
        def bfs(start: int) -> Dict[int, int]:
            distance_map = {}  # Dictionary to store distances from the start node
            queue = deque([(start, 0)])  # Initialize queue with the start node and distance 0
            distance_map[start] = 0  # Distance to the start node is 0

            # Process nodes in the queue
            while queue:
                node, distance = queue.popleft()  # Dequeue a node and its distance
                for neighbor in neighbors[node]:  # Iterate over all neighbors
                    if neighbor not in distance_map:  # If neighbor hasn't been visited
                        queue.append((neighbor, distance + 1))  # Enqueue neighbor with updated distance
                        distance_map[neighbor] = distance + 1  # Update distance map for the neighbor

            return distance_map
        
        # Get the distance maps for both nodes using BFS
        node1_dist = bfs(node1)  # Shortest distances from node1
        node2_dist = bfs(node2)  # Shortest distances from node2

        # Initialize result variables
        result = -1  # Variable to store the closest meeting node
        result_distance = sys.maxsize  # Variable to store the minimum maximum distance

        # Iterate through all nodes to find the closest meeting node
        for i in range(len(edges)):
            if i in node1_dist and i in node2_dist:  # Node must be reachable from both node1 and node2
                max_distance = max(node1_dist[i], node2_dist[i])  # Maximum distance to the current node from both node1 and node2
                if max_distance < result_distance:  # If this distance is smaller than the current result distance
                    result = i  # Update the result to the current node
                    result_distance = max_distance  # Update the result distance

        return result  # Return the closest meeting node

# Example usage:
# Create an instance of the Solution class
# solution = Solution()
# Test with a sample graph and print the result
# print(solution.closestMeetingNode([2, 2, 3, -1], 0, 1))  # Output: 2
# print(solution.closestMeetingNode([1, 2, -1], 0, 2))    # Output: 2
