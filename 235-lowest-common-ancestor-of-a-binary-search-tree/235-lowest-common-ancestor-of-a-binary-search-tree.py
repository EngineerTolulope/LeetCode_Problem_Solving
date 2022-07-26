# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root  # We start at the root node
        
        # Executes until we find the LCA
        while current:
            # If they are both less than the current node value search the left
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If they are both greater
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current