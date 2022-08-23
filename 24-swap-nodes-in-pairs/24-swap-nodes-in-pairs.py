# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous, current = dummy, head
        
        while current and current.next:
            # save pairs
            next_current = current.next.next
            second_node = current.next
            
            # swapping the pair
            current.next = next_current
            second_node.next = current
            previous.next = second_node
            
            # update pairs
            previous = current
            current = next_current
        return dummy.next
            