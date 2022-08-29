# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        # find length of linkedlist
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        if k == 0:
            return head
        
        # move to the pivot and rotate
        current = head
        for _ in range(length - k - 1):
            current = current.next
        new_head = current.next 
        current.next = None
        tail.next = head
        return new_head
        