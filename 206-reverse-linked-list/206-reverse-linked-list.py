# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Will do the recursive approach another day

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        
        while head: # Runs until head points to None
            temporary = head    # Creates a copy of head so we don't lose it
            head = head.next    # Jumps to the next variable in the linked list
            temporary.next = previous   # Change the next of the temporary variable to point to the previous
            previous = temporary    # The new varaible is saved to previous
        
        return previous # The previous now starts at the last variable
            
        
        