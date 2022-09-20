class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result, quadruplets = [], []
        
        def k_sum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quadruplets.append(nums[i])
                    k_sum(k - 1, i + 1, target - nums[i])
                    quadruplets.pop()
                return
            
            # base case, two sum ii
            left, right = start, len(nums) - 1
            while left < right:
                sum_ = nums[left] + nums[right]
                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                else:
                    result.append(quadruplets + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            return
        
        
        k_sum(4, 0, target)
        return result