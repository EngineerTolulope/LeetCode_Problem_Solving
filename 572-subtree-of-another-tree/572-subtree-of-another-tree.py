# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base cases.
        if not subRoot: return True # A null tree is a sub tree of any tree
        if not root and subRoot: return False # If a subroot is present and our root is null, then it's false
        
        if self.isSameTree(root, subRoot):   # If our helper function return true then they are the same
            return True
        
        # Checks if we find a sub tree in the left or right children
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))    
    # End of Function
    
    def isSameTree(self, first_tree, second_tree):
        # Base Cases
        if not first_tree and not second_tree:    # If they are both null
            return True
        
        # If they are both not null, and their values are equal
        if first_tree and second_tree and first_tree.val == second_tree.val:
            # Checks the left and right sub trees
            return (self.isSameTree(first_tree.left, second_tree.left) and   
                    self.isSameTree(first_tree.right, second_tree.right))
        
        # We get here if they are not equal. It means all of the above conditions were not met.
        return False
    