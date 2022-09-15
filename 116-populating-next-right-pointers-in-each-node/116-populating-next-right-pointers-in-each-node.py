"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        current, next_node = root, root.left if root else None
        
        while current and next_node:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left
                
            current = current.next
            if not current:
                current = next_node
                next_node = current.left
        return root
            