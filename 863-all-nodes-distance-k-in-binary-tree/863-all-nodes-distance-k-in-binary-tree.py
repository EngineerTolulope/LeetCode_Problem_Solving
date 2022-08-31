# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        result, visited = [], set()
        queue, node_to_neighbours = collections.deque([root]), collections.defaultdict(list)
        
        while queue:
            node = queue.popleft()
            
            if node.left:
                node_to_neighbours[node].append(node.left)
                node_to_neighbours[node.left].append(node)
                queue.append(node.left)
            if node.right:
                node_to_neighbours[node].append(node.right)
                node_to_neighbours[node.right].append(node)
                queue.append(node.right)
        
        queue = collections.deque([(target, 0)])
        while queue:
            node, distance = queue.popleft()
            visited.add(node)
            if k == distance:
                result.append(node.val)
                continue
            
            for edge in node_to_neighbours[node]:
                if edge in visited:
                    continue
                
                visited.add(edge)
                queue.append((edge, distance + 1))
        return result
        