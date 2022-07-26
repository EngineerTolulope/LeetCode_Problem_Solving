# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
First option is to use a hash set, if there is ever a node that correspond to the alrerady visited node we return false.
Second option is to use two different pointer that move with different speeds.  If they ever meet at the same position again, then there is loop so we return False
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head # Both pointers start at the same location
        
        while fast and fast.next:   # Because fast moves two at a time, so this checks the current and the next
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow: # If there is a cycle fast and slow will definitely meea   
                return True
        return False
            
        