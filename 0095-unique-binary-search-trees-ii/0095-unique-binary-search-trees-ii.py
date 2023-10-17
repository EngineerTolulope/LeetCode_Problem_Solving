
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}  # Dictionary to store previously computed results
        
        def generate(left, right):
            # Base case: If the left index is greater than the right index, return a list containing None
            if left > right:
                return [None]
            
            # Check if the current range of indices has already been computed
            if (left, right) in cache:
                return cache[(left, right)]
            
            result = []  # List to store the generated trees
            
            # Generate trees for each value in the current range
            for value in range(left, right + 1):
                # Generate all possible left subtrees
                for left_tree in generate(left, value - 1):
                    # Generate all possible right subtrees
                    for right_tree in generate(value + 1, right):
                        # Create a new tree with the current value as the root and the left and right subtrees
                        root = TreeNode(value, left_tree, right_tree)
                        result.append(root)
            
            # Store the generated trees in the cache for future use
            cache[(left, right)] = result
            
            return result
        
        # Call the generate function to generate the trees for the range [1, n]
        return generate(1, n)