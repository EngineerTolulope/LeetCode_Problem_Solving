# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        result = []

        while stack:
            current, visited = stack.pop()
            if current:
                if visited:
                    result.append(current.val)
                else:
                    stack.append((current, True))
                    stack.append((current.right, False))
                    stack.append((current.left, False))
        return result

        