# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_previous = dummy
        
        while True:
            kth_node = self.get_kth_node(group_previous, k)
            if not kth_node:    # not enough k nodes
                break
            group_next = kth_node.next
            
            # reverse group
            current, previous = group_previous.next, kth_node.next
            while current != group_next:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            
            temp = group_previous.next
            group_previous.next = kth_node
            group_previous = temp
        return dummy.next              
            
                
    def get_kth_node(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current
            
            