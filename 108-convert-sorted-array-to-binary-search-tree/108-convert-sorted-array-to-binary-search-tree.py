# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def create_binary_tree(left, right):
            if left > right:
                return None
            
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = create_binary_tree(left, middle - 1)
            root.right = create_binary_tree(middle + 1, right)
            return root
        return create_binary_tree(0, len(nums) - 1)
            