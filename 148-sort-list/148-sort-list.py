# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # split the linkedlist into half
        left = head
        right = self.get_middle_node(head)
        temp = right.next
        right.next = None
        right = temp
        
        left, right = self.sortList(left), self.sortList(right)
        merged_list = self.merge_lists(left, right)
        return merged_list
    
    
    def get_middle_node(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge_lists(self, list_1, list_2):
        tail = dummy = ListNode()
        while list_1 and list_2:
            if list_1.val < list_2.val:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next
            tail = tail.next
        if list_1:
            tail.next = list_1
        elif list_2:
            tail.next = list_2
        
        return dummy.next
            
        
        