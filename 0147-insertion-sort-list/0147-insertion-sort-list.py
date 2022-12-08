# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        previous, current = head, head.next
        
        while current:
            if current.val >= previous.val:
                previous, current = previous.next, current.next
                continue
            
            position = dummy
            while current.val > position.next.val:
                position = position.next
            
            previous.next = current.next
            current.next = position.next
            position.next = current
            current = previous.next
        
        return dummy.next