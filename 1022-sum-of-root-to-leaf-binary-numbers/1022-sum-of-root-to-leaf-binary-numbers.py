# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        all_nums = []

        def dfs(root, num):
            if not root:
                return

            num = num * 10 + root.val
            if not root.left and not root.right:
                all_nums.append(num)
                return
            dfs(root.left, num)
            dfs(root.right, num)

        def binary_to_decimal(binary):
            # Convert the input to a string to handle each digit
            binary_str = str(binary)
            
            # Initialize the decimal number
            decimal_number = 0
            
            # Iterate over the binary string in reverse order
            for index, digit in enumerate(reversed(binary_str)):
                if digit not in '01':
                    raise ValueError("Input must be a binary number (containing only 0s and 1s).")
                # Convert each digit to an integer and calculate its decimal value
                decimal_number += int(digit) * (2 ** index)
        
            return decimal_number
        
        dfs(root, 0)
        total_sum = 0
        for num in all_nums:
            total_sum += binary_to_decimal(num)

        return total_sum


             