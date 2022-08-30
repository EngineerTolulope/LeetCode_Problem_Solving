# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.is_mirror_tree(root.left, root.right)
    
    def is_mirror_tree(self, left, right):
        if left and right:
            return (left.val == right.val and 
                    self.is_mirror_tree(left.left, right.right) and
                    self.is_mirror_tree(left.right, right.left))

        return left == right
