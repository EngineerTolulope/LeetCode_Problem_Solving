# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth_first_search(root):
            if not root:    # if the tree is empty
                return [True, 0]
            
            left, right = depth_first_search(root.left), depth_first_search(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        
        return depth_first_search(root)[0] 
            
            