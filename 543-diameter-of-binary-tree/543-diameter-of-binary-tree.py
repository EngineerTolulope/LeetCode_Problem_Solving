# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def depth_first_search(root):   # returns the height of the tree
            nonlocal max_diameter
            if not root:
                return -1
            
            left_height = depth_first_search(root.left)
            right_height = depth_first_search(root.right)
            total_diameter = 2 + left_height + right_height
            max_diameter = max(max_diameter, total_diameter)
            return 1 + max(left_height, right_height)
        
        
        depth_first_search(root)
        return max_diameter
            