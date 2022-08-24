# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 1
        queue = [(root, 0)]
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            
            for _ in range(len(queue)):
                node, index = queue.pop(0)
                
                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))
        return max_width
        