# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        result = []
        
        def dfs(node):
            if not node:
                return "None"
            
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            subtrees[s].append(node)
            
            if len(subtrees[s]) == 2:
                result.append(subtrees[s][0])
            
            return s

        dfs(root)
        return result

    def findDuplicateSubtrees_(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        
        def dfs(node):
            if not node:
                return "None"
            
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subtrees[s]) == 1:
                result.append(node)
            subtrees[s].append(node)
            return s

        result = []
        dfs(root)
        return result