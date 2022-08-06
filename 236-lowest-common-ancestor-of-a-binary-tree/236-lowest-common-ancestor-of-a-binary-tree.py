# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        
        left_side = self.lowestCommonAncestor(root.left, p, q)
        right_side = self.lowestCommonAncestor(root.right, p, q)
        
        if (left_side and right_side) or (root in [p, q]):
            return root
        else:
            return left_side or right_side