# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid_check(left, node, right):
            # Base case. Returns null if nothing to check
            if not node:    
                return True
            
            # Return false if it's not a valid binary tree
            if not (left < node.val < right):
                return False
            
            # Checks the Left and Right Nodes
            return (is_valid_check(left, node.left, node.val) and
                    is_valid_check(node.val, node.right, right))
        
        # Returns the final answer
        return is_valid_check(float("-inf"), root, float("inf"))