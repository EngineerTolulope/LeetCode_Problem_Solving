from typing import List
from collections import defaultdict
import sys

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph.
        # 'neighbors' maps each node to a list of tuples (neighbor, distance)
        neighbors = defaultdict(list)
        for start, end, distance in roads:
            neighbors[start].append((end, distance))
            neighbors[end].append((start, distance))

        # Define a DFS function to traverse the graph.
        def dfs(node: int):
            nonlocal result  # Use the 'result' variable from the outer scope
            if node in visited:
                return  # If the node has already been visited, return

            visited.add(node)  # Mark the node as visited
            # Iterate through all neighbors of the current node
            for neighbor, distance in neighbors[node]:
                # Update the result with the minimum distance encountered so far
                result = min(result, distance)
                # Recursively perform DFS on the neighbor
                dfs(neighbor)

        # Initialize 'result' to the maximum possible integer value
        # This ensures any valid distance found will be smaller
        result = sys.maxsize
        # Initialize a set to keep track of visited nodes
        visited = set()
        # Start the DFS traversal from node 1 (assuming nodes are 1-indexed)
        dfs(1)

        return result  # Return the minimum distance found

# Example usage:
# Create an instance of the Solution class
# solution = Solution()
# Test with a sample graph and print the result
# print(solution.minScore(5, [[1, 2, 9], [1, 3, 4], [2, 4, 6], [3, 4, 3], [3, 5, 7]]))  # Output: 3
