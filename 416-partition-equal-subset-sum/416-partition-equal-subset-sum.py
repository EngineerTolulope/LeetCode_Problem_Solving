class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:  # if odd return false
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums)):
            temp_dp = dp.copy()
            for num in dp:
                total = num + nums[i]
                if total == target:
                    return True
                temp_dp.add(total)
            dp = temp_dp
        return True if target in dp else False