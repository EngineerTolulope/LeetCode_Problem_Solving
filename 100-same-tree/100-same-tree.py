# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if not p and not q: # Two empty trees are equal
            return True
        # If one of them is empty or their values aren't equal
        if not p or not q or p.val != q.val:
            return False
        
        left_part = self.isSameTree(p.left, q.left)
        right_part = self.isSameTree(p.right, q.right)
        
        return left_part and right_part # If both the right and left parts are equal