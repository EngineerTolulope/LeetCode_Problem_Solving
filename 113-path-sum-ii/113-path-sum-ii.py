# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        found_paths = []
        
        def depth_first_search(root, target_sum, current_path):
            if not root.left and not root.right:
                if target_sum == root.val:
                    found_paths.append(current_path + [root.val])
            if root.left:
                depth_first_search(root.left, target_sum - root.val, current_path + [root.val])
            if root.right:
                depth_first_search(root.right, target_sum - root.val, current_path + [root.val])

        
        depth_first_search(root, targetSum, [])
        return found_paths
            
        