# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize two dummy nodes to start the less-than and greater-or-equal lists
        less_than_head = ListNode(0)
        greater_equal_head = ListNode(0)

        # Initialize tails for both lists
        less_than_tail = less_than_head
        greater_equal_tail = greater_equal_head

        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                # Append to the less-than list
                less_than_tail.next = current
                less_than_tail = less_than_tail.next
            else:
                # Append to the greater-or-equal list
                greater_equal_tail.next = current
                greater_equal_tail = greater_equal_tail.next
            current = current.next
        
        # Combine the two lists
        less_than_tail.next = greater_equal_head.next
        greater_equal_tail.next = None  # Terminate the list

        # Return the combined list, starting from the less-than list head
        return less_than_head.next   