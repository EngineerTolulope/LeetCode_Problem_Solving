"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None : None}
        current = head
        while current:
            new = Node(current.val)
            old_to_new[current] = new
            current = current.next
            
        current = head
        while current:
            new = old_to_new[current]
            new.next = old_to_new[current.next]
            new.random = old_to_new[current.random]
            current = current.next
        
        return old_to_new[head]