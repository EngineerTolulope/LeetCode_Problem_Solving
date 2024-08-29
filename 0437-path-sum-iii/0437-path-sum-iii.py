# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        number_of_paths = 0
        frequency = {0 : 1}
        
        def depth_first_search(root, previous_sum):
            nonlocal number_of_paths
            
            if not root:
                return
            
            current_sum = previous_sum + root.val
            remaining_sum = current_sum - targetSum
            if remaining_sum in frequency:
                number_of_paths += frequency[remaining_sum]
            frequency[current_sum] = 1 + frequency.get(current_sum, 0)
            
            depth_first_search(root.left, current_sum)
            depth_first_search(root.right, current_sum)
            frequency[current_sum] -= 1
            
        depth_first_search(root, 0)
        return number_of_paths