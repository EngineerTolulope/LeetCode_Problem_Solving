# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        current, previous = head, dummy

        while current:
            next_ = current.next

            if current.val == val:
                previous.next = next_
            else:
                previous = current
            current = current.next
        return dummy.next

