# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_A, current_A = 0, headA
        len_B, current_B = 0, headB
        
        while current_A:
            len_A += 1
            current_A = current_A.next
        while current_B:
            len_B += 1
            current_B = current_B.next
        
        
        current_A, current_B = headA, headB
        if len_A > len_B:
            for _ in range(len_A - len_B):
                current_A = current_A.next
        if len_B > len_A:
            for _ in range(len_B - len_A):
                current_B = current_B.next
        
        while current_A != current_B:
            current_A = current_A.next
            current_B = current_B.next
        return current_A