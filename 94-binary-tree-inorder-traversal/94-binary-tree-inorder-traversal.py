# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(root):
            if not root:    # If the root node is empty 
                return
            
            inorder(root.left)  # Go as left as you can
            result.append(root.val) # Get the root node before going right
            inorder(root.right)
        
        inorder(root)
        return result