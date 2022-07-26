# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case. If Null return None
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])  # Root node is always the first in preorder
        middle = inorder.index(preorder[0])    # The inorder tell us what goes in the left and right
        
        # New preorder skips the root and includes the next number of elements based on the middle
        # New inorder takes from all elements from the beginning to the middle - 1
        root.left = self.buildTree(preorder[1:middle+1], inorder[:middle])
        
        # They both take the remaining elements on the right side after the middle
        root.right = self.buildTree(preorder[middle+1:], inorder[middle+1:])
        
        # Only the first method call hasn't returned a value yet
        return root
        