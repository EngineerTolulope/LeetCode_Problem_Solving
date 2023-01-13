# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        
        # get to left node
        left_previous, current = dummy, dummy.next
        for _ in range(left - 1):
            left_previous, current = current, current.next
            
        # now current=left, and left_previous = node before left
        # reverse from left to right
        previous = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
            
        # update pointers
        left_previous.next.next = current   # current is at node after right
        left_previous.next = previous   # previous is at right node
        return dummy.next