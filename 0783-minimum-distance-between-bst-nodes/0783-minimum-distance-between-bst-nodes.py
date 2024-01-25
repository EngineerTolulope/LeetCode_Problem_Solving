# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result, previous_node = sys.maxsize, None
        
        def dfs(current_node):
            if not current_node:
                return
            
            dfs(current_node.left)
            nonlocal previous_node, result
            if previous_node:
                difference = current_node.val - previous_node.val
                result = min(result, difference)
                # if result == 1:
                #     return result
            previous_node = current_node
            dfs(current_node.right)
        
        dfs(root)
        return result
        
        