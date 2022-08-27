# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle of linkedlist (slow)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse middle to end
        previous = None
        while slow:
            temporary = slow.next
            slow.next = previous
            previous = slow
            slow = temporary
            
        # check if palindrome
        left, right = head, previous
        while right:    # right going to point to None at middle
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            
        
        
        
        