from typing import List, Tuple, Deque, Optional
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[Tuple[int, int]], blueEdges: List[Tuple[int, int]]) -> List[int]:
        # Build adjacency lists for red and blue edges
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for src, dst in redEdges:
            red_graph[src].append(dst)

        for src, dst in blueEdges:
            blue_graph[src].append(dst)
        
        # Initialize the answer list with -1, indicating unreachable nodes
        distances = [-1] * n
        # Initialize the queue with the start node (node 0) and both color options (None for the first move)
        queue = deque([(0, 0, None)])  # (node, distance, last_edge_color)
        # Set to track visited nodes with specific incoming edge colors
        visited = set()
        visited.add((0, None))

        # BFS to explore the shortest paths
        while queue:
            node, distance, last_edge_color = queue.popleft()
            
            # If it's the first time visiting this node, update its distance
            if distances[node] == -1:
                distances[node] = distance
            
            # Explore the neighbors with red edges if the last edge was not red
            if last_edge_color != "RED":
                for neighbor in red_graph[node]:
                    if (neighbor, "RED") not in visited:
                        visited.add((neighbor, "RED"))
                        queue.append((neighbor, distance + 1, "RED"))
            
            # Explore the neighbors with blue edges if the last edge was not blue
            if last_edge_color != "BLUE":
                for neighbor in blue_graph[node]:
                    if (neighbor, "BLUE") not in visited:
                        visited.add((neighbor, "BLUE"))
                        queue.append((neighbor, distance + 1, "BLUE"))
        
        return distances

# Example usage:
# solution = Solution()
# print(solution.shortestAlternatingPaths(3, [[0, 1], [1, 2]], [[0, 2]]))
# Output: [0, 1, 1]
