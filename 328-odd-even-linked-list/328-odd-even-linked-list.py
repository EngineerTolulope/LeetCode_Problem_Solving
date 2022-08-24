# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        is_odd = True
        even_pointer, odd_pointer = ListNode(), ListNode()
        even_head, odd_head = even_pointer, odd_pointer
        current_pointer = head
        
        while current_pointer:
            if is_odd:
                odd_pointer.next = current_pointer
                odd_pointer = odd_pointer.next
            else:
                even_pointer.next = current_pointer
                even_pointer = even_pointer.next
            is_odd = not is_odd
            current_pointer = current_pointer.next
        odd_pointer.next = even_head.next
        even_pointer.next = None
        return odd_head.next