# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The is an iterative solution utilizing the in order traversal
        
        current = root  # Tracks what node we are at
        stack = []  # Stores the nodes waiting to be processed
        n = 0   # When n == k, we return the kth node value
        
        
        while current or stack:
            # While the current variable is not null, tries to check the left most nodes
            while current:
                stack.append(current)
                current = current.left
        
            # At this point current is at a Null node
            current = stack.pop()
            n += 1
            
            if n == k:  # This condition will definitely be reached
                return current.val
            current = current.right
        