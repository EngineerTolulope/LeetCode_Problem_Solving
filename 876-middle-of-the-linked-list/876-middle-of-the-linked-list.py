# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer, slow_pointer = head, head
        
        while fast_pointer != None and fast_pointer.next != None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        
        return slow_pointer