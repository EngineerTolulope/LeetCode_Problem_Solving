# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}
        def generate(left, right):
            if left > right:
                return [None]
            if (left, right) in cache:
                return cache[(left, right)]
            
            result = []
            for value in range(left, right + 1):
                for left_tree in generate(left, value - 1):
                    for right_tree in generate(value + 1, right):
                        root = TreeNode(value, left_tree, right_tree)
                        result.append(root)
            cache[(left, right)] = result
            return result
        return generate(1, n)
            