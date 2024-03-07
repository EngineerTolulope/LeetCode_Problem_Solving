# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
         # Base case: if n is even or 0, no full binary trees possible
        if n % 2 == 0:
            return []

        # Base case: if n is 1, return a single node tree
        if n == 1:
            return [TreeNode(0)]

        result = []
        # Iterate over all possible number of nodes for left and right subtrees
        for left_nodes in range(1, n, 2):
            right_nodes = n - 1 - left_nodes
            left_trees = self.allPossibleFBT(left_nodes)
            right_trees = self.allPossibleFBT(right_nodes)

            # Generate all possible combinations of left and right subtrees
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)

        return result