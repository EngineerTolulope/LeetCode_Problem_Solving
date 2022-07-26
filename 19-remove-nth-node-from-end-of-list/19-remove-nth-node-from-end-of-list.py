# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # So that left will be at the node that sets the next pointer
        dummy_node = ListNode(0, head)
        
        left, right = dummy_node, dummy_node
        
        # Setting right starting position
        i = 0
        while i < (n + 1) and right:  # We want a gap of n + 1 between left and right  pointer
            right = right.next
            i += 1
            
        # Continue until right is null
        while right:
            left = left.next
            right = right.next
            
        # Deleting the nth node from the end
        left.next = left.next.next
        
        return dummy_node.next
        
        
        
            
        
        
            
        