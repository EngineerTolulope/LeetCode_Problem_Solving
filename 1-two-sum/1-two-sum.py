class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}    # To store checked numbers and their index
        
        for i, num in enumerate(nums):
            diff = target - num # Get the difference from target
            if diff in checked: # If the difference is in one of our checked numbers
                return [checked[diff], i]
            
            checked[num] = i    # Adds the new number to the hash
            
            
        