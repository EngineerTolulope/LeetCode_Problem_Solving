# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        
        queue, result = collections.deque(), []
        queue.append(root)
        left_to_right = True
        while queue:
            temp_result = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                temp_result.append(node.val)
                queue += filter(None, (node.left, node.right))
            
            if left_to_right:
                result.append(temp_result)
            else:
                result.append(temp_result[::-1])
            left_to_right = not left_to_right
        return result
                
        
        