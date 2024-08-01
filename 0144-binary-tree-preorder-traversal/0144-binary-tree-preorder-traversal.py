from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list and stack
        result = []
        stack = [root] if root else []

        # Iteratively traverse the tree
        while stack:
            current = stack.pop()
            result.append(current.val)

            # Push right child first so that left is processed first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                
        return result

# Example usage:
# tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
# solution = Solution()
# print(solution.preorderTraversal(tree))  # Output: [1, 2, 3]
