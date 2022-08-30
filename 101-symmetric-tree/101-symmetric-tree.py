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
        
        def depth_first_search(left, right):
            if left and right:
                return (left.val == right.val and depth_first_search(left.left, right.right) and
                        depth_first_search(left.right, right.left))

            return left == right
        
        
        return depth_first_search(root.left, root.right)