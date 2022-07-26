# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:    # If there are no lists to merge
            return None
        
        # Run loop when there are at list two lists to combine
        while len(lists) >= 2:
            combined_lists = [] # Resets combined lists to empty
            
            for i in range(0, len(lists), 2):   # Two lists at a time
                list1 = lists[i]
                list2 = lists[i+1] if (i + 1) < len(lists) else None
                
                # Appends each two pairs of lists
                combined_lists.append(self.mergeTwoLists(list1, list2))
            
            lists = combined_lists  # Stores the combined lists as a new lists variable
        return lists[0]
    # End of Main Function
    
    
    # Helper Function        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Creates a dummy node so our loop executes
        tail = dummy
        
        # We only perform comparison if they are both not empty
        while list1 and list2:
            if list1.val <= list2.val:  # Assigns the smallest value's node to tail.next
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next    # Regardless of the above conditions we should move to next node
        
        # If we finished at least one of the list, and the other one is not empty
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next