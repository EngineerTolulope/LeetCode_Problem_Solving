class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        def compare_combination(num_1, num_2):
            if num_1 + num_2 > num_2 + num_1:
                return -1
            else:
                return 1
        
        nums.sort(key=cmp_to_key(compare_combination))
        return str(int("".join(nums)))
        
            