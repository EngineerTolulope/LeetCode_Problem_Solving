# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        left_tail, right_tail = left, right

        current = head
        while current:
            if current.val < x:
                left_tail.next = current
                left_tail = left_tail.next
            else:
                right_tail.next = current
                right_tail = right_tail.next
            current = current.next
        
        left_tail.next = right.next
        right_tail.next = None
        return left.next