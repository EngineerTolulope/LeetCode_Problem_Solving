# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, node2 = head, head, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                node2 = fast
                break
                
        if not node2: return node2
        
        node1 = head
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1