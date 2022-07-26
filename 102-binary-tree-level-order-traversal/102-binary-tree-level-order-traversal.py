# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        # We are implementing a bfs search
        queue = collections.deque()
        queue.append(root)
        
        # We loop while our queue is not empty
        while queue:
            queue_len = len(queue)  # Queue length
            level_items = []
            
            # Going through the length of the queue
            for i in range(queue_len):
                node = queue.popleft()  # Pop from the left
                
                if node:    # If node is not null
                    level_items.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level_items:   # Append to result if level is not an empty list
                result.append(level_items)
        return result
                