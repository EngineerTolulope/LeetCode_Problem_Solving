# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
               
        def dfs_search(node):
            # Base case. If tree is null
            if not node:
                return 0
            
            left_part = dfs_search(node.left)
            right_part = dfs_search(node.right)
            
            return 1 + max(left_part, right_part)   # A tree with one node has a depth of 1 
        
        return dfs_search(root)