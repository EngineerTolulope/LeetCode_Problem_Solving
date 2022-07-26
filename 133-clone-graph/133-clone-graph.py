"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}
        
        def dfs_search(node):
            # Base case. If we checked it already return the copy node
            if node in old_to_new:
                return old_to_new[node]
            
            # Creates a new node using the current node's value
            copy_node = Node(node.val)  
            old_to_new[node] = copy_node
            
            # Go through the neighbors and get the copy node they refer to
            # Then append to neighbors
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs_search(neighbor))
            
            return copy_node # Only the first node hasn't returned yet
        # End of helper function
        
        return dfs_search(node) if node else None
                