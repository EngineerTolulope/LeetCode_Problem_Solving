# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def depth_first_search(root, max_value):
            if not root:
                return 0
            
            result = 1 if root.val >= max_value else 0
            max_value = max(root.val, max_value)
            result += (depth_first_search(root.left, max_value) + 
                       depth_first_search(root.right, max_value))
            return result
        return depth_first_search(root, root.val)