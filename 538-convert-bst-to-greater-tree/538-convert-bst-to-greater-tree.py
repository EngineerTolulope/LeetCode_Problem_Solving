# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_sum = 0
        def dfs(node):
            if not node:
                return
            nonlocal current_sum
            
            dfs(node.right)
            temp = node.val
            node.val += current_sum
            current_sum += temp
            dfs(node.left)
            return
        dfs(root)
        return root