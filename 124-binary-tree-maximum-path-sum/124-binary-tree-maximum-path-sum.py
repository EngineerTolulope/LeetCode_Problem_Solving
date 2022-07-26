# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val
        
        # Returns max path value without split
        def dfs_search(root):
            # Base Case
            if not root:
                return 0    # Because we only care about the max values
            
            nonlocal result # Allows us to access our outer result variable
            
            # Takes the maximum, uses zero if it is the number is negative
            left_max = max(dfs_search(root.left), 0)
            right_max = max(dfs_search(root.right), 0)
            
            # Computes the max path sum with split. This is only for our result variable
            result = max(result, root.val + left_max + right_max)
            
            # Returns the max path without a split to upper node
            return root.val + max(left_max, right_max)  # Can only take the left or right value
        # End of Helper Function
        
        dfs_search(root)
        return result          
            