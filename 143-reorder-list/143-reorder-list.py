# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        # find the second half of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of linked list
        second = slow.next
        previous = slow.next = None
        while second:
            next_node = second.next
            second.next = previous
            previous = second
            second = next_node
            
        # merge two linked list
        first, second = head, previous
        while second:
            next_node_1, next_node_2 = first.next, second.next
            second.next = first.next
            first.next = second
            first, second = next_node_1, next_node_2
            
            
            