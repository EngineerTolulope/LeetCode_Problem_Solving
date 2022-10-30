# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:      
        def dfs(root):  # returns (with_root, without_root)
            if not root:
                return (0, 0)
            
            left_pair, right_pair = dfs(root.left), dfs(root.right)
            with_root = root.val + left_pair[1] + right_pair[1]
            without_root = max(left_pair) + max(right_pair)
            return (with_root, without_root)
        
        
        return max(dfs(root))