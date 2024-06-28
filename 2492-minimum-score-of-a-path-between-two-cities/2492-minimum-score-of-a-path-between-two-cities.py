from typing import List
from collections import defaultdict
import sys

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph.
        neighbors = defaultdict(list)
        for start, end, distance in roads:
            neighbors[start].append((end, distance))
            neighbors[end].append((start, distance))

        # Initialize variables for the result and visited set
        self.result = sys.maxsize
        self.visited = set()
        
        # Start the DFS traversal from node 1 (assuming nodes are 1-indexed)
        self._dfs(1, neighbors)
        
        return self.result

    def _dfs(self, node: int, neighbors: defaultdict(list)):
        # If the node has already been visited, return
        if node in self.visited:
            return

        # Mark the node as visited
        self.visited.add(node)
        
        # Iterate through all neighbors of the current node
        for neighbor, distance in neighbors[node]:
            # Update the result with the minimum distance encountered so far
            self.result = min(self.result, distance)
            # Recursively perform DFS on the neighbor
            self._dfs(neighbor, neighbors)

# Example usage:
# solution = Solution()
# print(solution.minScore(5, [[1, 2, 9], [1, 3, 4], [2, 4, 6], [3, 4, 3], [3, 5, 7]]))  # Output: 3
