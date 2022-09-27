# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flatten_tree(root):
            if not root:
                return None
            
            left_tail = flatten_tree(root.left)
            right_tail = flatten_tree(root.right)
            if left_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            
            return right_tail or left_tail or root
        flatten_tree(root)